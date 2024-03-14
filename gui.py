import tkinter as tk
import platform
from tkinter import filedialog, messagebox, scrolledtext as tksc
from encode import Encoder
from decode import Decoder

if platform.system() == 'Darwin':
    FONT = 'PingFang SC'
else:
    FONT = 'yu gothic ui light'

TEXT = '#88C0D0'
WIDGETS = '#434C5E'
GREEN = '#A3BE8C'
RED = '#BF616A'
BACKG = '#2E3440'

class choice_window(tk.Frame):
    def __init__(self, parent, encode_frame, decode_frame):
        super().__init__(parent, padx=50, pady=0, bg=BACKG)
        self.encode_button = tk.Button(self, text="Encode", font=(FONT, 20), command=self.encode_button_clicked, bg=WIDGETS, fg=TEXT, activebackground=GREEN, activeforeground=TEXT, highlightbackground=BACKG)
        self.encode_button.pack(pady=10)
        self.decode_button = tk.Button(self, text="Decode", font=(FONT, 20), command=self.decode_button_clicked, bg=WIDGETS, fg=TEXT, activebackground=GREEN, activeforeground=TEXT, highlightbackground=BACKG)
        self.decode_button.pack(pady=10)
        self.quit_button = tk.Button(self, text="Quit", font=(FONT, 20), command=self.quit_button_clicked, bg=WIDGETS, fg=TEXT, activebackground=RED, activeforeground=TEXT, highlightbackground=BACKG)
        self.quit_button.pack(pady=10)
        self.decode_frame = decode_frame
        self.encode_frame = encode_frame

    def encode_button_clicked(self):
        self.encode_frame.pack(expand=True, fill=tk.BOTH)
        self.destroy()

    def decode_button_clicked(self):
        self.decode_frame.pack(expand=True, fill=tk.BOTH)
        self.destroy()

    def quit_button_clicked(self):
        self.quit()

class encoder_menu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=BACKG, padx=20, pady=10)
        self.encoder = Encoder()
        self.output_dir = ""
        self.msg = ""
        self.suffix = 0
        self.file_name = 'encoder_output'
        self.title = tk.Label(self, text="Encoder", font=(FONT, 20), bg=BACKG, fg=TEXT)
        self.title.grid(row=0, column=0, columnspan=2)
        self.msg_label = tk.Label(self, text="Enter a message to encode:", font=(FONT, 15), bg=BACKG, fg=TEXT)
        self.msg_label.grid(row=1, column=0, sticky='e', pady=(0, 5))
        self.msg_entry = tk.Entry(self, font=(FONT, 15), bg=WIDGETS, fg=TEXT, highlightbackground=BACKG)
        self.msg_entry.grid(row=1, column=1, sticky='ew', pady=(0, 5))
        self.name_label = tk.Label(self, text="Enter a name for the file:", font=(FONT, 15), bg=BACKG, fg=TEXT)
        self.name_label.grid(row=2, column=0, sticky='e', pady=(0, 5))
        self.name_entry = tk.Entry(self, font=(FONT, 15), bg=WIDGETS, fg=TEXT, highlightbackground=BACKG)
        self.name_entry.grid(row=2, column=1, sticky='e', pady=(0, 5))
        self.output_dir_label = tk.Label(self, text="Select an output directory -->", font=(FONT, 15), bg=BACKG, fg=TEXT)
        self.output_dir_label.grid(row=3, column=0, sticky='e', pady=(0, 5))
        self.output_dir_select_button = tk.Button(self, text="Select", font=(FONT, 15), command=self.select_output_dir, bg=WIDGETS, fg=TEXT, activebackground=GREEN, activeforeground=TEXT, highlightbackground=BACKG)
        self.output_dir_select_button.grid(row=3, column=1, sticky='ew', pady=(0, 5))
        self.suffix_label = tk.Label(self, text="Enter an optional code(0-65535):", font=(FONT, 15), bg=BACKG, fg=TEXT)
        self.suffix_label.grid(row=4, column=0, pady=(0, 5))
        self.suffix_entry = tk.Entry(self, font=(FONT, 15), bg=WIDGETS, fg=TEXT, highlightbackground=BACKG)
        self.suffix_entry.grid(row=4, column=1, sticky='nwe', pady=(0, 5))
        self.encode_button = tk.Button(self, text="Encode!", font=(FONT, 15), command=self.encode_button_clicked, bg=WIDGETS, fg=TEXT, activebackground=GREEN, activeforeground=TEXT, highlightbackground=BACKG)
        self.encode_button.grid(row=5, column=0, columnspan=2)

    def encode_button_clicked(self):
        self._disable_input()
        self.msg = self.msg_entry.get()
        if self.name_entry.get() != '':
            self.file_name = self.name_entry.get()
        try:
            self.suffix = int(self.suffix_entry.get())
        except ValueError:
            self.suffix = 0
        if self.suffix not in range(0, 65536):
            self.suffix = 0
        if self.suffix == 0:
            self.encoder.encode(self.msg, self.output_dir, self.file_name)
        else:
            self.encoder.encode(self.msg, self.output_dir, self.file_name, self.suffix)
        
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
        self.name_entry.config(state='disabled')

    def _enable_input(self):
        self.msg_entry.config(state='normal')
        self.suffix_entry.config(state='normal')
        self.output_dir_select_button.config(state='normal')
        self.encode_button.config(state='normal')
        self.name_entry.config(state='normal')

