from application import db
from application.models import Base
from sqlalchemy.orm import relationship, backref
from application.trips.models import Trip 
from application.levels.models import Level 

class TripLevel(Base):
    __tablename__ = "trip_level"

    trip_id = db.Column(db.Integer, db.ForeignKey('trip.id'), nullable=False)
    level_id = db.Column(db.Integer, db.ForeignKey('level.id'), nullable=False)

    trip = relationship(Trip, backref=backref("trip_level", cascade="all, delete-orphan"))
    level = relationship(Level, backref=backref("trip_level", cascade="all, delete-orphan"))

    def __init__(self, trip_id):
        self.trip_id = trip_id