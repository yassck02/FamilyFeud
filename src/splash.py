import urwid

from Page import *

# ---------------------------------------------------------------------

class SplashPage(Page):

    def __init__(self):

        splash_text_filepath = '/Users/Connor/Documents/School/College/Semester 8/Networking/FamilyFeud/res/splash.txt'

        splash_text = ''
        with open(splash_text_filepath) as splash_text_file:
            splash_text = urwid.Text(splash_text_file.read(), align='center')

        self.widget = urwid.Filler(
            urwid.Pile([
                (1, urwid.Filler(urwid.Text("Welcome to:", align='center'), valign='middle')),
                (8, urwid.Filler(splash_text, valign='middle')),
                (4, urwid.Filler(urwid.Text(('command', u"> Press any key to continue <"), align='center'), valign='middle', top=3))
            ])
        )

        self.header = urwid.AttrMap(
            urwid.Text(u'Family Feud'), 
            'titlebar'
        )

        self.footer = urwid.Text(
            [(u'Press ('), ('ESC', u'esc'), (u') to quit. ')]
        )

# ---------------------------------------------------------------------
