from flask import Flask, render_template, request, redirect, session # added request
from user import User
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("read.html", all_users=users)


@app.route('/add_page')
def add_pg():
    return render_template("create.html")

@app.route('/create', methods=['post'])
def create():
    data = {'f_name' : request.form['f_name'], 'l_name' : request.form['l_name'], 'email' : request.form['email']}
    User.create_user(data)
    return redirect('/')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
