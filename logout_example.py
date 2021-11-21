import socket
import json


# Create a socket object
connectedSocket = socket.socket()

# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
connectedSocket.connect(('127.0.0.1', port))

x = {
    "action": "logout",
    "username": "Bobby",
}
y = json.dumps(x)
y = y.encode('utf-8')
ylen = len(y)
ylen_str = str(ylen).encode('utf-8')
ylen_buffer = b' ' * (1024 - len(ylen_str)) + ylen_str
connectedSocket.send(ylen_buffer)
connectedSocket.send(y)


# receive data from the server and decoding to get the string.
print(connectedSocket.recv(1024).decode())
print(connectedSocket.recv(1024).decode())
print(connectedSocket.recv(1024).decode())

# close the connection
connectedSocket.close()