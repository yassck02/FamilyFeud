import urwid

import networkManager as nm

from gameplay  import GameplayPage
from history   import HistoryPage
from info      import InfoPage
from login     import LoginPage
from records   import RecordsPage
from selection import SelectionPage
from splash    import SplashPage

# ---------------------------------------------------------------------

# Color sceme
palette = [
    ( None, 'white', ''),
    ('black_on_yellow', 'black', 'yellow'),
    ('blue', 'dark blue', ''),
    ('green', 'dark green', ''),
    ('red', 'dark red', ''),
    ('pink', 'dark magenta', ''),
    ('yellow', 'yellow', ''),
    ('yellow_blink', 'yellow,blink', ''),
    ('blink', 'blink', ''),
    ('bold', 'bold', ''),
    ('underline', 'underline', ''),
    ('italics', 'italics', ''),
]

# Header (Top bar)
header = urwid.AttrMap(
    urwid.Text(u'Family Feud'), 'black_on_yellow'
)

# Footer (bottom bar)
footer = urwid.Text([
    (u'Quit: ('), ('red', u'esc'), (u'), '),
    (u'Navigate: ('), ('blue', u'up, down'), (u'), '),
    (u'Select: ('), ('green', u'enter'), (u'), '),
    (u'Back: ('), ('pink', u'delete'), (u')')
])

# ---------------------------------------------------------------------

# Create the base widget (The main window)
content =  urwid.SolidFill(fill_char='*')
base = urwid.Frame(content, header=header, footer=footer)

# Create an instance of each page
gameplayPage  = GameplayPage()
historyPage   = HistoryPage()
infoPage      = InfoPage()
loginPage     = LoginPage()
recordsPage   = RecordsPage()
selectionPage = SelectionPage()
splashPage    = SplashPage()

# ---------------------------------------------------------------------

def show(page):
    """Displays the given page by assigning the main windows body to its widget"""

    header.original_widget.set_text( page.header_text)
    base.body = urwid.LineBox( page.widget )

# ---------------------------------------------------------------------

def dialog(self):
    ''' Overlays a dialog box on top of the console UI '''

    # Header
    header_text = urwid.Text(('banner', 'Help'), align = 'center')
    header = urwid.AttrMap(header_text, 'banner')

    # Body
    body_text = urwid.Text('Hello world', align = 'center')
    body_filler = urwid.Filler(body_text, valign = 'top')
    body_padding = urwid.Padding(
        body_filler,
        left = 1,
        right = 1
    )
    body = urwid.LineBox(body_padding)

    # Footer
    footer = urwid.Button('Okay', self.do)
    footer = urwid.AttrWrap(footer, 'selectable', 'focus')
    footer = urwid.GridFlow([footer], 8, 1, 1, 'center')

    # Layout
    layout = urwid.Frame(
        body,
        header = header,
        footer = footer,
        focus_part = 'footer'
    )

    return layout

# ---------------------------------------------------------------------

def unhandled_input(key):
    """Handles all input that hasent already been handled"""
    
    if key == 'esc':
        # nm.disconnect()
        raise urwid.ExitMainLoop()
    elif key == 'backspace':
        show(selectionPage)

# ---------------------------------------------------------------------


