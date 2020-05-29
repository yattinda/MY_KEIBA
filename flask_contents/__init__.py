from flask import Flask

app = Flask(__name__)
# app = Flask(__name__,template_folder="templates")


import flask_blog.views
