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

    def render(self, file_out, ind="    "):
        attributes = ''
        for (key, value) in self.attributes.items():
            attributes += (' {key} = "{value}"'.format(key = key, value = value))
        file_out.write(u'\n%s<%s%s>\n' % (ind, self.tag, attributes))
        for item in self.content:
            try:
                item.render(file_out, ind + self.indent)
            except AttributeError:
                file_out.write(self.indent + ind)
                file_out.write(item)
        file_out.write(u'\n%s</%s>' % (ind, self.tag))


class Html(Element):
    tag = "head"

    def render(self, file_out, ind=u""):
        print("hmtl")
        file_out.write(u"<!DOCTYPE html>")
        Element.render(self, file_out)


class Head(Element):
    tag = "head"


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class OneLineTag(Element):
    def render(self, file_out, ind="    "):
        attributes = '  '
        for (key,value) in self.attributes.items():
            attributes += (' {key} = "{value}"'.format(key = key, value = value))
        file_out.write(u'\n%s<%s%s>\n' % (ind, self.tag, attributes))
        for item in self.content:
            try:
                item.render(file_out, ind + self.indent)
            except AttributeError:
                file_out.write(self.indent + ind)
                file_out.write(unicode(item))
        file_out.write(u'\n%s</%s>' % (ind, self.tag))


class SelfClosingTag(Element):
    def __init__(self, **attributes):
        self.attributes = attributes

    def render(self, file_out, ind = "    "):
        attributes = ''
        for (key, value) in self.attributes.items():
            attributes += (' {key} = "{value}"'.format(key = key, value = value))
        file_out.write(u'\n%s<%s%s>\n' % (ind, self.tag, attributes))


class Hr(SelfClosingTag):
    tag = "hr"


class Title(OneLineTag):
    tag = "title"


class A(Element):
    def __init__(self, link, content):
        self.link = link
        if content:
            self.content = [content]
        else:
            content = []


class H(OneLineTag):
    def __init__(self, level, content, **attributes):
        OneLineTag.__init__(self, content, **attributes)

        self.tag = u"h%i"%level


class Ul(Element):
    tag = "ul"


class Li(Element):
    tag = "Li"


class Meta(SelfClosingTag):
    tag = "meta"
