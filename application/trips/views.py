from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.auth.models import User
from application.trips.models import Trip
from application.trip_sport.models import TripSport
from application.trip_level.models import TripLevel
from application.trip_user.models import TripUser
from application.trips.forms import TripForm, SearchForm

from application.sports.models import Sport

from application.levels.models import Level

import datetime


@app.route("/trips/", methods=["GET"])
@login_required
def trips_index():
    return render_template("trips/list.html", trips=Trip.query.all())


@app.route("/trips/mytrips", methods=["GET"])
@login_required
def trips_mytrips():
    return render_template("trips/mytrips.html", trips=Trip.find_user_trips(current_user.id))


@app.route("/trips/registrations", methods=["GET"])
@login_required
def trips_registrations():
    return render_template("trips/registrations.html", trips=Trip.find_registrations(current_user.id))


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
    previous_sports = Sport.query.join(TripSport).join(Trip).filter(
        (TripSport.sport_id == Sport.id) & (TripSport.trip_id == trip_id)).all()
    all_levels = Level.query.all()
    previous_levels = Level.query.join(TripLevel).join(Trip).filter(
        (TripLevel.level_id == Level.id) & (TripLevel.trip_id == trip_id)).all()

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

    t = Trip.query.get(trip_id)

    db.session().delete(t)
    db.session().commit()

    return redirect(url_for("trips_index"))

@app.route("/trips/<trip_id>", methods=["GET"])
@login_required
def trips_display(trip_id):

    trip = Trip.query.get(trip_id)
    reg = trip.number_of_registrations()
    full = False

    if reg >= trip.max_participants:
        full = True

    return render_template("trips/display.html", trip=trip, user_id=current_user.id, registrations=reg, full=full)


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

@app.route("/trips/search", methods=["GET", "POST"])
@login_required
def trips_search():

    form = SearchForm(request.form)

    if request.method == "GET":
        return render_template("trips/search.html", form=form)

    if not form.validate():
        return render_template("trips/search.html", form=form)

    price = form.price.data
    start_date = form.start_date.data

    query = db.session().query(Trip)
    if price:
        query = query.filter(price >= Trip.price)
    if start_date:
        query = query.filter(start_date <= Trip.start_date)
    query = query.order_by(Trip.start_date)

    results = query.all()

    return render_template("trips/list.html", trips=results)
    

