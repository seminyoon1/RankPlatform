from flask import Flask, render_template, request, redirect, url_for
from testData.data import getData
from FlaskConnector import getDictItems

app = Flask(__name__)
arr = []

#if you have AWS working: comment this line and uncomment out lines labeled in the functions
#arrDict = list(getData().items())

userAccount = False #needed for account testing
voted = False

@app.route('/')
def index():
    #basic rendering, must be in the templates folder

    #comment out
    arrDict = list(getDictItems(2).items())

    #arrDict1 = list(getDictItems(3).items())
    #arrDict2 = list(getDictItems(4).items())
    if voted == True:
        return redirect(url_for('vote'))
    return render_template("home.html", arrItem = arrDict[0][0], 
                                        arrNum = arrDict[0][1], 
                                        arrItem2 = arrDict[1][0], 
                                        arrNum2 = arrDict[1][1], 
                                        comments=arr)
 
#app.route("variable name") correlates to the function, called from html button form action
@app.route('/vote', methods=['GET', 'POST'])
def vote():
    global voted
    if request.method == "POST":
        # request.form['vote'] = the element use has chosen
        if voted == False and request.form['vote'] != "You must wait.":
            voted = True
            return render_template("home.html", arrItem = "You have voted!", arrItem2 = "You have voted!")
        else:
            return redirect('/')
    elif voted == True:
        voted = False
        return render_template("home.html", arrItem = "You must wait.", arrItem2 = "You must wait.")
    return redirect('/')

@app.route('/text', methods=['GET', 'POST'])
def text():

    #comment out
    arrDict = list(getDictItems(2).items())

    if request.method == "GET":
        return render_template("home.html", arrItem = arrDict[0][0], 
                                            arrNum = arrDict[0][1], 
                                            arrItem2 = arrDict[1][0], 
                                            arrNum2 = arrDict[1][1], 
                                            comments=arr)
    arr.append(request.form["text_input"])
    if request.method == "POST":
        #this gets the value from a html form
        value = request.form.get("text_input")
        print(value)
    return redirect(url_for('text'))

@app.route('/reset', methods=['GET', 'POST'])
def reset():

    #comment out (idk if its useful)
    #arrDict = list(getDictItems(2).items())

    if request.method == "GET":
        return render_template("home.html")
    #    return render_template("home.html", arrItem = arrDict[0][0], 
    #                                        arrNum = arrDict[0][1], 
    #                                        arrItem2 = arrDict[1][0], 
    #                                        arrNum2 = arrDict[1][1], 
    #                                        comments=arr)
    arr.clear()
    return redirect(url_for('reset'))
    
if __name__ == '__main__':
   app.run(debug=True)