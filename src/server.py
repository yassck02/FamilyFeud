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

#=====================================================================

def handle(socket, address):
	"""Handles an incomming socket connection"""

	# Recieve and handle the clients response
	response = socket.recv(1024).decode("ascii")

	if response.command.playGame:
		playGame(socket, address)

	elif response.command.getHistory:
		getHistory(socket)

	elif response.command.getRecord:
		getRecord(socket)

	# End the connection
	print("Disconnected from " + str(address))
	socket.close()

#=====================================================================

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

#=====================================================================

def getRandomQuestion():
	"""Opens the questions.json file ad Returns a random question from it"""

	question = {}

	# open the questions file
	with open(questionFilePath) as file:

		# load the json
		questions = json.load(file)

		# choose a random index
		index = randint(1, len(questions))
		question = questions[index]

	return question

#=====================================================================

# def readUsersFile():

#---------------------------------------------------------------------

# def registerUser():

#---------------------------------------------------------------------

def getUserRecord(username):
	"""Opens the users.json file and calclates the record of an individual user"""

	# open the useres file
	with open(usersFilePath) as file:

		# load the json
		users = json.load(file)

		bestRecord = { 'date': '', 'score': 0 }

		# search for the user in question
		for user in users:
			if(user['username'] == username):

				# make sure the user has played alteast 1 game
				if(len(user['history']) <= 0):
					print("User has no play history")

				# loop through all their records
				for record in user['history']:
					if (record['score'] > bestRecord['score']):
						bestRecord = record

				return (user, bestRecord)
	
		# if the user doesent exist
		print("Username does not exist")

#---------------------------------------------------------------------

# def addToUserHistory():

#---------------------------------------------------------------------

def getPopulationRecord(): 
	"""Opens the users.json file and calclates the record of all users"""

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

	return (user, bestRecord)

#=====================================================================

def parse(message):
	"""Extracts the command, and arguments from a message string"""
	
	tokens = message.split("\r\n")

	command = tokens[0]
	arguments = {}

	for token in tokens: 
		argument = token.split(" ")
		key = argument[0]
		value = argument[1]
		arguments.update({key: value})

	return (command, arguments)

#=====================================================================

def main():

	r = getPopulationRecord()
	print(r)

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
		_socket.send("connected".encode())
		print("Connected to " + str(address))
		start_new_thread(handle, (connection, address))

#=====================================================================

main()

#=====================================================================
