import sqlite3 as sql

from model import *

from flask import Flask, render_template, request, redirect, jsonify


app = Flask(__name__)


#home
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('loginnew.html')
    else:
        return render_template('home.html')

@app.route('/login', methods=['POST'])
def dologin():
    if checklogin(request.form['id_user'],request.form['password']):
        session['logged_in'] = True
        return render_template('home.html')
    else:
        flash ('wrong password!')
        return render_template('loginnew.html')
        return redirect('/')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return home()


@app.route('/alphabet')
#@login_required
def alpha():
    return render_template ('alphabet.html')


@app.route('/numbering')
#@login_required
def new():
    return render_template('numbering.html')

@app.route('/greeting')
def greeting():
    return render_template('greeting.html')

@app.route('/salamsejahtera')
def greeting1():
    return render_template('salamsejahtera.html')

@app.route('/terimakasih')
def greeting2():
    return render_template('terimakasih.html')

@app.route('/maaf')
def greeting3():
    return render_template('maaf.html')

@app.route('/tolong')
def greeting4():
    return render_template('tolong.html')

@app.route('/quiz')
def quizz():
    return render_template('quiz.html')


if __name__=='__main__':
    app.secret_key = "!mzo53678912489"
    app.run(debug=True,host='0.0.0.0', port=4000)
