from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.trips.models import Trip
from application.trips.forms import (TripForm)

from application.sports.models import Sport

from application.levels.models import Level

import datetime

@app.route("/trips/", methods=["GET"])
def trips_index():
    return render_template("trips/list.html", trips = Trip.query.all())

@app.route("/trips/new")
@login_required
def trips_form():
    form = TripForm(request.form)
    form.sports.choices = [(c.id, c.name) for c in Sport.query.all()]
    form.levels.choices = [(c.id, c.name) for c in Level.query.all()]
    return render_template("trips/new.html", form = form)


@app.route("/trips/<trip_id>", methods=["POST"])
@login_required
def trips_editor(trip_id):
    return render_template("trips/edit.html", form = TripForm(), trip = Trip.query.get(trip_id))


@app.route("/trips/", methods=["POST"])
@login_required
def trips_create():
    form = TripForm(request.form)
    form.sports.choices = [(c.id, c.name) for c in Sport.query.all()]
    form.levels.choices = [(c.id, c.name) for c in Level.query.all()]

    if not form.validate():
        return render_template("trips/new.html", form = form)

    t = Trip(form.name.data)
    t.price = form.price.data
    t.destination = form.destination.data
    t.start_date = form.start_date.data
    t.end_date = form.end_date.data
    t.description = form.description.data
    t.registration_dl = form.registration_dl.data
    t.max_participants = form.max_participants.data
    t.account_id = current_user.id

    sport_records = Sport.query.all()
    accepted = []
    for sport in sport_records:
        if sport.id in form.sports.data:
            accepted.append(sport)
    t.sports = accepted

    level_records = Level.query.all()
    accepted = []
    for level in level_records:
        if level.id in form.levels.data:
            accepted.append(level)
    t.levels = accepted

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("trips_index"))

@app.route("/trips/edit/<trip_id>", methods=["POST"])
@login_required
def trips_edit(trip_id):

    form = TripForm(request.form)

    if not form.validate():
        return render_template("trips/edit.html", form = form, trip = Trip.query.get(trip_id))

    t = Trip.query.get(trip_id)
    t.price = form.price.data
    t.destination = form.destination.data
    t.start_date = form.start_date.data
    t.end_date = form.end_date.data
    t.registration_dl = form.registration_dl.data
    t.max_participants = form.max_participants.data

    db.session().commit()

    return redirect(url_for("trips_index"))

@app.route("/trips/delete/<trip_id>", methods=["POST"])
@login_required
def trips_delete(trip_id):

    Trip.query.filter(Trip.id == trip_id).delete()

    db.session().commit()

    return redirect(url_for("trips_index"))

@app.route("/trips/sport/<sport_id>", methods=["GET"])
def search_by_sport(sport_id):

    return render_template("trips/search.html", trips=Trip.find_trips_with_sport(sport_id))







