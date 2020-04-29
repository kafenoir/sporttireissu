from application import db
from application.models import Base
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text


class Trip(Base):

    name = db.Column(db.String(32), nullable=False)
    destination = db.Column(db.String(32), nullable=False)
    start_date = db.Column(db.DateTime, default=db.func.current_date())
    end_date = db.Column(db.DateTime, default=db.func.current_date())
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(144), nullable=False)
    registration_dl = db.Column(db.DateTime, default=db.func.current_date())
    max_participants = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey(
        'account.id'), nullable=False)

    sports = relationship('Sport', secondary='trip_sport')

    levels = relationship('Level', secondary='trip_level')

    users = relationship('User', secondary='trip_user')

    def __init__(self, name):
        self.name = name
        self.destination = "Ei määritelty"
        self.price = 0
        self.description = "Tervetuloa matkalleni!"
        self.max_participants = 10

    def convertStartDate(self):
        return self.start_date.strftime("%d-%m-%Y")

    def convertEndDate(self):
        return self.end_date.strftime("%d-%m-%Y")

    def convertRegDL(self):
        return self.registration_dl.strftime("%d-%m-%Y")

    def number_of_registrations(self):

        stmt = text(
            "SELECT COUNT(*) FROM Account"
            " LEFT JOIN Trip_User ON Trip_User.account_id = Account.id"
            " LEFT JOIN Trip ON Trip.id = Trip_User.trip_id"
            " WHERE Trip.id = " + str(self.id))

        res = db.engine.execute(stmt)
        row = res.fetchone()
        response = row[0]

        return response

    @staticmethod
    def find_trips_with_sport(s):
        stmt = text("SELECT Trip.id, Trip.name FROM Trip"
                    " LEFT JOIN Trip_Sport ON Trip_Sport.trip_id = Trip.id"
                    " LEFT JOIN Sport ON Sport.id = Trip_Sport.sport_id"
                    " WHERE Sport.id = " + s)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id": row[0], "name": row[1]})

        return response

    @staticmethod
    def find_user_trips(user_id):
        stmt = text(
            "SELECT Trip.id, Trip.name, Trip.destination, Trip.start_date, Trip.end_date FROM Trip"
            " LEFT JOIN Account ON Account.id = Trip.account_id"
            " WHERE Account.id = " + str(user_id) +
            " ORDER BY Trip.registration_dl")

        res = db.engine.execute(stmt)

        response = []
        sep = ' '
        for row in res:
            response.append(
                {"id": row[0], "name": row[1], "destination": row[2], "start_date": row[3].split(sep, 1)[0], "end_date": row[4].split(sep, 1)[0]})

        return response

    @staticmethod
    def find_registrations(user_id):

        stmt = text(
            "SELECT Trip.id, Trip.name, Trip.destination, Trip.start_date, Trip.end_date FROM Trip"
            " LEFT JOIN Trip_User ON Trip_User.trip_id = Trip.id"
            " LEFT JOIN Account ON Account.id = Trip_User.account_id"
            " WHERE Account.id = " + str(user_id) +
            " ORDER BY Trip.registration_dl")

        res = db.engine.execute(stmt)

        response = []
        sep = ' '
        for row in res:
                response.append(
                    {"id": row[0], "name": row[1], "destination": row[2], "start_date": row[3].split(sep, 1)[0], "end_date": row[4].split(sep, 1)[0]})

        return response
    
