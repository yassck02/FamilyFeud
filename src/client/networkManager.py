from socket import *
import json

_socket = socket(AF_INET, SOCK_STREAM)

port = 6969

connected = False
loggedin = False

def connect(ip_address):
    """ Creates a socket connection to the givn address and port
        Returns true if success, fales if not """

    # Attempt to connect
    _socket.connect((ip_address, port))

    # Reciev and act on the response
    response = recieve()
    if (response['code'] != 200):
        _socket.close()
        connected = False
        return False
    else:
        connected = True
        return True

def disconnect():
    """ Closes the socket connection """

    if(connected == False):
        return

    request = { 'command': 'disconnect' }
    send(request)
    _socket.close()
    connected = False

# ---------------------------------------------------------------------

def recieve():
    """ Recieves a json string from the server and converts it to a dictionary """

    jsonString = _socket.recv(1024).decode("ascii")
    message = json.loads(jsonString)

    return message

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def send(dictionary):
    """ Converts the dictionary to a json string and sends it to the server"""

    jsonString = json.dumps(dictionary)
    _socket.send(jsonString.encode())


# ---------------------------------------------------------------------