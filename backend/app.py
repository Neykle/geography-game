from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Geography Game API is running!"

@app.route("/api/message")
def message():
    return jsonify({
        "message": "Hello from Flask!"
    })

if __name__ == "__main__":
    app.run(debug=True)