
class Page:
    """The base class for every other page"""

    def __init__(self, widget, header_text): 
        self.header_text = header_text
        self.widget = widget

    def willShow():
        """Called before the page gets displayed to the user"""

    def didShow():
        """Called before the page is remoded or replaced by another"""
