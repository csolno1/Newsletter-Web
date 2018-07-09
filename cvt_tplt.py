import os
import re
import glob
import string

staticFiles = [
    "css/*",
    "images/*",
    "js/*",
]

def moveStaticFiles():
    staticFilePath = "newsletter/news/static/news/"
    for file in staticFiles:
        paths = glob.glob(file)
        for path in paths:
            dir = path.rsplit('\\', 1)[0]
            if(not os.path.exists(staticFilePath + dir)):
                os.makedirs(staticFilePath + dir)
            import shutil
            shutil.copyfile(path, staticFilePath + path)


def createTemplate(replaces):
    #replaces.append()

    html_name = replaces.name
    regexes = replaces.regexes
    templatePath = "newsletter/news/templates/news/"
    i = open(html_name, "r", encoding='utf-8')
    o = open(templatePath + html_name, "w", encoding='utf-8')
    c = i.read()
    i.close()


    for pre, after in regexes:
        c = re.sub(pre, after, c)

    o.write(c)
    o.close()

    return

class Replaced:

    def __init__(self):
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
moveStaticFiles()