import urwid

from Page import *

# ---------------------------------------------------------------------

class LoginPage(Page):

    def __init__(self):

        self.widget = urwid.Filler(
            urwid.Text("login_page", align='center')
        )

        self.header = urwid.Text(
            ('titlebar', u'Login'), 
        )

        self.footer = urwid.Text(
            [(u'Press ('), ('ESC', u'esc'), (u') to quit. ')]
        )

# ---------------------------------------------------------------------
