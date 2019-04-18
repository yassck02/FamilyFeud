import urwid

import networkManager as nm

from gameplay  import GameplayPage
from history   import HistoryPage
from info      import InfoPage
from login     import LoginPage
from records   import RecordsPage
from register  import RegisterPage
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
    ('blink', 'blink', ''),
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
registerPage  = RegisterPage()
selectionPage = SelectionPage()
splashPage    = SplashPage()

# ---------------------------------------------------------------------

def show(page):
    """Displays the given page by assigning the main windows body to its widget"""

    header.original_widget.set_text( page.header_text)
    base.body = urwid.LineBox( page.widget )

# ---------------------------------------------------------------------

def popup(title, message):
    pass

# ---------------------------------------------------------------------

def unhandled_input(key):
    """Handles all input that hasent already been handled"""
    
    if key == 'esc':
        # nm.disconnect()
        raise urwid.ExitMainLoop()
    elif key == 'backspace':
        show(selectionPage)

# ---------------------------------------------------------------------


