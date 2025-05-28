from flask import Flask, request, render_template
from .ats_scanner import ats_scanner, ats_score

app = Flask(__name__)


@app.route('/')
def hello():
    """
    Landing page for the web application
    TODO: create a template for the landing page, and rename the function
    """
    return 'Hello, welcome to ATS-Maxxer, your CV will be' \
        ' a diamond in the rough!'


@app.route('/about')
def about():
    """
    About page for the web application
    TODO: style the template for the about page
    """
    return render_template('about.html')


@app.route('/scanner', methods=['GET', 'POST'])
def scanner():
    """
    Scans through a text looking for keywords and returning the number of keywords
    TODO: Style the template
    """
    if request.method == 'POST':
        text = request.form['text']
        keyword_count = ats_scanner(text)

        return str(ats_score(keyword_count))
    else:
        return render_template('text-evaluator.html')


if __name__ == '__main__':
    app.run()
