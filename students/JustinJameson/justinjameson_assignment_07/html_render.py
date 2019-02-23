#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = 'html'
    def __init__(self, content=''):
        self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        out_file.write("<{}>\n".format(self.tag))
        for content in self.contents:
            out_file.write(content)
            out_file.write("\n")
        out_file.write("</{}>\n".format(self.tag))


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
