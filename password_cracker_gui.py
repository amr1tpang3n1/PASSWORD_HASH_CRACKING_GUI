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
        self.minInput.trace_variable("w",self.inputValidationMin)

        self.maxInput = StringVar()
        entry_box1 = Entry(self.BruteForce, font="cambria 15", width="10", textvariable=self.maxInput)
        entry_box1.place(x=485, y=120)
        self.maxInput.trace_variable("w",self.inputValidationMax)

        style_ = ttk.Style()
        style_.configure('my.TButton',font="cambria 14")

        self.buttonBrute = ttk.Button(self.BruteForce, text="Start Attack",style = 'my.TButton')
        self.buttonBrute.place(x=330, y=180)

        self.Result_Progress_Text = Label(self.BruteForce, width = 105, height = 12 , bg = "white", state = "disabled")
        self.Result_Progress_Text.place(x=30,y = 220)

        self.Brute_PW_Found = Label(self.BruteForce,text=f"Cracked Password Will be Displayed Here", bg = "#abcdef", font="Cambria 14")
        self.Brute_PW_Found.place(x=30,y=420)

        self.root.mainloop()

    def bruteForceAttack(self):
        pass

    def inputValidationMin(self,*args):
        try:
            a = str(self.minInput.get())
            int(self.minInput.get())
        except Exception:
            a = str(self.minInput.get())
            if a != "":
                self.minInput.set(a[:-1])

    def inputValidationMax(self,*args):
        try:
            a = str(self.maxInput.get())
            int(self.maxInput.get())
        except Exception:
            a = str(self.maxInput.get())
            if a != "":
                self.maxInput.set(a[:-1])


Password_Cracker()

