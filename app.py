from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/home")
def home():
	return render_template('index.html')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/locations")
def locations():
	return render_template('locations.html')

@app.route("/menu")
def menu():
	return render_template('menu.html')\

@app.route("/staff")
def staff():
	return render_template('staff.html')
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', debug = True)
