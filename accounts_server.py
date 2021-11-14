from socket import *
import json
import account_functions

serverPort = 12345
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))
serverSocket.listen(1)

accounts = {}
userKey = 0

while True:
    connectionSocket, addr = serverSocket.accept()

    # We expect the first 1024 bytes to tell us how long the next message will be
    msg_len = connectionSocket.recv(1024).decode('utf-8')
    msg_len = int(msg_len)

    # We receive the number of bytes we were told to expect (msg_len)
    receivedRaw = connectionSocket.recv(msg_len).decode('utf-8')
    received = json.loads(receivedRaw)

    account_functions.route_request(received)

    # # If the client wants to create a new account
    # if received["action"] == "create":
    #     accounts[userKey] = {"username": received["username"], "description": received["description"]}
    #     # Client is given "token" that is tied to the account they created
    #     response_body = json.dumps({"userToken": userKey}).encode('utf-8')
    #     print(response_body)
    #     response_head = format_response(response_body)
    #     userKey += 1
    #     connectionSocket.send(response_head)
    #     connectionSocket.send(response_body)
    # # If the client wants to retrieve info about an account
    # elif received["action"] == "retrieve":
    #     userToken = received["userToken"]
    #     response_body = json.dumps(accounts[int(userToken)]).encode('utf-8')
    #     response_head = format_response(response_body)
    #     connectionSocket.send(response_head)
    #     connectionSocket.send(response_body)
    print(accounts)