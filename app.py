from flask import Flask, render_template, jsonify, request
  
app = Flask(__name__)
@app.route('/')
def index():
   return render_template("index.html")
  
@app.route('/my_form', methods=['POST'])
def my_form():
    form_input = request.form['comment_content']
    # Now that get value back to server can send it to a DB(use Flask-SQLAlchemy)
    return(form_input)
 
if __name__ == '__main__':
   app.run(debug=True)