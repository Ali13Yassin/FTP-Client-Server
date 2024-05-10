#------------------------------------<Initialization Start>-------------------------------------------------------
from tkinter import * #The UI module that this program relies on
from tkinter import messagebox #This is a function that allows making windows message boxes, has to be called separetly
from tkinter.ttk import * #Theamed tkinter which makes the UI look ever so slightly modern
import os
from pathlib import Path
import threading

from ftp_server_test import *

os.chdir(Path(__file__).parent) #Changes cmd directory to the one that has the py file

#Checks if the required python files exist
# if os.path.exists("Corefunctions.py") and os.path.exists("Exportfunctions.py"):
#     from Corefunctions import * #The library I made that handles backend operations
#     from Exportfunctions import * #The library I made that exports information
# else:
#     messagebox.showerror("Error", "Critical files are missing, please redownload the application to function properly.")
#     quit()

#Starts the program
def start():
    # filecheck()#Checks if other database files exist and creates them
    window() #Defines properties of the main window
    mainmenu() #The first menu to the application
    wind.mainloop() #Makes the window apear

#Defines properties of the main window
def window():
    global wind,div,fnt #Defines the main window, and div
    wind = Tk()
    centx = int((wind.winfo_screenwidth() - 600) / 2) #Gets coordinates of where to center the window on x-axis
    centy = int((wind.winfo_screenheight() - 400) / 2) #Gets coordinates of where to center the window on y-axis
    wind.geometry("600x400+{}+{}".format(centx, centy)) #Centers the window
    wind.grid_rowconfigure(1, weight=1)     #Helps center objects
    wind.grid_columnconfigure(1, weight=1)  #Helps center objects
    wind.title("SMP project")
    fnt = "Manrope" #To be able to change font through one change
    div = Frame(wind) #Funny name from html that's not gonna cause issues at all lolol
    div.pack() #The frame keeps the layout decent

def mainmenu():
    clear() #To clear last menu when coming back
    port_num = StringVar()
    
    frame = Frame(wind)
    frame.pack(fill='both', expand=True)
    # Configure the grid
    frame.grid_rowconfigure(0, weight=2)  # 20% of the space goes here
    frame.grid_rowconfigure(1, weight=8)  # 80% of the space goes here
    style = ttk.Style()
    style.configure("Custom.TFrame", background="red")
    frame1 = Frame(frame, style="Custom.TFrame")
    frame1.grid(row=0, column=0, sticky="nsew")
    frame2 = Frame(frame, style="Custom.TFrame")
    frame2.grid(row=1, column=0, sticky="nsew")
    # Label(frame, text="Welcome to Ethel project\nThis is the main menu\nUnfinished version", font=(fnt, 15)).grid(row=0, column=0, columnspan=2, sticky="nsew")
    # Entry(frame, textvariable=port_num).grid(row=1, column=0, padx=10, pady=10)
    Button(frame, text="Start server", command=lambda: start_listen(int(port_num.get()))).grid(row=1, column=0, padx=10, pady=10)
    Button(frame, text="Courses actions", command=placeholder).grid(row=2, column=1, padx=10, pady=10)

def start_listen(port):
    arg = [port] #Needs to be a list to be able to pass arguments to the thread
    t1 = threading.Thread(target=start_listening, args=arg)
    t1.start()

#------------------------------------<Initialization End>-------------------------------------------------------
#------------------------------------<General Start>-------------------------------------------------------
#Used as a placeholder for menus I didn't add
def placeholder():
    clear() #To clear last menu
    Label(div, text="Placeholder menu").grid(row=0, column=0, padx=10, pady=10)
    Button(div, text="Main menu",command=mainmenu).grid(row=2, column=0, padx=10, pady=10)

#Deletes the widgets from previous menu and cleares memory from them
def clear():
    for widget in div.winfo_children():
        widget.destroy() #Used this instead of forget to clear memory

#------------------------------------<General End>-------------------------------------------------------
start() #Starts the application