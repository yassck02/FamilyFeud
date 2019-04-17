#  Client program for the Family Feud game
#  Authors: 	Logan Docherty, Todd Noreen, Connor Yass
#  Created on: 	2/26/2019

from windowManager import WindowManager

from gameplay  import GameplayPage
from history   import HistoryPage
from info      import InfoPage
from login     import LoginPage
from records   import RecordsPage
from register  import RegisterPage
from selection import SelectionPage
from splash    import SplashPage

# ---------------------------------------------------------------------

# Create an instance of each page
gameplayPage  = GameplayPage()
historyPage   = HistoryPage()
infoPage      = InfoPage()
loginPage     = LoginPage()
recordsPage   = RecordsPage()
registerPage  = RegisterPage()
selectionPage = SelectionPage()
splashPage    = SplashPage()

# Create the window manager
windowManager = WindowManager()
windowManager.push(infoPage)
windowManager.show()

# ---------------------------------------------------------------------
