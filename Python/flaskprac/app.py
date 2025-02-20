from flask import Flask, make_response, redirect, render_template, request, url_for, session
from markupsafe import escape

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['name']
        response = make_response(render_template('cookie.html'))
        response.set_cookie('userId', user)
        session['name'] = user
        return response

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userId')
    return f"hi {escape(name)}" 

@app.route('/hello/<name>')
def hellobro(name):
    return "hi %s "%name

@app.route('/admin')  # decorator for route(argument) function
def hello_admin():  # binding to hello_admin call
    return "admin"


@app.route('/guest/<guest>')
def hello_guest(guest):  # binding to hello_guest call
    return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':  # dynamic binding of URL to function
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))

if __name__=="__main__":
    app.debug = True
    app.run() 
    app.run(debug = True) 
