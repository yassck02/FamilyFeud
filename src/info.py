import urwid
import json

from Page import *

# ---------------------------------------------------------------------

class InfoPage(Page):

    def __init__(self):
        """Credits and resources are read from the credits file"""

        credits_text_filepath = '/Users/Connor/Documents/School/College/Semester 8/Networking/FamilyFeud/res/credits.json'
        resources_text_filepath = '/Users/Connor/Documents/School/College/Semester 8/Networking/FamilyFeud/res/resources.json'

        self.header = urwid.AttrMap(
            urwid.Text(u'Info'), 
            'titlebar'
        )

        self.footer = urwid.Text(
            [(u'Press ('), ('ESC', u'esc'), (u') to quit. '),
            (u'Press ('), ('BACK', u'backspace'), (u') to go back. ')]
        )

        with open(credits_text_filepath) as credits_text_file:
            self.credits = json.load(credits_text_file)

        with open(resources_text_filepath) as resources_text_file:
            self.resources = json.load(resources_text_file)

        self.widget = urwid.Filler(
            urwid.Columns([
                urwid.Pile([urwid.Text([contributor['name'], ": ", contributor['email']], align='center') for contributor in self.credits['contributors']]),
                urwid.Pile([urwid.Text([resource['description'], ": ", resource['link']], align='center') for resource in self.resources['resources']])
            ])
        )

# ---------------------------------------------------------------------
