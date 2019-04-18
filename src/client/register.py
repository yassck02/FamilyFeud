import urwid

import networkManager as nm
import windowManager as wm

from page import Page

# ---------------------------------------------------------------------

class RegisterPage(Page):

    def __init__(self):

        self.username_textbox  = urwid.Edit(caption='Username: ')
        self.password1_textbox = urwid.Edit(caption='Password: ')
        self.password2_textbox = urwid.Edit(caption='Password: ')

        self.enter_button = urwid.Button(('yellow', u'Register'), on_press=self.register)
        self.enter_button._label.align = 'center'

        self.error_label = urwid.Text("")

        widget = urwid.Filler(
            urwid.Pile([
                (2, urwid.Filler( urwid.Padding(self.username_textbox,  width=30, align='center') )),
                (2, urwid.Filler( urwid.Padding(self.password1_textbox, width=30, align='center') )),
                (2, urwid.Filler( urwid.Padding(self.password2_textbox, width=30, align='center') )),
                (2, urwid.Filler( urwid.Padding(self.enter_button,      width=20, align='center') )),
                (2, urwid.Filler( urwid.Padding(self.error_label,       width=20, align='center') )),
            ])
        )

        header_text = "Register"

        footer =  [(u'Presasdasds ('), ('yellow', u'esc'), (u') to quit. ')]

        Page.__init__(self, widget, header_text, footer)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def register(self, button):
        """ Sends the register mesage to the server """

        username  = self.username_textbox.get_edit_text()
        password1 = self.password1_textbox.get_edit_text()
        password2 = self.password2_textbox.get_edit_text()

        if (password1 != password2):
            self.error_label.set_text("ERROR: Passwords do not match")
            return

        request = { 'command': 'register', 'username': username, 'password': password1 }
        nm.send(socket, request)

        # recieve the response
        response = nm.recieve(socket)

        # act on the response
        if (response['code'] == 200):
            self.error_label.set_text("Register success!")
        else:
            self.error_label.set_text("ERROR: ", response['description'])

# ---------------------------------------------------------------------
