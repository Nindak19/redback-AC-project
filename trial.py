#Sahil And Cullan - 2022
#Redbakc Racing UNSW Data Science 
#importing tkinter and the message boxes and scrolledtext widget
from tkinter import *
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from PIL import Image, ImageTk
#the inbuilt csv function allows to read and open csv files
import csv
import json
from tkinter.filedialog import asksaveasfile

#setting font
LARGE_FONT = ("Verdana", 12)

setup = {  #dictionary of tuples, where order is [static, minimum_value, maximum_value]
    'suspensions.ini': {
    #parameters broken up by file location
        '[FRONT]': { 
            'TOE_OUT': [], #toe_out_l; length increase of steering link in mm
            'STATIC_CAMBER': [], #camber_F
            'DAMP_BUMP': [], #damp_slow_bump_F
            'DAMP_FAST_BUMP': [], #damp_fast_bump_F
            'DAMP_REBOUND': [], #damp_slow_rebound_F
            'DAMP_FAST_REBOUND': [], #damp_fast_rebound_F
            'SPRING_RATE': [], #wheel_rate_F
            'ROD_LENGTH': [],  #rod_length_F
            'PACKER_RANGE': [], #packer_range_F; max sus travel
            'BUMP_STOP_RATE': [], #bump_stop_F; packer rate
            'TRACK': [] #front track
        }, '[HEAVE_FRONT]': {
            'ROD_LENGTH': [],
            'SPRING_RATE': [],
            'DAMP_BUMP': [],
            'DAMP_FAST_BUMP': [],
            'DAMP_REBOUND': [],
            'DAMP_FAST_REBOUND': []
        }, '[REAR]': {
            'TOE_OUT': [], #toe_out_R; lenght of increase of steering link
            'STATIC_CAMBER': [], #camber_R
            'DAMP_BUMP': [], #damp_slow_bump_R
            'DAMP_FAST_BUMP': [], #damp_fast_bump_R
            'DAMP_REBOUND': [], #damp_slow_rebound_R
            'DAMP_FAST_REBOUND': [], #damp_fast_rebound_R
            'SPRING_RATE': [], #wheel_rate_R
            'ROD_LENGTH': [], #rod_length_R
            'PACKER_RANGE': [], #packer_range_R
            'BUMP_STOP_RATE': [], #bump_stop_R
            'TRACK': [] #rear track
        }, '[HEAVE_REAR]': {
            'ROD_LENGTH': [],
            'SPRING_RATE': [],
            'DAMP_BUMP': [],
            'DAMP_FAST_BUMP': [],
            'DAMP_REBOUND': [],
            'DAMP_FAST_REBOUND': []
        }, '[ARB]': {
            'FRONT': [], #arb_F
            'REAR': [] #arb_R
        }, '[BASIC]': {
            'WHEELBASE': [], #wheelbase
            'CG_LOCATION': [] #center of mass
        } 
    }, 'tyres.ini': {
        #tyres.ini file
        '[FRONT]': {
            'PRESSURE_STATIC': [] #pressure_F
        }, '[REAR]': {
            'PRESSURE_STATIC': [] #pressure_R                  
            }
    }, 'drivetrain.ini': {
        #drivetrain.ini
        '[DIFFERENTIAL]': {
            'POWER': [],  #differential on power lock
            'COAST': [], #differential off power lock
            'PRELOAD': [] #diff preload
        }
    }, 'brakes.ini': {
        #brakes.ini
        '[DATA]': {
            'FRONT_SHARE': [], #brake bias
            'MAX_TORQUE': [] #brake power
        }
    }, 'race.ini': {
        #race.ini
        '[RACE]': {
            "TRACK": [],
            "MODEL": []
        }, "[TEMPERATURE]": {
            "AMBIENT": [],
            "ROAD": []
        }
    }
}

# def writetoJSONFile(path, setup):
#     json.dump(setup, path)

def populate_setup(ini_name, list1, list2, header1, header2):
    # Reset each of the values for header1 to enter new values
    for parameter in setup[ini_name][header1]:
        setup[ini_name][header1][parameter] = []
    for value in list1:
        setup_value = value.get()
        for parameter in setup[ini_name][header1]:
            if setup[ini_name][header1][parameter] == []:
                setup[ini_name][header1][parameter] = setup_value
                break
    if list2 == []:
        return
    else:
        # Reset each of the values for header2 to enter new values
        for parameter in setup[ini_name][header2]:
            setup[ini_name][header2][parameter] = []
        for value in list2:
            setup_value = value.get()
            for parameter in setup[ini_name][header2]:
                if setup[ini_name][header2][parameter] == []:
                    setup[ini_name][header2][parameter] = setup_value
                    break
    return
        

