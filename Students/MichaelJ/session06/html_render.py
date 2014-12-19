"""
A program to render HTML in a pretty fashion.

HTML Renderer

A program to print HTML properly with indenting.
Can be used for presentation.
"""


class Element(object):
    def __init__(self, text=None, **kwargs):
        if not text:
            self.new = []
        else:
            self.new = [text]
        self.attributes = kwargs

    def render(self):
        opening_tag = "<>"
        closing_tag = "</>"

    def render(self):
        all_out = [self.opening_tag] + self + [self.closing_tag]
        print "\n".join(all_out)

    def append(self, Element):

