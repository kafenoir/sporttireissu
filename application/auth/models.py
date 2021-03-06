from application import db
from application.models import Base

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    email = db.Column(db.String(144), nullable=False)
    address = db.Column(db.String(144), nullable=False)

    trips = db.relationship("Trip", backref='account', lazy=True)

    def __init__(self, name, username, password, email, address):
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        self.address = address

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def get_trips(self):
        return self.trips