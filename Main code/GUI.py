#------------------------------------<Initialization Start>-------------------------------------------------------
from tkinter import * #The UI module that this program relies on
from tkinter import messagebox #This is a function that allows making windows message boxes, has to be called separetly
from tkinter.ttk import * #Theamed tkinter which makes the UI look ever so slightly modern
import os
from pathlib import Path
import threading
from PIL import Image, ImageTk
import FTP_client as clienter
# import FTP_server as serverer
import webbrowser
from tkinter import messagebox
from user_management import *
import socket

os.chdir(Path(__file__).parent) #Changes cmd directory to the one that has the py file
root_location = Path(__file__).parent #The location of the main file

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
    wind.iconbitmap("imgs/dog2.ico")  # Set the icon
    centx = int((wind.winfo_screenwidth() - 800) / 2) #Gets coordinates of where to center the window on x-axis
    centy = int((wind.winfo_screenheight() - 500) / 2) #Gets coordinates of where to center the window on y-axis
    wind.geometry("800x500+{}+{}".format(centx, centy)) #Centers the window
    wind.title("FTP project")
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
    style.configure("Title.TLabel", background="#391D0D", foreground="white", font=(fnt, 15, "bold"), padding=(5, 0))
    style.configure("navbutton.TLabel", background="#A5622F", foreground="white", font=(fnt, 12))  # Change the font of the text
    style.map("navbutton.TLabel",foreground=[('pressed', '#391D0D'), ('active', 'white')],background=[('pressed', '!disabled', '#FFE7D4'), ('active', '#E99A5D')])
    navbar = Frame(DivisionFrame, style="navbar.TFrame")
    navbar.grid(row=0, column=0, sticky="nsew")
    main_frame = Frame(DivisionFrame, style="Custom2.TFrame")
    main_frame.grid(row=1, column=0, sticky="nsew")
    Label(navbar, text="FTP Project", style="Title.TLabel").grid(row=0, column=0)
    Entry(main_frame, textvariable=port_num).grid(row=0, column=0, padx=10, pady=10)
    Button(navbar, text="FTP server", command=server_menu, style="navbutton.TLabel").grid(row=0, column=1, padx=10, pady=10)
    Button(navbar, text="FTP client", command=client_connect_menu, style="navbutton.TLabel").grid(row=0, column=2, padx=10, pady=10)
    # Button(navbar, text="Easy transfer", command=easy_menu, style="navbutton.TLabel").grid(row=0, column=3, padx=10, pady=10)
    Button(navbar, text="About", command=settings_menu, style="navbutton.TLabel").grid(row=0, column=4, padx=10, pady=10)
    server_menu() #Starts the server menu

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
#------------------------------------<Initialization End>-------------------------------------------------------
#------------------------------------<Menus Start>-------------------------------------------------------
def server_menu():
    clear() #Clears the previous menu
    server_back = Frame(main_frame, style="Custom2.TFrame")
    server_back.pack(fill='both', expand=True)
    server_back.grid_columnconfigure(0, weight=1)
    server_back.grid_columnconfigure(1, weight=1)
    server_back.grid_rowconfigure(0, weight=1)

    #Options frame
    options_frame = Frame(server_back, style="Custom2.TFrame")
    options_frame.grid(row=0, column=1, sticky='nsew')

    #Connection frame
    connection_frame = Frame(options_frame, style="navbar.TFrame")
    connection_frame.pack(padx=10, pady=10)
    global server_status
    server_status = StringVar()
    server_status.set("Server is off")
    style.configure("settings.TLabel", background="#391D0D", foreground="white", font=(fnt, 15))
    Label(connection_frame, text="Server settings", style="Title.TLabel").grid(row=0, column=0)
    Label(connection_frame, text="Server status:", style="settings.TLabel").grid(row=2, column=0)
    Label(connection_frame, text=server_status.get(), style="settings.TLabel").grid(row=2, column=1)
    Label(connection_frame, text="Server IP:", style="settings.TLabel").grid(row=3, column=0)
    Label(connection_frame, text=get_ip_address(), style="settings.TLabel").grid(row=3, column=1)

    #Securoty frame
    security_frame = Frame(options_frame, style="navbar.TFrame")
    security_frame.pack(padx=10, pady=10)
    style.configure("settings.TLabel", background="#391D0D", foreground="white", font=(fnt, 15))
    Label(security_frame, text="Server Security", style="Title.TLabel").grid(row=0, column=0)
    Button(security_frame, text="Account management", command=user_management_menu, style="navbutton.TLabel").grid(row=2, column=0, padx=10, pady=10)
    
    #Controlling the server
    control_frame = Frame(server_back, style="Custom2.TFrame")
    control_frame.grid(row=0, column=0, sticky='nsew')
    style.configure("server_off_button.TLabel", background="#A5622F", foreground="white", font=(fnt, 20, "bold"), padding=(10, 10))  # Change the font of the text
    style.map("server_off_button.TLabel",foreground=[('pressed', '#391D0D'), ('active', 'white')],background=[('pressed', '!disabled', '#FFE7D4'), ('active', '#E99A5D')])
    Button(control_frame, text="Start server", command=start_new_cmd_with_python_script, style="server_off_button.TLabel").pack(expand=True)
