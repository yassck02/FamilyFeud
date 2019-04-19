import urwid

import networkManager as nm
import windowManager as wm

from page import Page

# ---------------------------------------------------------------------

class HistoryPage(Page):

    def __init__(self):

        widget = urwid.Filler(
            urwid.Text("history_page", align='center')
        )

        header_text = "History"

        Page.__init__(self, widget, header_text)


    def getHistory(socket):
        """ gets the history of an individual user """

        username = raw_input("Which user would you lke to get the history for? ")
        
        request = { 'command': 'getHistory', 'username': username }
        send(socket, request)

        # recieve the response
        response = recieve(socket)

        # act on the response
        if (response['code'] == 200):
            print(response['history'])
        else:
            print("ERROR: ", response['description'])

# ---------------------------------------------------------------------
