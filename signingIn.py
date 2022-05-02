from flask import Flask
app = Flask(__name__)
MyCrypt=encrpython()
@app.route("/")
def index():
    return render_template('index.html')
if __name__ == "__main__":
     app.run()