server_on = False


def server_button_code():
    global server_on
    if server_on:
        style.configure("server_off_button.TLabel", background="#A5622F", foreground="white", font=(fnt, 20, "bold"), padding=(10, 10))  # Change the font of the text
        style.map("server_off_button.TLabel",foreground=[('pressed', '#391D0D'), ('active', 'white')],background=[('pressed', '!disabled', '#FFE7D4'), ('active', '#E99A5D')])
        # server_stopper()
        server_on = False
    else:
        style.configure("server_on_button.TLabel", background="#C43333", foreground="white", font=(fnt, 20, "bold"), padding=(10, 10))  # Change the font of the text
        style.map("server_on_button.TLabel",foreground=[('pressed', 'black'), ('active', 'white')],background=[('pressed', '!disabled', '#F67171'), ('active', '#E80000')])
        start_new_cmd_with_python_script()
        server_on = True

def user_management_menu():
    new_window = Toplevel(wind)
    new_window.title("Server files")
    back_frame = Frame(new_window, style="navbar.TFrame")
    back_frame.pack(fill='both', expand=True)
    # Create a Treeview widget
    user_tree = Treeview(back_frame)

    # Define columns
    user_tree["columns"] = ("Name", "Password")

    # Format columns
    user_tree.column("#0", width=0, stretch=NO)
    user_tree.column("Name", anchor=W, width=200)
    user_tree.column("Password", anchor=W, width=200)

    # Create headings
    user_tree.heading("#0", text="", anchor=W)
    user_tree.heading("Name", text="Name", anchor=W)
    user_tree.heading("Password", text="Password", anchor=W)

    # Add data to the treeview
    allusers = jsonR("users.json")
    for key in allusers:
        user_tree.insert("", "end", text=key, values=(key, allusers[key]))

    # Display the treeview
    user_tree.pack(fill=BOTH, expand=True)
    user_tree = Treeview(new_window, columns=("Username", "Password"), selectmode='browse')
    def new_user():
        new_user_frame = Frame(back_frame, style="navbar.TFrame")
        new_user_frame.pack(pady=5)
        new_username = StringVar()
        new_password = StringVar()
        def confirm():
            if new_username.get() not in allusers:
                allusers[new_username.get()] = new_password.get()
                jsonW("users.json", allusers)
                os.makedirs("myusers/{}".format(new_username.get()), exist_ok=True)
                new_window.destroy()
            else:
                messagebox.showerror("Error", "Username already exists")
        Options_frame.destroy()
        Label(new_user_frame, text="Username:", style="settings.TLabel").grid(row=0, column=0)
        Entry(new_user_frame, textvariable=new_username).grid(row=0, column=1)
        Label(new_user_frame, text="Password:", style="settings.TLabel").grid(row=1, column=0)
        Entry(new_user_frame, textvariable=new_password).grid(row=1, column=1)
        Button(new_user_frame, text="Confirm", command=confirm, style="navbutton.TLabel").grid(row=2, column=1)

    def delete_user():
        response = messagebox.askyesno("Warning", "Are you sure you want to delete the selected users?")
        if response:
            user_tree.update()
            selected_items = user_tree.selection()
            print(selected_items)
            for item in selected_items:
                del allusers[user_tree.item(item)["values"][0]]
                print(user_tree.item(item)["values"][0])
                jsonW("users.json", allusers)
                os.rmdir("myusers/{}".format(user_tree.item(item)["values"][0]))
                new_window.destroy()

    def edit_user():
        edit_user_frame = Frame(back_frame, style="navbar.TFrame")
        edit_user_frame.pack(pady=5)
        new_username = StringVar()
        new_password = StringVar()
        def confirm():
            if new_username.get() not in allusers:
                allusers[new_username.get()] = new_password.get()
                jsonW("users.json", allusers)
                os.makedirs("myusers/{}".format(new_username.get()), exist_ok=True)
                new_window.destroy()
            else:
                messagebox.showerror("Error", "Username already exists")
        Options_frame.destroy()
        Label(edit_user_frame, text="Username:", style="settings.TLabel").grid(row=0, column=0)
        Entry(edit_user_frame, textvariable=new_username).grid(row=0, column=1)
        Label(edit_user_frame, text="Password:", style="settings.TLabel").grid(row=1, column=0)
        Entry(edit_user_frame, textvariable=new_password).grid(row=1, column=1)
        Button(edit_user_frame, text="Confirm", command=confirm, style="navbutton.TLabel").grid(row=2, column=1)

    Options_frame = Frame(back_frame, style="navbar.TFrame")
    Options_frame.pack(pady=5)
    Button(Options_frame, text="Add user", command=new_user, style="navbutton.TLabel").grid(row=0, column=0, pady=5, padx=5)
    Button(Options_frame, text="delete user", command=delete_user, style="navbutton.TLabel").grid(row=0, column=1, pady=5, padx=5)
    Button(Options_frame, text="Edit user", command=edit_user, style="navbutton.TLabel").grid(row=0, column=2, pady=5, padx=5)

