import urwid

import networkManager as nm
import windowManager as wm

from page import Page

# ---------------------------------------------------------------------

class RegisterPage(Page):

    def __init__(self):

        widget = urwid.Filler(
            urwid.Text("register_page", align='center')
        )

        header_text = "Register"

        footer = urwid.Text(
            [(u'Press ('), ('ESC', u'esc'), (u') to quit. ')]
        )

        Page.__init__(self, widget, header_text, footer)


    def register(socket):
        """ Sends the register mesage to the server """

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
