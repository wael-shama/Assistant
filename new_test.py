from flask import Flask, redirect, url_for, session, request
from flask_oauthlib.client import OAuth
import os
import secrets
import config

app = Flask("EASYUP")
app.secret_key = secrets.token_hex(16)

oauth = OAuth(app)

google = oauth.remote_app(
    'google',
    consumer_key=config.GOOGLE_CLIENT_ID,
    consumer_secret=config.GOOGLE_SECRET_ID,
    request_token_params={
        'scope': 'email profile'
    },
    base_url='http://127.0.0.1:5000',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)

# @app.route('/')
# def index():
#     if 'google_token' in session:
#         me = google.get('userinfo')
#         return 'Logged in as id=%s name=%s email=%s' % (me.data['id'], me.data['name'], me.data['email'])
#     else:
#         return redirect(url_for('login'))

# @app.route('/google/login')
# def login():
#     return google.authorize(callback=url_for('authorized', _external=True))

# @app.route('/google/auth')
# def authorized():
#     resp = google.authorized_response()
#     if resp is None:
#         return 'Access denied: reason=%s error=%s' % (
#             request.args['error_reason'],
#             request.args['error_description']
#         )
#     session['google_token'] = (resp['access_token'], '')
#     me = google.get('userinfo')
#     return 'Logged in as id=%s name=%s email=%s' % (me.data['id'], me.data['name'], me.data['email'])

# @app.route('/google/auth')
# def authorized():
#     resp = google.authorized_response()
#     if resp is None:
#         return 'Access denied: reason=%s error=%s' % (
#             request.args['error_reason'],
#             request.args['error_description']
#         )
#     session['google_token'] = (resp['access_token'], '')
#     me_response = google.get('userinfo', verify=False)
#     me_content = me_response.content
#     return 'Logged in as id=%s name=%s email=%s' % (me_content['id'], me_content['name'], me_content['email'])

# @app.route('/logout')
# def logout():
#     session.pop('google_token', None)
#     return redirect(url_for('index'))

# @google.tokengetter
# def get_google_oauth_token():
#     return session.get('google_token')

@app.route('/')
def index():
    if 'google_token' in session:
        me_response = google.get('userinfo')
        me_content = me_response.content
        return 'Logged in as id=%s name=%s email=%s' % (me_content['id'], me_content['name'], me_content['email'])
    else:
        return redirect(url_for('login'))

@app.route('/google/login')
def login():
    return google.authorize(callback=url_for('authorized', _external=True))

@app.route('/google/auth')
def authorized():
    resp = google.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['google_token'] = (resp['access_token'], '')
    me_response = google.get('userinfo', token=session['google_token'][0])
    me_content = me_response.content
    return 'Logged in as id=%s name=%s email=%s' % (me_content['id'], me_content['name'], me_content['email'])

@app.route('/logout')
def logout():
    session.pop('google_token', None)
    return redirect(url_for('index'))

@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')


if __name__ == '__main__':
    app.run()