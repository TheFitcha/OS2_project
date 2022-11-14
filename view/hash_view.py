from tkinter import *
from tkinter import font
from tkinter.ttk import *


class Hash_Screen(Frame):
    def __init__(self, parent, controller) -> None:
        Frame.__init__(self, parent)
        self.controller = controller

        # fileLoadFrame
        fileLoadFrame = Frame(master=self)
        fileLoadFrame.pack(pady=10, padx=10)
    
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

        dataDisplayLabel = Label(master=showDataFrame, text="Podaci: ", width=15)
        dataDisplayLabel.grid(row=1, column=0, pady=10, padx=10)

        dataDisplayStr = StringVar(value="Example")
        dataDisplayTxtBox = Text(master=showDataFrame, height=10, width=50)
        dataDisplayTxtBox.insert(END, dataDisplayStr)
        dataDisplayTxtBox.grid(row=1, column=1)

        # cryptButtonsFrame
        cryptButtonsFrame = Frame(master=self)
        cryptButtonsFrame.pack(pady=10, padx=10)

        encryptBtn = Button(master=cryptButtonsFrame, text="Hashiraj", width=20)
        encryptBtn.grid(row=0, column=0, pady=10, sticky=E)

        # cryptResultFrame
        cryptResultFrame = Frame(master=self)
        cryptResultFrame.pack(pady=10, padx=10)

        resultDisplayLabel = Label(master=cryptResultFrame, text="Rezultat: ", width=15)
        resultDisplayLabel.grid(row=1, column=0, pady=10, padx=2)

        resultDisplayStr = StringVar(value="Example")
        resultDisplayTxtBox = Text(master=cryptResultFrame, height=10, width=50)
        resultDisplayTxtBox.insert(END, resultDisplayStr)
        resultDisplayTxtBox.grid(row=1, column=1)
