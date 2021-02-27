from flask import Flask, render_template
from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, View, Link, Text, Separator

app = Flask(__name__)
nav = Nav(app)

nav.register_element('my_navbar', Navbar("thenav", View('Home Page', 'index')))


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
