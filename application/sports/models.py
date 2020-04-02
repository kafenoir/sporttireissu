from application import db

class Sport(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)

    trips_sports = db.relationship("TripSport", backref='sport', lazy=True)

    def __init__(self, name):
        self.name = name

class TripSport(db.Model):

    trip_id = db.Column(db.Integer, db.ForeignKey('trip.id'), primary_key=True, nullable=False)
    sport_id = db.Column(db.Integer, db.ForeignKey('sport.id'), primary_key=True, nullable=False)

    def __init__(self, trip_id):
        self.trip_id = trip_id



