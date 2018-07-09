import os
import re
def createTemplate(replaces):
    replaces.append()

    html_name = replaces.name
    regexes = replaces.regexes
    templatePath = "newsletter/news/templates/news/"
    i = open(html_name, "r")
    o = open(templatePath + html_name, "w")
    c = i.read()
    i.close()


    for pre, after in regexes:
        c = re.sub(pre, after, c)

    o.write(c)
    o.close()

    return

class Replaced:

    def append(self):
        self.regexes = Replaced.regexes + self.regexes


    regexes = [
        (r"(<!doctype html>)", r"{% load static %}\n\1"),
    ]

class Index(Replaced):

    name = "index.html"
    regexes = [
        (r"([\w\d\-\/\.]*\.[a-z]+)", r"{% static 'news/\1' %}"),
        
    ]

createTemplate(Index())