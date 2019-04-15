import urwid
import time

# ---------------------------------------------------------------------

copyright_text = 'TCL Technologies 2019'
splash_text_filepath = '/Users/Connor/Documents/School/College/Semester 8/Networking/FamilyFeud/res/splash.txt'

# ---------------------------------------------------------------------

splash_text = ''

with open(splash_text_filepath) as splash_text_file:
    splash_text = urwid.Text(splash_text_file.read(), align='center')



widget = urwid.Filler(splash_text, valign='middle', top=1, bottom=1)

# ---------------------------------------------------------------------
