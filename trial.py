#importing tkinter and the message boxes and scrolledtext widget
from tkinter import *
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
#the inbuilt csv function allows to read and open csv files
import csv

#setting font
LARGE_FONT = ("Verdana", 12)


#_______________________________________________________________________________
#_______________________SWITCHING FRAMES________________________________________________________
class Frames(tk.Tk):

#__________________________INITIALISE_____________________________________________________
    def __init__(self, *args, **kwargs):  #args and kwargs are used to pass arguments in the functions
        
        tk.Tk.__init__(self, *args, **kwargs )
        # a container which contains the frames
        #args are arguments, indicating any number of variables, a list of arguments,
        # kwargs- keyboard arguments,we are passing through dictionaries,
        container = tk.Frame(self)#defining it as a frame
        #fills the container frame with the pages
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}
        # a for loop to switch between the frames
        #main page is the create array frame
        #sort function is the sort and search page
        #help page is for online help
        for F in (MainPage, Help, Suspensions, Suspensions_Heave, Suspensions_Other, Drivetrain, Tyres, Brakes):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")
            frame.config(bg='#e8f8f5') #colour scheme
        self.show_frame(MainPage)
#____________________________SHOW FRAME___________________________________________________
    def show_frame(self, cont):
        #raising the frame to the wanted frame
        frame = self.frames[cont]
        frame.tkraise()

#_______________________________________________________________________________
#___________________________CREATE ARRAY PAGE____________________________________________________
class MainPage(tk.Frame):
#________________________INITIALISE_______________________________________________________
    #arrangement of buttons and input and labels
    #you need to use controller to pass variables between classes
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        # label 
        lblE = tk.Label(self,  text='daniel avocado')#defining it as a label
        lblE.place(x=10, y=50)#placement
        lblE.config(bg='#e8f8f5', fg='#255D83')#colour scheme
        inputE = Entry(self)#defining it as a inputbox
        inputE.place(x=100, y=50)#placement
        inputE.config(bg='#255D83', fg='#e8f8f5')#colour scheme

        #button to switch to other pages, lambda is a must when switching pages
        #defining it as a button
        btnSort = tk.Button(self, text="Main",command=lambda: controller.show_frame(MainPage))
        btnSort.place(x=0, y=0)#placement
        btnSort.config(bg='#255D83', fg='#e8f8f5')#colour scheme

        btnSort = tk.Button(self, text="Suspensions",command=lambda: controller.show_frame(Suspensions))
        btnSort.place(x=38, y=0)#placement
        btnSort.config(bg='#255D83', fg='#e8f8f5')#colour scheme

        btnSort = tk.Button(self, text="Suspensions Heave",command=lambda: controller.show_frame(Suspensions_Heave))
        btnSort.place(x=114, y=0)#placement
        btnSort.config(bg='#255D83', fg='#e8f8f5')#colour scheme

        btnSort = tk.Button(self, text="Suspensions Other",command=lambda: controller.show_frame(Suspensions_Other))
        btnSort.place(x=225, y=0)#placement
        btnSort.config(bg='#255D83', fg='#e8f8f5')#colour scheme

        btnSort = tk.Button(self, text="Tyres",command=lambda: controller.show_frame(Tyres))
        btnSort.place(x=333, y=0)#placement
        btnSort.config(bg='#255D83', fg='#e8f8f5')#colour scheme

        btnSort = tk.Button(self, text="Drivetrain",command=lambda: controller.show_frame(Drivetrain))
        btnSort.place(x=370, y=0)#placement
        btnSort.config(bg='#255D83', fg='#e8f8f5')#colour scheme

        btnSort = tk.Button(self, text="Brakes",command=lambda: controller.show_frame(Brakes))
        btnSort.place(x=431, y=0)#placement
        btnSort.config(bg='#255D83', fg='#e8f8f5')#colour scheme

        #a exit button to exit the gui
        #defining it as a button
        #use lambda to pass the main window as a function to destroy it in the module
        btnExit =  tk.Button(self, text="Exit", command=lambda: self.exit(window))
        btnExit.place(x=400, y=400)#placement
        btnExit.config(bg='#255D83', fg='#e8f8f5')#colour scheme

        #button to switch to help page, the command lambda is a must when switching pages
        #defining it as a button
        btn = tk.Button(self, text="Help",command=lambda: controller.show_frame(Help))
        btn.place(x=300, y=400)#placement
        btn.config(bg='#255D83', fg='#e8f8f5')#colour scheme



#_________________________CLOSE PROGRAM______________________________________________________
    def exit(self,window):
        #submodule which links to the exit button to close the program
        
        window.destroy()
