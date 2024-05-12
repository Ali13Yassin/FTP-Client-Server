import ftplib
import os
from pathlib import Path

os.chdir(Path(__file__).parent)

# Connect to the FTP server
def connect_to_server(host, username, password):
    global ftp_server
    ftp_server = ftplib.FTP(host, username, password)
    print("Connected to " + host)
    print(ftp_server.getwelcome())
    return ftp_server

# List the files in the current directory
def list_files():
    print("Files in the current directory:")
    files = ftp_server.dir()
    print(ftp_server.nlst())
    return files

# Change the current directory
def change_directory(directory):
    print("Changing to directory: ")
    ftp_server.cwd(directory)

# Create a new directory
def create_directory(directory_name):
    print("Creating directory: ")
    ftp_server.mkd(directory_name)

# Download a file from the FTP server
def download_file(file):
    with open(file, "wb") as f:
        ftp_server.retrbinary("RETR " + file, f.write)

# Upload a file to the FTP server
def upload_file(file):
    print("Uploading file: ")
    with open(file, "rb") as f:
        ftp_server.storbinary("STOR " + file, f)

# Close the connection to the FTP server
def close_connection():
    ftp_server.quit()

connect_to_server("ftp.dlptest.com", "dlpuser", "rNrKYTX9g7z3RgJRmxWuGHbeu")
print(ftp_server.nlst())
files = ftp_server.dir()
change_directory(ftp_server.nlst()[0])

print(ftp_server.nlst())
print(ftp_server.pwd())