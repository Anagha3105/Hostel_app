from sqlite3.dbapi2 import Cursor
from flask import Flask, request, render_template, redirect
import os
import sqlite3

currentlocation = os.path.dirname(os.path.abspath(__file__))
myapp = Flask(__name__)


@myapp.route("/")
def homepage():
    return render_template("homepage.html")


@myapp.route("/", methods=["POST"])
def checklogin():
    UN = request.form['Username']
    PW = request.form["Password"]

    sqlconnection = sqlite3.Connection(currentlocation + "\Login.db")
    cursor = sqlconnection.cursor()
    query1 = "SELECT Username , Password From Users WHERE Username={UN} AND Password = {PW} "

    rows = Cursor.execute(query1)
    rows = rows.fetchall()
    if len(rows) == 1:
        return render_template("LoggedIn.html")
    else:
        return render_template("/register")


@myapp.route("/register", methods=["GET", "POST"])
def registerpage():
    if request.method == "POST":
        dUN = request.form["DUsername"]
        dPW = request.form["DPassword"]
        Uemail = request.form["EmalUser"]
        sqlconnection = sqlite3.Connection(currentlocation + "\Login.db")
        cursor = sqlconnection.cursor()
        query1 = "INSERT INTO Users VALUES('{dUN}','{dPW}', '{Uemail}')"
        cursor.execute(query1)
        sqlconnection.commit()
        return redirect("/")
    return render_template("Register.html")


if __name__ == "__main__":
    myapp.run()
