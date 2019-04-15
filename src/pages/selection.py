import urwid

# ---------------------------------------------------------------------

def on_press_play():
    print('play was pressed')

def on_press_history():
    print('get history was pressed')

def on_press_record():
    print('get record was pressed')

# ---------------------------------------------------------------------

widget = urwid.LineBox(
    original_widget = urwid.Filler(
        body = urwid.Pile(
            [urwid.Button(label=('button_1', u'PLAY'), on_press=on_press_play),
             urwid.Divider(div_char=' '),
             urwid.Button(label=('button_2', u'Get History'), on_press=on_press_history),
             urwid.Button(label=('button_2', u'Get Record'), on_press=on_press_record)
            ]
        ),
        top=1,
        bottom=1
    ), 
    title=''
)

# ---------------------------------------------------------------------
