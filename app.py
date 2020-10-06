from flask import Flask, jsonify, render_template
from db import Database

app = Flask(__name__)
# to allow for debugging and auto-reload
app.config['FLASK_ENV'] = "development"
# app.config['DEBUG'] = True

db = Database('cpu_loads.db')
db.create()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/cpu-load')
@app.route('/cpu-load/')
def load_show_last_10():
    history = db.get_last()
    return render_template('load-history.html',
                           history=history,
                           length=len(history))


@app.route('/cpu-load/last/<quantity>')
def load_show_last_n(quantity):
    history = db.get_last(quantity)
    return render_template('load-history.html',
                           history=history,
                           length=len(history))


@app.route('/cpu-load/in-last/<quantity>/<time_period>')
def load_show_time_period(quantity=1, time_period="minutes"):
    history = db.get_in_last(quantity, time_period)
    return render_template('load-history.html',
                           history=history,
                           length=len(history))




if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
