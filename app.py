from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "This subdomain is takenover by Cybrik"
