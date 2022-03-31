from flask import Flask


app = Flask(__name__)

@app.route("/index")
@app.route("/")
def index() :
	try :
		f=open("index.html")
		s=f.read()
		f.close()
		return s[s.find("<"):]
	except:
		return "page not found"

@app.route("/about")
def about() :
	return "<h1>О сайте</h1>"



if __name__ == "__main__" :
	app.run(debug=True)