def submit_function():
    files = [('JSON File', '*.json')]
    fileName = 'trial_data'
    filepos = asksaveasfile(filetypes = files,defaultextension = json, initialfile = fileName)
    # writetoJSONFile(filepos, setup)
    json.dump(setup, filepos)


#_______________________________________________________________________________
#_______________________________SWITCHING FRAMES________________________________
class Frames(tk.Tk):

#________________________________INITIALISE_____________________________________
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
        # loop to switch between the frames
        #main page is the create array frame
        #help page is for online help
        for F in (MainPage, Help, General, Suspensions, Suspensions_Heave, Suspensions_Other, Drivetrain, Tyres, Brakes):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")
            frame.config(bg='black') #colour scheme
        self.show_frame(MainPage)
#_________________________________SHOW FRAME____________________________________
    def show_frame(self, cont):
        #raising the frame to the wanted frame
        frame = self.frames[cont]
        frame.tkraise()

#_______________________________________________________________________________
#______________________________CREATE ARRAY PAGE________________________________
class MainPage(tk.Frame):
#_________________________________INITIALISE____________________________________
    #arrangement of buttons and input and labels
    #you need to use controller to pass variables between classes
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        
        image2 = Image.open("hi3.jpg")
        image2 = image2.resize((960,540))
        test2 = ImageTk.PhotoImage(image2)
        label2 = tk.Label(self, image=test2, borderwidth=0)
        label2.image = test2
        label2.place(x=-100, y=50)

        image1 = Image.open("hi.png")
        #image1 = image1.resize((300,300))
        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(self, image=test, borderwidth=0)
        label1.image = test
        label1.place(x=575, y=-50)
        #button to switch to other pages, lambda is a must when switching pages
        #defining it as a button
        btnSort = tk.Button(self, text="Main",command=lambda: controller.show_frame(MainPage))
        btnSort.place(x=0, y=0)#placement
        btnSort.config(bg='#74000c', fg='#e8f8f5')#colour scheme

        btnSort = tk.Button(self, text="General",command=lambda: controller.show_frame(General))
        btnSort.place(x=38, y=0)#placement
        btnSort.config(bg='#74000c', fg='#e8f8f5')#colour scheme

        btnSort = tk.Button(self, text="Suspensions",command=lambda: controller.show_frame(Suspensions))
        btnSort.place(x=88, y=0)#placement
        btnSort.config(bg='#74000c', fg='#e8f8f5')#colour scheme

        btnSort = tk.Button(self, text="Suspensions Heave",command=lambda: controller.show_frame(Suspensions_Heave))
        btnSort.place(x=163, y=0)#placement
        btnSort.config(bg='#74000c', fg='#e8f8f5')#colour scheme

        btnSort = tk.Button(self, text="Suspensions Other",command=lambda: controller.show_frame(Suspensions_Other))
        btnSort.place(x=274, y=0)#placement
        btnSort.config(bg='#74000c', fg='#e8f8f5')#colour scheme

        btnSort = tk.Button(self, text="Tyres",command=lambda: controller.show_frame(Tyres))
        btnSort.place(x=382, y=0)#placement
        btnSort.config(bg='#74000c', fg='#e8f8f5')#colour scheme

        btnSort = tk.Button(self, text="Drivetrain",command=lambda: controller.show_frame(Drivetrain))
        btnSort.place(x=419, y=0)#placement
        btnSort.config(bg='#74000c', fg='#e8f8f5')#colour scheme

        btnSort = tk.Button(self, text="Brakes",command=lambda: controller.show_frame(Brakes))
        btnSort.place(x=480, y=0)#placement
        btnSort.config(bg='#74000c', fg='#e8f8f5')#colour scheme

        #a exit button to exit the gui
        #defining it as a button
        #use lambda to pass the main window as a function to destroy it in the module
        btnExit =  tk.Button(self, text="Exit", command=lambda: self.exit(controller))
        btnExit.place(x=470, y=700)#placement
        btnExit.config(bg='#74000c', fg='#e8f8f5')#colour scheme

        #button to switch to help page, the command lambda is a must when switching pages
        #defining it as a button
        btn = tk.Button(self, text="Help",command=lambda: controller.show_frame(Help))
        btn.place(x=524, y=00)#placement
        btn.config(bg='#74000c', fg='#e8f8f5')#colour scheme

        submitbtn = tk.Button(self, text="Save Setup", command= lambda: submit_function())
        submitbtn.place(y=700, x=350)#placement
        submitbtn.config(bg='#74000c', fg='#e8f8f5')#colour scheme



#_________________________CLOSE PROGRAM______________________________________________________
    def exit(self, window):
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

