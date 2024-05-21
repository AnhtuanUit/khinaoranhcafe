from flask import Flask, request, redirect, render_template, session
from flask_session import Session

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
@login_required
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        # Set the session
        session["username"] = request.form.get("username")
        return redirect("/")

@app.route("/about")
def about():
    return apology("TODO")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any username
    session.clear()

    # Redirect user to login form
    return redirect("/")