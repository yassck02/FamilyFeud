from socket import *
import json

_socket = socket(AF_INET, SOCK_STREAM)

def connect(ip, port):
    _socket.connect(ip, port)

    response = recieve()
    if (response['code'] != 200):
        _socket.close()
        print("ERROR: Could not connect to server :(")
        return
    else:
        print("+ Connected to " + str(ip) + " on port " + str(port))

def disconnect():
    request = { 'command': 'disconnect' }
    send(_socket, request)
    _socket.close()
    print("- Disconnected from server")

# ---------------------------------------------------------------------

def recieve():
    """ Recieves a json string from the server and converts it to a dictionary """

    jsonString = _socket.recv(1024).decode("ascii")
    message = json.loads(jsonString)

    #print("RECIEVED: ", jsonString)
    return message

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def send(dictionary):
    """ Converts the dictionary to a json string and sends it to the server"""

    jsonString = json.dumps(dictionary)
    _socket.send(jsonString.encode())

    #print("SENDING: ", jsonString)

# ---------------------------------------------------------------------