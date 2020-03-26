from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.trips.models import Trip
from application.trips.forms import TripForm

import datetime

@app.route("/trips/", methods=["GET"])
def trips_index():
    return render_template("trips/list.html", trips = Trip.query.all())

@app.route("/trips/new")
@login_required
def trips_form():
    return render_template("trips/new.html", form = TripForm())


@app.route("/trips/<trip_id>", methods=["POST"])
@login_required
def trips_editor(trip_id):
    return render_template("trips/edit.html", trip = Trip.query.get(trip_id))


@app.route("/trips/", methods=["POST"])
@login_required
def trips_create():
    form = TripForm(request.form)

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

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("trips_index"))

@app.route("/trips/<trip_id>/", methods=["POST"])
@login_required
def trips_edit(trip_id):

    t = Trip.query.get(trip_id)
    t.name = request.form.get("name")
    t.price = request.form.get("price")
    t.destination = request.form.get("destination")
    t.start_date = datetime.datetime.strptime(request.form.get("start_date"), "%Y-%m-%d").date()
    t.end_date = datetime.datetime.strptime(request.form.get("end_date"), "%Y-%m-%d").date()
    t.description = request.form.get("description")
    t.registration_dl = datetime.datetime.strptime(request.form.get("registration_dl"), "%Y-%m-%d").date()
    t.max_participants = request.form.get("max_participants")
    db.session().commit()

    return redirect(url_for("trips_index"))

