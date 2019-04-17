import urwid

from Page import *

# ---------------------------------------------------------------------

class SelectionPage(Page):

    def __init__(self):

        self.widget = urwid.Filler(
            body = urwid.Pile([
                    (2, urwid.Button(label=('button_1', u'PLAY'), on_press=self.on_press_play)),
                    (1, urwid.Button(label=('button_2', u'Get History'), on_press=self.on_press_history)),
                    (1, urwid.Button(label=('button_2', u'Get Record'), on_press=self.on_press_record))
                ]
            ),
            top=1,
            bottom=1
        )

        self.header = urwid.AttrMap(
            urwid.Text(u'Main Menu'), 
            'titlebar'
        )

        self.footer = urwid.Text(
            [(u'Press ('), ('ESC', u'esc'), (u') to quit. ')]
        )

    def on_press_play(button):
        pass

    def on_press_history(button):
        pass

    def on_press_record(button):
        pass

# ---------------------------------------------------------------------