import subprocess

def start_new_cmd_with_python_script():
    # Start a new command prompt window running a Python script
    server_status.set("Server is on")
    subprocess.Popen(["cmd", "/c", "start", "cmd", "/k", "python", "FTP_server.py"])


def client_connect_menu():
    clear() #Clears the previous menu
    client_back = Frame(main_frame, style="Custom2.TFrame")
    client_back.pack(fill='both', expand=True)
    client_back.grid_columnconfigure(0, weight=1)
    client_back.grid_rowconfigure(0, weight=1)

    #Controlling the server
    # security_frame = Frame(options_frame, style="navbar.TFrame")
    # security_frame.pack(padx=10, pady=10)
    control_frame = Frame(client_back, style="navbar.TFrame")
    control_frame.grid(row=0, column=0)
    

    addr_frame = Frame(control_frame, style="navbar.TFrame")
    addr_frame.grid(row=0, column=0)
    uname_frame = Frame(control_frame, style="navbar.TFrame")
    uname_frame.grid(row=1, column=0)
    pass_frame = Frame(control_frame, style="navbar.TFrame")
    pass_frame.grid(row=2, column=0)

    address = StringVar()
    username = StringVar()
    password = StringVar()

    style.configure("settings.TLabel", background="#391D0D", foreground="white", font=(fnt, 15))
    style.configure("darkbrown.TEntry", background="#391D0D", foreground="black", font=(fnt, 15))
    Label(addr_frame, text="Server address:", style="settings.TLabel").grid(row=0, column=0)
    Entry(addr_frame, textvariable=address, width=20, style='darkbrown.TEntry').grid(row=0, column=1)
    Label(uname_frame, text="Username:", style="settings.TLabel").grid(row=0, column=0)
    Entry(uname_frame, textvariable=username, width=20, style='darkbrown.TEntry').grid(row=0, column=1)
    Label(pass_frame, text="Password:", style="settings.TLabel").grid(row=0, column=0)
    Entry(pass_frame, textvariable=password, width=20, style='darkbrown.TEntry').grid(row=0, column=1)
    style.configure("server_off_button.TLabel", background="#A5622F", foreground="white", font=(fnt, 15, "bold"))  # Change the font of the text
    style.map("server_off_button.TLabel",foreground=[('pressed', '#391D0D'), ('active', 'white')],background=[('pressed', '!disabled', '#FFE7D4'), ('active', '#E99A5D')])
    Button(control_frame, text="Connect to server", command=lambda: clienter_start(address.get(),username.get(),password.get()), style="server_off_button.TLabel").grid(row=3, column=0, pady=10)