#____________________________________________________________________________________________
#_________________________________________GENERAL_______________________________________________
class General(tk.Frame):
#_____________________INITIALISE__________________________________________________________
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="General", font=("Arial", 25))#defining it as a label
        label.pack(pady=10, padx=10)#placement
        label.config(bg='black', fg='white')#colour scheme

        lblE = tk.Label(self,  text='RACE', font=LARGE_FONT)#defining it as a label
        lblE.place(x=10, y=50)#placement
        lblE.config(bg='black', fg='white')#colour scheme

        lblE = tk.Label(self,  text='TEMPERATURES', font=LARGE_FONT)#defining it as a label
        lblE.place(x=410, y=50)#placement
        lblE.config(bg='black', fg='white')#colour scheme

        arb_params = ['TRACK', 'CAR']
        BASIC_params = ['AIR TEMP', 'ROAD TEMP']

        label_y = 100
        front_input = []
        for i in arb_params:
            lblE = tk.Label(self,  text=i)#defining it as a label
            lblE.place(x=10, y=label_y)#placement
            lblE.config(bg='#e8f8f5', fg='#255D83')#colour scheme
            inputE = Entry(self)#defining it as a inputbox
            inputE.place(x=180, y=label_y)#placement
            inputE.config(bg='#74000c', fg='white')#colour scheme
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
            inputE.config(bg='#74000c', fg='white')#colour scheme
            rear_input.append(inputE)
            label_y = label_y +50

        #defining it as a button
        mainpagebtn = tk.Button(self, text="Main page",command=lambda: controller.show_frame(MainPage))
        mainpagebtn.place(y=690, x=50)#placement
        mainpagebtn.config(bg='#255D83', fg='#e8f8f5')#colour scheme

        submitbtn = tk.Button(self, text="Submit Values", command= lambda: populate_setup('race.ini', front_input, rear_input, '[RACE]', '[TEMPERATURE]'))
        submitbtn.place(y=690, x=350)#placement
        submitbtn.config(bg='#255D83', fg='#e8f8f5')#colour scheme

#_______________________________________________________________________________
#________________________________ABOUT US PAGE__________________________________       
class Suspensions(tk.Frame):
#_________________________________INITIALISE____________________________________
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Suspensions", font=("Arial", 25))#defining it as a label
        label.pack(pady=10, padx=10)#placement
        label.config(bg='black', fg='white')#colour scheme

        lblE = tk.Label(self,  text='FRONT', font=LARGE_FONT)#defining it as a label
        lblE.place(x=10, y=50)#placement
        lblE.config(bg='black', fg='white')#colour scheme

        lblE = tk.Label(self,  text='REAR', font=LARGE_FONT)#defining it as a label
        lblE.place(x=410, y=50)#placement
        lblE.config(bg='black', fg='white')#colour scheme

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
            inputE.config(bg='#74000c', fg='white')#colour scheme
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
            inputE.config(bg='#74000c', fg='white')#colour scheme
            rear_input.append(inputE)
            label_y = label_y +50
    
        #defining it as a button
        mainpagebtn = tk.Button(self, text="Main page",command=lambda: controller.show_frame(MainPage))
        mainpagebtn.place(y=690, x=50)#placement
        mainpagebtn.config(bg='#255D83', fg='#e8f8f5')#colour scheme

        # button to enter suspension values into setup dictionary
        # if giving in raw lists don't work, then just apply .get() to each value and make new lists (this could be done in submit_function)
        submitbtn = tk.Button(self, text="Submit Values", command= lambda: populate_setup('suspensions.ini', front_input, rear_input, '[FRONT]', '[REAR]'))
        submitbtn.place(y=690, x=350)#placement
        submitbtn.config(bg='#255D83', fg='#e8f8f5')#colour scheme

