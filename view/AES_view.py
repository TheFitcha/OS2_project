from tkinter import *
from tkinter import font
from tkinter.ttk import *

class AES_Screen(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.ctr = controller
        # fileLoadFrame
        fileLoadFrame = Frame(master=self)
        fileLoadFrame.pack(pady=10, padx=10)

        publicKeyLabel = Label(fileLoadFrame, text="Ključ: ")
        publicKeyLabel.grid(row=0, column=0, pady=10, padx=10)

        global publicKeyFnStr
        publicKeyFnStr = StringVar()
        
        publicKeyFileName = Label(master=fileLoadFrame, textvariable=publicKeyFnStr, width=30)
        publicKeyFileName.grid(row=0, column=1, pady=10, padx=10)

        # keysFrame
        keysFrame = Frame(master=fileLoadFrame)
        keysFrame.grid(row=0, column=3, pady=10, padx=10)

        publicKeyLoadBtn = Button(master=keysFrame, width=7.5, text="Ucitaj ključ", command=lambda: self.ctr.load_file('key', 'AES'))        
        publicKeyLoadBtn.grid(row=0, column=0, padx=1)

        publicKeyGenerateBtn = Button(master=keysFrame, width=7.5, text="Generiraj ključ", command=lambda: self.ctr.generate_AES_key())
        publicKeyGenerateBtn.grid(row=0, column=1, padx=1)

        # fileLoadFrame
        dataLabel = Label(master=fileLoadFrame, text="Podaci: ")
        dataLabel.grid(row=1, column=0, pady=10, padx=10)

        global dataStr
        dataStr = StringVar()

        dataFileName = Label(master=fileLoadFrame, textvariable=dataStr, width=30)
        dataFileName.grid(row=1, column=1, pady=10, padx=10)

        dataLoadBtn = Button(master=fileLoadFrame, width=24, text="Ucitaj podatke", command=lambda: self.ctr.load_file('data', 'AES'))
        dataLoadBtn.grid(row=1, column=3, pady=10, padx=10)

        # showDataFrame
        showDataFrame = Frame(master=self)
        showDataFrame.pack(padx=10, pady=10)

        keyDisplayLabel = Label(master=showDataFrame, text="Ključ: ", width=15)
        keyDisplayLabel.grid(row=0, column=0, pady=10, padx=10)

        global keyValueStr
        keyValueStr = StringVar()

        keyDisplayEntry = Entry(master=showDataFrame, state=DISABLED, textvariable=keyValueStr)
        keyDisplayEntry.grid(row=0, column=1, columnspan=3, sticky=W+E)

        dataDisplayLabel = Label(master=showDataFrame, text="Podaci: ", width=15)
        dataDisplayLabel.grid(row=1, column=0, pady=10, padx=10)

        global dataDisplayTxtBox
        dataDisplayTxtBox = Text(master=showDataFrame, height=10, width=50)
        dataDisplayTxtBox.grid(row=1, column=1)

        # cryptButtonsFrame
        cryptButtonsFrame = Frame(master=self)
        cryptButtonsFrame.pack(pady=10, padx=10)

        encryptBtn = Button(master=cryptButtonsFrame, text="Enkriptiraj", width=20, command=lambda: self.ctr.AES_encrypt())
        encryptBtn.grid(row=0, column=0, pady=10)

        decryptBtn = Button(master=cryptButtonsFrame, text="Dekriptiraj", width=20, command=lambda: self.ctr.AES_decrypt())
        decryptBtn.grid(row=0, column=1, pady=10, padx=2)

        # cryptResultFrame
        cryptResultFrame = Frame(master=self)
        cryptResultFrame.pack(pady=10, padx=10)

        resultDisplayLabel = Label(master=cryptResultFrame, text="Rezultat: ", width=15)
        resultDisplayLabel.grid(row=1, column=0, pady=10, padx=2)

        global resultDisplayTxtBox
        resultDisplayTxtBox = Text(master=cryptResultFrame, height=10, width=50)
        resultDisplayTxtBox.grid(row=1, column=1)

    def show_data(which, filename, value):
        if which == 'key':
            publicKeyFnStr.set(filename)
            keyValueStr.set(value)
        elif which == 'data':
            dataStr.set(filename)
            dataDisplayTxtBox.config(state=NORMAL)
            dataDisplayTxtBox.delete(1.0, END)
            dataDisplayTxtBox.insert(END, value)
            dataDisplayTxtBox.config(state=DISABLED)
        
    def show_aes_result(result):
        resultDisplayTxtBox.config(state=NORMAL)
        resultDisplayTxtBox.delete(1.0, END)
        resultDisplayTxtBox.insert(END, result)
        resultDisplayTxtBox.config(state=DISABLED)




       

