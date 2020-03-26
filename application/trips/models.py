from application import db
from datetime import datetime

class Trip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    destination = db.Column(db.String(32), nullable=False)
    start_date = db.Column(db.DateTime, default=db.func.current_date())
    end_date = db.Column(db.DateTime, default=db.func.current_date())
    price = db.Column(db.Integer, nullable = False)
    description = db.Column(db.String(144), nullable=False)
    registration_dl = db.Column(db.DateTime, default=db.func.current_date())
    max_participants = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name):
        self.name = name
        self.destination = "Ei määritelty"
        self.price = 0
        self.description = "Tervetuloa matkalleni!"
        self.max_participants = 10

    def convertStartDate(self):
        return self.start_date.strftime("%Y-%m-%d")

    def convertEndDate(self):
        return self.end_date.strftime("%Y-%m-%d")

    def convertRegDL(self):
        return self.registration_dl.strftime("%Y-%m-%d")
        
