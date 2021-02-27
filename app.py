from flask import Flask, redirect, render_template
from flask_nav import Nav
from flask_nav.elements import Navbar,Subgroup,View,Link,Text,Separator
app = Flask(__name__)
nav = Nav(app)
nav.register_element('navbar',Navbar('mynav' , View('Home','index')))


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
