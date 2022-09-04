from random import randint
from flask import Flask
app = Flask(__name__)


@app.route("/random")
def random():
    random_number = randint(1, 10)
    return {'random': random_number}


if __name__ == "__main__":
    app.run(host='127.0.0.0', debug=True, port=5000)
