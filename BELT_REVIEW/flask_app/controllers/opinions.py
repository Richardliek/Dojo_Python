from crypt import methods
from flask import render_template,redirect,session,request, flash
from flask_app.models.opinion import Opinion
from flask_app import app
from flask_app.models.user import User

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("dashboard.html",user=User.get_by_id(data), opinions = Opinion.get_all())

## show create form - GET
@app.route("/opinions/add")
def add_opinion():
    return render_template("add_opinion.html")

## Process create - POST
@app.route('/opinions/add', methods=['POST'])
def create_opinion():
    if not Opinion.validate_create(request.form):
        return redirect('/opinions/add')
    opinion_data = {
        'movie_title' : request.form['movie_title'],
        'experience' : request.form['experience'],
        'date_watched' : request.form['date_watched'],
        'rating' : request.form['rating'],
        'user_id' : session['user_id']
    }
    Opinion.create_opinion(opinion_data)
    return redirect('/dashboard')

## Remaining get request
@app.route('/opinions/<int:id>')
def show_opinion(id):
    data = {
        'id' : id
    }
    return render_template("show_opinion.html", opinion = Opinion.get_one(data))

@app.route('/opinions/<int:id>/edit')
def edit_opinion(id):
    data = {
        'id' : id
    }
    return render_template("edit_opinion.html", opinion = Opinion.get_one(data))

@app.route("/opinions/<int:id>/delete")
def delete_opinion(id):
    data = {
        'id': id
    }
    return render_template("delete_opinion.html", opinion= Opinion.get_one(data))

## remaining POST request
@app.route("/opinions/<int:id>/update", methods=["POST"])
def update_opinion(id):
    if not Opinion.validate_opinion(request.form):
        return redirect(f"/opinions/{id}/edit")
    Opinion.update(request.form)
    return redirect(f"/opinions/{id}")

@app.route("/opinions/<int:id>/destroy", methods=["POST"])
def destroy_opinion(id):
    Opinion.destroy(request.form)
    return redirect("/dashboard") 