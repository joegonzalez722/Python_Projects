#import socket library
import socket

#create socket object
s = socket.socket()
print ("Socket created successfully")

# reserve a port in pc, in this case it is 40674, but anything works
IP_Hostname = "200.200.200.5"
port = 40674

#bind the port
s.bind(('', port))
print("socket binded to %s" %(port))

#put socket into listening mode
s.listen(5)
print ("socket is listening")

#a forever loop until interrupt or error occurs
while True:

    #establish a connection with the client
    c, addr = s.accept()
    print ('got connection from', addr)
