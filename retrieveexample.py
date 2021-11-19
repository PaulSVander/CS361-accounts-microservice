import socket
import json

# Create a socket object
connectedSocket = socket.socket()

# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
connectedSocket.connect(('127.0.0.1', port))


a = {
    "action": "retrieve",
    "username": "Bobby"
}
b = json.dumps(a)
b = b.encode('utf-8')
blen = len(b)
blen_str = str(blen).encode('utf-8')
blen_buffer = b' ' * (1024 - len(blen_str)) + blen_str
connectedSocket.send(blen_buffer)
connectedSocket.send(b)


# receive data from the server and decoding to get the string.
print(connectedSocket.recv(1024).decode())
print(connectedSocket.recv(1024).decode())


# close the connection
connectedSocket.close()
