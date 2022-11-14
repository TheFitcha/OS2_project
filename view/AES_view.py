from tkinter import *
from tkinter import font
from tkinter.ttk import *

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
        encryptBtn.grid(row=0, column=0, pady=10)

        decryptBtn = Button(master=cryptButtonsFrame, text="Dekriptiraj", width=20)
        decryptBtn.grid(row=0, column=1, pady=10, padx=2)

        # cryptResultFrame
        cryptResultFrame = Frame(master=self)
        cryptResultFrame.pack(pady=10, padx=10)

        resultDisplayLabel = Label(master=cryptResultFrame, text="Rezultat: ", width=15)
        resultDisplayLabel.grid(row=1, column=0, pady=10, padx=2)

        resultDisplayStr = StringVar(value="Example")
        resultDisplayTxtBox = Text(master=cryptResultFrame, height=10, width=50)
        resultDisplayTxtBox.insert(END, resultDisplayStr)
        resultDisplayTxtBox.grid(row=1, column=1)

       

