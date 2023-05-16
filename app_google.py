from flask import Flask, redirect, request, jsonify
from google.oauth2 import id_token
from google.auth.transport import requests
import config

app = Flask(__name__)
app.secret_key = 'super-secret-key'

@app.route('/login')
def login():
    # Redirect the user to Google's sign-in page.
    client_id = config.GOOGLE_CLIENT_ID
    redirect_uri = 'http://127.0.0.1:5000/callback'
    scope = 'openid email profile'
    state = 'random-state-string'
    auth_url = f'https://accounts.google.com/o/oauth2/v2/auth?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&state={state}&response_type=code'
    return redirect(auth_url)

@app.route('/callback')
def callback():
    # Exchange the authorization code for an access token and ID token.
    client_id = config.GOOGLE_CLIENT_ID
    client_secret = config.GOOGLE_SECRET_ID
    redirect_uri = 'http://127.0.0.1:5000/callback'
    code = request.args.get('code')
    token_url = 'https://oauth2.googleapis.com/token'
    token_params = {
        'code': code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code',
    }
    response = requests.post(token_url, data=token_params).json()
    access_token = response['access_token']
    id_token = response['id_token']
    
    # Verify the ID token and get the user's email address and name.
    id_info = id_token.verify_oauth2_token(id_token, requests.Request(), client_id)
    email = id_info['email']
    name = id_info['name']

    # TODO: Authenticate the user in your app and redirect to the appropriate page.

if __name__ == '__main__':
    app.run(debug=True)