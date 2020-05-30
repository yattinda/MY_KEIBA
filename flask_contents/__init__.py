from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("flask_contents.config")

#他のプログラムはdbという変数を参照することでDBを扱える
db = SQLAlchemy(app)

import flask_contents.views
