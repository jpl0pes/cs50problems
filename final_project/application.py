import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError

from api_helper import pocket_articles

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/essays", methods=["GET","POST"])
def essays():
    return render_template("essays.html")

##I'm just going to use Google Docs and then publish them via HTML on the website manually.
##If I start to get a bit more articles I can create a sort of CMS in which I can fetch the articles from there.

##ALL ARTICLES:

@app.route("/essays/london_tube", methods=["GET","POST"])
def london_tube():
    return render_template("essays/london_tube.html")

@app.route("/essays/disagree_commit", methods=["GET","POST"])
def disagree_commit():
    return render_template("essays/disagree_commit.html")

@app.route("/essays/culture_sapiens", methods=["GET","POST"])
def culture_sapiens():
    return render_template("essays/culture_sapiens.html")


@app.route("/articles", methods=["GET","POST"])
def articles():
    articles = pocket_articles()
    print(pocket_articles)
    return render_template("articles.html", articles=articles)


##Develop API to fetch favorite articles from pocket.

@app.route("/projects", methods=["GET","POST"])
def projects():
    return render_template("projects.html")

##A list of multiple pages that have all the projects that I've worked on.


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return print(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
