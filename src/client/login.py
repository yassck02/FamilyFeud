import urwid

import networkManager as nm
import windowManager as wm

from page import Page

# ---------------------------------------------------------------------

class LoginPage(Page):

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def __init__(self):

        self.server_addr_textbox = urwid.Edit(caption='Server IP: ')
        self.server_addr_textbox.set_edit_text('127.0.0.1')
        
        self.username_textbox = urwid.Edit(caption='Username: ')
        self.username_textbox.set_edit_text('connor')

        self.password_textbox = urwid.Edit(caption='Password: ')
        self.password_textbox.set_edit_text('connor')

        self.btn_login = urwid.Button(('yellow', u'Login'), on_press=self.on_btn_press)
        self.btn_login._label.align = 'center'

        self.btn_register = urwid.Button(('yellow', u'Register'), on_press=self.on_btn_press)
        self.btn_register._label.align = 'center'

        self.message_login = urwid.Text("")
        self.message_login.align = 'center'

        widget = urwid.Filler(
            urwid.Pile([
                (2, urwid.Filler( urwid.Padding(self.server_addr_textbox, width=30, align='center') )),
                (2, urwid.Filler( urwid.Padding(self.username_textbox,    width=30, align='center') )),
                (2, urwid.Filler( urwid.Padding(self.password_textbox,    width=30, align='center') )),
                (2, urwid.Filler( urwid.Padding(self.btn_login,           width=20, align='center') )),
                (2, urwid.Filler( urwid.Padding(self.btn_register,        width=20, align='center') )),
                (2, urwid.Filler( urwid.Padding(self.message_login,       width=50, align='center') )),
            ])
        )

        header_text = "Login"

        Page.__init__(self, widget, header_text)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def on_btn_press(self, button):

        # Get the user inputs form the text field
        ip_address  = self.server_addr_textbox.get_edit_text()
        username    = self.username_textbox.get_edit_text()
        password    = self.password_textbox.get_edit_text()

        # Make sure the address is not empty
        if (ip_address == ""):
            self.message_login.set_text([('red', u"ERROR: "), u"Server address field cannot be empty"])
            return

        # Make sure the username is not empty
        if (username == ""):
            self.message_login.set_text([('red', u"ERROR: "), u"Username field cannot be empty"])
            return

        # Make sure the username is not empty
        if (password == ""):
            self.message_login.set_text([('red', u"ERROR: "), u"Password field cannot be empty"])
            return

        # Attempt to connect to the server via the network manager
        if (nm.connect(ip_address) == False):

            self.message_login.set_text([('red', u"ERROR: "), u"Could not connect to server"])

        else:
        
            # create the request command based on which button was pressed
            command = ""
            if button._label.text == "Register":
                command = 'register'
            else:
                command = 'login'

            # Send the request to the server
            request = { 'command': command, 'username': username, 'password': password }
            nm.send(request)

            # recieve and act on the response
            response = nm.recieve()
            if (response['code'] == 200):
                self.message_login.set_text([('green', command), u": success!"])
                nm.loggedin = True
                wm.show(wm.selectionPage)
            else:
                self.message_login.set_text([('red', u"ERROR: "), response['description']])
                nm.disconnect()

        # Clear the text fields
        self.server_addr_textbox.set_edit_text("")
        self.username_textbox.set_edit_text("")
        self.password_textbox.set_edit_text("")

# ---------------------------------------------------------------------
