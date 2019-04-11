#  Client program for the Family Feud game
#  Authors: 	Logan Docherty, Todd Noreen, Connor Yass
#  Created on: 	2/26/2019

from socket import *	# For use of socket
import json				# for r/w question and user files

# ---------------------------------------------------------------------

def getRecord(socket):
	""" gets the record of an individual user, or the whole population """

	username = raw_input("Which user would you lke to get the record for? ")
	
	request = { 'command': 'getRecord', 'username': username }
	send(socket, request)

	# recieve the response
	response = recieve(socket)

	# act on the response
	if (response['code'] == 200):
		print(response['record'])
	else:
		print("ERROR: ", response['description'])

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def getHistory(socket):
	""" gets the history of an individual user """

	username = raw_input("Which user would you lke to get the history for? ")
	
	request = { 'command': 'getHistory', 'username': username }
	send(socket, request)

	# recieve the response
	response = recieve(socket)

	# act on the response
	if (response['code'] == 200):
		print(response['history'])
	else:
		print("ERROR: ", response['description'])
	
#---------------------------------------------------------------------

def playGame(socket):
	""" The main game function """

	# Tell the server we want to start a game
	request = { 'command': 'playGame' }
	send(socket, request)

	for i in range(3):

		#recieve a question
		question = recieve(socket)
		print(question)

		# send the guess to the server
		guess = raw_input("Input your guess: ")
		request = { 'guess': guess }
		send(socket, request)

	# Recieve the total score
	totalScore = recieve(socket)
	print(totalScore)


# ---------------------------------------------------------------------

def register(socket):
	""" Creates a new user on the server """

	username = raw_input("Input your username: ")
	while (len(username) <= 0):
		username = raw_input("Must be more than 0 characters. Try again: ")

	password1 = raw_input("Input your password: ")
	while (len(password1) <= 0):
		password1 = raw_input("Must be more than 0 characters. Try again: ")

	password2 = raw_input("Re enter your password: ")
	while (password1 != password2):
		password2 = raw_input("Passwords do not match. Try again: ")

	request = { 'command': 'register', 'username': username, 'password': password1 }
	send(socket, request)

	# recieve the response
	response = recieve(socket)

	# act on the response
	if (response['code'] == 200):
		print("Register success")
	else:
		print("ERROR: ", response['description'])

# ---------------------------------------------------------------------

def login(socket):
	""" Logs the user into the server """

	# input the username and password
	username = raw_input("Input your username: ")
	password = raw_input("Input your password: ")

	# send it to the server
	request = { 'command': 'login', 'username': username, 'password': password }
	send(socket, request)

	# recieve the response
	response = recieve(socket)

	# act on the response
	if (response['code'] == 200):
		print("Login success")
	else:
		print("ERROR: ", response['description'])

# ---------------------------------------------------------------------

def recieve(socket):
	""" Recieves a json string from the server and converts it to a dictionary """

	jsonString = socket.recv(1024).decode("ascii")
	message = json.loads(jsonString)

	#print("RECIEVED: ", jsonString)
	return message

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def send(socket, dictionary):
	""" Converts the dictionary to a json string and sends it to the server"""

	jsonString = json.dumps(dictionary)
	socket.send(jsonString.encode())

	#print("SENDING: ", jsonString)

# ---------------------------------------------------------------------

def main():

	# Define  a server port number and server address
	ip = "localhost"
	port = 20123

	# ip = raw_input("Server ip address: ")
	# port = raw_input("Server port number: ")

	# Create a client TCP socket to connect with the server
	_socket = socket(AF_INET, SOCK_STREAM)
	_socket.connect((ip, port))

	# Obtain the response from the server
	response = recieve(_socket)
	if (response['code'] != 200):
		_socket.close()
		print("Could not connect to server :(")
		return
	else:
		print("+ Connected to " + str(ip) + " on port " + str(port))

	while(True):

		print('-----------------------------------------')

		# Ask the user what they would like to do
		print("\t[0] Register")
		print("\t[1] Login")
		print("\t[2] Play Game")
		print("\t[3] Get Record")
		print("\t[4] Get History")
		print("\t[5] Quit (Disconnect)")

		tmp = raw_input("Input your selection: ")

		print('- - - - - - - - - - - - - - - - - - - - -')

		if "0" in tmp:
			register(_socket)
		elif "1" in tmp:
			login(_socket)
		elif "2" in tmp:
			playGame(_socket)
		elif "3" in tmp:
			getRecord(_socket)
		elif "4" in tmp:
			getHistory(_socket)
		elif "5" in tmp:
			break
		else: 
			print("ERROR: Unrecognized selection...")

	# Terminate the conection
	print("- Disconnecting")

	request = { 'command': 'disconnect' }
	send(_socket, request)

	_socket.close()

# ---------------------------------------------------------------------

main()

# ---------------------------------------------------------------------
