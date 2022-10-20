from flask import Flask, render_template, request
app = Flask(__name__, template_folder='views')

######################################################################################


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
      data = request.form

      username=data['username']
      pw=data['pw']
      
      correct = 1 
      
      #check db data
      
      if correct:
        return render_template("welcome.html")

    return render_template("login.html")

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route('/', methods=["GET", "POST"])
def reg():
  if request.method == "POST":
    data = request.form

    email=data['email']
    username=data['username']
    roll=data['roll']
    pw=data['pw']

    #update deails to db2

    return render_template("login.html")
  return render_template("welcome.html")


######################################################################################
if __name__ == "__main__":  
  app.run(debug=True)