from flask import Flask, render_template, request
import requests
import config
from flask import redirect

# Get your client ID and client secret from the Google Developer Console
CLIENT_ID = config.GOOGLE_CLIENT_ID
CLIENT_SECRET = config.GOOGLE_SECRET_ID

# Set the redirect URI to http://localhost:5000
REDIRECT_URI = "http://localhost:5000"

# Create a Flask application
app = Flask(__name__)

# Create a session object
session = requests.Session()

# Define a route for the login page
@app.route("/google/login")
def login():
    # Get the authorization URL
    authorization_url = "https://accounts.google.com/o/oauth2/auth?client_id={}&redirect_uri={}&scope=https://www.googleapis.com/auth/userinfo.email".format(CLIENT_ID, REDIRECT_URI)

    # Redirect the user to the authorization URL
    return redirect(authorization_url)

# Define a route for the callback page
@app.route("/google/auth")
def callback():
    # Get the authorization code from the request
    code = request.args.get("code")

    # Exchange the authorization code for an access token
    access_token_url = "https://accounts.google.com/o/oauth2/token?client_id={}&client_secret={}&code={}&redirect_uri={}".format(CLIENT_ID, CLIENT_SECRET, code, REDIRECT_URI)

    # Make the request to exchange the authorization code for an access token
    response = session.post(access_token_url)

    # Get the access token from the response
    access_token = response.json()["access_token"]

    # Use the access token to make requests to the Google API
    # For example, you can use the access token to get the user's email address
    user_info_url = "https://www.googleapis.com/oauth2/v3/userinfo?access_token={}".format(access_token)

    # Make the request to get the user's email address
    response = session.get(user_info_url)

    # Get the user's email address from the response
    user_email = response.json()["email"]

    # Store the user's email address in a session variable
    session["user_email"] = user_email

    # Redirect the user to the home page
    return redirect("/home")

# Define a route for the home page
@app.route("/home")
def home():
    # Get the user's email address from the session variable
    user_email = session.get("user_email")

    # Render the home page template with the user's email address
    return render_template("home.html", user_email=user_email)

if __name__ == "__main__":
    app.run(debug=True)