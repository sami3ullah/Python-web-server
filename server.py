from socket import *
import time
from _thread import *
serverPort = 6000
serverSocket = socket(AF_INET,  SOCK_STREAM)#ServerSocket = TCP
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("Server Running\nPort:%i"%serverPort)
#ServiceThread Function Connects multiple Clients to the server
def ServiceThread(connectionSocket):
        while 1:
                data = connectionSocket.recv(2048)
                if not data: #if Client Disconnects then break out of loop and close the connection
                        print(connectionSocket.getpeername(),' Disconnected')
                        break;
                mdata = data.decode() #Decoding and storing in received data to mdata varibale
                print("From Client: ",connectionSocket.getpeername(),">>",mdata)
                try: #Error message will be sent in case of non integer input from the client
                        r = eval(mdata) #This function automatically evaluates a string and converts it into intger
                        string = str(r) #After the string is evaulated. It requires to be converted into string in order to send it to the client.
                except:
                        string = 'Cannot Compute such Input. Try Again' #Error Message
                connectionSocket.sendall(string.encode())
        connectionSocket.close()
while 1:
	connectionSocket, addr = serverSocket.accept()
	print("Client Connected: "+addr[0]+" Port: "+ str(addr[1]))
	start_new_thread(ServiceThread, (connectionSocket,))#Creates a new thread everytime a new client is connected
serverSocket.close()
