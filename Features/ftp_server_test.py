# first of all import the socket library 
import socket

# next create a socket object 
s = socket.socket()

# reserve a port on your computer in our 
# case it is 12345 but it can be anything 

# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests 
# coming from other computers on the network 



def start_listening(port):
    s.bind(('', port))
    print ("socket binded to %s" %(port))

    # put the socket into listening mode 
    s.listen(5) #Number indicates how many possible connections can be queued
    print ("socket is listening")

    # Establish connection with client.
    c, addr = s.accept()
    print ('Got connection from', addr )

    # send a thank you message to the client. encoding to send byte type. 
    c.send('Thank you for connecting'.encode())

    # Close the connection with the client 
    c.close()