from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    total_fruits = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    print(request.form)
    print(f"Charging {request.form['first_name']} {request.form['last_name']} for {total_fruits} fruits")
    return render_template("checkout.html", f_name=request.form["first_name"], l_name=request.form["last_name"], stud_id=request.form["student_id"], str_berry=request.form["strawberry"], ras_berry=request.form["raspberry"], apple=request.form["apple"])

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    