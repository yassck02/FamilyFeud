#  Client program for the Family Feud game
#  Authors: 	Logan Docherty, Todd Noreen, Connor Yass
#  Created on: 	2/26/2019

import urwid

import networkManager as nm
import windowManager as wm

loop = urwid.MainLoop(wm.base, palette=wm.palette, unhandled_input=wm.unhandled_input)
wm.show(wm.splashPage)
loop.run()