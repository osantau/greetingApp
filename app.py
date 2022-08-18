from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ba4f91591e22c2ae8dfc3527eb548d772e209ee431885815482463fb798617cd'

@app.route("/hello")
def index():
    flash("what's your name ?")
    return render_template("index.html")

@app.route("/greet", methods=["POST","GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) +", great to see you !")
    return render_template("index.html")