from flask import Flask
"""starts a flask web application"""


app = Flask(__name__)


@app.route("/", strict_slashes=False)
@app.route("/home")
def home():
    """Returns the given string"""
    return ("<h1>Home Page</h1>")


@app.route("/about", strict_slashes=False)
def about():
    """Returns the given string"""
    return ("<h1>About Page</h1>")


if __name__ == "__main__":
    app.run(debug=True)