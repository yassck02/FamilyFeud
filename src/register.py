import urwid

from Page import *

# ---------------------------------------------------------------------

class RegisterPage(Page):

    def __init__(self):

        self.widget = urwid.Filler(
            urwid.Text("register_page", align='center')
        )

        self.header = urwid.AttrMap(
            urwid.Text(u'Register'), 
            'titlebar'
        )

        self.footer = urwid.Text(
            [(u'Press ('), ('ESC', u'esc'), (u') to quit. ')]
        )

# ---------------------------------------------------------------------
