#------------------------------------<Initialization Start>-------------------------------------------------------
from tkinter import * #The UI module that this program relies on
from tkinter import messagebox #This is a function that allows making windows message boxes, has to be called separetly
from tkinter.ttk import * #Theamed tkinter which makes the UI look ever so slightly modern
import os
from pathlib import Path
import threading
from PIL import Image, ImageTk

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
    global wind,div,fnt #Defines the main window, and div and font as global variables
    wind = Tk()
    wind.iconbitmap("dog2.ico")  # Set the icon
    centx = int((wind.winfo_screenwidth() - 800) / 2) #Gets coordinates of where to center the window on x-axis
    centy = int((wind.winfo_screenheight() - 500) / 2) #Gets coordinates of where to center the window on y-axis
    wind.geometry("800x500+{}+{}".format(centx, centy)) #Centers the window
    wind.title("SMP project")
    fnt = "Manrope" #To be able to change font through one change
    div = Frame(wind) #Funny name from html that's not gonna cause issues at all lolol
    div.pack() #The frame keeps the layout decent

def mainmenu():
    global main_frame, style #To clear last menu when coming back
    port_num = StringVar()
    DivisionFrame = Frame(wind)
    DivisionFrame.pack(fill='both', expand=True)
    # Configure the grid
    DivisionFrame.grid_rowconfigure(0, weight=0)  # 20% of the space goes here
    DivisionFrame.grid_rowconfigure(1, weight=10)  # 80% of the space goes here
    DivisionFrame.grid_columnconfigure(0, weight=1)
    style = Style()
    style.configure("navbar.TFrame", background="#391D0D")
    style.configure("Custom2.TFrame", background="#6F3F29")
    style.configure("Title.TLabel", background="#391D0D", foreground="white", font=(fnt, 15, "bold"))
    style.configure("navbutton.TLabel", background="#A5622F", foreground="white", font=(fnt, 12))  # Change the font of the text
    style.map("navbutton.TLabel",foreground=[('pressed', '#391D0D'), ('active', 'white')],background=[('pressed', '!disabled', '#FFE7D4'), ('active', '#E99A5D')])
    navbar = Frame(DivisionFrame, style="navbar.TFrame")
    navbar.grid(row=0, column=0, sticky="nsew")
    main_frame = Frame(DivisionFrame, style="Custom2.TFrame")
    main_frame.grid(row=1, column=0, sticky="nsew")
    Label(navbar, text="The Ethel Project", style="Title.TLabel").grid(row=0, column=0)
    Entry(main_frame, textvariable=port_num).grid(row=0, column=0, padx=10, pady=10)
    Button(navbar, text="FTP server", command=server_menu, style="navbutton.TLabel").grid(row=0, column=1, padx=10, pady=10)
    Button(navbar, text="FTP client", command=client_menu, style="navbutton.TLabel").grid(row=0, column=2, padx=10, pady=10)
    Button(navbar, text="Easy transfer", command=easy_menu, style="navbutton.TLabel").grid(row=0, column=3, padx=10, pady=10)
    Button(navbar, text="Settings", command=settings_menu, style="navbutton.TLabel").grid(row=0, column=4, padx=10, pady=10)


#------------------------------------<Initialization End>-------------------------------------------------------
#------------------------------------<Menus Start>-------------------------------------------------------
def server_menu():
    clear() #Clears the previous menu
    Button(main_frame, text="server menu test", command=placeholder, style="navbutton.TLabel").grid(row=0, column=4, padx=10, pady=10)

def client_menu():
    clear() #Clears the previous menu
    Button(main_frame, text="client menu test", command=placeholder, style="navbutton.TLabel").grid(row=0, column=4, padx=10, pady=10)

def easy_menu():
    clear() #Clears the previous menu
    Button(main_frame, text="easy menu test", command=placeholder, style="navbutton.TLabel").grid(row=0, column=4, padx=10, pady=10)

