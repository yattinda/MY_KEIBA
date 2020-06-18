from flask import request, redirect, url_for, render_template, flash, session
from flask_contents import app
from jinja2 import FileSystemLoader
from flask_contents import db
from flask_contents.model.entries import Entry


# app.jinja_loader = FileSystemLoader("templates/entries")
@app.route('/')
def show_index():
    return render_template("index.html")

@app.route('/plus',methods=["GET","POST"])
def plus():
    try:
        entry = Entry(
        racecourse = request.form["racecourse"],
        racedate = request.form["racedate"],
        racenum = request.form["racenum"],
        horsename = request.form["horsename"],
        coursetype = request.form["coursetype"],
        distance = request.form["distance"],
        condition = request.form["condition"],
        groundcondition =request.form["groundcondition"],
        sign = request.form["sign"],
        comment = request.form["comment"],
        )
        db.session.add(entry)
        db.session.commit()
        flash("register new data")
        return redirect("/")

    except:
        flash("error! :Some forms are not filled")
        return redirect("/")

@app.route('/find')
def render_find():
    return render_template("find.html")

@app.route('/index')
def render_index():
    return render_template("index.html")

@app.route('/sarch',methods=["GET","POST"])
def sarch():
    horsedata = Entry.query.filter_by(horsename = request.form["want_horsename"]).all()
    horsedata.reverse()
    horsename = request.form["want_horsename"]
    return render_template("/history.html",horsedata = horsedata, horsename = horsename)

@app.route('/show_comment/<int:id>', methods=["GET"])
def show_comment(id):
    horsedata = Entry.query.get(id)
    return render_template("/comment.html",horsedata = horsedata)

@app.route('/delete/<int:id>', methods=["GET","POST"])
def delete(id):
    delete_data = Entry.query.get(id)
    delete_horsename = delete_data.horsename
    db.session.delete(delete_data)
    db.session.commit()
    horsedata = Entry.query.filter_by(horsename = delete_horsename).all()
    horsedata.reverse()
    return render_template("/history.html",horsedata = horsedata)
