
class Page:
    """The base class for every other page"""

    def __init__(self, widget, header_text): 
        self.header_text = header_text
        self.widget = widget