def client_connected_menu(addr):
    clear() #Clears the previous menu
    client_back = Frame(main_frame, style="Custom2.TFrame")
    client_back.pack(fill='both', expand=True)
    client_back.grid_columnconfigure(0, weight=1)
    client_back.grid_rowconfigure(0, weight=1)

    info_frame = Frame(client_back, style="navbar.TFrame")
    info_frame.grid(row=0, column=0)
    # info_frame.pack_propagate(0)
    Label(info_frame, text="Connection information", style="Title.TLabel").grid(row=0, column=0)
    Label(info_frame, text="Address: ", style="settings.TLabel").grid(row=1, column=0)
    adress_info = Label(info_frame, text=addr, style="settings.TLabel")
    adress_info.grid(row=1, column=1)
    Label(info_frame, text="Connection status: ", style="settings.TLabel").grid(row=2, column=0)
    connection_info = Label(info_frame, text="Connected", style="settings.TLabel")
    connection_info.grid(row=2, column=1)

    action_frame = Frame(client_back, style="navbar.TFrame")
    action_frame.grid(row=1, column=0)
    Label(action_frame, text="Actions", style="Title.TLabel").grid(row=0, column=0)
    Button(action_frame, text="View all files", command=lambda: view_files_menu(0), style="navbutton.TLabel").grid(row=1, column=0, padx=10, pady=10)
    Button(action_frame, text="Download file", command=lambda: view_files_menu(1), style="navbutton.TLabel").grid(row=2, column=0, padx=10, pady=10)
    Button(action_frame, text="Upload file", command=lambda: view_files_menu(2), style="navbutton.TLabel").grid(row=3, column=0, padx=10, pady=10)
    
    style.configure("server_on_button.TLabel", background="#C43333", foreground="white", font=(fnt, 15))  # Change the font of the text
    style.map("server_on_button.TLabel",foreground=[('pressed', 'black'), ('active', 'white')],background=[('pressed', '!disabled', '#F67171'), ('active', '#E80000')])
    Button(action_frame, text="Disconnect", command=lambda: (clienter.close_connection(), client_connect_menu()), style="server_on_button.TLabel").grid(row=4, column=0, padx=10, pady=10)

def view_files_menu(action):
    new_window = Toplevel(wind)
    new_window.title("Server files")
    back_frame = Frame(new_window, style="navbar.TFrame")
    back_frame.pack(fill='both', expand=True)
    # Create a Treeview widget
    tree = Treeview(back_frame)

    # Define columns
    tree["columns"] = ("Name", "Size", "Type")

    # Format columns
    tree.column("#0", width=0, stretch=NO)
    tree.column("Name", anchor=W, width=200)
    tree.column("Size", anchor=W, width=100)
    tree.column("Type", anchor=W, width=100)

    # Create headings
    tree.heading("#0", text="", anchor=W)
    tree.heading("Name", text="Name", anchor=W)
    tree.heading("Size", text="Size", anchor=W)
    tree.heading("Type", text="Type", anchor=W)

    # Add data to the treeview
    lines = clienter.list_files()
    for i in range(len(lines)):
        name = lines[i].split()[-1]
        size = lines[i].split()[-5]
        if lines[i].split()[0] == "drwxrwxrwx":
            Filetype = "Directory"
        else:
            Filetype = "File"
        tree.insert("", "end", text=i, values=(name, size, Filetype))

    # Display the treeview
    tree.pack(fill=BOTH, expand=True)
    if action == 1:
        def download():
            selected_items = tree.selection()
            for item in selected_items:
                clienter.download_file(tree.item(item)["values"][0])
        Button(back_frame, text="Download", command=download, style="navbutton.TLabel").pack(pady=10)

    elif action == 2:
        tree = Treeview(new_window, columns=("File Name", "Size", "Type"), selectmode='browse')
        def upload():
            from tkinter.filedialog import askopenfilename
            file_path = askopenfilename()
            if file_path:
                selected_items = tree.selection()
                if selected_items != ():
                    clienter.change_directory(tree.item(selected_items[0])["values"][0])
                clienter.upload_file(file_path)
                new_window.destroy()
        def new_fold():
            new_fold_name = StringVar()
            Entry_frame = Frame(back_frame)
            Entry_frame.pack(pady=5)
            selected_items = tree.selection()
            def confirm():
                if selected_items != ():
                    clienter.change_directory(tree.item(selected_items[0])["values"][0])
                clienter.create_directory(new_fold_name.get())
                new_window.destroy()
            Label(Entry_frame, text="New folder name:").grid(row=0, column=0)
            Entry(Entry_frame, textvariable=new_fold_name).grid(row=0, column=1)
            Button(Entry_frame, text="Create", command=confirm).grid(row=0, column=2)
            selected_items = tree.selection()
        Button(back_frame, text="Upload", command=upload, style="navbutton.TLabel").pack(pady=5)
        Button(back_frame, text="Create new folder", command=new_fold, style="navbutton.TLabel").pack(pady=5)
    elif action == 0:
        def delete():
            selected_items = tree.selection()
            if messagebox.askyesno("Warning", "Are you sure you want to delete the selected files?"):
                for item in selected_items:
                    clienter.delete_file(tree.item(item)["values"][0])
                new_window.destroy()
        Button(back_frame, text="Delete selected items", command=delete, style="navbutton.TLabel").pack(pady=5)

