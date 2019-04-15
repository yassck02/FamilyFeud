import urwid

# Color sceme
palette = [
    ('titlebar', 'black', 'yellow'),
    ('ESC', 'red', 'black'),
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

# Body (main frame)
base = urwid.Frame(body=body, header=header, footer = footer)
