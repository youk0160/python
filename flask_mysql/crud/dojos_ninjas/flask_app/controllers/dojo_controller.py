from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo

@app.route('/dojos')
def index():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("index.html", all_dojos=dojos)


@app.route('/dojos/<int:id>')
def one_dojo(id):
    data = {
        "dojo_id" : id
    }
    one_dojo = Dojo.find_dojo(data)
    print(one_dojo)
    return render_template("one_dojo.html", dojo = one_dojo)

@app.route('/create/dojo', methods=['post'])
def create_dojo():
    data = {'name' : request.form['name']}
    Dojo.save(data)
    return redirect('/dojos')