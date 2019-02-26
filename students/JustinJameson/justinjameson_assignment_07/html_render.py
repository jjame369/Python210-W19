#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = 'html'

    def __init__(self, content='',**kwargs):
        self.contents = [content]
        self.attributes = ''.join([' %s == "%s"' % (key, value) for key, value in kwargs.items()])


    def append(self, new_content):
        self.contents.append(new_content)
        out_file.write("<{}>\n".format(self.tag))

    def render(self, out_file):
        # out_file.write("<{}>\n".format(self.tag))
        out_file.write("<{} {}>\n".format(self.tag, self.attibutes))
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)




class Html (Element):
    """Order of tags
    <!DOCTYPE html> declaration defines this document to be HTML5
    <html> element is the root element of an HTML page
    <head> element contains meta information about the document
    <title> element specifies a title for the document
    <body> element contains the visible page content
    <h1> element defines a large heading
    <p> element defines a paragraph"""
    tag = 'html'


class Body (Element):
    tag = 'body'


class P (Element):
    tag = 'p'


class Head (Element):
    tag = 'head'


class OneLineTag(Element):
    def render(self, out_file):
        out_file.write("<{}>".format(self.tag))
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))

    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = "title"
