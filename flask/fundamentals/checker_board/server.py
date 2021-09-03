from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def default_board():
    return render_template("index.html", row=8, col=8)	# notice the 2 new named arguments!

@app.route('/<y>')
def dyn_width_board(y):
    return render_template("index.html", row=8, col=int(y))

@app.route('/<x>/<y>')
def custom_board(x,y):
    return render_template("index.html", row=int(x), col=int(y))

if __name__=="__main__":
    app.run(debug=True)

