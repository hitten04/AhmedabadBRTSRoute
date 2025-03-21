from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from app import IRCTCRoute
import staticData as s

class Window_1:
    def __init__(self, master):
        self.master = master
        self.master.title("IRCTC Shortest Route Finder")
        self.master.geometry('1350x750')
        self.master.minsize(500, 500)
        self.master.config(bg='#1e1e2e')  # Dark background

        self.Frame = Frame(self.master, bg='#1e1e2e')
        self.Frame.pack()

        self.initial_stop = StringVar()
        self.target_stop = StringVar()
        self.route = StringVar()
        self.dis = StringVar()

        self.Lbl_Title = Label(self.Frame, text='Search Route', font=('Arial', 40, 'bold'), bg='#1e1e2e', fg='#ffcc00')
        self.Lbl_Title.grid(row=0, column=0, columnspan=3, pady=40)

        self.Login_Frame_1 = LabelFrame(self.Frame, relief='ridge', bg='#282a36', fg='white', bd=10, font=('Arial', 20, 'bold'))
        self.Login_Frame_1.grid(row=1, column=0, padx=20, pady=10)
        
        self.Login_Frame_2 = LabelFrame(self.Frame, relief='ridge', bg='#282a36', fg='white', bd=10, font=('Arial', 20, 'bold'))
        self.Login_Frame_2.grid(row=2, column=0, padx=20, pady=10)
        
        self.Login_Frame_3 = LabelFrame(self.Frame, relief='ridge', bg='#282a36', fg='white', bd=10, font=('Arial', 20, 'bold'))
        self.Login_Frame_3.grid(row=3, column=0, padx=20, pady=10)

        # Labels and Entries
        self.Label_initial_stop = Label(self.Login_Frame_1, text='Initial Stop:', font=('Arial', 18, 'bold'), bg='#282a36', fg='white')
        self.Label_initial_stop.grid(row=0, column=0, padx=10, pady=10)
        self.text_initial_stop = ttk.Combobox(self.Login_Frame_1, values=s.railway_stations, font=('Arial', 16), textvariable=self.initial_stop)
        self.text_initial_stop.grid(row=0, column=1, padx=10, pady=10)
        
        self.Label_target_stop = Label(self.Login_Frame_1, text='Target Stop:', font=('Arial', 18, 'bold'), bg='#282a36', fg='white')
        self.Label_target_stop.grid(row=1, column=0, padx=10, pady=10)
        self.text_target_stop = ttk.Combobox(self.Login_Frame_1, values=s.railway_stations, font=('Arial', 16), textvariable=self.target_stop)
        self.text_target_stop.grid(row=1, column=1, padx=10, pady=10)

        self.Label_route = Label(self.Login_Frame_3, text='Shortest Route:', font=('Arial', 18, 'bold'), bg='#282a36', fg='white')
        self.Label_route.grid(row=0, column=0, padx=10, pady=10)
        self.text_route = Entry(self.Login_Frame_3, font=('Arial', 16), textvariable=self.route, width=50, bg='#44475a', fg='white')
        self.text_route.grid(row=0, column=1, padx=10, pady=10)

        self.Label_distance = Label(self.Login_Frame_3, text='Distance:', font=('Arial', 18, 'bold'), bg='#282a36', fg='white')
        self.Label_distance.grid(row=1, column=0, padx=10, pady=10)
        self.text_distance = Entry(self.Login_Frame_3, font=('Arial', 16), textvariable=self.dis, state=DISABLED, bg='#44475a', fg='white')
        self.text_distance.grid(row=1, column=1, padx=10, pady=10)

        # Buttons
        btn_style = {'font': ('Arial', 15, 'bold'), 'width': 12, 'bd': 3, 'relief': 'ridge', 'fg': 'white'}

        self.btnSearch = Button(self.Login_Frame_2, text='Search', bg='#50fa7b', **btn_style, command=self.search)
        self.btnSearch.grid(row=0, column=0, padx=10, pady=10)

        self.btnReset = Button(self.Login_Frame_2, text='Reset', bg='#ff5555', **btn_style, command=self.Reset)
        self.btnReset.grid(row=0, column=1, padx=10, pady=10)

        self.btnExit = Button(self.Login_Frame_2, text='Exit', bg='#bd93f9', **btn_style, command=self.Exit)
        self.btnExit.grid(row=0, column=2, padx=10, pady=10)

    def search(self):
        if self.target_stop.get() == self.initial_stop.get():
            tkinter.messagebox.showerror("Error", "Both stations cannot be the same!")
            return
        values = IRCTCRoute.search_route(IRCTCRoute(), self.initial_stop.get(), self.target_stop.get())
        if values != "Invalid bus stops.":
            self.route.set(' → '.join(values[0]))
            self.dis.set(str(values[1]))
        else:
            tkinter.messagebox.showerror("Error", "Stations not found!")

    def Reset(self):
        self.initial_stop.set("")
        self.target_stop.set("")
        self.route.set("")
        self.dis.set("")
        self.text_initial_stop.focus()

    def Exit(self):
        if tkinter.messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.master.destroy()

root = Tk()
app = Window_1(root)
root.mainloop()