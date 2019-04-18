
class Page:
    """The base class for every other page"""

    def __init__(self, widget, header_text, footer): 
        self.header_text = header_text
        self.footer = footer
        self.widget = widget