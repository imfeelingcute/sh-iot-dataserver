from flask import Flask

app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.debug = True
    app.run(server="10.25.16.163:5000")
