from socket import *
import json

serverPort = 12345
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))
serverSocket.listen(1)

accounts = {}
userKey = 0


def format_response(pre_response):
    """
    Takes the encoded JSON response and creates the information that needs to be sent before it

    """
    response_len = len(pre_response)
    response_header = str(response_len).encode('utf-8')
    response_header += b' ' * (1024 - len(response_header))
    return response_header


while True:
    connectionSocket, addr = serverSocket.accept()

    """
    Since bytes are continously being sent over the connection we have to send information about
    the length of the information we are sending as well
    """

    # We expect the first 1024 bytes to tell us how long the next message will be
    msg_len = connectionSocket.recv(1024).decode('utf-8')
    msg_len = int(msg_len)

    # We receive the number of bytes we were told to expect (msg_len)
    receivedRaw = connectionSocket.recv(msg_len).decode('utf-8')
    received = json.loads(receivedRaw)

    # If the client wants to create a new account
    if received["action"] == "create":
        accounts[userKey] = {"username": received["username"], "description": received["description"]}
        # Client is given "token" that is tied to the account they created
        response_body = json.dumps({"userToken": userKey}).encode('utf-8')
        print(response_body)
        response_head = format_response(response_body)
        userKey += 1
        connectionSocket.send(response_head)
        connectionSocket.send(response_body)
    # If the client wants to retrieve info about an account
    elif received["action"] == "retrieve":
        userToken = received["userToken"]
        response_body = json.dumps(accounts[int(userToken)]).encode('utf-8')
        response_head = format_response(response_body)
        connectionSocket.send(response_head)
        connectionSocket.send(response_body)
    print(accounts)