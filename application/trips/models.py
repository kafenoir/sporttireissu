from application import db
from application.models import Base
from datetime import datetime

from sqlalchemy.sql import text

trip_sport = db.Table('trip_sport', db.Column('trip_id', db.Integer, db.ForeignKey('trip.id'), primary_key=True), db.Column('sport_id', db.Integer, db.ForeignKey('sport.id'), primary_key=True))

trip_level = db.Table('trip_level', db.Column('trip_id', db.Integer, db.ForeignKey('trip.id'), primary_key=True), db.Column('level_id', db.Integer, db.ForeignKey('level.id'), primary_key=True))

trip_user = db.Table('trip_user', db.Column('trip_id', db.Integer, db.ForeignKey('trip.id'), primary_key=True), db.Column('account_id', db.Integer, db.ForeignKey('account.id'), primary_key=True))

class Trip(Base):

    name = db.Column(db.String(32), nullable=False)
    destination = db.Column(db.String(32), nullable=False)
    start_date = db.Column(db.DateTime, default=db.func.current_date())
    end_date = db.Column(db.DateTime, default=db.func.current_date())
    price = db.Column(db.Integer, nullable = False)
    description = db.Column(db.String(144), nullable=False)
    registration_dl = db.Column(db.DateTime, default=db.func.current_date())
    max_participants = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    sports = db.relationship('Sport', secondary=trip_sport, lazy='subquery', backref=db.backref('trip_sports', lazy=True))

    levels = db.relationship('Level', secondary=trip_level, lazy='subquery', backref=db.backref('trip_levels', lazy=True))

    users = db.relationship('User', secondary=trip_user, lazy='subquery', backref=db.backref('trip_users', lazy=True))

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

    @staticmethod
    def find_trips_with_sport(s):
        stmt = text("SELECT Trip.id, Trip.name FROM Trip"
                    " LEFT JOIN Trip_Sport ON Trip_Sport.trip_id = Trip.id"
                    " LEFT JOIN Sport ON Sport.id = Trip_Sport.sport_id"
                    " WHERE Sport.id = " + s)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name": row[1]})
        
        return response
        
        
