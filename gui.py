import tkinter as tk
from tkinter import filedialog, messagebox
from encode import Encoder
from decode import Decoder
from os import path

NAVY = '#000022'
TEAL = '#3e8989'
GREEN = '#b0fe76'
RED = '#95190c'
PURPLE = '#a997df'

class choice_window(tk.Frame):
    def __init__(self, parent, encode_frame, decode_frame):
        super().__init__(parent, padx=50, pady=0, bg=PURPLE)
        self.encode_button = tk.Button(self, text="Encode", font=('yu gothic ui light', 20), command=self.encode_button_clicked, bg=TEAL, fg=NAVY, activebackground=GREEN, activeforeground=NAVY, highlightbackground=PURPLE)
        self.encode_button.pack(pady=10)
        self.decode_button = tk.Button(self, text="Decode", font=('yu gothic ui light', 20), command=self.decode_button_clicked, bg=TEAL, fg=NAVY, activebackground=GREEN, activeforeground=NAVY, highlightbackground=PURPLE)
        self.decode_button.pack(pady=10)
        self.quit_button = tk.Button(self, text="Quit", font=('yu gothic ui light', 20), command=self.quit_button_clicked, bg=TEAL, fg=NAVY, activebackground=RED, activeforeground=NAVY, highlightbackground=PURPLE)
        self.quit_button.pack(pady=10)
        self.decode_frame = decode_frame
        self.encode_frame = encode_frame

    def encode_button_clicked(self):
        self.encode_frame.tkraise()
        self.destroy()

    def decode_button_clicked(self):
        self.decode_frame.tkraise()
        self.destroy()

    def quit_button_clicked(self):
        self.quit()

class encoder_menu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=PURPLE)
        self.encoder = Encoder()
        self.output_dir = ""
        self.msg = ""
        self.suffix = 0
        self.title = tk.Label(self, text="Encoder", font=('yu gothic ui light', 20), bg=PURPLE, fg=NAVY)
        self.title.grid(row=0, column=0, columnspan=2)
        self.msg_label = tk.Label(self, text="Enter a message to encode:", font=('yu gothic ui light', 15), bg=PURPLE, fg=NAVY)
        self.msg_label.grid(row=1, column=0)
        self.msg_entry = tk.Entry(self, font=('yu gothic ui light', 15), bg=TEAL, fg=NAVY, highlightbackground=PURPLE)
        self.msg_entry.grid(row=1, column=1)
        self.output_dir_label = tk.Label(self, text="Select an output directory -->", font=('yu gothic ui light', 15), bg=PURPLE, fg=NAVY)
        self.output_dir_label.grid(row=2, column=0)
        self.output_dir_select_button = tk.Button(self, text="Select", font=('yu gothic ui light', 15), command=self.select_output_dir, bg=TEAL, fg=NAVY, activebackground=GREEN, activeforeground=NAVY, highlightbackground=PURPLE)
        self.output_dir_select_button.grid(row=2, column=1)
        self.suffix_label = tk.Label(self, text="Enter an optional code for extra security(0-65535):\nNote: this must be hand delivered to the reciever.", font=('yu gothic ui light', 15), bg=PURPLE, fg=NAVY)
        self.suffix_label.grid(row=3, column=0)
        self.suffix_entry = tk.Entry(self, font=('yu gothic ui light', 15), bg=TEAL, fg=NAVY, highlightbackground=PURPLE)
        self.suffix_entry.grid(row=3, column=1)
        self.encode_button = tk.Button(self, text="Encode!", font=('yu gothic ui light', 15), command=self.encode_button_clicked, bg=TEAL, fg=NAVY, activebackground=GREEN, activeforeground=NAVY, highlightbackground=PURPLE)
        self.encode_button.grid(row=4, column=0, columnspan=2)

    def encode_button_clicked(self):
        self._disable_input()
        self.msg = self.msg_entry.get()
        try:
            self.suffix = int(self.suffix_entry.get())
        except ValueError:
            self.suffix = 0
        if self.suffix not in range(0, 65536):
            self.suffix = 0
        if self.suffix == 0:
            self.encoder.encode(self.msg, self.output_dir)
        else:
            self.encoder.encode(self.msg, self.output_dir, self.suffix)
        
        messagebox.showinfo(title="Success", message="Successfully encoded message!")
        self._enable_input()

    def select_output_dir(self):
        self.output_dir = filedialog.askdirectory()
        self.output_dir_label.config(text=f'Output Directory: {self.output_dir}')

    def _disable_input(self):
        self.msg_entry.config(state='disabled')
        self.suffix_entry.config(state='disabled')
        self.output_dir_select_button.config(state='disabled')
        self.encode_button.config(state='disabled')

    def _enable_input(self):
        self.msg_entry.config(state='normal')
        self.suffix_entry.config(state='normal')
        self.output_dir_select_button.config(state='normal')
        self.encode_button.config(state='normal')

class decoder_menu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.decoder = Decoder()
        self.suffix = 0
        self.file_path = path.expanduser("~/Documents/encoder_output0.gif")
        self.title = tk.Label(self, text="Decoder")
        self.title.grid(row=0, column=0, columnspan=2)
        self.select_file_label = tk.Label(self, text="Select a file to decode:")
        self.select_file_label.grid(row=1, column=0)
        self.load_file_button = tk.Button(self, text="Select", command=self.select_file)
        self.load_file_button.grid(row=1, column=1)
        self.file_path_label = tk.Label(self, text=f'File Path: {self.file_path}')
        self.file_path_label.grid(row=2, column=0, columnspan=2)
        self.suffix_label = tk.Label(self, text="Enter the code for extra security(if applicable):")
        self.suffix_label.grid(row=3, column=0)
        self.suffix_entry = tk.Entry(self, font=('yu gothic ui light', 15), bg=TEAL, fg=NAVY, highlightbackground=PURPLE)
        self.suffix_entry.grid(row=3, column=1)
        self.decode_button = tk.Button(self, text="Decode!", command=self.decode_button_clicked)
        self.decode_button.grid(row=4, column=0, columnspan=2)

    def select_file(self):
        self.file_path = filedialog.askopenfilename()
        self.file_path_label.config(text=f'File Path: {self.file_path}')

    def decode_button_clicked(self):
        try:
            self.suffix = int(self.suffix_entry.get())
        except ValueError:
            self.suffix = 0
        if self.suffix == 0:
            self.decoder.decode(self.file_path)
        else:
            self.decoder.decode(self.file_path, self.suffix)