def settings_menu():
    clear() #Clears the previous menu
    setting_back = Frame(main_frame, style="Custom2.TFrame")
    setting_back.pack(fill='both', expand=True)
    setting_back.grid_columnconfigure(0, weight=1)
    setting_back.grid_columnconfigure(1, weight=1)
    setting_back.grid_rowconfigure(0, weight=1)
    options_frame = VerticalScrolledFrame(setting_back, style="Custom2.TFrame")
    options_frame.grid(row=0, column=0, sticky='nsew')

    #Description frame
    style.configure("desc_title.TLabel", background="#6F3F29", foreground="white", font=(fnt, 25, "bold"))
    style.configure("desc_version.TLabel", background="#6F3F29", foreground="white", font=(fnt, 10))
    style.configure("desc_repo.TLabel", background="#6F3F29", foreground="white", font=(fnt, 15))
    description_frame = Frame(setting_back, style="Custom2.TFrame")
    description_frame.grid(row=0, column=1, sticky='nsew')
    img = ImageTk.PhotoImage(Image.open("dog2.jpg"))
    image_label = Label(description_frame, image=img)
    image_label.image = img
    image_label.pack()
    Label(description_frame, text="The Ethel project", style="desc_title.TLabel").pack()
    Label(description_frame, text="Version 1.0", style="desc_version.TLabel").pack()

    #Redirect to repo
    Repo_frame = Frame(description_frame, style="Custom2.TFrame")
    img2 = ImageTk.PhotoImage(Image.open("GitHub2.png"))
    image_git = Label(Repo_frame, image=img2)
    image_git.image = img2
    image_git.grid(row=0, column=0)
    Button(Repo_frame, text="See GitHub repo", style="desc_repo.TLabel").grid(row=0, column=1)
    Repo_frame.pack(padx=10, pady=10)

    Button(options_frame.interior, text="settings options test", command=placeholder, style="navbutton.TLabel").pack(padx=10, pady=10)
    Button(options_frame.interior, text="settings options test", command=placeholder, style="navbutton.TLabel").pack(padx=10, pady=10)
    Button(options_frame.interior, text="settings options test", command=placeholder, style="navbutton.TLabel").pack(padx=10, pady=10)
    Button(options_frame.interior, text="settings options test", command=placeholder, style="navbutton.TLabel").pack(padx=10, pady=10)
    Button(options_frame.interior, text="settings options test", command=placeholder, style="navbutton.TLabel").pack(padx=10, pady=10)
    Button(options_frame.interior, text="settings options test", command=placeholder, style="navbutton.TLabel").pack(padx=10, pady=10)
    Button(options_frame.interior, text="settings options test", command=placeholder, style="navbutton.TLabel").pack(padx=10, pady=10)
    Button(options_frame.interior, text="settings options test", command=placeholder, style="navbutton.TLabel").pack(padx=10, pady=10)
    Button(options_frame.interior, text="settings options test", command=placeholder, style="navbutton.TLabel").pack(padx=10, pady=10)
    Button(options_frame.interior, text="settings options test", command=placeholder, style="navbutton.TLabel").pack(padx=10, pady=10)
    Button(options_frame.interior, text="settings options test", command=placeholder, style="navbutton.TLabel").pack(padx=10, pady=10)
    Button(options_frame.interior, text="settings options test", command=placeholder, style="navbutton.TLabel").pack(padx=10, pady=10)
    Button(options_frame.interior, text="settings options test", command=placeholder, style="navbutton.TLabel").pack(padx=10, pady=10)
    Button(options_frame.interior, text="settings options test", command=placeholder, style="navbutton.TLabel").pack(padx=10, pady=10)
    Button(options_frame.interior, text="settings options test", command=placeholder, style="navbutton.TLabel").pack(padx=10, pady=10)
    Button(options_frame.interior, text="settings options test", command=placeholder, style="navbutton.TLabel").pack(padx=10, pady=10)
    Button(options_frame.interior, text="settings options test", command=placeholder, style="navbutton.TLabel").pack(padx=10, pady=10)
    Button(options_frame.interior, text="settings options test", command=placeholder, style="navbutton.TLabel").pack(padx=10, pady=10)
    Button(options_frame.interior, text="settings options test", command=placeholder, style="navbutton.TLabel").pack(padx=10, pady=10)
    Button(options_frame.interior, text="settings options test", command=placeholder, style="navbutton.TLabel").pack(padx=10, pady=10)

class VerticalScrolledFrame(Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame.
    * Construct and pack/place/grid normally.
    * This frame only allows vertical scrolling.
    """
    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)

        # Create a canvas object and a vertical scrollbar for scrolling it.
        vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = Canvas(self, bd=0, highlightthickness=0, yscrollcommand=vscrollbar.set, bg="#6F3F29")
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=canvas.yview)

        # Reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # Create a frame inside the canvas which will be scrolled with it.
        self.interior = interior = Frame(canvas, style="Custom2.TFrame")
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=NW)

        # Track changes to the canvas and frame width and sync them,
        # also updating the scrollbar.
        def _configure_interior(event):
            # Update the scrollbars to match the size of the inner frame.
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # Update the canvas's width to fit the inner frame.
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # Update the inner frame's width to fill the canvas.
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)


#------------------------------------<Menus End>-------------------------------------------------------
#------------------------------------<General Start>-------------------------------------------------------
#Used as a placeholder for menus I didn't add
def placeholder():
    print("Button pressed")

#Deletes the widgets from previous menu and cleares memory from them
def clear():
    for widget in main_frame.winfo_children():
        widget.destroy() #Used this instead of forget to clear memory

#------------------------------------<General End>-------------------------------------------------------
start() #Starts the application