from flask import Flask, render_template, request, redirect, url_for
  
app = Flask(__name__)
arr = []
@app.route('/')
def index():
   return render_template("home.html")
 
@app.route('/text', methods=['GET', 'POST'])
def text():
    if request.method == "GET":
        return render_template("home.html", comments=arr)   
    arr.append(request.form["text_input"])
    return redirect(url_for('text'))

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    if request.method == "GET":
        return render_template("home.html")
    arr.clear()
    return redirect(url_for('reset'))
if __name__ == '__main__':
   app.run(debug=True)