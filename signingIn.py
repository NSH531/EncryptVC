from flask import Flask
app = Flask(__name__)
MyCrypt=encrpython()
@app.route("/")
def index():
     return "Welcome to Codez Up"
if __name__ == "__main__":
     app.run()
