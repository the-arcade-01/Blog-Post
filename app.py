from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

data = [
    {
        "author" : "Aashish",
        "title" : "One Down",
        "pages" : 300
    },
    {
        "author" : "Sreeraj",
        "title" : "One Up",
        "pages" : 299
    }
]

@app.route('/')
def index():
    return render_template('index.html',context = data)

@app.route('/login', methods=["POST","GET"])
def login():
    if request.method == "POST":
        # name = request.form["nm"]
        return redirect(url_for("user"))
    else:
        return render_template('login.html')

@app.route('/user')
def user():
    return render_template('user.html',name="Aashish")

if __name__ == "__main__":
    app.run(debug=True)