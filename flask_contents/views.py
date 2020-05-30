from flask import request, redirect, url_for, render_template, flash, session
from flask_contents import app
from jinja2 import FileSystemLoader

# app.jinja_loader = FileSystemLoader("templates/entries")
@app.route('/')
def show_entries():
    return render_template("index.html")

@app.route('/find')
def render_find():
    return render_template("find.html")

@app.route('/index')
def render_index():
    return render_template("index.html")
