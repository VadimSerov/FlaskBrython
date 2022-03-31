from flask import Flask, render_template

app = Flask(__name__)

menu = ["Установка","Первое приложение","Обратная связь"]

@app.route("/index")
@app.route("/")
def index() :
	try :
		s=render_template("index.html", title="Brython Flask L4" , menu= menu )
		return s
	except:
		return "page index not found"

@app.route("/about")
def about() :
	try :
		s=render_template("about.html")
		return s
	except:
		return "page about not found"


if __name__ == "__main__" :
	app.run(debug=True)

