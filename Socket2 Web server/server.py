'''
Kenneth Munk
302322007
CSC138
Socket 2 Assignment
'''
#import socket module

from socket import *

#importing code from the tcpserver.py assignment
tcpPort = 6789
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start

#binding to local 
tcpSocket.bind(('',tcpPort))
#Fill in end

while True:
    tcpSocket.listen(1)
    print('The server is probably ready to receive')
    print 'Ready to serve...'
    connectionSocket, addr = tcpSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = #Fill in start #Fill in end
        #Send one HTTP header line into socket
        #Fill in start

        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
            connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start

        #Fill in end
        #Close client socket
        #Fill in start

        #Fill in end
serverSocket.close()