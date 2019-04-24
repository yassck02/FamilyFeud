import urwid

from page import Page
import windowManager as wm

import json
import os

# ---------------------------------------------------------------------

class InstructionsPage(Page):

    def __init__(self):
        """Credits and resources are read from the credits file"""

        dirname = os.path.dirname(__file__)
        instructions_text_filepath   = os.path.join(dirname, '../../res/instructions.txt')

        self.btn_start = urwid.Button(('yellow_blink', u"Start!"), on_press=self.on_press_start)
        self.btn_start._label.align = 'center'

        header_text = "Instructions"

        with open(instructions_text_filepath) as instructions_text_file:
            instructions = instructions_text_file.read()

        widget = urwid.Filler(
            urwid.Pile([

                urwid.Padding(
                    urwid.Text(instructions, align='left'),
                    width=65, align='center'
                ),

                urwid.Divider(div_char=' ', top=1, bottom=1),

                urwid.Padding(self.btn_start, width=30, align='center')

            ])
        )

        Page.__init__(self, widget, header_text)

    # - - - -  - - - -  - - - -  - - - -  - - - -  - - - -  - - - -  -

    def on_press_start(self, button):
        wm.show(wm.gameplayPage)

    # - - - -  - - - -  - - - -  - - - -  - - - -  - - - -  - - - -  -

    def willShow(self):
        pass

    def didShow(self):
        pass

# ---------------------------------------------------------------------