#_______________________________________________________________________________
#________________________ABOUT US PAGE______________________________________________________        
class Help(tk.Frame):
#_____________________INITIALISE__________________________________________________________
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Help im failing uni", font=LARGE_FONT)#defining it as a label
        label.pack(pady=10, padx=10)#placement
        label.config(bg='#e8f8f5', fg='#255D83')#colour scheme

        lblE = tk.Label(self,  text='dumbass trimesters')#defining it as a label
        lblE.place(x=10, y=50)#placement
        lblE.config(bg='#e8f8f5', fg='#255D83')#colour scheme


        #defining it as a button
        mainpagebtn = tk.Button(self, text="Main page",command=lambda: controller.show_frame(MainPage))
        mainpagebtn.place(y=470, x=50)#placement
        mainpagebtn.config(bg='#255D83', fg='#e8f8f5')#colour scheme

#_______________________________________________________________________________
#________________________ABOUT US PAGE______________________________________________________        
class Suspensions(tk.Frame):
#_____________________INITIALISE__________________________________________________________
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Suspensions", font=("Arial", 25))#defining it as a label
        label.pack(pady=10, padx=10)#placement
        label.config(bg='#e8f8f5', fg='#255D83')#colour scheme

        lblE = tk.Label(self,  text='FRONT', font=LARGE_FONT)#defining it as a label
        lblE.place(x=10, y=50)#placement
        lblE.config(bg='#e8f8f5', fg='#255D83')#colour scheme

        lblE = tk.Label(self,  text='REAR', font=LARGE_FONT)#defining it as a label
        lblE.place(x=410, y=50)#placement
        lblE.config(bg='#e8f8f5', fg='#255D83')#colour scheme

        susp_params = ['TOE_OUT', 'STATIC_CAMBER', 'DAMP_BUMP', 'DAMP_FAST_BUMP', 
                        'DAMP_REBOUND', 'DAMP_FAST_REBOUND', 'SPRING_RATE', 'ROD_LENGTH', 
                        'PACKER_RANGE', 'BUMP_STOP_RATE', 'TRACK']

        label_y = 100
        front_input = []
        for i in susp_params:
            lblE = tk.Label(self,  text=i)#defining it as a label
            lblE.place(x=10, y=label_y)#placement
            lblE.config(bg='#e8f8f5', fg='#255D83')#colour scheme
            inputE = Entry(self)#defining it as a inputbox
            inputE.place(x=180, y=label_y)#placement
            inputE.config(bg='#255D83', fg='#e8f8f5')#colour scheme
            front_input.append(inputE)
            label_y = label_y +50

        label_y = 100
        rear_input = []
        for i in susp_params:
            lblE = tk.Label(self,  text=i)#defining it as a label
            lblE.place(x=410, y=label_y)#placement
            lblE.config(bg='#e8f8f5', fg='#255D83')#colour scheme
            inputE = Entry(self)#defining it as a inputbox
            inputE.place(x=580, y=label_y)#placement
            inputE.config(bg='#255D83', fg='#e8f8f5')#colour scheme
            rear_input.append(inputE)
            label_y = label_y +50

        #defining it as a button
        mainpagebtn = tk.Button(self, text="Main page",command=lambda: controller.show_frame(MainPage))
        mainpagebtn.place(y=690, x=50)#placement
        mainpagebtn.config(bg='#255D83', fg='#e8f8f5')#colour scheme

