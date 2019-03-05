#  Client program for the Family Feud game
#  Authors: 	Logan Docherty, Todd Noreen, Connor Yass
#  Created on: 	2/26/2019

from socket import *	# For use of socket
import curses			# For Text based UI

#=====================================================================

def getRecord(socket):

	# Send the 'getRecord' request to the server
	socket.send("getRecord".encode())

	# Obtain the response message from the server
	response = socket.recv(1024).decode("ascii")
	if ("which ip address" not in response):
		socket.close()
		print("Server not ready to retrieve records :(")
		return
	else:
		print("> Server says: " + response)

	# Tell the server the IP address we want the records for
	ip = raw_input("Input the ip address (###.###.###.###)? ")
	socket.send(ip.encode())
	
	# Obtain the response message from the server
	response = socket.recv(1024).decode("ascii")
	print("> Server says: " + response)

#---------------------------------------------------------------------

def getHistory(socket):

	# Tell the 'getHistory' request to the server
	socket.send("getHistory".encode())

	# Obtain the response message from the server
	response = socket.recv(1024).decode("ascii")
	if ("which ip address" not in response):
		socket.close()
		print("Server not ready to retrieve history :(")
		return
	else:
		print("> Server says: " + response)

	# Tell the server the IP address we want the records for
	ip = raw_input("Input the ip address (###.###.###.###)? ")
	socket.send(ip.encode())
	
	# Obtain the response message from the server
	response = socket.recv(1024).decode("ascii")
	print("> Server says: " + response)

#---------------------------------------------------------------------

def playGame(socket):

	# Tell the 'playGame' request to the server
	socket.send("playGame".encode())

	# Obtain the response message from the server
	response = socket.recv(1024).decode("ascii")
	if ("guess a number" not in response):
		socket.close()
		print("Server is not ready to play the game :(")
		return
	else:
		print("> Server says: " + response)

	# Loop until the number os guessed correctly
	while True:

		# send the guess to the server
		myGuess = raw_input("Input your guess: ")
		socket.send(myGuess.encode())

		# Recieve its response
		response = socket.recv(1024).decode("ascii")
		print("> Server says: " + response)

		if("correct" in response):
			break

#=====================================================================

# def register():

#=====================================================================

def main():

	# Define  a server port number and server address
	ip = "localhost"
	port = 20123

	# Create a client TCP socket to connect with the server
	_socket = socket(AF_INET, SOCK_STREAM)
	_socket.connect((ip, port))

	# Obtain the response from the server
	response = _socket.recv(1024).decode("ascii")
	if ("what would you like" not in response):
		_socket.close()
		print("Server not ready to connect :(")
		return
	else:
		print("Connected to " + str(ip) + " on port " + str(port))
		print("> Server says: " + response)

	# Ask the user what they would like to do
	print("\t[0] Play Game")
	print("\t[1] Get Score History")
	print("\t[2] Get Player Record")
	tmp = raw_input("Input your selection: ")

	if "0" in tmp:
		playGame(_socket)
	elif "1" in tmp:
		getHistory(_socket)
	elif "2" in tmp:
		getRecord(_socket)
	else: 
		print("Unrecognized selection...")

	# Terminate the conection
	print("Closing conenction")
	_socket.close()

#=====================================================================

def parse(message):
	
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

screen = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

main()

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()

#=====================================================================
