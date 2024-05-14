import ftplib
import os
from pathlib import Path
from tkinter import messagebox

os.chdir(Path(__file__).parent)

# Connect to the FTP server
def connect_to_server(host, username, password):
    global ftp_server
    try:
        # Your ftplib code here
        ftp_server = ftplib.FTP(host, username, password)
    except ftplib.all_errors as e:
        error_string = str(e)
        messagebox.showerror("Error", error_string)
        return error_string

# List the files in the current directory
def list_files():
    lines = []
    ftp_server.dir(lambda line: lines.append(line))
    return lines

# Change the current directory
def change_directory(directory):
    ftp_server.cwd(directory)

# Create a new directory
def create_directory(directory_name):
    ftp_server.mkd(directory_name)

# Download a file from the FTP server
def download_file(file):
    with open(file, "wb") as f:
        ftp_server.retrbinary("RETR " + file, f.write)

# Upload a file to the FTP server
def upload_file(file):
    with open(file, "rb") as f:
        ftp_server.storbinary("STOR " + file, f)

def delete_file(file):
    ftp_server.delete(file)

# Close the connection to the FTP server
def close_connection():
    ftp_server.quit()


# connect_to_server("127.0.0.1", "someuser", "12345")
# lines = []
# ftp_server.dir(lambda line: lines.append(line))
# name = lines[2].split()[-1]
# time = lines[2].split()[-2]
# day = lines[2].split()[-3]
# month = lines[2].split()[-4]
# size = lines[2].split()[-5]
# if lines[2].split()[0] == "drwxrwxrwx":
#     Filetype = "Directory"
# else:
#     Filetype = "File"
# print(name, time, day, month, size, Filetype)
# print(ftp_server.size("dog.jpg"))
# print(ftp_server.nlst())
# ftp_server.dir()
# upload_file("dog.jpg")
# print(ftp_server.nlst())
# create_directory("test")
# change_directory("test")
# ftp_server.dir()
# print(ftp_server.nlst())
# print(ftp_server.pwd())