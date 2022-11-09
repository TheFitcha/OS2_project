from tkinter import *
from tkinter import font
from tkinter.ttk import *
from file_handlers import *

# consts
WINDOW_HEIGHT = 350
WINDOW_WIDTH = 500
MAIN_COLOR = "aliceblue"

# style setup
buttonMainStyle = Style()

class MainWindow(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, *kwargs)

        # main window setup
        # mainWindow = Tk()
        # mainWindow.config(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        # mainWindow.title("Krypter")
        # mainWindow.withdraw()
        # mainWindow.resizable(False, False)

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
        for frame in (AES_Screen, RSA_Screen, Hash_Screen, Signature_Screen):
            self.frames[frame.__name__] = frame(parent=container, controller=self)
            self.frames[frame.__name__].grid(row=0, column=0, sticky="nsew")

        self.show_frame("AES_Screen")

    def show_frame(self, page):
        self.frames[page].tkraise()


class AES_Screen(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        # fileLoadFrame
        fileLoadFrame = Frame(master=self)
        fileLoadFrame.pack(pady=10, padx=10)

        publicKeyLabel = Label(fileLoadFrame, text="Ključ: ")
        publicKeyLabel.grid(row=0, column=0, pady=10, padx=10)

        publicKeyFnStr = StringVar()
        publicKeyFileName = Label(master=fileLoadFrame, textvariable=publicKeyFnStr, width=30)
        publicKeyFileName.grid(row=0, column=1, pady=10, padx=10)

        # keysFrame
        keysFrame = Frame(master=fileLoadFrame)
        keysFrame.grid(row=0, column=3, pady=10, padx=10)

        publicKeyLoadBtn = Button(master=keysFrame, width=7.5, text="Ucitaj ključ")        
        publicKeyLoadBtn.grid(row=0, column=0, padx=1)

        publicKeyGenerateBtn = Button(master=keysFrame, width=7.5, text="Generiraj ključ")
        publicKeyGenerateBtn.grid(row=0, column=1, padx=1)

        # fileLoadFrame
        dataLabel = Label(master=fileLoadFrame, text="Podaci: ")
        dataLabel.grid(row=1, column=0, pady=10, padx=10)

        dataStr = StringVar()
        dataFileName = Label(master=fileLoadFrame, textvariable=dataStr, width=30)
        dataFileName.grid(row=1, column=1, pady=10, padx=10)

        dataLoadBtn = Button(master=fileLoadFrame, width=24, text="Ucitaj podatke")
        dataLoadBtn.grid(row=1, column=3, pady=10, padx=10)

        # showDataFrame
        showDataFrame = Frame(master=self)
        showDataFrame.pack(padx=10, pady=10)

        keyDisplayLabel = Label(master=showDataFrame, text="Ključ: ", width=15)
        keyDisplayLabel.grid(row=0, column=0, pady=10, padx=10)

        keyValueStr = StringVar(value="Example")
        keyDisplayEntry = Entry(master=showDataFrame, state=DISABLED, textvariable=keyValueStr)
        keyDisplayEntry.grid(row=0, column=1, columnspan=3, sticky=W+E)

        dataDisplayLabel = Label(master=showDataFrame, text="Podaci: ", width=15)
        dataDisplayLabel.grid(row=1, column=0, pady=10, padx=10)

        dataDisplayStr = StringVar(value="Example")
        dataDisplayTxtBox = Text(master=showDataFrame, height=10, width=50)
        dataDisplayTxtBox.insert(END, dataDisplayStr)
        dataDisplayTxtBox.grid(row=1, column=1)

        # cryptButtonsFrame
        cryptButtonsFrame = Frame(master=self)
        cryptButtonsFrame.pack(pady=10, padx=10)

        encryptBtn = Button(master=cryptButtonsFrame, text="Enkriptiraj", width=20)
        encryptBtn.grid(row=0, column=0, pady=10, sticky=E)

        decryptBtn = Button(master=cryptButtonsFrame, text="Dekriptiraj", width=20)
        decryptBtn.grid(row=0, column=1, pady=10, padx=2, sticky=E)

        # cryptResultFrame
        cryptResultFrame = Frame(master=self)
        cryptResultFrame.pack(pady=10, padx=10)

        resultDisplayLabel = Label(master=cryptResultFrame, text="Rezultat: ", width=15)
        resultDisplayLabel.grid(row=1, column=0, pady=10, padx=2)

        resultDisplayStr = StringVar(value="Example")
        resultDisplayTxtBox = Text(master=cryptResultFrame, height=10, width=50)
        resultDisplayTxtBox.insert(END, resultDisplayStr)
        resultDisplayTxtBox.grid(row=1, column=1)

class RSA_Screen(Frame):
    def __init__(self, parent, controller) -> None:
        Frame.__init__(self, parent)
        self.controller = controller

        # fileLoadFrame
        fileLoadFrame = Frame(master=self)
        fileLoadFrame.pack(pady=10, padx=10)

        publicKeyLabel = Label(fileLoadFrame, text="Javni ključ: ")
        publicKeyLabel.grid(row=0, column=0, pady=10, padx=10)

        publicKeyFnStr = StringVar()
        publicKeyFileName = Label(master=fileLoadFrame, textvariable=publicKeyFnStr, width=30)
        publicKeyFileName.grid(row=0, column=1, pady=10, padx=10)

        publicKeyLoadBtn = Button(master=fileLoadFrame, width=15, text="Ucitaj javni ključ")
        publicKeyLoadBtn.grid(row=0, column=3, pady=10, padx=10)

        dataLabel = Label(master=fileLoadFrame, text="Tajni ključ: ")
        dataLabel.grid(row=1, column=0, pady=10, padx=10)

        dataStr = StringVar()
        dataFileName = Label(master=fileLoadFrame, textvariable=dataStr, width=30)
        dataFileName.grid(row=1, column=1, pady=10, padx=10)

        dataLoadBtn = Button(master=fileLoadFrame, width=15, text="Ucitaj tajni ključ")
        dataLoadBtn.grid(row=1, column=3, pady=10, padx=10)
        pass

class Hash_Screen(Frame):
    def __init__(self, parent, controller) -> None:
        Frame.__init__(self, parent)
        self.controller = controller
        pass

class Signature_Screen(Frame):
    def __init__(self, parent, controller) -> None:
        Frame.__init__(self, parent)
        self.controller = controller
        pass


if __name__ == "__main__":
    main = MainWindow()
    main.mainloop()