def easy_menu():
    clear() #Clears the previous menu
    easy_back = Frame(main_frame, style="Custom2.TFrame")
    easy_back.pack(fill='both', expand=True)
    easy_back.grid_columnconfigure(0, weight=1)
    easy_back.grid_columnconfigure(1, weight=1)
    easy_back.grid_rowconfigure(0, weight=1)
    options_frame = VerticalScrolledFrame(easy_back, style="Custom2.TFrame")
    options_frame.grid(row=0, column=0, sticky='nsew')

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
    # img = ImageTk.PhotoImage(Image.open("imgs/dog2.jpg"))
    # image_label = Label(description_frame, image=img)
    # image_label.image = img
    # image_label.pack()
    Label(description_frame, text="FTP project", style="desc_title.TLabel").pack()
    Label(description_frame, text="Version 1.0", style="desc_version.TLabel").pack()

    #Redirect to repo
    Repo_frame = Frame(description_frame, style="Custom2.TFrame")
    img2 = ImageTk.PhotoImage(Image.open("imgs/GitHub2.png"))
    image_git = Label(Repo_frame, image=img2, style="desc_repo.TLabel")
    image_git.image = img2
    image_git.grid(row=0, column=0)
    Button(Repo_frame, text="See GitHub repo", style="desc_repo.TLabel",command=lambda: webbrowser.open("https://github.com/Ali13Yassin/The-Ethel-Project")).grid(row=0, column=1)
    Repo_frame.pack(padx=10, pady=10)

    #Settings options

    def settings_visual_load():
        #TODO: load the settings from the settings file then apply them to the checkboxes
        pass
    #This makes the settings save when any checkbox is pressed
    def on_checkbutton_press():
        #TODO: call the function that saves the settings
        pass
    
    
    #All the settings are stored in these variables
    checkbutton_logs = IntVar()

    checkbutton_autosave = IntVar()
    
    style.configure('Settings_checkbox.TCheckbutton', background='#391D0D', indicatorbackground='#E99A5D', indicatorcolor='#391D0D', foreground='#A5622F', focuscolor='#E99A5D')
    ftp_settings_frame = Frame(options_frame.interior, style="navbar.TFrame")
    ftp_settings_frame.pack(padx=10, pady=10)
    Label(ftp_settings_frame, text="FTP settings", style="Title.TLabel").grid(row=0, column=0)
    Label(ftp_settings_frame, text="Server logs", style="settings.TLabel").grid(row=1, column=0)
    Checkbutton(ftp_settings_frame, style="Settings_checkbox.TCheckbutton", command=lambda: on_checkbutton_press(), variable=checkbutton_logs).grid(row=1, column=1)
    

    easy_settings_frame = Frame(options_frame.interior, style="navbar.TFrame")
    easy_settings_frame.pack(padx=10, pady=10)
    Label(easy_settings_frame, text="Easy transfer settings", style="Title.TLabel").grid(row=0, column=0)
    Label(easy_settings_frame, text="Auto Accept", style="settings.TLabel").grid(row=1, column=0)
    Checkbutton(easy_settings_frame, style="Settings_checkbox.TCheckbutton", command=lambda: on_checkbutton_press(), variable=checkbutton_autosave).grid(row=1, column=1)

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

def clienter_start(adr,usr,pwd):
    clienter.connect_to_server(adr,usr,pwd)
    if clienter.list_files() != []:
        client_connected_menu(adr)
    #TODO: use threading to add a loop that checks if the connection is still active
    else:
        pass
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