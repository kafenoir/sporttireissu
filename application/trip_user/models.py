from application import db
from application.models import Base
from sqlalchemy.orm import relationship, backref
from application.trips.models import Trip 
from application.auth.models import User 

class TripUser(Base):
    __tablename__ = "trip_user"

    trip_id = db.Column(db.Integer, db.ForeignKey('trip.id'), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    trip = relationship(Trip, backref=backref("trip_user", cascade="all, delete-orphan"))
    user = relationship(User, backref=backref("trip_user", cascade="all, delete-orphan"))

    def __init__(self, trip_id):
        self.trip_id = trip_id