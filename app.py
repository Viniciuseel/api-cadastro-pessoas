from flask import Flask

app = Flask(__name__)


@app.route('/ping')
def ping():  # put application's code here
    return{"messge": "pong"}




if __name__ == '__main__':
    app.run(debug=True)


