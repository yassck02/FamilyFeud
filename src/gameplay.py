import urwid

from Page import *

# ---------------------------------------------------------------------

class GameplayPage(Page):

    def __init__(self):

        self.widget = urwid.Filler(
            urwid.Text("gameplay_page", align='center')
        )

        self.header = urwid.AttrMap(
            urwid.Text(u'Game Play'), 
            'titlebar'
        )

        self.footer = urwid.Text(
            [(u'Press ('), ('ESC', u'esc'), (u') to quit. ')]
        )

# ---------------------------------------------------------------------
