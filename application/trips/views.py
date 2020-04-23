from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.trips.models import Trip, trip_sport, trip_level
from application.trips.forms import (TripForm)

from application.sports.models import Sport

from application.levels.models import Level

import datetime


@app.route("/trips/", methods=["GET"])
@login_required
def trips_index():
    return render_template("trips/list.html", trips=Trip.query.all(), user_id=current_user.id)


@app.route("/trips/new", methods=["GET", "POST"])
@login_required
def trips_create():

    form = TripForm(request.form)
    form.sports.choices = [(c.id, c.name) for c in Sport.query.all()]
    form.levels.choices = [(c.id, c.name) for c in Level.query.all()]

    if request.method == "GET":
        return render_template("trips/new.html", form=form)

    t = Trip(form.name.data)
    t.price = form.price.data
    t.destination = form.destination.data
    t.start_date = form.start_date.data
    t.end_date = form.end_date.data
    t.description = form.description.data
    t.registration_dl = form.registration_dl.data
    t.max_participants = form.max_participants.data
    t.account_id = current_user.id

    if not form.validate():
        return render_template("trips/new.html", form=form)

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


@app.route("/trips/edit/<trip_id>", methods=["GET", "POST"])
@login_required
def trips_edit(trip_id):

    t = Trip.query.get(trip_id)

    if t.account_id != current_user.id:
        return redirect(url_for("trips_index"))

    form = TripForm(request.form)
    form.sports.choices = [(c.id, c.name) for c in Sport.query.all()]
    form.levels.choices = [(c.id, c.name) for c in Level.query.all()]
    all_sports = Sport.query.all()
    previous_sports = Sport.query.join(trip_sport).join(Trip).filter(
        (trip_sport.c.sport_id == Sport.id) & (trip_sport.c.trip_id == trip_id)).all()
    all_levels = Level.query.all()
    previous_levels = Level.query.join(trip_level).join(Trip).filter(
        (trip_level.c.level_id == Level.id) & (trip_level.c.trip_id == trip_id)).all()

    if request.method == "GET":
        return render_template("trips/edit.html", form=form, trip=t, sports=all_sports, levels=all_levels, previous_sports=previous_sports, previous_levels=previous_levels)

    if not form.validate():
        return render_template("trips/edit.html", form=form, trip=t, sports=all_sports, levels=all_levels, previous_sports=previous_sports, previous_levels=previous_levels)

    t.price = form.price.data
    t.destination = form.destination.data
    t.start_date = form.start_date.data
    t.end_date = form.end_date.data
    t.description = form.description.data
    t.registration_dl = form.registration_dl.data
    t.max_participants = form.max_participants.data
    t.account_id = current_user.id

    for sport in all_sports:
        if sport.id in form.sports.data and sport not in previous_sports:
            t.sports.append(sport)
        elif sport.id not in form.sports.data and sport in previous_sports:
            t.sports.remove(sport)

    for level in all_levels:
        if level.id in form.levels.data and level not in previous_levels:
            t.levels.append(level)
        elif level.id not in form.levels.data and level in previous_levels:
            t.levels.remove(level)

    db.session().add(t)
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

@app.route("/trips/<trip_id>", methods=["GET"])
@login_required
def trips_display(trip_id):
    return render_template("trips/display.html", trip=Trip.query.get(trip_id), user_id=current_user.id)

@app.route("/trips/register/<trip_id>", methods=["POST"])
@login_required
def trips_register(trip_id):

    trip = Trip.query.get(trip_id)
    trip.users.append(current_user)

    db.session().add(trip)
    db.session().commit()

    return render_template("trips/display.html", trip=trip, user_id=current_user.id)

@app.route("/trips/cancel/<trip_id>", methods=["POST"])
@login_required
def trips_cancel_registration(trip_id):

    trip = Trip.query.get(trip_id)
    trip.users.remove(current_user)

    db.session().add(trip)
    db.session().commit()

    return render_template("trips/display.html", trip=trip, user_id=current_user.id)


