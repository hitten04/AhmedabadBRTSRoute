from tkinter import *
import tkinter.messagebox
import os

class Window_1:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Window")
        self.master.geometry('1350x750')
        self.master.minsize(500, 500)
        self.master.config(bg="#1e1e2e")  # Dark modern background

        self.Frame = Frame(self.master, bg="#1e1e2e")
        self.Frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        # Title Label
        self.Lbl_Title = Label(
            self.Frame,
            text="IRCTC Route System",
            font=("Arial", 40, "bold"),
            bg="#1e1e2e",
            fg="#50fa7b",
        )
        self.Lbl_Title.grid(row=0, column=0, columnspan=3, pady=40)

        self.Lbl_Subtitle = Label(
            self.Frame,
            text="Login",
            font=("Arial", 25, "bold"),
            bg="#1e1e2e",
            fg="#bd93f9",
        )
        self.Lbl_Subtitle.grid(row=1, column=0, columnspan=2, pady=35)

        # Login Frames
        self.Login_Frame_1 = LabelFrame(
            self.Frame,
            width=1350,
            height=600,
            relief="ridge",
            bg="#282a36",
            bd=15,
            font=("Arial", 20, "bold"),
        )
        self.Login_Frame_1.grid(row=2, column=0)

        self.Login_Frame_2 = LabelFrame(
            self.Frame,
            width=1000,
            height=600,
            relief="ridge",
            bg="#282a36",
            bd=15,
            font=("Arial", 20, "bold"),
        )
        self.Login_Frame_2.grid(row=3, column=0)

        # Labels and Entries
        self.Label_Username = Label(
            self.Login_Frame_1,
            text="Username",
            font=("Arial", 20, "bold"),
            bg="#282a36",
            fg="#f8f8f2",
            bd=20,
        )
        self.Label_Username.grid(row=0, column=0)

        self.text_Username = Entry(
            self.Login_Frame_1,
            font=("Arial", 20, "bold"),
            textvariable=self.Username,
            bg="#44475a",
            fg="white",
            insertbackground="white",
            relief=FLAT,
        )
        self.text_Username.grid(row=0, column=1, padx=50)

        self.Label_Password = Label(
            self.Login_Frame_1,
            text="Password",
            font=("Arial", 20, "bold"),
            bg="#282a36",
            fg="#f8f8f2",
            bd=20,
        )
        self.Label_Password.grid(row=1, column=0)

        self.text_Password = Entry(
            self.Login_Frame_1,
            font=("Arial", 20, "bold"),
            show="*",
            textvariable=self.Password,
            bg="#44475a",
            fg="white",
            insertbackground="white",
            relief=FLAT,
        )
        self.text_Password.grid(row=1, column=1)

        # Buttons with hover effects
        self.btnLogin = Button(
            self.Login_Frame_2,
            text="Login",
            width=10,
            font=("Arial", 15, "bold"),
            bg="#50fa7b",
            fg="black",
            activebackground="#69ff94",
            activeforeground="black",
            relief=FLAT,
            command=self.Login,
        )
        self.btnLogin.grid(row=3, column=0, padx=8, pady=20)

        self.btnReset = Button(
            self.Login_Frame_2,
            text="Reset",
            width=10,
            font=("Arial", 15, "bold"),
            bg="#ffb86c",
            fg="black",
            activebackground="#ffdab9",
            activeforeground="black",
            relief=FLAT,
            command=self.Reset,
        )
        self.btnReset.grid(row=3, column=1, padx=8, pady=20)

        self.btnExit = Button(
            self.Login_Frame_2,
            text="Exit",
            width=10,
            font=("Arial", 15, "bold"),
            bg="#ff5555",
            fg="black",
            activebackground="#ff6e6e",
            activeforeground="black",
            relief=FLAT,
            command=self.Exit,
        )
        self.btnExit.grid(row=3, column=2, padx=8, pady=20)

    # Login Logic
    def Login(self):
        u = self.Username.get()
        p = self.Password.get()

        if u == "admin" and p == "12345678":
            self.__menu__()
        else:
            tkinter.messagebox.showerror("Login Failed", "Error: Wrong Credentials")
            self.Username.set("")
            self.Password.set("")

    # Reset Function
    def Reset(self):
        self.Username.set("")
        self.Password.set("")
        self.text_Username.focus()

    # Exit Function
    def Exit(self):
        exit_confirm = tkinter.messagebox.askokcancel("Exit", "Confirm if you want to Exit")
        if exit_confirm:
            self.master.destroy()

    # Redirect to Another Script
    def __menu__(self):
        filename = "user.py"
        os.system(filename)
        os.system("python " + filename)

root = Tk()
app = Window_1(root)
root.mainloop()
