from flask import Flask, render_template, jsonify, request
from playfair import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/encrypt", methods=["POST"])
def encrypt():
    data = request.get_json()
    message = data.get('message', '')
    key = data.get('key', '').lower().split()
    matrix = build_matrix(key)
    encrypted_message = encrypt_message(message, matrix)
    return jsonify(
        key=' '.join(key),  # Join the key list back into a string
        original_message=message,
        encrypted_message=encrypted_message
    )

if __name__ == "__main__":
    app.run(debug=True)
