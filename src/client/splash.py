import urwid

import networkManager as nm
import application as app

from page import Page
import os

# ---------------------------------------------------------------------

class SplashPage(Page):

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def __init__(self):

        dirname = os.path.dirname(__file__)
        splash_text_filepath   = os.path.join(dirname, '../../res/splash.txt')

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

        Page.__init__(self, widget, header_text)

    # - - - -  - - - -  - - - -  - - - -  - - - -  - - - -  - - - -  -

    def willShow(self):
        pass

    def didShow(self):
        pass

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    
    def on_press_enter(self, button):
        app.show(app.loginPage)

# ---------------------------------------------------------------------
