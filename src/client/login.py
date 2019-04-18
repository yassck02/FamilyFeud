import urwid

import networkManager as nm
import windowManager as wm

from page import Page

# ---------------------------------------------------------------------

class LoginPage(Page):

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def __init__(self):

        self.server_addr_textbox = urwid.Edit(caption='Server IP: ')
        self.username_textbox = urwid.Edit(caption='Username: ')
        self.password_textbox = urwid.Edit(caption='Password: ')

        self.btn_login = urwid.Button(('yellow', u'Login'), on_press=self.on_btn_press)
        self.btn_login._label.align = 'center'

        self.btn_register = urwid.Button(('yellow', u'Register'), on_press=self.on_btn_press)
        self.btn_register._label.align = 'center'

        self.error_label = urwid.Text("")

        widget = urwid.Filler(
            urwid.Pile([
                (3, urwid.Filler( urwid.Padding(self.server_addr_textbox, width=30, align='center') )),
                (2, urwid.Filler( urwid.Padding(self.username_textbox,    width=30, align='center') )),
                (2, urwid.Filler( urwid.Padding(self.password_textbox,    width=30, align='center') )),
                (2, urwid.Filler( urwid.Padding(self.btn_login,           width=20, align='center') )),
                (1, urwid.Filler( urwid.Padding(self.btn_register,        width=20, align='center') )),
                (2, urwid.Filler( urwid.Padding(self.error_label,         width=20, align='center') )),
            ])
        )

        header_text = "Login"

        footer =  [(u'Presasdasds ('), ('yellow', u'esc'), (u') to quit. ')]

        Page.__init__(self, widget, header_text, footer)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def on_btn_press(self, button):

        # Get the user inputs form the text field
        ip_address  = self.server_addr_textbox.get_edit_text()
        username    = self.username_textbox.get_edit_text()
        password    = self.password_textbox.get_edit_text()

        # Make sure the address is not empty
        if (ip_address == ""):
            self.error_label.set_text('red', u"ERROR: Server addres field is empty")
            return

        # Attempt to connect to the server via the network manager
        if (nm.connect(ip_address) == False):
            self.error_label.set_text('red', u"ERROR: Could not connect to server")
            return

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
            self.error_label.set_text([command, " success!"])
            return True
        else:
            self.error_label.set_text("ERROR: ", response['description'])
            return False

        # Clear the text fields
        self.server_addr_textbox.set_edit_text("")
        self.username_textbox.set_edit_text("")
        self.password_textbox.set_edit_text("")

# ---------------------------------------------------------------------
