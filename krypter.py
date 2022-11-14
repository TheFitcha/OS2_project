from tkinter import *
from tkinter import font
from tkinter.ttk import *
import controller.controller as ctr
from view import AES_view, RSA_view, hash_view, signature_view

# consts
WINDOW_HEIGHT = 350
WINDOW_WIDTH = 500
MAIN_COLOR = "aliceblue"

# style setup
# frameMainStyle = Style()
# frameMainStyle.configure('Main.TFrame', background='red')

class MainWindow(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, *kwargs)

        self.title("Krypter")
        self.resizable(False, False)
        self.title_font = font.Font(family="Helvetica", size=12, weight="bold")

        # options switcher frame
        switcher = Frame(self)
        switcher.pack(side="top", fill="both", expand=True, padx=10)
        for i in range(4):
            switcher.grid_rowconfigure(i, weight=1)
            switcher.grid_columnconfigure(i, weight=1)


        AES_btn = Button(master=switcher, text="AES", width=15,
                            command=lambda: self.show_frame("AES_Screen"))
        AES_btn.grid(row=0, column=0, padx=10, pady=10)
        RSA_btn = Button(master=switcher, text="RSA", width=15,
                            command=lambda: self.show_frame("RSA_Screen"))
        RSA_btn.grid(row=0, column=1, padx=10, pady=10)
        hash_btn = Button(master=switcher, text="Hash", width=15,
                            command=lambda: self.show_frame("Hash_Screen"))
        hash_btn.grid(row=0, column=2, padx=10, pady=10)
        signature_btn = Button(master=switcher, text="Digitalni potpis", width=15,
                            command=lambda: self.show_frame("Signature_Screen"))
        signature_btn.grid(row=0, column=3, padx=10, pady=10)

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for frame in (AES_view.AES_Screen, RSA_view.RSA_Screen, hash_view.Hash_Screen, signature_view.Signature_Screen):
            self.frames[frame.__name__] = frame(parent=container, controller=ctr.Controller(frame))
            self.frames[frame.__name__].grid(row=0, column=0, sticky="nsew")

        self.show_frame("AES_Screen")

    def show_frame(self, page):
        self.frames[page].tkraise()


if __name__ == "__main__":
    main = MainWindow()
    main.mainloop()