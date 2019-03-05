#  Server program for the Family Feud game
#  Authors: 	Logan Docherty, Todd Noreen, Connor Yass
#  Created on: 	2/26/2019

from socket import *		# for use of socket
from random import randint  # for use of random integer
from thread import *		# for use of thread
import math					# for use of log

#=====================================================================

def handle(socket, address):
	"""Handles an incomming socket connection"""

	# Recieve and handle the clients response
	response = socket.recv(1024).decode("ascii")

	if args.playGame:
		playGame(socket, address)
	elif args.getHistory:
		getHistory(socket)
	elif args.getRecord:
		getRecord(socket)

	# End the connection
	print("Disconnected from " + str(address))
	socket.close()

#=====================================================================

def getRecord(socket):
	"""Retrieves a record from the suers file"""

	# Ask the user what they want to do
	socket.send("which ip address would you like to see the record for?".encode())

	# Obtain the response message from the client
	ip = socket.recv(1024).decode("ascii")

	# open the records file
	file = open("records.txt", "r+")

	# search for records file for the largest score for the ip address
	record = -1.0
	for line in file:
		if str(ip) in line:
			tokens = line.split("\t")
			if float(tokens[1]) > record:
				record = float(tokens[1])

	file.close()

	# Send the records that were found
	if record > 0:
		socket.send(str(record).encode())
	else:
		socket.send(("no record exists for " + str(ip)).encode())

#---------------------------------------------------------------------

def getHistory(socket):
	"""Gets a play history (for an individual or the population) from the users file"""

	# Ask the user what they want to do
	socket.send("which ip address would you like to see the history of?".encode())

	# Obtain the response message from the client
	ip = socket.recv(1024).decode("ascii")

	# open the records file
	file = open("records.txt", "r+")

	# search for records file for the ip
	response = "\n"
	for line in file:
		if str(ip) in line:
			tokens = line.split("\t")
			response += tokens[1]

	file.close()

	# Send the records that were found
	socket.send(response.encode())

#---------------------------------------------------------------------

def playGame(socket, address):
	"""Begins the 2 minute Family Feude gameplay loop"""

	# Generate a random number between 1 and 99 using the randint function
	num = randint(1, 99)
	guessCount = 0

	# Send a request to the client to ask for a guess of number between 1 and 99.
	socket.send("guess a number between 1 and 99".encode())	

	# Create a loop to process guesses from the client (allow infinite number of attempts)
	loop = True
	while loop:

		# Obtain the guess sent by the client through the socket
		response = socket.recv(1024).decode("ascii")
		guess = int(response)

		# Compare the guess with the random number generated. Send corresponding reminder
		# "higher", "lower", or "correct" to the client. For correct case, exit the loop
		guessCount += 1
		if guess > num:
			socket.send("lower".encode())
		elif guess < num:
			socket.send("higher".encode())
		else:
			socket.send("correct".encode())
			loop = False

			# store the score
			file = open("records.txt", "a+")
			score = math.log(num, 2) / guessCount
			file.write(str(address) + "\t" + str(score) + "\n")
			file.close()

#=====================================================================

# def getRandomQuestion():

# def readQuestionsFile():

#=====================================================================

# def readUsersFile():

# def registerUser():

# def getUserRecord():

# def addToUserHistory():

# def getPopulationRecord():

#=====================================================================

def parse(message):
	"""Extracts the command, and arguements from a message string"""
	
	tokens = message.split("\r\n")

	command = tokens[0]
	arguments = {}

	for token in tokens: 
		argument = token.split(" ")
		key = arguement[0]
		value = arguement[1]
		arguments.update({key: value})

	return (command, arguments)


#=====================================================================

def main():

	parse("getRecord\r\nindividual\t127.0.0.1")

	# Create a server socket
	_socket = socket(AF_INET, SOCK_STREAM)

	# Define  a server port number, bind it to the server socket, and listen
	port = 20123
	_socket.bind(("", port))
	_socket.listen(1)
	print ("Listening on port " + str(port))

	# Create an infinite loop to process all connection requests
	while True:

		# Create a connection socket for each connection request received
		connection, address = _socket.accept()
		print("Connected to " + str(address))
		start_new_thread(handle, (connection, address))

#=====================================================================

main()

#=====================================================================
