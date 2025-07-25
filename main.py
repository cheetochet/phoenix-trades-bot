nfrom flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    print("Hello my name is Chetan.")
    return jsonify({"Choo Choo": "Welcome to your Flask app chetan🚅"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
