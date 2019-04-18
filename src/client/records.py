import urwid

import networkManager as nm
import windowManager as wm

from page import Page

# ---------------------------------------------------------------------

class RecordsPage(Page):

    def __init__(self):

        widget = urwid.Filler(
            urwid.Text("records_page", align='center')
        )

        header_text = "Records"

        footer = urwid.Text(
            [(u'Press ('), ('ESC', u'esc'), (u') to quit. ')]
        )

        Page.__init__(self, widget, header_text, footer)


    def getRecord(socket):
        """ gets the record of an individual user, or the whole population """

        username = raw_input("Which user would you lke to get the record for? ")
        
        request = { 'command': 'getRecord', 'username': username }
        send(socket, request)

        # recieve the response
        response = recieve(socket)

        # act on the response
        if (response['code'] == 200):
            print(response['record'])
        else:
            print("ERROR: ", response['description'])

# ---------------------------------------------------------------------
