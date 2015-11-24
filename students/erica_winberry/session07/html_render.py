class Element:

    indent = 2
    tag = ""

    def __init__(self, content=None, **kwargs):
        self.content = []
        if content is not None:
            self.content.append(content)
        self.kwargs = kwargs

    def append(self, content):
        self.content.append(content)

    def render(self, f, ind=" "):
        start_tag = "\n<{}".format(self.tag)
        if self.kwargs:
            f.write(start_tag)
            for k, v in self.kwargs.items():
                attribute = '{}="{}"'.format(k, v)
                f.write(" " + attribute)
            f.write(">")
        else:
            f.write(start_tag + ">")
        for element in self.content:
            try:
                element.render(f)
            except AttributeError:
                f.write(str(element))
        end_tag = "\n</{}>".format(self.tag)
        f.write(end_tag)


class Body(Element):

    tag = "body"


class Head(Element):

    tag = "head"


class Html(Element):

    indent = 0
    tag = "html"


class Link(Element):

    tag="a"

    def __init__(self, link=None, content=None, **kwargs):
        Element.__init__(self, content=None)
        self.link = link
        self.content = []
        if content is not None:
            self.content.append(content)
            self.kwargs = kwargs

    def render(self, f, ind=" "):
        start_tag = '<{} href="{}"'.format(self.tag, self.link)
        if self.kwargs:
            f.write(start_tag)
            for k, v in self.kwargs.items():
                attribute = '{}="{}"'.format(k, v)
                f.write(" " + attribute)
            f.write(">")
        else:
            f.write(start_tag + ">")
        for element in self.content:
            try:
                element.render(f)
            except AttributeError:
                f.write(str(element))
        end_tag = "</{}> ".format(self.tag)
        f.write(end_tag)


class ListItem(Element):

    tag = "li"


class Paragraph(Element):

    tag = "p"


class UnordList(Element):

    tag = "ul"


class OneLineTag(Element):

    def render(self, f, ind=" "):
        start_tag = "\n<{}>".format(self.tag)
        f.write(start_tag)
        for element in self.content:
            try:
                element.render(f)
            except AttributeError:
                f.write(str(element))
        end_tag = "</{}>".format(self.tag)
        f.write(end_tag)


class Header(OneLineTag):

    tag = "h"

    def __init__(self, level=None, content=None, **kwargs):
        OneLineTag.__init__(self, content=None)
        self.level = level
        self.content = []
        if content is not None:
            self.content.append(content)
            self.kwargs = kwargs

    def render(self, f, ind=" "):
        start_tag = '\n<{}{:d}'.format(self.tag, self.level)
        if self.kwargs:
            f.write(start_tag)
            for k, v in self.kwargs.items():
                attribute = '{}="{}"'.format(k, v)
                f.write(" " + attribute)
            f.write(">")
        else:
            f.write(start_tag + ">")
        for element in self.content:
            try:
                element.render(f)
            except AttributeError:
                f.write(str(element))
        end_tag = '</{}{:d}>'.format(self.tag, self.level)
        f.write(end_tag)


class Title(OneLineTag):

    tag = "title"


class SelfClosingTag(Element):

    indent = 0

    def render(self, f, ind=" "):
        start_tag = "\n<{}".format(self.tag)
        if self.kwargs:
            f.write(start_tag)
            for k, v in self.kwargs.items():
                attribute = '{}="{}"'.format(k, v)
                f.write(" " + attribute)
            f.write(" />")
        else:
            f.write(start_tag + " />")


class HRule(SelfClosingTag):

    tag = "hr"


class LineBreak(SelfClosingTag):

    tag = "br"