#________________________ABOUT US PAGE______________________________________________________        
class Suspensions_Heave(tk.Frame):
#_____________________INITIALISE__________________________________________________________
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Suspensions Heave", font=("Arial", 25))#defining it as a label
        label.pack(pady=10, padx=10)#placement
        label.config(bg='black', fg='white')#colour scheme

        lblE = tk.Label(self,  text='FRONT', font=LARGE_FONT)#defining it as a label
        lblE.place(x=10, y=50)#placement
        lblE.config(bg='black', fg='white')#colour scheme

        lblE = tk.Label(self,  text='REAR', font=LARGE_FONT)#defining it as a label
        lblE.place(x=410, y=50)#placement
        lblE.config(bg='black', fg='white')#colour scheme

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
            inputE.config(bg='#74000c', fg='white')#colour scheme
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
            inputE.config(bg='#74000c', fg='white')#colour scheme
            rear_input.append(inputE)
            label_y = label_y +50

        #defining it as a button
        mainpagebtn = tk.Button(self, text="Main page",command=lambda: controller.show_frame(MainPage))
        mainpagebtn.place(y=690, x=50)#placement
        mainpagebtn.config(bg='#255D83', fg='#e8f8f5')#colour scheme

        submitbtn = tk.Button(self, text="Submit Values", command= lambda: populate_setup('suspensions.ini', front_input, rear_input, '[HEAVE_FRONT]', '[HEAVE_REAR]'))
        submitbtn.place(y=690, x=350)#placement
        submitbtn.config(bg='#255D83', fg='#e8f8f5')#colour scheme

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
            inputE.config(bg='#74000c', fg='white')#colour scheme
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
            inputE.config(bg='#74000c', fg='white')#colour scheme
            rear_input.append(inputE)
            label_y = label_y +50

        #defining it as a button
        mainpagebtn = tk.Button(self, text="Main page",command=lambda: controller.show_frame(MainPage))
        mainpagebtn.place(y=690, x=50)#placement
        mainpagebtn.config(bg='#255D83', fg='#e8f8f5')#colour scheme

        submitbtn = tk.Button(self, text="Submit Values", command= lambda: populate_setup('suspensions.ini', front_input, rear_input, '[ARB]', '[BASIC]'))
        submitbtn.place(y=690, x=350)#placement
        submitbtn.config(bg='#255D83', fg='#e8f8f5')#colour scheme
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
            inputE.config(bg='#74000c', fg='white')#colour scheme
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
            inputE.config(bg='#74000c', fg='white')#colour scheme
            rear_input.append(inputE)
            label_y = label_y +50

        #defining it as a button
        mainpagebtn = tk.Button(self, text="Main page",command=lambda: controller.show_frame(MainPage))
        mainpagebtn.place(y=690, x=50)#placement
        mainpagebtn.config(bg='#255D83', fg='#e8f8f5')#colour scheme

        submitbtn = tk.Button(self, text="Submit Values", command= lambda: populate_setup('tyres.ini', front_input, rear_input, '[FRONT]', '[REAR]'))
        submitbtn.place(y=690, x=350)#placement
        submitbtn.config(bg='#255D83', fg='#e8f8f5')#colour scheme

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
            inputE.config(bg='#74000c', fg='white')#colour scheme
            front_input.append(inputE)
            label_y = label_y +50

        #defining it as a button
        mainpagebtn = tk.Button(self, text="Main page",command=lambda: controller.show_frame(MainPage))
        mainpagebtn.place(y=690, x=50)#placement
        mainpagebtn.config(bg='#255D83', fg='#e8f8f5')#colour scheme

        submitbtn = tk.Button(self, text="Submit Values", command= lambda: populate_setup('drivetrain.ini', front_input, [], '[DIFFERENTIAL]', ''))
        submitbtn.place(y=690, x=350)#placement
        submitbtn.config(bg='#255D83', fg='#e8f8f5')#colour scheme

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
            inputE.config(bg='#74000c', fg='white')#colour scheme
            front_input.append(inputE)
            label_y = label_y +50

        #defining it as a button
        mainpagebtn = tk.Button(self, text="Main page",command=lambda: controller.show_frame(MainPage))
        mainpagebtn.place(y=690, x=50)#placement
        mainpagebtn.config(bg='#255D83', fg='#e8f8f5')#colour scheme

        submitbtn = tk.Button(self, text="Submit Values", command= lambda: populate_setup('brakes.ini', front_input, [], '[DATA]', ''))
        submitbtn.place(y=690, x=350)#placement
        submitbtn.config(bg='#255D83', fg='#e8f8f5')#colour scheme


#_______________________________________________________________________________
#______________________MAIN PROGRAM_________________________________________________________
def main():
    window = Frames()#defining what the window will show --- it will have frames(pages)
    window.title('Redback Asseto Corsa Launcher')

    # image2 = Image.open("hi3.jpg")
    # image2 = image2.resize((960,540))
    # test2 = ImageTk.PhotoImage(image2)
    # label2 = tk.Label(image=test2, borderwidth=0)
    # label2.image = test2
    # label2.place(x=-100, y=50)

    # image1 = Image.open("hi.png")
    # #image1 = image1.resize((300,300))
    # test = ImageTk.PhotoImage(image1)
    # label1 = tk.Label(image=test, borderwidth=0)
    # label1.image = test
    # label1.place(x=575, y=-50)

    window.config(bg='#e8f8f5')#colour scheme
    window.geometry("800x800")#size of window
    window.resizable(width=False, height=False)#not letting the user resize the window
    window.mainloop()#running the gui

# Basically checks that the code is being run tby the user, and not imported by some other functions
if __name__ == '__main__':
    main()





'''
Click submit button:
submit_function(ini file (str), header (str, e.g. [FRONT]), list):
	populate_setup(ini file (str), header (str, e.g. [FRONT]), setup, list)
	
populate_setup(ini, header, setup, list):
for value in list:
	setup_value = value.get()
	for parameter in setup[ini][header]:
		setup[ini][header][parameter] = setup_value
return


FOR NOW PLAN IS:
two buttons for front and rear 
run submit_function for each by giving name of ini file and header 
'''