__author__ = 'mat'
from flask import Flask, render_template, url_for
from databaze import napeti_pole as napeti
from databaze import napln_db
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.tmpl')


@app.route('/clanky')
def clanky():
    napln_db()
    pole = napeti()
    return render_template('clanky.tmpl',pole=pole)

@app.route('/dokumentace')
def dokumantace():
    return render_template('dokumentace.tmpl')




if __name__ == '__main__':
    app.run(debug=True)
