# required package to create sockets:
import socket

URL = "127.0.0.1"       # domain name
PORT_NUMBER = 9000            # port number (80: port for http web servers)
BUFFERSIZE = 512
FILE_NAME = "romeo.txt"

# create the socket:
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # (Address Family, Socket Type)

# connect to the created socket:
mySocket.connect((URL, PORT_NUMBER))

# command to be sent:
command = 'GET http://{}/{} HTTP/1.0\r\n\r\n'.format(URL, FILE_NAME).encode()    # convert Unicode into UTF-8 data

# send the previous command:
mySocket.send(command)


# the main program:
while True:
    # receive data:
    data = mySocket.recv(BUFFERSIZE)   # recv(BufferSize)
    
    # something bad happened !!
    if len(data) < 1:
        break
    
    # convert UTF-8 into Unicode data:
    print(data.decode(), end=' ')
    
# close the connection:
mySocket.close()