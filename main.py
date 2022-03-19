from flask import render_template, Flask # flask

app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("home.html")

@app.route('/nasty/')
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
