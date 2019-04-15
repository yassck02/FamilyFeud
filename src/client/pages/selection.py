def on_press_play():
    print('play was pressed')

def on_press_history():
    print('get history was pressed')

def on_press_record():
    print('get record was pressed')

page = urwid.LineBox(
    urwid.Filler(
        body=urwid.Pile(
            [urwid.Button(label='Play!', on_press='on_press_play'),
             urwid.Divider(div_char=' ')
             urwid.Button(label='Get History', on_press='on_press_history'),
             urwid.Button(label='Get Record', on_press='on_press_record')
            ]
        ),
        top=1,
        bottom=1
    )
)