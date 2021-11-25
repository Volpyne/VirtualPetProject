from flask import Flask, request, redirect, url_for
from flask import render_template
from web.services import authentication


app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if not authentication.validate_credentials(request.form['login'], request.form['password']):
            error = 'invalid credentials'
        else:
            return redirect(url_for('start'))
    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        if not authentication.create_user(request.form['login'], request.form['password'], request.form['mail']):
            error = 'User could not be created'
        else:
            return redirect(url_for('start'))
    return render_template('register.html', error=error)

@app.route('/start')
def start():
    users =authentication.obtain_users()
    return render_template('start.html', users=users)

@app.route('/diary', methods=['GET', 'POST'])
def diary():
    error = None
    if request.method == 'POST':
        if not authentication.create_diary(request.form['name']):
            error = 'Diary could not be created'
        else:
            return redirect(url_for('diary'))
    return render_template('diary.html', error=error)

if __name__ == '__main__':
    app.debug = True
    app.run(port=5002)


