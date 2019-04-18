import urwid

import networkManager as nm
import windowManager as wm

from page import Page

# ---------------------------------------------------------------------

class SplashPage(Page):

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def __init__(self):

        splash_text_filepath = '/Users/Connor/Documents/School/College/Semester 8/Networking/FamilyFeud/res/splash.txt'

        btn_enter = urwid.Button(('yellow_blink', u"Press enter to continue"), on_press=self.on_press_enter)
        btn_enter._label.align = 'center'

        splash_text = ''
        with open(splash_text_filepath) as splash_text_file:
            splash_text = urwid.Text(('yellow', splash_text_file.read()), align='center')

        widget = urwid.Filler(
            urwid.Pile([
                (1, urwid.Filler(urwid.Text("Welcome to:", align='center'), valign='middle')),
                (8, urwid.Filler(splash_text, valign='middle')),
                (4, urwid.Filler( urwid.Padding(btn_enter, width=30, align='center') , valign='middle'))
            ])
        )

        header_text = ""

        footer = urwid.Text(
            [(u'Press ('), ('ESC', u'esc'), (u') to quit. ')]
        )

        Page.__init__(self, widget, header_text, footer)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    
    def on_press_enter(self, button):
        wm.show(wm.selectionPage)

# ---------------------------------------------------------------------
