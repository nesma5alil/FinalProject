from flask import Flask , render_template ,request
app = Flask(__name__)



@app.route("/")
def website():
	return render_template ("home.html")
@app.route("/about")
def About():
	return render_template ("about.html")
@app.route("/contactus")
def contactUs():
	return render_template ("FP.html")
@app.route("/howtoapply")
def applyy():
	return render_template ("apply.html")
		

if __name__=="__main__":
	app.run(port=4053, debug=True)
	