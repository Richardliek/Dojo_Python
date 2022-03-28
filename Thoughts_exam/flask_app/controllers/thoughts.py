from crypt import methods
from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.thought import Thought
from flask_app.models.user import User


@app.route('/dashboard')
def thoughts():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('dashboard.html',user=User.get_by_id(data), thoughts=Thought.get_all())

@app.route('/thoughts/add',methods=["POST"])
def add_thought():
    thought_data = {
        'thought' : request.form['thought'],
        'user_id' : session['user_id']
    }
    Thought.add_thought(thought_data)
    return redirect('/dashboard')
