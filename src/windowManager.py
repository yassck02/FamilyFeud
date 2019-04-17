import urwid



# ---------------------------------------------------------------------

class WindowManager:

    def __init__(self):

        # Color sceme
        self.palette = [
            ('titlebar', 'black', 'yellow'),
            ('ESC', 'dark red', ''),
            ('BACK', 'dark magenta', ''),
            ('contributor', 'yellow', ''),
            ('button_1', 'white', 'dark blue'),
            ('button_2', 'white', 'dark red'),
            ('command', 'blink', '')
        ]

        # Header (Top bar)
        self.header = urwid.AttrMap(
            urwid.Text(u'Family Feud'), 
            'titlebar'
        )

        # Footer (bottom bar)
        self.footer = urwid.Text(
            [(u'Press ('), ('ESC', u'esc'), (u') to quit. ')]
        )

        # Create the base widget (The main window)
        self.base = urwid.Frame(body=urwid.Text('Family Feud'), header=self.header, footer=self.footer)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def push(self, page):
        """Displays the given page by assigning the main windows body to its widget"""

        self.base.footer = page.footer
        self.base.header = page.header
        self.base.body = page.widget

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def handle_input(self, key):
        if key == 'esc':
            raise urwid.ExitMainLoop()

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def show(self):
        """Displays the main window widget and starts the loop"""

        self.loop = urwid.MainLoop(self.base, palette=self.palette, unhandled_input=self.handle_input)
        self.loop.run()

# ---------------------------------------------------------------------
