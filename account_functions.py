def route_request(request):
    """
    Takes the JSON request and parses it then calls the appropriate function based on
    the request type
    """
    if request["action"] == "create":
        create_account(request)
    elif request["action"] == "login":
        login(request)
    elif request["action"] == "edit":
        edit(request)
    elif request["action"] == "retrieve":
        retrieve(request)

    return


def create_account(request):
    """
    Creates a new user account. Verifies username is not a duplicate.

    Requires: username, password, and description
    returns: 0 with "account created' msg on success, 1 with error message if unsuccessful
            ex. {"0": "account created"}
    """

    return


def login(request):
    """
    Logs in the user specified in the request. Verifies existence of username and matching password
    for that username.

    Requires: username, password
    returns: 0 with "logged in" msg on success, 1 with "invalid user" msg, 2 with "incorrect password" msg
            ex. {"0": "logged in"}
    """

    return


def edit(request):
    """
    Edits the description field for the specified user.

    Requires: username, new_description
    returns: 0 with "updated description" msg on success, 1 with "invalid user" msg
            ex. {"0": "updated description"}
    """

    return


def retrieve(request):
    """
    Returns all account information for the specified user. Verifies existence of user.

    requires: username
    Returns: on success returns account as JSON ex. {"username":{username}, "password":{password},
            "description":{description}"
            1 with "invalid user" msg on failure
    """
    return


def format_response(pre_response):
    """
    Takes the encoded JSON response and creates the information that needs to be sent before it

    """
    response_len = len(pre_response)
    response_header = str(response_len).encode('utf-8')
    response_header += b' ' * (1024 - len(response_header))
    return response_header
