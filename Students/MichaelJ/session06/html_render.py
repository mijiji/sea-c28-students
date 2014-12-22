"""
A program to render HTML in a pretty fashion.

HTML Renderer

A program to print HTML properly with indenting.
Can be used for presentation.
"""


class Element(object):
    tag = "html"
    indent = "    "

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
        for key, value in self.attributes.items():
            file_out.write(' %s="%s" '%(key, value))


class Html(Element):
    tag = "head"


class Head(Element):
    tag = "head"


class Body(Element):
    tag ="body"


class P(Element):
    tag = "p"


class OneLineTag(Element):
    def render(self, file_out, ind=""):
        file_out.write("%s<%s> %s </%s>\n" % (ind, self.tag, self.content[0], self.tag_name)


class SelfClosingTag(Element):
    def render(self, file_out, ind=""):
        if self.content:
            file_out.write("5s<5s<5s 5s/>\n") %(ind, self.tag_name,self.content[0]))
        else file_out.write("%s<%s /n") % (ind, self.tag_name))


class A(Element):
    def __init__(self, link, content):
        self.link = link
        if content:
            self.content = [content]
        else.content = []


class Ul(Element):
    tag = "ul"


class Li(Element):
    tag = "Li"
