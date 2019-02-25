from flask import Flask, render_template, redirect, request

app = Flask(__name__)

WORDS = []
with open("large","r") as file:
    for line in file.readlines():
        WORDS.append(line.rstrip())

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    words = []
    q = request.args.get("q")
    for word in WORDS:
        if word.startswith(q):
            words.append(word)
    
    return render_template("search.html",words=words)