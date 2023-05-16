from flask import Flask, redirect, request, session, render_template, url_for
# from google.oauth2 import id_token
# from google.auth.transport import requests


from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


import config
# from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = config.GOOGLE_SECRET_ID

# Define Google OAuth2 client ID
CLIENT_ID = config.GOOGLE_CLIENT_ID

# Define Google OAuth2 endpoint for token validation
GOOGLE_AUTH_ENDPOINT = 'https://oauth2.googleapis.com/tokeninfo'

@app.route('/')
def index():
    return render_template('index_4.html')


@app.route('/login', methods=['POST'])
def login():
    # Redirect the user to Google's sign-in page.
    client_id = config.GOOGLE_CLIENT_ID
    redirect_uri = 'http://127.0.0.1:5000/callback'
    # scope = 'openid email profile'
    # state = 'random-state-string'
    auth_url = f'https://accounts.google.com/o/oauth2/v2/auth?client_id={client_id}&redirect_uri={redirect_uri}'
    return redirect(auth_url)

@app.route('/callback')
def callback():
    # Handle the Google authorization response
    try:
        # Validate the authorization code and exchange it for a token
        token = id_token.verify_oauth2_token(
            request.args.get('code'),
            requests.Request(),
            CLIENT_ID
        )
        # Save the email address in the session
        session['email'] = token['email']
        return redirect(url_for('home'))
    except ValueError:
        # Handle an error while validating the token
        return 'Google authorization failed.'


@app.route('/home')
def home():
    # Get the user's email from session
    email = session.get('email')
    if email:
        return render_template('home.html', email=email)
    else:
        return redirect(url_for('index'))


def google_auth():
    # Generate the Google OAuth2 login URL
    url = f'https://accounts.google.com/o/oauth2/v2/auth?' \
          f'client_id={CLIENT_ID}&' \
          f'redirect_uri="127.0.0.1:5000"/callback&' \
          f'response_type=code&' \
          f'scope=email%20profile'
    return url


if __name__ == '__main__':
    app.run(debug=True)