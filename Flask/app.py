from flask import Flask
from flask import render_template
from flask import request

credentials = {"huh445": "placeholder"}

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="Password Entering thingo")

@app.route('/about')
def about():
    return "This is the about page"

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    if credentials[username] == password:
        return f"Welcome {username}"
    else:
        return f'Hello, {username}, your username and password are incorrect'

if __name__ == "__main__":
    app.run(debug=True)