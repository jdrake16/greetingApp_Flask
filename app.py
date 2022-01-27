from flask import Flask, render_template, request, flash

#creates class for the app
app = Flask(__name__)
app.secret_key = "manbearpig"


@app.route("/hello")

def index():
	flash("What's your name?")
	return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
	flash("Hi " + str(request.form['name_input']) + ", good to see ya!")
	return render_template("index.html")
	


