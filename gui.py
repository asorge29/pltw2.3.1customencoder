import tkinter as tk
from tkinter import filedialog
from encode import Encoder

NAVY = '#000022'
TEAL = '#3e8989'
GREEN = '#b0fe76'
RED = '#95190c'
PURPLE = '#a997df'

class choice_window(tk.Frame):
    def __init__(self, parent, encode_frame, decode_frame):
        super().__init__(parent, padx=50, pady=0, bg=PURPLE)
        self.encode_button = tk.Button(self, text="Encode", font=('yu gothic ui light', 20), command=self.encode_button_clicked, bg=TEAL, fg=NAVY, activebackground=GREEN, activeforeground=NAVY)
        self.encode_button.pack(pady=10)
        self.decode_button = tk.Button(self, text="Decode", font=('yu gothic ui light', 20), command=self.decode_button_clicked, bg=TEAL, fg=NAVY, activebackground=GREEN, activeforeground=NAVY)
        self.decode_button.pack(pady=10)
        self.quit_button = tk.Button(self, text="Quit", font=('yu gothic ui light', 20), command=self.quit_button_clicked, bg=TEAL, fg=NAVY, activebackground=RED, activeforeground=NAVY)
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
        self.msg_entry = tk.Entry(self, font=('yu gothic ui light', 15), bg=TEAL, fg=NAVY)
        self.msg_entry.grid(row=1, column=1)
        self.output_dir_label = tk.Label(self, text="Select an output directory -->", font=('yu gothic ui light', 15), bg=PURPLE, fg=NAVY)
        self.output_dir_label.grid(row=2, column=0)
        self.output_dir_select_button = tk.Button(self, text="Select", font=('yu gothic ui light', 15), command=self.select_output_dir, bg=TEAL, fg=NAVY, activebackground=GREEN, activeforeground=NAVY)
        self.output_dir_select_button.grid(row=2, column=1)
        self.suffix_label = tk.Label(self, text="Enter an optional code for extra security(0-65535):\nNote: this must be hand delivered to the reciever.", font=('yu gothic ui light', 15), bg=PURPLE, fg=NAVY)
        self.suffix_label.grid(row=3, column=0)
        self.suffix_entry = tk.Entry(self, font=('yu gothic ui light', 15), bg=TEAL, fg=NAVY)
        self.suffix_entry.grid(row=3, column=1)
        self.encode_button = tk.Button(self, text="Encode!", font=('yu gothic ui light', 15), command=self.encode_button_clicked, bg=TEAL, fg=NAVY, activebackground=GREEN, activeforeground=NAVY)
        self.encode_button.grid(row=4, column=0, columnspan=2)

    def encode_button_clicked(self):
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

    def select_output_dir(self):
        self.output_dir = filedialog.askdirectory()
        self.output_dir_label.config(text=f'Output Directory: {self.output_dir}')

class decoder_menu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self, text="Decoder")
        self.label.pack()