import urwid

import networkManager as nm
import windowManager as wm

from page import Page

# ---------------------------------------------------------------------

class LoginPage(Page):

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def __init__(self):

        self.username_textbox = urwid.Edit(caption='Username: ')
        self.password_textbox = urwid.Edit(caption='Password: ')

        self.enter_button = urwid.Button(('yellow', u'Login'), on_press=self.login)
        self.enter_button._label.align = 'center'

        self.error_label = urwid.Text("")

        widget = urwid.Filler(
            urwid.Pile([
                (2, urwid.Filler( urwid.Padding(self.username_textbox, width=30, align='center') )),
                (2, urwid.Filler( urwid.Padding(self.password_textbox, width=30, align='center') )),
                (2, urwid.Filler( urwid.Padding(self.enter_button,     width=20, align='center') )),
                (2, urwid.Filler( urwid.Padding(self.error_label,      width=20, align='center') )),
            ])
        )

        header_text = "Login"

        # footer = urwid.Text(
        #     [(u'Navigate: ('), ('yellow', u'/\ \/'), (')'),
        #      (u'Select: ('), ('yellow', u'enter'), (')')]
        # )

        footer =  [(u'Presasdasds ('), ('yellow', u'esc'), (u') to quit. ')]

        Page.__init__(self, widget, header_text, footer)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def login(self):
        """ Sends the login message to the server and waits for a response """

        # input the username and password
        username = self.username_textbox.get_edit_text()
        password = self.password_textbox.get_edit_text()

        # Check for empty inputs
        # if(username == "" | password == ""):
        #     return

        # send it to the server
        request = { 'command': 'login', 'username': username, 'password': password }
        NM.send(request)

        # recieve the response
        response = NM.recieve()

        # act on the response
        if (response['code'] == 200):
            self.username_textbox.set_edit_text("")
            self.password_textbox.set_edit_text("")
        else:
            self.username_textbox.set_edit_text("")
            self.password_textbox.set_edit_text("")

# ---------------------------------------------------------------------
