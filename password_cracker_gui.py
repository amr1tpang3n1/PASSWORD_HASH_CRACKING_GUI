from tkinter import ttk
from tkinter import *
import itertools
import hashlib


class Password_Cracker:
    def __init__(self):
        """
        This is a python based hash cracking tool which can be useful for cracking the password hashes of different
        algorithms.
        Developed by : Amrit Pangeni
        Available at Github : https://github.com/amr1tpang3n1/PASSWORD_HASH_CRACKING_GUI

        """
        ############################################## ROOT GUI ########################################################
        self.root = Tk()
        self.root.config(background="#abcdef")
        self.root.title("AMRASH Password Hash Cracking Tool")
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

        ################################################################################################################
        ###################################### Brute Force Attack GUI ##################################################
        ################################################################################################################

        labelCharset = Label(self.BruteForce, text="Charset :", bg="#abcdef",
                             font="cambria 14")
        labelCharset.place(x=30, y=10)

        self.Charset = StringVar()
        EntryCharset = Entry(self.BruteForce, font="cambria 15", width="31", textvariable=self.Charset)
        EntryCharset.place(x=115, y=10)
        self.Charset.set("abcdefghijklmnopqrstuvwxyz")

        labelHashT = Label(self.BruteForce, text="Algorithm Type :", bg="#abcdef",
                           font="cambria 14")
        labelHashT.place(x=470, y=10)

        self.comboBox = ttk.Combobox(self.BruteForce, values=("Sha1", "Sha2", "Md5"), state='readonly')
        self.comboBox.set("Md5")
        self.comboBox.place(x=620, y=15)

        label1 = Label(self.BruteForce, text="Password Hash to Crack :", bg="#abcdef",
                       font="cambria 14")
        label1.place(x=30, y=50)

        self.hashInput = StringVar()
        hash_entry = Entry(self.BruteForce, font="cambria 12", width="81", textvariable=self.hashInput)
        hash_entry.place(x=30, y=85)
        hash_entry.focus()

        label2 = Label(self.BruteForce, text="Minimum Length :", bg="#abcdef",
                       font="cambria 14")
        label2.place(x=30, y=120)

        label3 = Label(self.BruteForce, text="Minimum Length :", bg="#abcdef",
                       font="cambria 14")
        label3.place(x=320, y=120)

        self.minInput = StringVar()
        entry_box1 = Entry(self.BruteForce, font="cambria 15", width="10", textvariable=self.minInput)
        entry_box1.place(x=195, y=120)
        self.minInput.trace_variable("w", self.inputValidationMin)

        self.maxInput = StringVar()
        entry_box1 = Entry(self.BruteForce, font="cambria 15", width="10", textvariable=self.maxInput)
        entry_box1.place(x=485, y=120)
        self.maxInput.trace_variable("w", self.inputValidationMax)

        style_ = ttk.Style()
        style_.configure('my.TButton', font="cambria 14")

        self.buttonBrute = ttk.Button(self.BruteForce, text="Start Attack", style='my.TButton',
                                      command=self.validation_algo)
        self.buttonBrute.place(x=330, y=175)

        self.Result_Progress_Text = Text(self.BruteForce, width=92, height=12, bg="white")
        self.Result_Progress_Text.place(x=30, y=220)

        self.Brute_PW_Found = Label(self.BruteForce, bg="#70adda", width="73", font="Cambria 14")
        self.Brute_PW_Found.place(x=30, y=420)

        ################################################################################################################
        ###################################### Dictionary Attack GUI ###################################################
        ################################################################################################################
        labelCharset1 = Label(self.Dictionary, text="Dictionary :", bg="#abcdef",
                              font="cambria 14")
        labelCharset1.place(x=30, y=10)

        self.browse = StringVar()
        EntryCharset1 = Entry(self.Dictionary, font="cambria 15", width=51, textvariable=self.browse)
        EntryCharset1.place(x=140, y=10)

        self.buttonDict = Button(self.Dictionary, text="Browse", command=self.browse_file)
        self.buttonDict.place(x=715, y=10)
        self.buttonDict.focus()

        labelHashT1 = Label(self.Dictionary, text="Algorithm Type :", bg="#abcdef",
                            font="cambria 14")
        labelHashT1.place(x=470, y=45)

        self.comboBox1 = ttk.Combobox(self.Dictionary, values=("Sha1", "Sha2", "Md5"), state='readonly')
        self.comboBox1.set("Md5")
        self.comboBox1.place(x=620, y=50)

        label0 = Label(self.Dictionary, text="Password Hash to Crack :", bg="#abcdef",
                       font="cambria 14")
        label0.place(x=30, y=50)

        self.hashInputdict = StringVar()
        hash_entry1 = Entry(self.Dictionary, font="cambria 12", width="81", textvariable=self.hashInputdict)
        hash_entry1.place(x=30, y=85)
        hash_entry1.focus()

        style_ = ttk.Style()
        style_.configure('my.TButton', font="cambria 14")

        self.buttonDict = ttk.Button(self.Dictionary, text="Start Attack", style='my.TButton',
                                     command=self.validation_algo1)
        self.buttonDict.place(x=330, y=120)

        self.Result_Progress_Text1 = Text(self.Dictionary, width=92, height=16, bg="white")
        self.Result_Progress_Text1.place(x=30, y=160)

        self.Dict_PW_Found = Label(self.Dictionary, bg="#70adda", width="73", font="Cambria 14")
        self.Dict_PW_Found.place(x=30, y=420)

        self.root.mainloop()

    def inputValidationMin(self, *args):
        try:
            a = str(self.minInput.get())
            int(self.minInput.get())
        except Exception:
            a = str(self.minInput.get())
            if a != "":
                self.minInput.set(a[:-1])

    def inputValidationMax(self, *args):
        try:
            a = str(self.maxInput.get())
            int(self.maxInput.get())
        except Exception:
            a = str(self.maxInput.get())
            if a != "":
                self.maxInput.set(a[:-1])

    def validation_algo(self):
        self.Result_Progress_Text.delete('1.0', END)
        self.validationList = [str(self.hashInput.get()), str(self.minInput.get()), str(self.maxInput.get()),
                               str(self.Charset.get()), str(self.comboBox.get())]
        if "" in self.validationList or " " in self.validationList:
            self.Result_Progress_Text.insert("1.0", "All Fields are Mandatory and Can't be left Empty !\n")
        else:
            if self.validationList[4] == "Md5":
                if len(self.validationList[0]) != 32:
                    self.Result_Progress_Text.insert("1.0", "Invalid Hash was Given: Md5 doesn't Match\n")
                else:
                    self.Process_BruteForce()

            elif self.validationList[4] == "Sha1":
                if len(self.validationList[0]) != 40:
                    self.Result_Progress_Text.insert("1.0", "Invalid Hash was Given: Sha1 doesn't Match\n")
                else:
                    self.Process_BruteForce()
            elif self.validationList[4] == "Sha2":
                if len(self.validationList[0]) != 40:
                    self.Result_Progress_Text.insert("1.0", "Invalid Hash was Given: Sha2 doesn't Match\n")
                else:
                    self.Process_BruteForce()

    def Process_BruteForce(self):
        self.Brute_PW_Found.place_forget()

        hash_to_crack = self.validationList[0]
        min = self.validationList[1]
        max = self.validationList[2]
        charset = self.validationList[3]
        hashtype = self.validationList[4]
        flag = False
        for i in range(int(min), int(max) + 1):
            if flag:
                break
            # Generating Combinations of Length i
            combinations = itertools.product(charset, repeat=i)
            for i in combinations:
                if hashtype == "Md5":
                    if hashlib.md5("".join(i).encode()).hexdigest() == hash_to_crack:
                        self.Result_Progress_Text.insert('1.0', f"Password Found: {''.join(i)}\n")
                        self.Brute_PW_Found.config(bg="#f0ea3a",
                                                   text=f"Password Hash Successfully Cracked : {''.join(i)}")
                        self.Brute_PW_Found.place(x=30, y=420)
                        flag = True
                        break

                    else:
                        self.Result_Progress_Text.insert('1.0', f"Trying Password : {''.join(i)}\n")

                elif hashtype == "Sha1":
                    if hashlib.sha1("".join(i).encode()).hexdigest() == hash_to_crack:
                        self.Result_Progress_Text.insert('1.0', f"Password Found {''.join(i)}\n")
                        self.Brute_PW_Found.config(text=f"Password Hash Successfully Cracked : {''.join(i)}",
                                                   bg="#f0ea3a")
                        self.Brute_PW_Found.place(x=30, y=420)
                        flag = True
                        break

                    else:
                        self.Result_Progress_Text.insert('1.0', f"Trying Password : {''.join(i)}\n")

                elif hashtype == "Sha2":
                    if hashlib.md5("".join(i).encode()).hexdigest() == hash_to_crack:
                        self.Result_Progress_Text.insert('1.0', f"Password Found: {''.join(i)}\n")
                        self.Brute_PW_Found.config(text=f"Password Hash Successfully Cracked : {''.join(i)}",
                                                   bg="#f0ea3a")
                        self.Brute_PW_Found.place(x=30, y=420)

                        flag = True
                        break
                    else:
                        self.Result_Progress_Text.insert('1.0', f"Trying Password : {''.join(i)}\n")
        if not flag:
            self.Result_Progress_Text.insert('1.0', f'Password not Found , Trying Changing the charset or length\n')

    # Other Hash Algorithms can be added easily as above.
    def validation_algo1(self):
        self.Result_Progress_Text.delete('1.0', END)
        self.validationList1 = [str(self.hashInputdict.get()) ,str(self.browse.get()), str(self.comboBox1.get())]
        if "" in self.validationList1 or " " in self.validationList1:
            self.Result_Progress_Text1.insert("1.0", "All Fields are Mandatory and Can't be left Empty !\n")
        else:
            if self.validationList1[2] == "Md5":
                if len(self.validationList1[0]) != 32:
                    self.Result_Progress_Text1.insert("1.0", "Invalid Hash was Given: Md5 doesn't Match\n")
                else:
                    self.dictionary_attack()

            elif self.validationList1[2] == "Sha1":
                if len(self.validationList1[0]) != 40:
                    self.Result_Progress_Text1.insert("1.0", "Invalid Hash was Given: Sha1 doesn't Match\n")
                else:
                    self.dictionary_attack()

            elif self.validationList1[2] == "Sha2":
                if len(self.validationList1[0]) != 40:
                    self.Result_Progress_Text1.insert("1.0", "Invalid Hash was Given: Sha2 doesn't Match\n")
                else:
                    self.dictionary_attack()

    def dictionary_attack(self):
        self.Dict_PW_Found.place_forget()
        hash_to_crack = str(self.validationList1[0])
        file_path = str(self.validationList1[1])
        hash_type = str(self.validationList1[2])
        flag = False
        try:
            dictionaryFile = open(file_path, 'r')
            # This statement will print every line in the file
            passwordList = []
            for x in dictionaryFile:
                x = x.strip()
                passwordList.append(x)

            if hash_type == "Md5":
                for i in passwordList:
                    password = i.encode()
                    passwordHash = hashlib.md5(password).hexdigest()
                    if passwordHash == hash_to_crack:
                        self.Result_Progress_Text1.insert('1.0',f'Password Cracked Successfully : : {i}\n')
                        self.Dict_PW_Found.config(text = f"Password Successfully Cracked : {i}",bg="#f0ea3a")
                        self.Dict_PW_Found.place(x=30, y=420)

                        flag = True
                        break
                    else:
                        self.Result_Progress_Text1.insert('1.0',f'Attempting {i} as a password ... \n')

            elif hashType.strip() == "Sha2":
                for i in passwordList:
                    password = i.encode()
                    passwordHash = hashlib.sha256(password).hexdigest()
                    if passwordHash == hash_to_crack:
                        self.Result_Progress_Text1.insert('1.0',f'Password Cracked Successfully : {i}\n')
                        self.Dict_PW_Found.config(text = f"Password Successfully Cracked : {i}",bg="#f0ea3a")
                        self.Dict_PW_Found.place(x=30, y=420)

                        flag = True
                        break
                    else:
                        self.Result_Progress_Text1.insert('1.0',f'Attempting {i} as a password ... \n')

            elif hashType.strip() == "Sha1":
                for i in passwordList:
                    password = i.encode()
                    passwordHash = hashlib.sha1(password).hexdigest()
                    if passwordHash == hash_to_crack:
                        self.Result_Progress_Text1.insert('1.0',f'Password Cracked Successfully : {i}\n')
                        self.Dict_PW_Found.config(text = f"Password Successfully Cracked : {i}",bg="#f0ea3a")
                        self.Dict_PW_Found.place(x=30, y=420)

                        flag = True
                        break
                    else:
                        self.Result_Progress_Text1.insert('1.0',f'Attempting {i} as a password ... \n')

            if not flag:
                self.Result_Progress_Text1.insert('1.0', f'Password not Found , Trying Changing the charset or length\n')

        except Exception:
            self.Result_Progress_Text1.insert('1.0', f'Invalid Dictionary File \n')

    def browse_file(self):
        from tkinter import filedialog
        file = filedialog.askopenfilename()
        self.browse.set(file)


if __name__ == "__main__":
    Password_Cracker()
