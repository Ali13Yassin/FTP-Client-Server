import ftplib

session = ftplib.FTP("192.168.4.65", "user", "12345")
file =open("dog.jpg", "rb")
session.storbinary("STOR dog.jpg", file)
file.close()
session.quit()