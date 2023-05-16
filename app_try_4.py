from flask import Flask, render_template, redirect, url_for, session
from google.oauth2 import id_token
from google.auth.transport import requests
import os
import config

app = Flask(__name__)

# Set the secret key to enable session
app.secret_key = config.GOOGLE_SECRET_ID

# Set the client ID for Google Sign-In
app.config['GOOGLE_CLIENT_ID'] = config.GOOGLE_CLIENT_ID

# Set the redirect URI for Google Sign-In callback
app.config['GOOGLE_REDIRECT_URI'] = config.GOOGLE_REDIRECT_URI

@app.route('/')
def index():
    if 'email' in session:
        return 'Logged in as ' + session['email'] + '<br>' + \
               '<a href="/logout">Logout</a>'
    else:
        return render_template('index_4.html')

@app.route('/login')
def login():
    # Render the login button
    return render_template('login.html', client_id=app.config['GOOGLE_CLIENT_ID'])

@app.route('/callback')
def callback():
    # Verify the Google Sign-In response and get the user's email
    token = requests.args.get('token')
    try:
        # Verify the ID token using the Google Sign-In API
        idinfo = id_token.verify_oauth2_token(token, requests.Request(),
                                              app.config['GOOGLE_CLIENT_ID'])

        # If multiple clients access the backend server:
        if idinfo['aud'] not in [app.config['GOOGLE_CLIENT_ID']]:
            raise ValueError('Could not verify audience.')

        # Check that the user's email is verified
        if idinfo['email_verified']:
            email = idinfo['email']
            session['email'] = email
            return redirect(url_for('home'))
        else:
            return 'User email not available or not verified by Google.', 400

    except ValueError:
        # Invalid token
        return 'Invalid token', 400

@app.route('/home')
def home():
    # Get the user's email from session
    email = session.get('email')
    if email:
        return render_template('home.html', email=email)
    else:
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    # Clear the session and redirect to the index page
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)