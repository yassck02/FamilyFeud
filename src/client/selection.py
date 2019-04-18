import urwid

import networkManager as nm
import windowManager as wm

from page import Page

# ---------------------------------------------------------------------

class SelectionPage(Page):

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def __init__(self):

        btn_play = urwid.Button(("yellow", "Play"), on_press=self.on_press_play)
        btn_play._label.align = 'center'

        btn_history = urwid.Button(("yellow", "Check History"), on_press=self.on_press_history)
        btn_history._label.align = 'center'

        btn_record = urwid.Button(("yellow", "Check Record"), on_press=self.on_press_record)
        btn_record._label.align = 'center'

        btn_info = urwid.Button(("yellow", "Info"), on_press=self.on_press_info)
        btn_info._label.align = 'center'

        widget = urwid.Filler(
            urwid.Pile([
                (2, urwid.Filler( urwid.Padding(btn_play,    width=20, align='center') )),
                (2, urwid.Filler( urwid.Padding(btn_history, width=20, align='center') )),
                (2, urwid.Filler( urwid.Padding(btn_record,  width=20, align='center') )),
                (2, urwid.Filler( urwid.Padding(btn_info,    width=20, align='center') ))
            ])
        )

        header_text = "Main Menu"

        footer = urwid.Text(
            [(u'Press ('), ('ESC', u'esc'), (u') to quit. ')]
        )

        Page.__init__(self, widget, header_text, footer)

    # - - - -  - - - -  - - - -  - - - -  - - - -  - - - -  - - - -  -

    def on_press_play(self, button):
        wm.show(wm.gameplayPage)

    def on_press_history(self, button):
        wm.show(wm.historyPage)

    def on_press_record(self, button):
        wm.show(wm.recordsPage)

    def on_press_info(self, button):
        wm.show(wm.infoPage)

# ---------------------------------------------------------------------
