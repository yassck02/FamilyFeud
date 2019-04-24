import urwid

from page import Page

import json

# ---------------------------------------------------------------------

class EndPage(Page):

    def __init__(self):
        """Page that dislays after a game has finished"""

        header_text = ""

        widget = urwid.Filler(
            urwid.Pile([

                urwid.Divider(div_char=' ', top=1, bottom=1),
                
            ])
        )

        Page.__init__(self, widget, header_text)

    # - - - -  - - - -  - - - -  - - - -  - - - -  - - - -  - - - -  -

    def willShow(self):
        pass

# ---------------------------------------------------------------------
