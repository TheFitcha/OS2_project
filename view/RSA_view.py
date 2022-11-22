from tkinter import *
from tkinter.ttk import *

class RSA_Screen(Frame):
    def __init__(self, parent, controller) -> None:
        Frame.__init__(self, parent)
        self.ctr = controller

        # fileLoadFrame
        fileLoadFrame = Frame(master=self)
        fileLoadFrame.pack(pady=10, padx=10)

        publicKeyLabel = Label(fileLoadFrame, text="Javni ključ: ")
        publicKeyLabel.grid(row=0, column=0, pady=10, padx=10)

        global publicKeyFnStr
        publicKeyFnStr = StringVar()
        publicKeyFileName = Label(master=fileLoadFrame, textvariable=publicKeyFnStr, width=30)
        publicKeyFileName.grid(row=0, column=1, pady=10, padx=10)

        publicKeyLoadBtn = Button(master=fileLoadFrame, width=15, text="Ucitaj javni ključ", command=lambda: self.ctr.load_file('key', 'RSA_public'))
        publicKeyLoadBtn.grid(row=0, column=3, pady=10, padx=10)

        privateKeyLabel = Label(master=fileLoadFrame, text="Tajni ključ: ")
        privateKeyLabel.grid(row=1, column=0, pady=10, padx=10)

        global privateKeyFnStr
        privateKeyFnStr = StringVar()
        privateKeyFileName = Label(master=fileLoadFrame, textvariable=privateKeyFnStr, width=30)
        privateKeyFileName.grid(row=1, column=1, pady=10, padx=10)

        privateKeyLoadBtn = Button(master=fileLoadFrame, width=15, text="Ucitaj tajni ključ", command=lambda: self.ctr.load_file('key', 'RSA_private'))
        privateKeyLoadBtn.grid(row=1, column=3, pady=10, padx=10)
        
        generateKeysBtn = Button(master=fileLoadFrame, text="Generiraj ključeve", command=lambda: self.ctr.generate_RSA_key())
        generateKeysBtn.grid(row=2, column=1, columnspan=2, sticky=W+E, padx=10, pady=10)

        dataLabel = Label(master=fileLoadFrame, text="Podaci: ")
        dataLabel.grid(row=3, column=0, pady=10, padx=10)

        global dataStr
        dataStr = StringVar()
        dataFileName = Label(master=fileLoadFrame, textvariable=dataStr, width=30)
        dataFileName.grid(row=3, column=1, pady=10, padx=10)

        dataLoadBtn = Button(master=fileLoadFrame, width=15, text="Ucitaj podatke", command=lambda: self.ctr.load_file('data', 'RSA'))
        dataLoadBtn.grid(row=3, column=3, pady=10, padx=10)

        # showDataFrame
        showDataFrame = Frame(master=self)
        showDataFrame.pack(padx=10, pady=10)

        privateKeyDisplayName = Label(master=showDataFrame, text="Privatni ključ: ", width=15)
        privateKeyDisplayName.grid(row=0, column=0, pady=10, padx=10)

        global privateKeyValueStr
        privateKeyValueStr = StringVar()
        privateKeyDisplayEntry = Entry(master=showDataFrame, state=DISABLED, textvariable=privateKeyValueStr)
        privateKeyDisplayEntry.grid(row=0, column=1, columnspan=3, sticky=W+E)

        publicKeyDisplayName = Label(master=showDataFrame, text="Javni ključ: ", width=15)
        publicKeyDisplayName.grid(row=1, column=0, pady=10, padx=10)

        global publicKeyValueStr
        publicKeyValueStr = StringVar()
        publicKeyDisplayEntry = Entry(master=showDataFrame, state=DISABLED, textvariable=publicKeyValueStr)
        publicKeyDisplayEntry.grid(row=1, column=1, columnspan=3, sticky=W+E)

        dataDisplayLabel = Label(master=showDataFrame, text="Podaci: ", width=15)
        dataDisplayLabel.grid(row=2, column=0, pady=10, padx=10)

        global dataDisplayTxtBox
        dataDisplayTxtBox = Text(master=showDataFrame, height=10, width=50)
        dataDisplayTxtBox.grid(row=2, column=1)

        # cryptButtonsFrame
        cryptButtonsFrame = Frame(master=self)
        cryptButtonsFrame.pack(pady=10, padx=10)

        encryptBtn = Button(master=cryptButtonsFrame, text="Enkriptiraj", width=20, command=lambda: self.ctr.RSA_encrypt())
        encryptBtn.grid(row=0, column=0, pady=10, sticky=E)

        decryptBtn = Button(master=cryptButtonsFrame, text="Dekriptiraj", width=20, command=lambda: self.ctr.RSA_decrypt())
        decryptBtn.grid(row=0, column=1, pady=10, padx=2, sticky=E)

        # cryptResultFrame
        cryptResultFrame = Frame(master=self)
        cryptResultFrame.pack(pady=10, padx=10)

        resultDisplayLabel = Label(master=cryptResultFrame, text="Rezultat: ", width=15)
        resultDisplayLabel.grid(row=1, column=0, pady=10, padx=2)

        global resultDisplayTxtBox
        resultDisplayTxtBox = Text(master=cryptResultFrame, height=10, width=50)
        resultDisplayTxtBox.grid(row=1, column=1)

    def show_data(which, filename, value):
        if which == 'key_public':
            publicKeyFnStr.set(filename)
            publicKeyValueStr.set(value)
        elif which == 'key_private':
            privateKeyFnStr.set(filename)
            privateKeyValueStr.set(value)
        elif which == 'data':
            dataStr.set(filename)
            dataDisplayTxtBox.config(state=NORMAL)
            dataDisplayTxtBox.delete(1.0, END)
            dataDisplayTxtBox.insert(END, value)
            dataDisplayTxtBox.config(state=DISABLED)

    def show_rsa_result(result):
        resultDisplayTxtBox.config(state=NORMAL)
        resultDisplayTxtBox.delete(1.0, END)
        resultDisplayTxtBox.insert(END, result)
        resultDisplayTxtBox.config(state=DISABLED)
 