from application import db
from application.models import Base
from sqlalchemy.orm import relationship, backref
from application.trips.models import Trip 
from application.sports.models import Sport 

class TripSport(Base):
    __tablename__ = "trip_sport"

    trip_id = db.Column(db.Integer, db.ForeignKey('trip.id'), nullable=False)
    sport_id = db.Column(db.Integer, db.ForeignKey('sport.id'), nullable=False)

    trip = relationship(Trip, backref=backref("trip_sport", cascade="all, delete-orphan"))
    sport = relationship(Sport, backref=backref("trip_sport", cascade="all, delete-orphan"))

    def __init__(self, trip_id):
        self.trip_id = trip_id