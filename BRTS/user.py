from tkinter import*
import tkinter.messagebox                               # for messagebox                                             # for stringvariable                                 # for combobox
from app import BRTSRoute
from tkinter import ttk
import staticData as s

class Window_1:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Window")
        self.master.geometry('1350x750')
        self.master.minsize(500,500)
        self.master.config(bg = 'lightskyblue')
        self.Frame = Frame(self.master, bg = 'lightskyblue')
        self.Frame.pack()


        self.initial_stop = StringVar()                             # x = StringVar()  Holds a string; default value is " "
        self.target_stop = StringVar()
        self.route=StringVar()
        self.dis=StringVar()
        self.Lbl_Title = Label(self.Frame, text = 'Search route', font = ('arial',40,'bold'), bg = 'lightskyblue', fg = 'Black')
        self.Lbl_Title.grid(row = 0, column = 0, columnspan =3, pady = 40)
        
        self.Login_Frame_1 = LabelFrame(self.Frame, width = 1350, height = 600, relief = 'ridge', bg = 'lightskyblue', bd = 15,
                                        font = ('arial',20,'bold'))
        self.Login_Frame_1.grid(row = 1, column =0)
        self.Login_Frame_2 = LabelFrame(self.Frame, width = 1000, height = 600, relief = 'ridge',bg = 'lightskyblue', bd = 15,
                                        font = ('arial',20,'bold'))
        self.Login_Frame_2.grid(row = 2, column = 0)
        self.Login_Frame_3 = LabelFrame(self.Frame, width = 1350, height = 600, relief = 'ridge',bg = 'lightskyblue', bd = 15,
                                        font = ('arial',20,'bold'))
        self.Login_Frame_3.grid(row = 3, column = 0)


        #===================================================LABEL and ENTRIES=======================================================================
        self.Label_initial_stop = Label(self.Login_Frame_1, text = 'initial stop', font = ('arial',20,'bold'), bg = 'lightskyblue', bd = 20)
        self.Label_initial_stop.grid(row = 0, column = 0)
        self.text_initial_stop = ttk.Combobox(self.Login_Frame_1,values=s.bus_sta, font = ('arial',20,'bold'), textvariable = self.initial_stop)
        self.text_initial_stop.grid(row = 0, column = 1, padx = 50)                       
        
        self.Label_target_stop = Label(self.Login_Frame_1, text = 'target stop', font = ('arial',20,'bold'), bg = 'lightskyblue', bd = 20)
        self.Label_target_stop.grid(row = 1, column = 0)
        self.text_target_stop = ttk.Combobox(self.Login_Frame_1, values=s.bus_sta,font = ('arial',20,'bold'), textvariable = self.target_stop)
        self.text_target_stop.grid(row = 1, column = 1) 
        
        self.Label_stop = Label(self.Login_Frame_3, text = 'Shortest Route', font = ('arial',20,'bold'), bg = 'lightskyblue', bd = 20)
        self.Label_stop.grid(row = 0, column = 0)
        self.text_stop = Entry(self.Login_Frame_3, font = ('arial',20,'bold'), textvariable = self.route,width=50)
        self.text_stop.grid(row = 0, column = 1, padx = 50)                       
        
        self.Label_stop = Label(self.Login_Frame_3, text = 'Distance', font = ('arial',20,'bold'), bg = 'lightskyblue', bd = 20)
        self.Label_stop.grid(row = 1, column = 0)
        self.text_stop = Entry(self.Login_Frame_3, font = ('arial',20,'bold'), textvariable = self.dis,state=DISABLED)
        self.text_stop.grid(row = 1, column = 1) 
        #=============================================================BUTTONS=======================================================================
        self.btnLogin = Button(self.Login_Frame_2, text = 'Search', width = 10, font = ('airia',15,'bold'), command = self.search)
        self.btnLogin.grid(row = 3, column = 0, padx = 8, pady = 20)

        self.btnReset = Button(self.Login_Frame_2, text = 'Reset', width = 10, font = ('airia',15,'bold'), command = self.Reset)
        self.btnReset.grid(row = 3, column = 1, padx = 8, pady = 20)

        self.btnExit = Button(self.Login_Frame_2, text = 'Exit', width = 10, font = ('airia',15,'bold'), command = self.Exit)
        self.btnExit.grid(row = 3, column = 2, padx = 8, pady = 20)


        #======================================================Code for Login Button==================================================================
    def search(self):
        if str(self.target_stop.get())==str(self.initial_stop.get()):
            tkinter.messagebox.askokcancel("Login System", "Both Station Not Be Same")
            return
        print(str(self.target_stop.get()))
        values=BRTSRoute.search_route(BRTSRoute(),str(self.initial_stop.get()),str(self.target_stop.get()))
        s=''
        for i in list(values[0]):
            s=f'{s}-->{i}'
        if not (str(values)=="Invalid bus stops."):
            self.route.set(s)
            self.dis.set(str(values[1]))
        else:
            tkinter.messagebox.askokcancel("Login System", "Station Not Found")
        
        #======================================================Code for Reset Button==================================================================
    def Reset(self):
         self.initial_stop.set("")
         self.target_stop.set("")
         self.dis.set("")
         self.route.set("")
         self.text_initial_stop.focus()


        #======================================================Code for Exit Button==================================================================

    def Exit(self):
        self.Exit = tkinter.messagebox.askokcancel("Login System", "Confirm if you want to Exit")
        if self.Exit > 0:
            self.master.destroy()
            return

root = Tk()
app = Window_1(root)
root.mainloop()


