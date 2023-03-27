from flask import Flask, render_template, url_for
"""starts a flask web application"""


app = Flask(__name__)


# dummy data for testing
articles = [
    {
        'author': 'Kara Danvers',
        'title': 'Article 1',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias illo, eveniet odio quasi eaque sed voluptatum ducimus earum molestiae voluptates',
        'date_created': 'Jan 20, 2023'
    },
    {
        'author': 'James Olsen',
        'title': 'Article 2',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti doloribus dolorum quia. Ea esse excepturi blanditiis quas ullam, quae sed temporibus, ab a, magni deleniti.',
        'date_created': 'Feb 14, 2023'
    }
]

@app.route("/", strict_slashes=False)
@app.route("/home")
def home():
    """Returns the given page"""
    return render_template('home.html', articles=articles)

@app.route("/project_log", strict_slashes=False)
def project_log():
    """Returns the given page"""
    return render_template('project_log.html', title='Project Logs', articles=articles)

@app.route("/about", strict_slashes=False)
def about():
    """Returns the given page"""
    return render_template('about.html', title='About')


if __name__ == "__main__":
    app.run(debug=True)