import tkinter as tk
from gui import choice_window, encoder_menu, decoder_menu

if __name__ == "__main__":
    root = tk.Tk()
    root.title("PLTW Encode My Will to Live")
    encoder = encoder_menu(root)
    decoder = decoder_menu(root)
    choice_menu_frame = choice_window(root, encoder, decoder)
    choice_menu_frame.pack(expand=True, fill=tk.BOTH)
    root.resizable(False, False)
    root.mainloop()