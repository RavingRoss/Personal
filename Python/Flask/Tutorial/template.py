from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this is the HOME page"

@app.route("/<name>")
def user(name):
    return render_template("index.html", content=["tim", "joe", "bill"])

if __name__ == "__main__":
    app.run()