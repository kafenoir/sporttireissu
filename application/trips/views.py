from application import app, db
from flask import redirect, render_template, request, url_for
from application.trips.models import Trip
import datetime

@app.route("/trips/", methods=["GET"])
def trips_index():
    return render_template("trips/list.html", trips = Trip.query.all())

@app.route("/trips/new")
def trips_form():
    return render_template("trips/new.html")


@app.route("/trips/<trip_id>", methods=["POST"])
def trips_editor(trip_id):
    return render_template("trips/edit.html", trip = Trip.query.get(trip_id))


@app.route("/trips/", methods=["POST"])
def trips_create():
    t = Trip(request.form.get("name"))

    t.price = request.form.get("price")
    t.destination = request.form.get("destination")
    t.start_date = datetime.datetime.strptime(request.form.get("start_date"), "%Y-%m-%d").date()
    t.end_date = datetime.datetime.strptime(request.form.get("end_date"), "%Y-%m-%d").date()
    t.description = request.form.get("description")
    t.registration_dl = datetime.datetime.strptime(request.form.get("registration_dl"), "%Y-%m-%d").date()
    t.max_participants = request.form.get("max_participants")

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("trips_index"))

@app.route("/trips/<trip_id>/", methods=["POST"])
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

