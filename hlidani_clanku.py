__author__ = 'mat'
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.tmpl')


@app.route('/clanky')
def clanky():
    return render_template('clanky.tmpl')

@app.route('/dokumentace')
def dokumantace():
    return render_template('dokumentace.tmpl')




if __name__ == '__main__':
    app.run(debug=True)
