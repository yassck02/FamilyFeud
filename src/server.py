#  Server program for the Family Feud game
#  Authors: 	Logan Docherty, Todd Noreen, Connor Yass
#  Created on: 	2/26/2019

from socket import *		# for use of socket
from random import randint  # for use of random integer
from thread import *		# for use of thread
import math					# for use of log
import json					# for r/w question and user files

questionFilePath = "/Users/Connor/Documents/School/College/Semester 8/Networking/FamilyFeud/dat/questions.json"
usersFilePath = "/Users/Connor/Documents/School/College/Semester 8/Networking/FamilyFeud/dat/users.json"

import urwid

# ---------------------------------------------------------------------

def handle(socket, address):
	"""Handles an incomming socket connection"""

	# Recieve and handle the clients response
	while(True):

		request = recieve(socket)

		if request['command'] == "playGame":
			playGame(socket, address)

		elif request['command'] == "getHistory":
			getUserHistory(socket, request['username'])

		elif request['command'] == "getRecord":
			getUserRecord(socket, request['username'])

		elif request['command'] == "login":
			login(socket, request['username'], request['password'])

		elif request['command'] == "register":
			register(socket, address, request['username'], request['password'])

		elif request['command'] == "disconnect":
			break

	# End the connection
	print("- Disconnected from " + str(address))
	socket.close()

# ---------------------------------------------------------------------

def playGame(socket, address):
	"""Begins the Family Feude gameplay loop"""

	totalScore = 0

	# Main game loop starts here
	for i in range(3):

		# Send a random question
		question = getRandomQuestion()
		send(socket, question)

		# recieve the users answer
		userAnswer = recieve(socket)


		# calculate the running score
		totalScore += calculateScore(question, userAnswer)

	# Send the total score
	result = { "totalScore": totalScore }
	send(socket, result)

	# Store the result
	saveScore("username", totalScore)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def calculateScore(question, userAnswer):
	"""Calculates the score of the question for the given answer"""

	score = 0

	## TODO: Update so an exact match isnt necessary
	for answer in question["answers"]:
		if(answer['answer'] == userAnswer):
			score = answer['score']

	return score

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def saveScore(score, username):
	"""Opens the users file, searches for the username, and adds the score"""

	with open(usersFilePath, 'r+') as usersfile:

		# load the json from the file
		users = json.load(usersfile)

		# find the user
		for user in users:
			if(user['username'] == username):
				
				# add the record
				record = {
					'date': 'today',
					'score': score
				}
				user['history'].append(record)

		# save the file
		usersfile.seek(0)
		usersfile.write(json.dumps(users, indent=4))

# ---------------------------------------------------------------------

def loadQuestionsFile():
	"""Opens the users.json file and returns it as a json object"""
	
	with open(questionFilePath) as file:
		return json.load(file)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

questions = loadQuestionsFile()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def getRandomQuestion():
	""" Returns a random question from the list"""

	index = randint(1, len(questions))
	return questions[index]

# ---------------------------------------------------------------------

def register(socket, address, username, password):
	"""Adds the given user to the users file if it doesent already esist"""

	with open(usersFilePath, 'r+') as usersfile:

		# load the json from the file
		users = json.load(usersfile)

		# make sure the user doesent already exist
		for user in users:
			if(user['username'] == username):
				res = { 'code': 404, 'description': 'user already exists, please login' }
				send(socket, res)
				usersfile.close()
				return

		# create a new user
		newUser = {
			'username': username,
			'password': password,
			'addresses': [ address ],
			'history': [ ]
		}

		# write the user and save the file
		users.append(newUser)
		usersfile.seek(0)
		usersfile.write(json.dumps(users, indent=4))

		res = { 'code': 200, 'description': 'user added' }
		send(socket, res)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def login(socket, username, password):
	"""Logs the user in if their username exists and password is correct"""

	with open(usersFilePath) as usersfile:

		# load the users json array from the file
		users = json.load(usersfile)

		# search for the user and check the password
		for user in users:

			if(user['username'] == username):
				if(user['password'] == password):
					res = { 'code': 200, 'description': 'OK' }
					send(socket, res)
					usersfile.close()
					return
				else:
					res = { 'code': 404, 'description': 'invalid password' }
					send(socket, res)
					usersfile.close()
					return

		res = { 'code': 404, 'description': 'invalid username' }
		send(socket, res)

# ---------------------------------------------------------------------

def getUserRecord(socket, username):
	"""Opens the users.json file and calclates the record of an individual user"""

	with open(usersFilePath) as usersfile:

		# load the json from the file
		users = json.load(usersfile)

		bestRecord = { 'date': '', 'score': 0 }

		# search for the user in question
		for user in users:
			if(user['username'] == username):

				# make sure the user has played alteast 1 game
				if(len(user['history']) <= 0):
					response = { 'code': 410, 'description': 'username has no history' }
					send(socket, response)
					usersfile.close()
					return

				# loop through all their records
				for record in user['history']:
					if (record['score'] > bestRecord['score']):
						bestRecord = record

				response = { 'code': 200, 'record': bestRecord }
				send(socket, response)
				usersfile.close()
				return

		# if the user doesent exist ...
		response = { 'code': 404, 'description': 'invalid username' }
		send(socket, response)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def getPopulationRecord(socket): 
	"""Opens the users.json file then calclates and sends the record of all users"""

	with open(usersFilePath, "r") as usersfile:

		# load the json from the file
		users = json.load(usersfile)

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

def getUserHistory(socket, username):
	"""Opens the users.json file, and calculates then sends the record of an individual user"""

	with open(usersFilePath, "r") as usersfile:

		# load the json from the file
		users = json.load(usersfile)

		# search for the user in question
		for user in usersFile['users']:
			if(user['username'] == username):

				response = { 'code': 200, 'history': user['history']}
				send(socket, response)
				usersfile.close()
				return

	# if the user doesent exist
	response = { 'code': 404, 'description': 'invalid username'}
	send(socket, response)

# ---------------------------------------------------------------------

def recieve(socket):
	""" Recieves a json string from the client and converts it to a dictionary """

	jsonString = socket.recv(1024).decode("ascii")
	message = json.loads(jsonString)

	#print("RECIEVED: ", jsonString)
	return message

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def send(socket, dictionary):
	""" Converts the dictionary to a json string and sends it to the client"""

	jsonString = json.dumps(dictionary)
	socket.send(jsonString.encode())

	#print("SENDING: ", jsonString)

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
		print("+ Connected to " + str(address))
		response = { 'code': 200, 'description': 'OK' }
		send(connection, response)
		
		start_new_thread(handle, (connection, address))

# ---------------------------------------------------------------------

main()

# ---------------------------------------------------------------------
