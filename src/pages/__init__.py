import urwid

import credits
import splash
import gameplay
import history
import records
import selection

# ---------------------------------------------------------------------

# Color sceme
palette = [
    ('titlebar', 'black', 'yellow'),
    ('ESC', 'white', 'black'),
    ('button_1', 'white', 'dark blue'),
    ('button_2', 'white', 'dark red')
]

# Header (Top bar)
header = urwid.AttrMap(
    urwid.Text(u'Family Feud'), 
    'titlebar'
)

# Footer (bottom bar)
footer = urwid.Text(
    [u'Press (', ('ESC', u'esc'), u') to quit. ']
)

# Body (main content)
box = urwid.LineBox(splash.widget)

# Main window
base = urwid.Frame(body=box, header=header, footer=footer)

# ---------------------------------------------------------------------

def handle_input(key):
    if key == 'esc':
        raise urwid.ExitMainLoop()

def showPage(page):
    loop.widget.body = selection.widget

# ---------------------------------------------------------------------

loop = urwid.MainLoop(base, palette=palette, unhandled_input=handle_input)

loop.run()

# ---------------------------------------------------------------------

