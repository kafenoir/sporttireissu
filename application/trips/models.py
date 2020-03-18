from application import db

class Trip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    start_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    end_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    registration_dl = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, name):
        self.name = name
