# Amrit Pangeni
from tkinter import ttk
from tkinter import *


class Password_Cracker:
    def __init__(self):
        self.root = Tk()
        self.root.config(background="#abcdef")
        self.root.title("AMR Password Hash Cracking Tool")
        self.root.geometry("800x500")
        self.root.resizable(0, 0)
        self.root.iconbitmap("icon.ico")

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack()

        self.BruteForce = Frame(self.notebook, width=1000, height=700, bg="#70adda")
        self.Dictionary = Frame(self.notebook, width=1000, height=700, bg="#70adda")
        self.RainbowTable = Frame(self.notebook, width=1000, height=700, bg="#70adda")

        self.BruteForce.pack(fill=BOTH, expand=1)
        self.Dictionary.pack(fill=BOTH, expand=1)
        self.RainbowTable.pack(fill=BOTH, expand=1)

        self.notebook.add(self.BruteForce,
                          text="                                        Brute Force                                     ")
        self.notebook.add(self.Dictionary,
                          text="                            Dictionary Attack                                       ")
        self.notebook.add(self.RainbowTable,
                          text="                                   Rainbow Table Attack                                       ")

        # Brute Force Attack GUI
        label1 = Label(self.BruteForce, text="Hash Type & Password Hash to Crack :", bg="#abcdef",
                       font="cambria 14")
        label1.place(x=30,y=15)

        self.hashInput = StringVar()
        hash_entry = Entry(self.BruteForce, font="cambria 12", width="81", textvariable=self.hashInput)
        hash_entry.place(x=30, y=80)

        self.comboBox = ttk.Combobox(self.BruteForce, values=("Sha1", "Sha2", "Md5"), state='readonly')
        self.comboBox.set("Md5")
        self.comboBox.place(x=30, y=50)

        label2 = Label(self.BruteForce, text="Minimum Length :", bg="#abcdef",
                       font="cambria 14")
        label2.place(x=30,y=120)

        label3 = Label(self.BruteForce, text="Minimum Length :", bg="#abcdef",
                       font="cambria 14")
        label3.place(x=320,y=120)

        self.minInput = StringVar()
        entry_box1 = Entry(self.BruteForce, font="cambria 15", width="10", textvariable=self.minInput)
        entry_box1.place(x=195, y=120)

        entry_box1 = Entry(self.BruteForce, font="cambria 15", width="10", textvariable=self.minInput)
        entry_box1.place(x=485, y=120)

        style_ = ttk.Style()
        style_.configure('my.TButton',font="cambria 14")

        self.buttonBrute = ttk.Button(self.BruteForce, text="Start Attack",style = 'my.TButton')
        self.buttonBrute.place(x=330, y=180)

        self.Result_Label = Label(self.BruteForce)

        self.root.mainloop()

    def bruteForceAttack(self):
        pass

Password_Cracker()
