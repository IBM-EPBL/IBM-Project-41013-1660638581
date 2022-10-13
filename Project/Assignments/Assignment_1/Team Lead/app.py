import random, datetime, time, requests
from flask import Flask, render_template, request
app = Flask(__name__)

######################################################################################


@app.route("/display", methods=["GET", "POST"])
def display():
    if request.method == "POST":
        data = request.form
        return render_template("ass1/display.html",
         username=data['username'],
          email=data['email'],
           phone=data['phone'])
    return render_template("ass1/index.html")


@app.route('/')
def ass1():
  return render_template('ass1/index.html')


######################################################################################
if __name__ == "__main__":
  app.run(debug=True)