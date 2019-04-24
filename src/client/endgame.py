import urwid

import windowManager as wm

from page import Page

import json

# ---------------------------------------------------------------------

class EndgamePage(Page):

    def __init__(self):
        """Page that dislays after a game has finished"""

        self.btn_restart = urwid.Button(('yellow', u"Restart"), on_press=self.on_press_restart)
        self.btn_restart._label.align = 'center'

        self.btn_menu = urwid.Button(('yellow', u"Main Menu"), on_press=self.on_press_menu)
        self.btn_menu._label.align = 'center'

        self.score_label = urwid.Text("score: #", align='center')

        header_text = "Game Over"

        widget = urwid.Filler(
            urwid.Pile([

                urwid.Padding(self.score_label,  width=30, align='center'),

                urwid.Divider(div_char=' ', top=1, bottom=1),

                urwid.Padding(self.btn_restart, width=30, align='center'),

                urwid.Divider(div_char=' ', top=1, bottom=1),

                urwid.Padding(self.btn_menu, width=30, align='center')

            ])
        )

        Page.__init__(self, widget, header_text)

    # - - - -  - - - -  - - - -  - - - -  - - - -  - - - -  - - - -  -

    def willShow(self):
        pass

    def didShow(self):
        pass

    # - - - -  - - - -  - - - -  - - - -  - - - -  - - - -  - - - -  -

    def on_press_menu(self, button):
        wm.show(wm.selectionPage)

    def on_press_restart(self, button):
        wm.show(wm.instructionsPage)
        

# ---------------------------------------------------------------------
