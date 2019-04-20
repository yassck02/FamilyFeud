import urwid

import networkManager as nm
import windowManager as wm

from page import Page

# ---------------------------------------------------------------------

class HistoryPage(Page):

    def __init__(self):

        self.username_textbox = urwid.Edit(caption='Username: ')

        self.btn_search = urwid.Button(('yellow', u'Search'), on_press=self.on_btn_press)
        self.btn_search._label.align = 'center'

        self.history_list  = urwid.Pile([])
        self.history_list.contents.append((urwid.Text("asdasdasdasd", align='center'), ('given', 1)))
        self.message_label = urwid.Text("", align='center')

        widget = urwid.Filler(
            urwid.Pile([
                (2, urwid.Filler( urwid.Padding(self.username_textbox, width=30, align='center') )),
                (2, urwid.Filler( urwid.Padding(self.btn_search,       width=30, align='center') )),
                (8, self.history_list),
                (2, urwid.Filler( urwid.Padding(self.message_label,    width=50, align='center') ))
            ])
        )

        header_text = "Check History"

        Page.__init__(self, widget, header_text)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def on_btn_press(self, button):

        # Get the user inputs form the text field
        username = self.username_textbox.get_edit_text()

        # Make sure the username is not empty
        if (username == ""):
            self.message_label.set_text([('red', u"ERROR: "), u"Username field cannot be empty"])
            return

        # Create end the request to the server
        request = { 'command': 'getHistory', 'username': username }
        nm.send(request)

        # recieve and act on the response
        response = nm.recieve()
        if (response['code'] == 200):

            self.history_list = []
            for record in response['history']:
                self.history_list.widget_list.append( urwid.Text(record['date'] + ": " + str(record['score'])) )
            
            self.message_label.set_text(str(len(response['history'])) + " games played")
        
        else:

            self.history_list = []
            self.message_label.set_text([('red', u"ERROR: "), response['description']])

# ---------------------------------------------------------------------
