#importing tkinter and the message boxes and scrolledtext widget
from tkinter import *
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
#the inbuilt csv function allows to read and open csv files
import csv

#setting font
LARGE_FONT = ("Verdana", 12)
#initialise the list
alist = []

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
        for F in (MainPage, Help):
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
        #title
        label = tk.Label(self, text="no micheal no this is so not right", font=LARGE_FONT)#defining it as a label
        label.pack(pady=10, padx=10)#placement
        label.config(bg='#e8f8f5', fg='#255D83')#colour scheme
        # label 
        lblE = tk.Label(self,  text='daniel avocado')#defining it as a label
        lblE.place(x=10, y=50)#placement
        lblE.config(bg='#e8f8f5', fg='#255D83')#colour scheme
        inputE = Entry(self)#defining it as a inputbox
        inputE.place(x=100, y=50)#placement
        inputE.config(bg='#255D83', fg='#e8f8f5')#colour scheme

        # a scrolled text wdget 
        lblcsvstuff = tk.Label(self,  text='mazespin')#defining it as a label
        lblcsvstuff.place(x=10, y=150)#placement
        lblcsvstuff.config(bg='#e8f8f5', fg='#255D83')#colour scheme
        #defining it as a scrolledtext
        inputcsvstuff = scrolledtext.ScrolledText(self, width=55, height=5)
        inputcsvstuff.place(x=100, y=150)#placement
        inputcsvstuff.config(bg='#255D83', fg='#e8f8f5')#colour scheme

        #defining it as a button
        btncsv = tk.Button(self, text="Import csv", command=self.csv)
        btncsv.place(x=250, y=100)#placement
        btncsv.config(bg='#255D83', fg='#e8f8f5')#colour scheme
        
        inputcsvfilename = Entry(self)#defining it as a inputbox
        inputcsvfilename.place(x=100, y=100)#placement
        inputcsvfilename.config(bg='#255D83', fg='#e8f8f5')#colour scheme


        #a clear button to clear 
        #defining it as a button
        btnclear =  tk.Button(self, text="clear", command=self.clear)
        btnclear.place(x=380, y=45)#placement
        btnclear.config(bg='#255D83', fg='#e8f8f5')#colour scheme
        #a exit button to exit the gui
        #defining it as a button
        #use lambda to pass the main window as a function to destroy it in the module
        btnExit =  tk.Button(self, text="Exit", command=lambda: self.exit(window))
        btnExit.place(x=400, y=400)#placement
        btnExit.config(bg='#255D83', fg='#e8f8f5')#colour scheme
        #defining the varaibles so the controller can pass the variables betweeen the classes
        self.inputE = inputE
        self.inputcsvfilename = inputcsvfilename
        self.inputcsvstuff = inputcsvstuff
        #button to switch to help page, the command lambda is a must when switching pages
        #defining it as a button
        btn = tk.Button(self, text="Help",command=lambda: controller.show_frame(Help))
        btn.place(x=300, y=400)#placement
        btn.config(bg='#255D83', fg='#e8f8f5')#colour scheme
        # making alist global so it can be accessed by all submodules 
        global alist


#__________________________IMPORT CSV FILES_____________________________________________________
    # submodule to import csv files into the program
    def csv(self):
        #defining alist as global
        global alist
        #clearing the array output box
        self.inputcsvstuff.delete(1.0, 'end')
        #initialising the array
        alist = []
        #settign a variable to the name of the file
        filename= (self.inputcsvfilename.get())
        #adding the csv file extension to the end of the inputed file name
        csvfile = filename+'.csv'
        print(csvfile)
        #opening the csv file with the help of the csv module
        try:
            with open(csvfile) as csvDataFile:
                csvReader = csv.reader(csvDataFile)
            #appending the elements in the csv file to the array
                for row in csvReader:
                    alist.append(int(row[0]))
        except FileNotFoundError:
            messagebox.showerror('Error', 'Please enter a valid filename')
            self.inputcsvfilename.delete(0, 'end')
            
        print(alist)
        #showing the csv data
        self.inputcsvstuff.insert(END, alist)
        
#_________________________CLEAR BUTTON______________________________________________________
    def clear(self):
        #submodule which links to the clear button to clear all vairables and the input boxes
        global alist
        #clears the enter term input
        self.inputE.delete(0, 'end')
        #clears the length of array output
        self.inputlen.delete(0, 'end')
        #clears the unsorted arrray output
        self.inputunsorted.delete(1.0, 'end')
        #clears the array
        alist.clear()

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
#______________________MAIN PROGRAM_________________________________________________________
window = Frames()#defining what the window will show --- it will have frames(pages)
window.config(bg='#e8f8f5')#colour scheme
window.geometry("600x500")#size of window
window.resizable(width=False, height=False)#not letting the user resize the window
window.mainloop()#running the gui
