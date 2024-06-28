from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signdoctor')
def signdoctor():
    return render_template('signdoctor.html')

@app.route('/appointment')
def appointment():
    return render_template('appointment.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/medical')
def medical():
    return render_template('medical.html')

@app.route('/logindoctor')
def logindoctor():
    return render_template('logindoctor.html')

@app.route('/doctor')
def doctor():
    return render_template('doctor.html')


if __name__ == '__main__':
    app.run(debug=True)  # Use a different port, e.g., 8000

