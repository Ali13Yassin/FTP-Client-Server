from ftplib import FTP

# Connect to FTP server
ftp = FTP("127.0.0.1")
ftp.login(user="user", passwd="password")

# List files in the current directory
ftp.dir()

# Download a file
# filename = "example.txt"
# with open(filename, "wb") as file:
#     ftp.retrbinary("RETR " + filename, file.write)

# Upload a file
# filename = "example.txt"
# with open(filename, "rb") as file:
#     ftp.storbinary("STOR " + filename, file)

# Close connection
ftp.quit()
