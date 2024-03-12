import tkinter as tk
from gui import choice_window, encoder_menu, decoder_menu

if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    root.title("PLTW Encode My Will to Live")
    encoder = encoder_menu(root)
    decoder = decoder_menu(root)
    encoder.grid(row=0, column=0)
    decoder.grid(row=0, column=0)
    choice_menu_frame = choice_window(root, encoder, decoder)
    choice_menu_frame.grid(row=0, column=0, sticky="nsew")
    root.mainloop()