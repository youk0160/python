from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/welcome')
def welcome():
    if not 'first_name'in session:
        return redirect('/')
    return render_template("welcome.html", f_name=session['first_name'])

@app.route('/register', methods=['post'])
def register():
    if not User.validate_user(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['pwd'])
    data = {
        'first_name' : request.form['first_name'], 
        'last_name' : request.form['last_name'], 
        'email' : request.form['email'],
        'pwd' : pw_hash, 
    }
    User.save(data)
    session['first_name'] = request.form['first_name']
    return redirect('/welcome')

@app.route('/login', methods=['POST'])
def login():
    data = { "email" : request.form["email"] }
    user = User.get_by_email(data)

    if not user or not bcrypt.check_password_hash(user.pwd, request.form['pwd']):
        flash("Invalid Email/Password", 'login')
        return redirect("/")

    session['first_name'] = user.first_name
    return redirect("/welcome")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
