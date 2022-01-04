from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {'first_name' : 'Richard', 'last_name' : 'Liek'},
        {'first_name' : 'Pierome', 'last_name' : 'Sar'},
        {'first_name' : 'Graham', 'last_name' : 'Brown'},
        {'first_name' : 'Jared', 'last_name' : 'Plante'}
    ]
    return render_template("index.html",users=users)



if __name__=="__main__":
    app.run(debug=True)