class decoder_menu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=BACKG, padx=20, pady=10)
        self.decoder = Decoder()
        self.suffix = 0
        self.msg = 'Nothing has been decoded yet.'
        self.file_path = 'Select a file to decode^^^'
        self.title = tk.Label(self, text="Decoder", font=(FONT, 20), bg=BACKG, fg=TEXT)
        self.title.grid(row=0, column=0, columnspan=2, pady=(0, 5))
        self.select_file_label = tk.Label(self, text="Select a file to decode:", font=(FONT, 15), bg=BACKG, fg=TEXT)
        self.select_file_label.grid(row=1, column=0, sticky='e', pady=(0, 5))
        self.load_file_button = tk.Button(self, text="Select", command=self.select_file, font=(FONT, 15), bg=WIDGETS, fg=TEXT, activebackground=GREEN, activeforeground=TEXT, highlightbackground=BACKG)
        self.load_file_button.grid(row=1, column=1, sticky='w', pady=(0, 5))
        self.file_path_label = tk.Label(self, text=f'File Path: {self.file_path}', font=(FONT, 15), bg=BACKG, fg=TEXT)
        self.file_path_label.grid(row=2, column=0, columnspan=2, pady=(0, 5))
        self.suffix_label = tk.Label(self, text="Enter the extra code(if applicable):", font=(FONT, 15), bg=BACKG, fg=TEXT)
        self.suffix_label.grid(row=3, column=0, pady=(0, 5), sticky='e')
        self.suffix_entry = tk.Entry(self, font=(FONT, 15), bg=WIDGETS, fg=TEXT, highlightbackground=BACKG)
        self.suffix_entry.grid(row=3, column=1, pady=(0, 5), sticky='w')
        self.decode_button = tk.Button(self, text="Decode!", command=self.decode_button_clicked, font=(FONT, 15), bg=WIDGETS, fg=TEXT, activebackground=GREEN, activeforeground=TEXT, highlightbackground=BACKG)
        self.decode_button.grid(row=4, column=0, columnspan=2)
        self.output_label = tk.Label(self, text="Decoded Message:", font=(FONT, 15), bg=BACKG, fg=TEXT)
        self.output_label.grid(row=5, column=0, columnspan=2)
        self.msg_label = tksc.ScrolledText(self, font=(FONT, 15), bg=BACKG, fg=TEXT, highlightbackground=BACKG)
        self.msg_label.config(state='disabled', wrap='word')
        self.msg_label.grid(row=6, column=0, columnspan=2)

    def select_file(self):
        self.file_path = filedialog.askopenfilename()
        self.file_path_label.config(text=f'File Path: {self.file_path}')

    def decode_button_clicked(self):
        self._disable_input()
        try:
            self.suffix = int(self.suffix_entry.get())
        except ValueError:
            self.suffix = 0
        if self.suffix == 0:
            self.decoder.decode(self.file_path)
        else:
            self.decoder.decode(self.file_path, self.suffix)
        
        self.msg = self.decoder.msg
        if self.decoder.suffix_verified:
            self.msg_label.delete(1.0, tk.END)
            self.msg_label.insert(tk.END, self.msg)
            messagebox.showinfo(title="Success", message="Successfully decoded message!")
        else:           
            self.msg_label.delete(1.0, tk.END)
            self.msg_label.insert(tk.END, 'Invalid code')
            messagebox.showerror(title="Error", message="Invalid code")
        
        self._enable_input()


    def _disable_input(self):
        self.load_file_button.config(state='disabled')
        self.suffix_entry.config(state='disabled')
        self.decode_button.config(state='disabled')
        self.msg_label.config(state='normal')
        self.msg_label.delete(1.0, tk.END)
        self.msg_label.insert( tk.END, 'Decoding...')

    def _enable_input(self):
        self.load_file_button.config(state='normal')
        self.suffix_entry.config(state='normal')
        self.decode_button.config(state='normal')