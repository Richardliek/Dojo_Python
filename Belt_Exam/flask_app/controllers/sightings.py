from crypt import methods
from flask import render_template,redirect,session,request, flash
from flask_app.models.sighting import Sighting
from flask_app import app
from flask_app.models.user import User

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    user_data ={
        'id': session['user_id']
    }
    return render_template("dashboard.html",user=User.get_by_id(user_data), sightings=Sighting.get_all()) 


@app.route("/sightings/add")
def add_sighting():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id' : session['user_id']
    }
    return render_template("new_sighting.html", user= User.get_by_id(data))

@app.route('/sightings/add', methods=['POST'])
def create_sightings():
    if not Sighting.validate_sightings(request.form):
        return redirect('/sightings/add')
    sighting_data = {
        'location' : request.form['location'],
        'what_happened' : request.form['what_happened'],
        'num_sasquatch' : request.form['num_sasquatch'],
        'date_found' : request.form['date_found'],
        'user_id' : session['user_id']
    }
    Sighting.create_sighting(sighting_data)
    return redirect('/dashboard')

@app.route('/sightings/<int:id>')
def show_sighting(id):
    data = {
        'id' : id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("show_sighting.html", user=User.get_by_id(user_data), sighting = Sighting.get_one(data))

@app.route('/sightings/<int:id>/edit')
def edit_sighting(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id' : id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_sighting.html", user = User.get_by_id(user_data), sighting = Sighting.get_one(data))

@app.route("/sightings/<int:id>/update", methods=["POST"])
def update_sighting(id):
    if not Sighting.validate_sightings(request.form):
        return redirect(f"/sightings/{id}/edit")
    Sighting.update(request.form)
    return redirect('/dashboard')

@app.route('/sightings/<int:id>/delete')
def destroy_sighting(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Sighting.destroy(data)
    return redirect('/dashboard')