from flask import Flask, render_template, redirect, request, session
app=Flask(__name__)
app.secret_key="this is secret"

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/process', methods=['post'])
def save_form():
    session['name']=request.form['name']
    session['dojo_loc']=request.form['dojoLocat']
    session['fav_lang']=request.form['favLang']
    session['comment']=request.form['comment']
    return redirect('/result')

@app.route('/result')
def show_result():
    return render_template('result.html')

if __name__=="__main__":
    app.run(debug=True)