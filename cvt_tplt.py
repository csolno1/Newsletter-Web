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
            dir = path.rsplit('/', 1)[0]
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
        (r"([\w\d\-\/\.]*\.[a-z]+)", r"{% static 'news/\1' %}"),
    ]

class Index(Replaced):

    name = "index.html"
    regexes = [
        (r'<div class="card-columns">([\s\S\r]*)</div>', r'''
        <div class = "card-columns">
            {% for news in manyNews %}
                <div class="card">
                    <a class="nav-link text-dark" href="{% url 'news-details' news.id %}">
                        <img class="card-img-top" src="{{news.cover_image}}">
                        <div class="card-body">
                            <h5 class="card-title">{{news.title}}</h5>
                            <p>{{news.pub_date}}</p>
                        </div>
                    </a>
                </div>
            {% endfor %}
        </div>'''), 
        (r"{% static 'news/(.*)\.html' %}", r"{% url '\1' %}"), 
    ]


createTemplate(Index())
moveStaticFiles()