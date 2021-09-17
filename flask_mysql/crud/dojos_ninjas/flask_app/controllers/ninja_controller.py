from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/ninjas')
def new_ninja():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("add_ninja.html", all_dojos=dojos)

@app.route('/create/ninja', methods=['post'])
def create_ninja():
    data = {
        'first_name' : request.form['first_name'], 
        'last_name' : request.form['last_name'],
        'age' : request.form['age'],
        'dojo_id': request.form['dojo_id']}

    Ninja.save(data)

    return redirect(f"/dojos/{data['dojo_id']}")