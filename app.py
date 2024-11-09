from flask import Flask, jsonify, request

app = Flask(__name__)

visitors_count = 0


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/visitors", methods=["GET"])
def get_visitors():
    return f"Total visitors: {visitors_count}"


@app.route("/visit", methods=["POST"])
def visit():
    global visitors_count
    username = request.form.get("username")
    if username:
        visitors_count += 1
        return jsonify({"message": f"Welcome, {username}!"}), 200
    else:
        return jsonify({"error": "No username provided!"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
