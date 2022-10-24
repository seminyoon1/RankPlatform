from flask import Flask, render_template, request, redirect, url_for
from data import getData
import random

app = Flask(__name__)
arr = []
arrList = getData()

@app.route('/')
def index():
    itemss = random.choice(list(arrList.items()))
    #basic rendering, must be in the templates folder
    return render_template("home.html", arrItem = itemss[0], arrNum = itemss[1])
 
#app.route("variable name") correlates to the function, called from html button form action
@app.route('/text', methods=['GET', 'POST'])
def text():
    itemss = random.choice(list(arrList.items()))
    if request.method == "GET":
        return render_template("home.html", arrItem = itemss[0], arrNum = itemss[1], comments=arr)
    arr.append(request.form["text_input"])
    return redirect(url_for('text'))

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    itemss = random.choice(list(arrList.items()))
    if request.method == "GET":
        return render_template("home.html", arrItem = itemss[0], arrNum = itemss[1])
    arr.clear()
    return redirect(url_for('reset'))
if __name__ == '__main__':
   app.run(debug=True)