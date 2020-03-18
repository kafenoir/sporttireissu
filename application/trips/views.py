from application import app, db
from flask import redirect, render_template, request, url_for
from application.trips.models import Trip

@app.route("/trips/", methods=["GET"])
def trips_index():
    return render_template("trips/list.html", trips = Trip.query.all())

@app.route("/trips/new")
def trips_form():
    return render_template("trips/new.html")

@app.route("/trips/", methods=["POST"])
def trips_create():
    t = Trip(request.form.get("name"))

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("trips_index"))
