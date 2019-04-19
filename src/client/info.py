import urwid

from page import Page

import json

# ---------------------------------------------------------------------

class InfoPage(Page):

    def __init__(self):
        """Credits and resources are read from the credits file"""

        credits_text_filepath = '/Users/Connor/Documents/School/College/Semester 8/Networking/FamilyFeud/res/credits.json'
        resources_text_filepath = '/Users/Connor/Documents/School/College/Semester 8/Networking/FamilyFeud/res/resources.json'

        header_text = "Info"

        with open(credits_text_filepath) as credits_text_file:
            self.credits = json.load(credits_text_file)

        with open(resources_text_filepath) as resources_text_file:
            self.resources = json.load(resources_text_file)

        widget = urwid.Filler(
            urwid.Pile([

                urwid.Text(('yellow', u"Family Feud v0.9"), align='center'),

                urwid.Divider(div_char=' ', top=1, bottom=1),

                urwid.Text(('underline', u"Contributors"), align='center'),

                urwid.Columns([
                    urwid.Pile([urwid.Text([('bold',  contributor['name'] ), ":  "], align='right') for contributor in self.credits['contributors']]),
                    urwid.Pile([urwid.Text(('italics',contributor['email']),         align='left' ) for contributor in self.credits['contributors']]),
                ]),

                urwid.Divider(div_char=' ', top=1, bottom=1),

                urwid.Text(('underline', u"Resources"), align='center'),

                urwid.Columns([
                    urwid.Pile([urwid.Text([('bold',  resource['description'] ), ":  "], align='right') for resource in self.resources['resources']]),
                    urwid.Pile([urwid.Text(('italics',resource['link']),                 align='left' ) for resource in self.resources['resources']]),
                ])
            ])
        )

        Page.__init__(self, widget, header_text)

# ---------------------------------------------------------------------
