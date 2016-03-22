from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    ## example of rendering a template and passing in data
    country = {"name": "USA", "population":"999999", "capitol":"Washington, DC"}
    return render_template("index.html", country = country)

if __name__ == "__main__":
    app.run()