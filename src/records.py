import urwid

from Page import *

# ---------------------------------------------------------------------

class RecordsPage(Page):

    def __init__(self):

        self.widget = urwid.Filler(
            urwid.Text("records_page", align='center')
        )

        self.header = urwid.AttrMap(
            urwid.Text(u'Records'), 
            'titlebar'
        )

        self.footer = urwid.Text(
            [(u'Press ('), ('ESC', u'esc'), (u') to quit. ')]
        )

# ---------------------------------------------------------------------
