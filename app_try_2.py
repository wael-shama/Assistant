from flask import Flask, render_template, redirect, url_for, session, request
from google.oauth2 import id_token
from google.auth.transport import requests
import os
import config

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", default="fallback")

client_config = {
    "web": {
        "client_id": config.GOOGLE_CLIENT_ID,
        "project_id": "your-project-id",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_secret": config.GOOGLE_SECRET_ID,
        "redirect_uris": ["http://127.0.0.1:5000/login/callback"]
    }
}

@app.route('/')
def index():
    return render_template('index_4.html')

@app.route('/login_page')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # Redirect the user to Google's sign-in page.
    client_id = config.GOOGLE_CLIENT_ID
    redirect_uri = 'http://127.0.0.1:5000/callback'
    scope = 'openid email profile'
    state = 'random-state-string'
    auth_url = f'https://accounts.google.com/o/oauth2/v2/auth?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&state={state}&response_type=code'
    return redirect(auth_url)


# @app.route('/callback')
# def callback():
#     # Handle the Google authorization response
#     try:
#         # Get the authorization code from the response
#         auth_code = request.args.get('code')

#         # Exchange the authorization code for an access token
#         credentials = google_auth.credentials_from_clientinfo(
#             client_config,
#             scopes=['https://www.googleapis.com/auth/userinfo.email'],
#             code=auth_code)

#         # Get the user's email address from the access token
#         userinfo = google_auth.get_userinfo(credentials)
#         email = userinfo['email']

#         # Store the user's email in the session
#         session['email'] = email

#         return redirect(url_for('home'))

#     except Exception as e:
#         print(str(e))
#         return redirect(url_for('index'))

@app.route('/callback')
def callback():
    # Verify Google authentication response
    # token = request.args.get('token')
    print(request.form)

    try:
        # Specify the CLIENT_ID of the app that accesses the backend:
        # print("ALLL IS GOOOOOD" + token)
        # idinfo = id_token.verify_oauth2_token(token, requests.Request(), config.GOOGLE_CLIENT_ID)

        # print(idinfo)
        # Check that the user has signed in with the correct Google account
        # if idinfo['email'] != session['email']:
            # raise ValueError('Wrong email address')

        # Store the user's ID token in session
        # session['id_token'] = token

        return redirect(url_for('home'))
    except ValueError as e:
        # Invalid token
        return str(e), 400
    
@app.route('/home')
def home():
    # Get the user's email from session
    email = session.get('email')
    print("EMAAAAAAILLLLLL" + email)
    print(session)
    if email:
        return render_template('home.html', email=email)
    else:
        return redirect(url_for('index'))


# @app.route('/callback')
# def callback():
#     # Handle the Google authorization response
#     try:
#         # Verify the ID token
#         id_token = request.form['id_token']
#         id_info = id_token.verify_oauth2_token(id_token, requests.Request())
#         if id_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
#             raise ValueError('Invalid issuer')

#         # Store the user ID in the session
#         session['user_id'] = id_info['sub']

#         # Redirect to the home page
#         return redirect(url_for('home'))

#     except ValueError as e:
#         # Handle any errors
#         return 'Error: {}'.format(e)
    
# # @app.route('/callback')
# # def callback():
# #     # Handle the Google authorization response
    
# #     return redirect(url_for('home'))

# @app.route('/home')
# def home():
#     # Get the user's email from session
#     print(session)
#     email = session.get('email')
#     if email:
#         return render_template('home.html', email=email)
#     else:
#         return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
