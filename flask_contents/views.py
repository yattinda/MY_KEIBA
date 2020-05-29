from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from jinja2 import FileSystemLoader

# app.jinja_loader = FileSystemLoader("templates/entries")
@app.route('/')
def show_entries():
    return render_template("index.html")
