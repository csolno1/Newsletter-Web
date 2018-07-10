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
        (r"{{topleftbar}}", '''
        {% if login_in %}
            <a class="nav-link active" href="account.html">
                <img
                    src="images/home_black_18dp.png"
                    width="20"
                    height="20"
                    class="d-inline-block align-top"
                    alt="alt">个人空间</a>
        {% else %}
        <li class="nav-item dropdown active">
            <a
                class="nav-link dropdown-toggle"
                href="#"
                id="dropdown0"
                data-toggle="dropdown"
                aria-haspopup="true"
                aria-expanded="false">
                <img
                    src="images/face_black_18dp.png"
                    width="20"
                    height="20"
                    class="d-inline-block align-top"
                    alt="alt">账户
                <span class="sr-only">(current)</span>
            </a>
            <div class="dropdown-menu" aria-labelledby="dropdown0">
                <a class="dropdown-item" href="login.html">登录</a>
                <a class="dropdown-item" href="register.html">注册</a>
            </div>
        </li>
        {% endif %}
        '''
        ),
        (r"\"([\w\d\-\/\.]*\.[a-z]+)\"", r'''"{% static 'news/\1' %}"'''),
        (r"{% static 'news/(.*)\.html' %}", r"{% url '\1' %}"), 
    ]

class Index(Replaced):

    name = "index.html"
    regexes = [
        (r'<div class="card-columns">([\s\S\r]*)</div>', r'''
        <div class = "card-columns">
            {% for news in manyNews %}
                <div class="card">
                    <a class="nav-link text-dark" href="{% url 'news-details' news.id %}">
                        <img class="card-img-top" src="{% if news.cover_image %}{{news.cover_image}}{% endif %}">
                        <div class="card-body">
                            <h5 class="card-title">{{news.title}}</h5>
                            <p>{{news.pub_date}}</p>
                        </div>
                    </a>
                </div>
            {% endfor %}
        </div>'''), 
    ]

class Login(Replaced):
    name = "login.html"
    regexes = []

class Register(Replaced):
    name = "register.html"
    regexes = []

class NewsDetail(Replaced):
    name = "news_detail.html"
    regexes = []

class Account(Replaced):
    name = "account.html"
    regexes = []

createTemplate(Index())
createTemplate(Login())
createTemplate(Register())
createTemplate(NewsDetail())
createTemplate(Account())
moveStaticFiles()