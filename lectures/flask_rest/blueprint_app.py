from blp.test import hello
from flask import Flask


app = Flask(__name__)

app.register_blueprint(hello)

if __name__ == '__main__':
    app.run(debug=True)
