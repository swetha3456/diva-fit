from flask import Flask, render_template, session, url_for, redirect, request, flash
from dbfunctions import *
import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

app = Flask(__name__)
app.secret_key = b"030a8ee0eb274b3e7fd9db490b0fd6a532b1fa1f1fd6825c5852c7363358c4b6"

@app.route("/")
def about():
    return render_template("about.html")

@app.route("/home")
def home():
    if "username" not in session:
        return redirect(url_for("login"))

    return render_template("userhome.html")

@app.route("/calendar")
def calendar():
    if "username" not in session:
        return redirect(url_for("login"))

    return render_template("calendar.html")

@app.route("/exercise")
def exercise():
    if "username" not in session:
        return redirect(url_for("login"))

    return render_template("exercises.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        if authenticate_user(request.form["username"], request.form["password"], cur):
            session["username"] = request.form["username"]
            print(request.form["username"])
        else:
            flash("Invalid credentials")

        return redirect(url_for("home"))

    return render_template("login.html")

@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        return redirect(url_for("home"))

    return render_template("signin.html")

if __name__ == "__main__":
    app.run(debug=True)