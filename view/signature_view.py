from tkinter import *
from tkinter import font
from tkinter.ttk import *

class Signature_Screen(Frame):
    def __init__(self, parent, controller) -> None:
        Frame.__init__(self, parent)
        self.ctr = controller

        # switchModeFrame
        switchModeFrame = Frame(master=self, style='Main.TFrame')
        switchModeFrame.grid(row=0, column=0) # treba centrirati ovaj grid, a ne znam kako

        signBtn = Button(master=switchModeFrame, text="Potpiši", width=25, command=lambda: signFrame.tkraise())
        signBtn.grid(row=0, column=0, padx=10, pady=10)
        checkBtn = Button(master=switchModeFrame, text="Provjeri", width=25, command=lambda: checkFrame.tkraise())
        checkBtn.grid(row=0, column=1, padx=10, pady=10)

        #region signFrame
        # signFrame
        signFrame = Frame(master=self)
        signFrame.grid(row=1, column=0, sticky=N+S+E+W)

        fileLoadFrame = Frame(master=signFrame)
        fileLoadFrame.pack(pady=10, padx=10)

        privateKeyLabel = Label(fileLoadFrame, text="Privatni ključ: ")
        privateKeyLabel.grid(row=0, column=0, pady=10, padx=10)

        global privateKeyFnStr
        privateKeyFnStr = StringVar()
        privateKeyFileName = Label(master=fileLoadFrame, textvariable=privateKeyFnStr, width=30)
        privateKeyFileName.grid(row=0, column=1, pady=10, padx=10)

        privateKeyLoadBtn = Button(master=fileLoadFrame, width=25, text="Ucitaj privatni ključ", command=lambda: self.ctr.load_file('key', 'SIGNATURE_private'))
        privateKeyLoadBtn.grid(row=0, column=3, pady=10, padx=10)

        generateKeysBtn = Button(master=fileLoadFrame, text="Generiraj ključeve", command=lambda: self.ctr.generate_sign_keys())
        generateKeysBtn.grid(row=1, column=1, columnspan=2, sticky=W+E, padx=10, pady=10)

        dataLabel = Label(master=fileLoadFrame, text="Podaci: ")
        dataLabel.grid(row=2, column=0, pady=10, padx=10, sticky=W)

        # --------- 
        global dataFnStr
        dataFnStr = StringVar()
        # ---------
        dataFileName = Label(master=fileLoadFrame, textvariable=dataFnStr, width=30)
        dataFileName.grid(row=2, column=1, pady=10, padx=10)

        dataLoadBtn = Button(master=fileLoadFrame, width=15, text="Ucitaj podatke", command=lambda: self.ctr.load_file('data', 'SIGNATURE'))
        dataLoadBtn.grid(row=2, column=3, pady=10, padx=10)

        # showDataFrame
        showDataFrame = Frame(master=signFrame)
        showDataFrame.pack(padx=10, pady=10)

        privateKeyDisplayName = Label(master=showDataFrame, text="Privatni ključ: ", width=15)
        privateKeyDisplayName.grid(row=0, column=0, pady=10, padx=10)

        global privateKeyValueStr
        privateKeyValueStr = StringVar()
        privateKeyDisplayEntry = Entry(master=showDataFrame, state=DISABLED, textvariable=privateKeyValueStr)
        privateKeyDisplayEntry.grid(row=0, column=1, columnspan=3, sticky=W+E)

        dataDisplayLabel = Label(master=showDataFrame, text="Podaci: ", width=15)
        dataDisplayLabel.grid(row=2, column=0, pady=10, padx=10)

        global dataDisplaySignTxtBox
        dataDisplaySignTxtBox = Text(master=showDataFrame, height=10, width=50)
        dataDisplaySignTxtBox.grid(row=2, column=1)

        # cryptButtonsFrame
        cryptButtonsFrame = Frame(master=signFrame)
        cryptButtonsFrame.pack(pady=10, padx=10)

        encryptBtn = Button(master=cryptButtonsFrame, text="Potpiši", width=20, command=lambda: self.ctr.sign_file())
        encryptBtn.grid(row=0, column=0, pady=10, sticky=E)

        # cryptResultFrame
        cryptResultFrame = Frame(master=signFrame)
        cryptResultFrame.pack(pady=10, padx=10)

        resultDisplayLabel = Label(master=cryptResultFrame, text="Rezultat: ", width=15)
        resultDisplayLabel.grid(row=1, column=0, pady=10, padx=2)

        global resultDisplaySignTxtBox
        resultDisplaySignTxtBox = Text(master=cryptResultFrame, height=10, width=50)
        resultDisplaySignTxtBox.grid(row=1, column=1)
        #endregion

        #region checkFrame
        # checkFrame
        checkFrame = Frame(master=self)
        checkFrame.grid(row=1, column=0, sticky=N+S+E+W)

        # fileLoadFrame
        fileLoadFrame = Frame(master=checkFrame)
        fileLoadFrame.pack(pady=10, padx=10)

        publicKeyLabel = Label(fileLoadFrame, text="Javni ključ: ")
        publicKeyLabel.grid(row=0, column=0, pady=10, padx=10)

        global publicKeyFnStr
        publicKeyFnStr = StringVar()
        publicKeyFileName = Label(master=fileLoadFrame, textvariable=publicKeyFnStr, width=30)
        publicKeyFileName.grid(row=0, column=1, pady=10, padx=10)

        publicKeyLoadBtn = Button(master=fileLoadFrame, width=15, text="Učitaj javni kljuc", command=lambda: self.ctr.load_file('key', 'SIGNATURE_public'))
        publicKeyLoadBtn.grid(row=0, column=3, pady=10, padx=10)

        signLabel = Label(fileLoadFrame, text="Potpis: ")
        signLabel.grid(row=1, column=0, pady=10, padx=10)

        global signFnStr
        signFnStr = StringVar()
        signFileName = Label(master=fileLoadFrame, textvariable=signFnStr, width=30)
        signFileName.grid(row=1, column=1, pady=10, padx=10)

        signLoadBtn = Button(master=fileLoadFrame, width=15, text="Učitaj potpis", command=lambda: self.ctr.load_file('key', 'SIGNATURE_sign'))
        signLoadBtn.grid(row=1, column=3, pady=10, padx=10)

        dataLabel = Label(master=fileLoadFrame, text="Podaci: ")
        dataLabel.grid(row=2, column=0, pady=10, padx=10, sticky=W)

        dataFileName = Label(master=fileLoadFrame, textvariable=dataFnStr, width=30)
        dataFileName.grid(row=2, column=1, pady=10, padx=10)

        dataLoadBtn = Button(master=fileLoadFrame, width=15, text="Ucitaj podatke", command=lambda: self.ctr.load_file('data', 'SIGNATURE'))
        dataLoadBtn.grid(row=2, column=3, pady=10, padx=10)

        # showDataFrame
        showDataFrame = Frame(master=checkFrame)
        showDataFrame.pack(padx=10, pady=10)

        publicKeyDisplayName = Label(master=showDataFrame, text="Javni ključ: ", width=15)
        publicKeyDisplayName.grid(row=0, column=0, pady=10, padx=10)

        global publicKeyValueStr
        publicKeyValueStr = StringVar()
        publicKeyDisplayEntry = Entry(master=showDataFrame, state=DISABLED, textvariable=publicKeyValueStr)
        publicKeyDisplayEntry.grid(row=0, column=1, columnspan=3, sticky=W+E)

        dataDisplayLabel = Label(master=showDataFrame, text="Podaci: ", width=15)
        dataDisplayLabel.grid(row=2, column=0, pady=10, padx=10)

        global dataDisplayCheckTxtBox
        dataDisplayCheckTxtBox = Text(master=showDataFrame, height=10, width=50)
        dataDisplayCheckTxtBox.grid(row=2, column=1)

        # cryptButtonsFrame
        cryptButtonsFrame = Frame(master=checkFrame)
        cryptButtonsFrame.pack(pady=10, padx=10)

        encryptBtn = Button(master=cryptButtonsFrame, text="Provjeri", width=20, command=lambda: self.ctr.check_file())
        encryptBtn.grid(row=0, column=0, pady=10, sticky=E)

        # cryptResultFrame
        cryptResultFrame = Frame(master=checkFrame)
        cryptResultFrame.pack(pady=10, padx=10)

        resultDisplayLabel = Label(master=cryptResultFrame, text="Rezultat: ", width=15)
        resultDisplayLabel.grid(row=1, column=0, pady=10, padx=2)

        global resultDisplayCheckTxtBox
        resultDisplayCheckTxtBox = Text(master=cryptResultFrame, height=10, width=50)
        resultDisplayCheckTxtBox.grid(row=1, column=1)
        #endregion
        
        signFrame.tkraise()

    def show_data(which, filename, value):
        if which == 'key_public':
            publicKeyFnStr.set(filename)
            publicKeyValueStr.set(value)
        elif which == 'key_private':
            privateKeyFnStr.set(filename)
            privateKeyValueStr.set(value)
        elif which == 'sign':
            signFnStr.set(filename)
        elif which == 'data':
            dataFnStr.set(filename)
            dataDisplaySignTxtBox.config(state=NORMAL)
            dataDisplaySignTxtBox.delete(1.0, END)
            dataDisplaySignTxtBox.insert(END, value)
            dataDisplaySignTxtBox.config(state=DISABLED)
            dataDisplayCheckTxtBox.config(state=NORMAL)
            dataDisplayCheckTxtBox.delete(1.0, END)
            dataDisplayCheckTxtBox.insert(END, value)
            dataDisplayCheckTxtBox.config(state=DISABLED)

    def show_signature_result(which, result):
        if which == 'sign':
            resultDisplaySignTxtBox.config(state=NORMAL)
            resultDisplaySignTxtBox.delete(1.0, END)
            resultDisplaySignTxtBox.insert(END, result)
            resultDisplaySignTxtBox.config(state=DISABLED)
        elif which == 'check':
            resultDisplayCheckTxtBox.config(state=NORMAL)
            resultDisplayCheckTxtBox.delete(1.0, END)
            resultDisplayCheckTxtBox.insert(END, result)
            resultDisplayCheckTxtBox.config(state=DISABLED)
