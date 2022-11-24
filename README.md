# CS361-accounts-microservice
account tracker microservice for CS361

This is a group project in which each member created a microservice and a separate personal project. Each individuals personal project is required to use one or more of the other member's microservices.

This repository contains my basic account managing microservice. It is capable of creating accounts, logging in/out, editing/retrieving account information. (There is NO password encryption as that fell outside the scope of the assignment. "Passwords" are stored as simple text.") account_functions.py displays the methods for handling these requests. 

After starting the server (accounts_server.py), other group members are able to send requests in the following format:

{
    "action": [create/edit/etc.],
    "username": [name],
    "password": [password],
    "description": [user info text]
}

Several example requests/commands are available in the various "_example.py" files