#________________________ABOUT US PAGE______________________________________________________        
class Suspensions_Heave(tk.Frame):
#_____________________INITIALISE__________________________________________________________
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Suspensions Heave", font=("Arial", 25))#defining it as a label
        label.pack(pady=10, padx=10)#placement
        label.config(bg='#e8f8f5', fg='#255D83')#colour scheme

        lblE = tk.Label(self,  text='FRONT', font=LARGE_FONT)#defining it as a label
        lblE.place(x=10, y=50)#placement
        lblE.config(bg='#e8f8f5', fg='#255D83')#colour scheme

        lblE = tk.Label(self,  text='REAR', font=LARGE_FONT)#defining it as a label
        lblE.place(x=410, y=50)#placement
        lblE.config(bg='#e8f8f5', fg='#255D83')#colour scheme

        susp_params = ['ROD_LENGTH', 'SPRING_RATE', 'DAMP_BUMP', 'DAMP_FAST_BUMP', 
                        'DAMP_REBOUND', 'DAMP_FAST_REBOUND']

        label_y = 100
        front_input = []
        for i in susp_params:
            lblE = tk.Label(self,  text=i)#defining it as a label
            lblE.place(x=10, y=label_y)#placement
            lblE.config(bg='#e8f8f5', fg='#255D83')#colour scheme
            inputE = Entry(self)#defining it as a inputbox
            inputE.place(x=180, y=label_y)#placement
            inputE.config(bg='#255D83', fg='#e8f8f5')#colour scheme
            front_input.append(inputE)
            label_y = label_y +50

        label_y = 100
        rear_input = []
        for i in susp_params:
            lblE = tk.Label(self,  text=i)#defining it as a label
            lblE.place(x=410, y=label_y)#placement
            lblE.config(bg='#e8f8f5', fg='#255D83')#colour scheme
            inputE = Entry(self)#defining it as a inputbox
            inputE.place(x=580, y=label_y)#placement
            inputE.config(bg='#255D83', fg='#e8f8f5')#colour scheme
            rear_input.append(inputE)
            label_y = label_y +50

        #defining it as a button
        mainpagebtn = tk.Button(self, text="Main page",command=lambda: controller.show_frame(MainPage))
        mainpagebtn.place(y=690, x=50)#placement
        mainpagebtn.config(bg='#255D83', fg='#e8f8f5')#colour scheme

#_______________________________________________________________________________
#________________________ABOUT US PAGE______________________________________________________        
class Suspensions_Other(tk.Frame):
#_____________________INITIALISE__________________________________________________________
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Suspensions Other", font=("Arial", 25))#defining it as a label
        label.pack(pady=10, padx=10)#placement
        label.config(bg='#e8f8f5', fg='#255D83')#colour scheme

        lblE = tk.Label(self,  text='ARB', font=LARGE_FONT)#defining it as a label
        lblE.place(x=10, y=50)#placement
        lblE.config(bg='#e8f8f5', fg='#255D83')#colour scheme

        lblE = tk.Label(self,  text='BASIC', font=LARGE_FONT)#defining it as a label
        lblE.place(x=410, y=50)#placement
        lblE.config(bg='#e8f8f5', fg='#255D83')#colour scheme

        arb_params = ['FRONT', 'REAR']
        BASIC_params = ['WHEELBASE', 'CG_LOCATION']

        label_y = 100
        front_input = []
        for i in arb_params:
            lblE = tk.Label(self,  text=i)#defining it as a label
            lblE.place(x=10, y=label_y)#placement
            lblE.config(bg='#e8f8f5', fg='#255D83')#colour scheme
            inputE = Entry(self)#defining it as a inputbox
            inputE.place(x=180, y=label_y)#placement
            inputE.config(bg='#255D83', fg='#e8f8f5')#colour scheme
            front_input.append(inputE)
            label_y = label_y +50

        label_y = 100
        rear_input = []
        for i in BASIC_params:
            lblE = tk.Label(self,  text=i)#defining it as a label
            lblE.place(x=410, y=label_y)#placement
            lblE.config(bg='#e8f8f5', fg='#255D83')#colour scheme
            inputE = Entry(self)#defining it as a inputbox
            inputE.place(x=580, y=label_y)#placement
            inputE.config(bg='#255D83', fg='#e8f8f5')#colour scheme
            rear_input.append(inputE)
            label_y = label_y +50

        #defining it as a button
        mainpagebtn = tk.Button(self, text="Main page",command=lambda: controller.show_frame(MainPage))
        mainpagebtn.place(y=690, x=50)#placement
        mainpagebtn.config(bg='#255D83', fg='#e8f8f5')#colour scheme
