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
serverSocket.bind(('',tcpPort))

print("attempting launch")
#Fill in end

while True:
	serverSocket.listen(1)
	print('The server is probably ready to receive')
	print 'Ready to serve...'
	connectionSocket, addr = serverSocket.accept()
	try:
		message = connectionSocket.recv(1024)
		print (str(message))
		filename = message.split()[1]
		fileContents = open(filename[1:])
		#reading the file content of the desired file
		outputdata = fileContents.read()
		fileContents.close()
		print(str(outputdata))
		#Send one HTTP header line into socket
		#Fill in start
		connectionSocket.send("HTTP/1.0 200 OK\r\n\r\n")
		#Fill in end
		#Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i])
		connectionSocket.close()

	except IOError:

		#Send response message for file not found
		#Fill in start
		connectionSocket.send("404 Not Found")


		#Fill in end
		#Close client socket
		#Fill in start
		connectionSocket.close()
		#Fill in end

serverSocket.close()

print("launch end")