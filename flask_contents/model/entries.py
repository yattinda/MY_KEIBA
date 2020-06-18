from flask_contents import db

class Entry(db.Model):
    __tablename__ = "entries"
    id = db.Column(db.Integer, primary_key = True)
    racecourse = db.Column(db.String)
    racedate = db.Column(db.String)
    racenum = db.Column(db.String)
    horsename = db.Column(db.String)
    coursetype = db.Column(db.String)
    distance = db.Column(db.String)
    condition = db.Column(db.String)
    groundcondition = db.Column(db.String)
    sign = db.Column(db.String)
    comment = db.Column(db.Text)

    def __init__(self, racecourse = None, racedate = None, racenum = None, horsename = None, coursetype = None, distance = None, condition = None, groundcondition = None, sign = None, comment = None):
        self.racecourse = racecourse
        self.racedate = racedate
        self.racenum = racenum
        self.horsename = horsename
        self.coursetype = coursetype
        self.distance = distance
        self.condition = condition
        self.groundcondition = groundcondition
        self.sign = sign
        self.comment = comment

    def __repr__(self):
        return "<<<id{}:course{}:date{}:num{}:name{}:type{}:dis{}:cond{}:grn{}:sign{}:com{}>>>".format(self.id, self.racecourse, self.racenum, self.horsename, self.coursetype, self.distance, self.condition, self.groundcondition, self.sign, self.comment)
