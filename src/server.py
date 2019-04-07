#  Server program for the Family Feud game
#  Authors: 	Logan Docherty, Todd Noreen, Connor Yass
#  Created on: 	2/26/2019

from socket import *		# for use of socket
from random import randint  # for use of random integer
from thread import *		# for use of thread
import math					# for use of log
import json					# for r/w question and user files

questionFilePath = "/Users/Connor/Documents/School/College/Semester 8/Networking/FamilyFeud/res/questions.json"
usersFilePath = "/Users/Connor/Documents/School/College/Semester 8/Networking/FamilyFeud/res/users.json"

# ---------------------------------------------------------------------

def handle(socket, address):
	"""Handles an incomming socket connection"""

	# Recieve and handle the clients response
	while(True):

		req = recieve(socket)

		if req['command'] == "playGame":
			playGame(socket, address)

		elif req['command'] == "getHistory":
			getHistory(socket)

		elif req['command'] == "getRecord":
			getRecord(socket)

		elif req['command'] == "login":
			login(socket, req['username'], req['password'])

		elif req['command'] == "register":
			register(socket, address, req['username'], req['password'])

		elif req['command'] == "disconnect":
			break

	# End the connection
	print("Disconnected from " + str(address))
	socket.close()

# ---------------------------------------------------------------------

def playGame(socket, address):
	"""Begins the 2 minute Family Feude gameplay loop"""

	# Main game loop starts here
	loop = True
	while loop:

		# Obtain the guess sent by the client through the socket
		response = socket.recv(1024).decode("ascii")

		# store the score
		with open("records.txt", "a+") as file:
			score = math.log(num, 2) / guessCount
			file.write(str(address) + "\t" + str(score) + "\n")

# ---------------------------------------------------------------------

def getRandomQuestion():
	"""Opens the questions.json file and Returns a random question from it"""

	question = {}

	# open the questions file
	with open(questionFilePath) as file:

		# load the json
		questions = json.load(file)

		# choose a random index
		index = randint(1, len(questions))
		question = questions[index]

	return question

# ---------------------------------------------------------------------

def register(socket, address, username, password):

	# open the users file
	with open(usersFilePath, 'ra+') as file:

		# load the json
		users = json.load(file)

		# make sure the user doesent already exist
		for user in users:
			if(user['username'] == username):
				res = { 'code': 404, 'description': 'user already exists, please login' }
				send(socket, res)
				return

		# create a new user ...
		newUser = {
			'username': username,
			'password': password,
			'addresses': [ address ],
			'history': [ ]
		}

		# ... write it to the file
		file.write(json.dumps(newUser))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def login(socket, username, password):

	# open the users file
	with open(usersFilePath) as file:

		# load the json
		users = json.load(file)

		# search for the user and check the password
		for user in users:

			if(user['username'] == username):
				if(user['password'] == password):
					res = { 'code': 200, 'description': 'OK' }
					send(socket, res)
					return
				else:
					res = { 'code': 404, 'description': 'invalid password' }
					send(socket, res)
					return

		res = { 'code': 404, 'description': 'invalid username' }
		send(socket, res)


# ---------------------------------------------------------------------

def getUserRecord(username):
	"""Opens the users.json file and calclates the record of an individual user"""

	# open the users file
	with open(usersFilePath) as file:

		# load the json
		users = json.load(file)

		bestRecord = { 'date': '', 'score': 0 }

		# search for the user in question
		for user in users:
			if(user['username'] == username):

				# make sure the user has played alteast 1 game
				if(len(user['history']) <= 0):
					response = { 'code': 410, 'description': 'username has no history' }
					send(socket, response)
					return

				# loop through all their records
				for record in user['history']:
					if (record['score'] > bestRecord['score']):
						bestRecord = record

				response = { 'code': 200, 'record': bestRecord }
				send(socket, response)
				return
	
		# if the user doesent exist ...
		response = { 'code': 404, 'description': 'invalid username' }
		send(socket, response)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def getPopulationRecord(): 
	"""Opens the users.json file then calclates and sends the record of all users"""

	# open the useres file
	with open(usersFilePath) as file:

		# load the json
		users = json.load(file)

		bestUser = ""
		bestRecord = { 'date': '', 'score': 0 }

		# loop through each user
		for user in users:
			for record in user['history']:
				if (record['score'] > bestRecord['score']):
					bestRecord = record
					bestUser = user['username']

		response = { 'code': 200, 'record': bestRecord, 'user': bestUser }
		send(socket, response)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def getUserHistory(username):
	"""Opens the users.json file, and calculates then sends the record of an individual user"""

	# open the useres file
	with open(usersFilePath) as file:

		# load the json
		users = json.load(file)

		# search for the user in question
		for user in users:
			if(user['username'] == username):

				response = { 'code': 200, 'history': user['history']}
				send(socket, response)
	
		# if the user doesent exist
		response = { 'code': 404, 'description': 'invalid username'}
		send(socket, response)

# ---------------------------------------------------------------------

def recieve(socket):
	""" Recieves a json string from the server and converts it to a dictionary """

	jsonString = socket.recv(1024).decode("ascii")
	message = json.loads(jsonString)

	print("RECIEVED: ", jsonString)
	return message

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def send(socket, dictionary):
	""" Converts the dictionary to a json string and sends it to the server"""

	jsonString = json.dumps(dictionary)
	socket.send(jsonString.encode())

	print("SENDING: ", jsonString)

# ---------------------------------------------------------------------

def main():

	# Create a server socket
	_socket = socket(AF_INET, SOCK_STREAM)

	# Define  a server port number, bind it to the server socket, and listen
	port = 20123
	_socket.bind(("", port))
	_socket.listen(1)

	print ("FF Server: Listening on port " + str(port))

	# Create an infinite loop to process all connection requests
	while True:

		# Create a connection socket for each connection request received
		connection, address = _socket.accept()

		# tell the client its connetion attempt was succesful
		print("Connected to " + str(address))
		response = { 'code': 200, 'description': 'OK' }
		send(connection, response)
		
		start_new_thread(handle, (connection, address))

# ---------------------------------------------------------------------

main()

# ---------------------------------------------------------------------
