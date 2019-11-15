from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

post = [
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
    return render_template('index.html',context = post)

if __name__ == "__main__":
    app.run(debug=True)