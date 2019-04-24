import urwid
import networkManager as nm

from page import Page

# ---------------------------------------------------------------------

class GameplayPage(Page):

    def __init__(self):

        self.btn_submit = urwid.Button(('yellow', u"Submit"), on_press=self.on_press_submit)
        self.btn_submit._label.align = 'center'

        self.question_label = urwid.Text("", align='center')

        self.timer_label = urwid.Text("remaining time: #", align='left')
        self.score_label = urwid.Text("score: #", align='right')

        self.guess1_textbox = urwid.Edit(caption='Guess 1: ')
        self.guess2_textbox = urwid.Edit(caption='Guess 2: ')
        self.guess3_textbox = urwid.Edit(caption='Guess 3: ')

        widget = urwid.Filler(
            urwid.Padding( 
                urwid.Pile([

                    urwid.Columns([
                        self.timer_label,
                        self.score_label
                    ]),

                    urwid.Divider(div_char='-', top=1, bottom=1),

                    urwid.Text(('yellow_black', u"Question: "), align='center'),
                    self.question_label,

                    urwid.Divider(div_char='-', top=1, bottom=1),

                    self.guess1_textbox,
                    self.guess2_textbox,
                    self.guess3_textbox,

                    urwid.Divider(div_char='-', top=1, bottom=1),

                    urwid.Padding(self.btn_submit, width=30, align='center')
                ]),
            width=50, align='center')
        )

        header_text = "Gameplay"

        Page.__init__(self, widget, header_text)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def willShow(self):
        """called right before this page is displayed"""

        self.question_label.set_text("")

        self.guess1_textbox.set_edit_text("")
        self.guess2_textbox.set_edit_text("")
        self.guess3_textbox.set_edit_text("")

        self.timerFinished = False
        self.localScore = 0

    def didShow(self):
        """called right after this page is displayed"""

        self.startGame()

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    localScore = 0
    timerFinished = False

    def startGame(self):
        """Starts the gameplay loop by asking the server for a question
            and starting the countdown timer"""

        # tell the server we want to play a game
        request = { 'command': 'playGame' }
        nm.send(request)

        # recieve the first question from the server
        question = nm.recieve()
        self.question_label.set_text(question['prompt'])

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def on_press_submit(self, button):
        """Called when the user presses the 'submit' button"""

        # retrieve the guesses from the text boxes
        guess1 = self.guess1_textbox.edit_text
        guess2 = self.guess2_textbox.edit_text
        guess3 = self.guess3_textbox.edit_text
        
        # send the guesses to the server
        request = { 'guess1': guess1, 
                    'guess2': guess2, 
                    'guess3': guess3 }
        nm.send(request)

        # recieve the score from the server
        response = nm.recieve()
        self.localScore += response['score']
        self.score_label.set_text(str(self.localScore))

        # recieve the next question from the server
        question = nm.recieve()
        self.question_label.set_text(question['prompt'])

        # clear the responses
        self.guess1_textbox.set_edit_text("")
        self.guess2_textbox.set_edit_text("")
        self.guess3_textbox.set_edit_text("")

    # - - - -  - - - -  - - - -  - - - -  - - - -  - - - -  - - - -  -

    def onTimerFinish():
        self.timerFinished = True

# ---------------------------------------------------------------------