#_______________________________________________________________________________
#________________________ABOUT US PAGE______________________________________________________        
class Tyres(tk.Frame):
#_____________________INITIALISE__________________________________________________________
    def __init__(self, parent, controller):
        
        
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Tyres", font=("Arial", 25))#defining it as a label
        label.pack(pady=10, padx=10)#placement
        label.config(bg='#e8f8f5', fg='#255D83')#colour scheme

        lblE = tk.Label(self,  text='FRONT', font=LARGE_FONT)#defining it as a label
        lblE.place(x=10, y=50)#placement
        lblE.config(bg='#e8f8f5', fg='#255D83')#colour scheme

        lblE = tk.Label(self,  text='REAR', font=LARGE_FONT)#defining it as a label
        lblE.place(x=410, y=50)#placement
        lblE.config(bg='#e8f8f5', fg='#255D83')#colour scheme

        susp_params = ['PRESSURE_STATIC']

        label_y = 100
        front_input = []
        for i in susp_params:
            lblE = tk.Label(self,  text=i)#defining it as a label
            lblE.place(x=10, y=label_y)#placement
            lblE.config(bg='#e8f8f5', fg='#255D83')#colour scheme
            inputE = Entry(self)#defining it as a inputbox
            inputE.place(x=180, y=label_y)#placement
            inputE.config(bg='#255D83', fg='#e8f8f5')#colour scheme
            front_input.append(inputE)
            label_y = label_y +50

        label_y = 100
        rear_input = []
        for i in susp_params:
            lblE = tk.Label(self,  text=i)#defining it as a label
            lblE.place(x=410, y=label_y)#placement
            lblE.config(bg='#e8f8f5', fg='#255D83')#colour scheme
            inputE = Entry(self)#defining it as a inputbox
            inputE.place(x=580, y=label_y)#placement
            inputE.config(bg='#255D83', fg='#e8f8f5')#colour scheme
            rear_input.append(inputE)
            label_y = label_y +50

        #defining it as a button
        mainpagebtn = tk.Button(self, text="Main page",command=lambda: controller.show_frame(MainPage))
        mainpagebtn.place(y=690, x=50)#placement
        mainpagebtn.config(bg='#255D83', fg='#e8f8f5')#colour scheme

#_______________________________________________________________________________
#________________________ABOUT US PAGE______________________________________________________        
class Drivetrain(tk.Frame):
#_____________________INITIALISE__________________________________________________________
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Drivetrain", font=("Arial", 25))#defining it as a label
        label.pack(pady=10, padx=10)#placement
        label.config(bg='#e8f8f5', fg='#255D83')#colour scheme

        lblE = tk.Label(self,  text='DIFFERENTIAL', font=LARGE_FONT)#defining it as a label
        lblE.place(x=10, y=50)#placement
        lblE.config(bg='#e8f8f5', fg='#255D83')#colour scheme


        susp_params = ['POWER', 'COAST', 'PRELOAD']

        label_y = 100
        front_input = []
        for i in susp_params:
            lblE = tk.Label(self,  text=i)#defining it as a label
            lblE.place(x=10, y=label_y)#placement
            lblE.config(bg='#e8f8f5', fg='#255D83')#colour scheme
            inputE = Entry(self)#defining it as a inputbox
            inputE.place(x=180, y=label_y)#placement
            inputE.config(bg='#255D83', fg='#e8f8f5')#colour scheme
            front_input.append(inputE)
            label_y = label_y +50

        #defining it as a button
        mainpagebtn = tk.Button(self, text="Main page",command=lambda: controller.show_frame(MainPage))
        mainpagebtn.place(y=690, x=50)#placement
        mainpagebtn.config(bg='#255D83', fg='#e8f8f5')#colour scheme

#_______________________________________________________________________________
#________________________ABOUT US PAGE______________________________________________________        
class Brakes(tk.Frame):
#_____________________INITIALISE__________________________________________________________
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Brakes", font=("Arial", 25))#defining it as a label
        label.pack(pady=10, padx=10)#placement
        label.config(bg='#e8f8f5', fg='#255D83')#colour scheme

        lblE = tk.Label(self,  text='Data', font=LARGE_FONT)#defining it as a label
        lblE.place(x=10, y=50)#placement
        lblE.config(bg='#e8f8f5', fg='#255D83')#colour scheme


        susp_params = ['FRONT_SHARE', 'MAX_TORQUE']

        label_y = 100
        front_input = []
        for i in susp_params:
            lblE = tk.Label(self,  text=i)#defining it as a label
            lblE.place(x=10, y=label_y)#placement
            lblE.config(bg='#e8f8f5', fg='#255D83')#colour scheme
            inputE = Entry(self)#defining it as a inputbox
            inputE.place(x=180, y=label_y)#placement
            inputE.config(bg='#255D83', fg='#e8f8f5')#colour scheme
            front_input.append(inputE)
            label_y = label_y +50

        #defining it as a button
        mainpagebtn = tk.Button(self, text="Main page",command=lambda: controller.show_frame(MainPage))
        mainpagebtn.place(y=690, x=50)#placement
        mainpagebtn.config(bg='#255D83', fg='#e8f8f5')#colour scheme



#_______________________________________________________________________________
#______________________MAIN PROGRAM_________________________________________________________
window = Frames()#defining what the window will show --- it will have frames(pages)
window.title('Redback Asseto Corsa Launcher')
window.config(bg='#e8f8f5')#colour scheme
window.geometry("800x800")#size of window
window.resizable(width=False, height=False)#not letting the user resize the window
window.mainloop()#running the gui
