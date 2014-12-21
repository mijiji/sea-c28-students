"""
A program to render HTML in a pretty fashion.

HTML Renderer

A program to print HTML properly with indenting.
Can be used for presentation.
"""


class Element(object):
    tag = "html"
    indent = "  "

    def __init__(self, text=None, **kwargs):
        if not text:
            self.new = []
        else:
            self.new = [text]
        self.attributes = kwargs

    def append(self, element):
        self.additions.append(element)

    def render(self, file_out, ind=""):

        file_out.write("\n")
        file_out.write(ind)
        file_out.write("<%s>"%self.tag
        for content in self.info:
            content.render(file_out, ind + self.indent)


class Html

class Head(Element):
    tag "head"

class Body(Element):
    tag "body"

class P(Element):
    tag "p"

class OneLineTag(Element):
    def render(self, file_out, ind=""):
        file_out.write("\n")
        file_out.write(ind)
        file_out.write("</%s>"%self.tag)
