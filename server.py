import socket

HOSTNAME = "localhost"
PORTNUMBER = 9000
BACKLOG = 5
BUFFERSIZE = 5000

def createServer():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        serverSocket.bind((HOSTNAME, PORTNUMBER))
        serverSocket.listen(BACKLOG)        # if server is busy, hold 5 more requests.
        while True:
            clientSocket, address = serverSocket.accept()       # accept the connection with the client
            requestData = clientSocket.recv(BUFFERSIZE).decode()    # transfer UTF-8 into Unicode 
            pieces = requestData.split("\n")
            if len(pieces) > 0:
                print(pieces[0])
            
            # construct the response:
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body><h1>Hello, world!</h1></body></html>\r\n\r\n"
            
            # send response to client:
            clientSocket.sendall(data.encode())
            
            # shutting down the connection with that client:
            clientSocket.shutdown(socket.SHUT_WR)
        
        
    except KeyboardInterrupt:
        print("\nShutting down ...\n")
    except Exception as exc:
        print("Error:\n\t{}".format(exc))
    
    serverSocket.close()


if __name__ == "__main__":
    try:
        print("Access http://{}:{}".format(HOSTNAME, PORTNUMBER))
        createServer()
    except:
        print("Error .. Something went wrong!")