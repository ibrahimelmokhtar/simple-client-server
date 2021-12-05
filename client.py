# required package to create sockets:
import socket

URL = 'data.pr4e.org'       # domain name
PORT_NUMBER = 80            # port number (80: port for http web servers)

# create the socket:
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # (Address Family, Socket Type)

# connect to the created socket:
mySocket.connect((URL, PORT_NUMBER))

# command to be sent:
command = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()    # convert Unicode into UTF-8 data

# send the previous command:
mySocket.send(command)


# the main program:
while True:
    # receive data:
    data = mySocket.recv(512)   # recv(BufferSize)
    
    # something bad happened !!
    if len(data) < 1:
        break
    
    # convert UTF-8 into Unicode data:
    print(data.decode(), end=' ')
    
# close the connection:
mySocket.close()