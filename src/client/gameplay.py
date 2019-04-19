import urwid
import networkManager

from page import Page

# ---------------------------------------------------------------------

class GameplayPage(Page):

    def __init__(self):

        widget = urwid.Filler(
            urwid.Text("gameplay_page", align='center')
        )

        header_text = "Gameplay"

        footer = urwid.Text(
            [(u'Press ('), ('ESC', u'esc'), (u') to quit. ')]
        )

        Page.__init__(self, widget, header_text)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def playGame(socket):
        """ The main game function """

        # Tell the server we want to start a game
        request = { 'command': 'playGame' }
        send(socket, request)

        for i in range(3):

            #recieve a question
            question = recieve(socket)
            print(question)

            # send the guess to the server
            guess = raw_input("Input your guess: ")
            request = { 'guess': guess }
            send(socket, request)

        # Recieve the total score
        totalScore = recieve(socket)
        print(totalScore)

# ---------------------------------------------------------------------
