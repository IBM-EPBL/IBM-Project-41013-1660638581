from flask import Flask, render_template, request
app = Flask(__name__)

######################################################################################


@app.route("/display", methods=["GET", "POST"])
def display():
    if request.method == "POST":
        data = request.form
        return render_template("display.html",
         username=data['username'],
          email=data['email'],
           phone=data['phone'])
    return render_template("index.html")


@app.route('/')
def ass1():
  return render_template('index.html')


######################################################################################
if __name__ == "__main__":
  app.run(debug=True)