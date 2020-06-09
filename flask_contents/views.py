from flask import request, redirect, url_for, render_template, flash, session
from flask_contents import app
from jinja2 import FileSystemLoader
from flask_contents import db
from flask_contents.model.entries import Entry


# app.jinja_loader = FileSystemLoader("templates/entries")
@app.route('/')
def show_index():
    return render_template("index.html")

@app.route('/plus',methods=["POST"])
def plus():
    entry = Entry(
    racecourse = request.form["racecourse"],
    racedate = request.form["racedate"],
    racenum = request.form["racenum"],
    horsename = request.form["horsename"],
    distance = request.form["distance"],
    condition = request.form["condition"],
    sign = request.form["sign"],
    comment = request.form["comment"],
    )
    db.session.add(entry)
    db.session.commit()
    flash("new data")
    return redirect("index.html")



@app.route('/find')
def render_find():
    return render_template("find.html")

@app.route('/index')
def render_index():
    return render_template("index.html")
