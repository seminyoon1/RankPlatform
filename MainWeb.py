from flask import Flask, render_template, request, redirect, url_for
from testData.data import getData
import random

app = Flask(__name__)
arr = []
arrList = getData()

@app.route('/')
def index():
    dictItems = random.choice(list(arrList.items()))
    dictItems2 = random.choice(list(arrList.items()))
    #basic rendering, must be in the templates folder
    return render_template("home.html", arrItem = dictItems[0], 
                                        arrNum = dictItems[1], 
                                        arrItem2 = dictItems2[0], 
                                        arrNum2 = dictItems2[1], 
                                        comments=arr)
 
#app.route("variable name") correlates to the function, called from html button form action
@app.route('/text', methods=['GET', 'POST'])
def text():
    dictItems = random.choice(list(arrList.items()))
    dictItems2 = random.choice(list(arrList.items()))
    if request.method == "GET":
        return render_template("home.html", arrItem = dictItems[0], 
                                            arrNum = dictItems[1], 
                                            arrItem2 = dictItems2[0], 
                                            arrNum2 = dictItems2[1], 
                                            comments=arr)
    arr.append(request.form["text_input"])
    if request.method == "POST":
        #this gets the value from a html form
        value = request.form.get("text_input")
        print(value)
    return redirect(url_for('text'))

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    dictItems = random.choice(list(arrList.items()))
    dictItems2 = random.choice(list(arrList.items()))
    if request.method == "GET":
        return render_template("home.html", arrItem = dictItems[0], 
                                            arrNum = dictItems[1], 
                                            arrItem2 = dictItems2[0], 
                                            arrNum2 = dictItems2[1], 
                                            comments=arr)
    arr.clear()
    return redirect(url_for('reset'))
    
if __name__ == '__main__':
   app.run(debug=True)