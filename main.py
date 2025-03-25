import flask


# TODO: change this to your academic email
AUTHOR = "mkhosla@seas.upenn.edu"


app = flask.Flask(__name__)


# This is a simple route to test your server


@app.route("/")
def hello():
    return f"Hello from my Password Validator! &mdash; <tt>{AUTHOR}</tt>"


# This is a sample "password validator" endpoint
# It is not yet implemented, and will return HTTP 501 in all situations


@app.route("/v1/checkPassword", methods=["POST"])
def check_password():
    data = flask.request.get_json() or {}
    pw = data.get("password", "")

    # FIXME: to be implemented
    uppercase = sum(1 for c in pw if c.isupper())
    digit = sum(1 for c in pw if c.isdigit())
    special = sum(1 for c in pw if c in '!@#$%^&*')

    if len(pw) < 8:
        return flask.jsonify({"valid": False, "reason": "Too short"}), 501
    if uppercase < 2:
        return flask.jsonify({"valid": False, "reason": "Not enough Upper Case Letters"}), 501
    if digit < 2:
        return flask.jsonify({"valid": False, "reason": "Not enough Digits"}), 501
    if special < 1:
        return flask.jsonify({"valid": False, "reason": "No special character"}), 501
    return flask.jsonify({"valid": True, "reason": "Password is Good"}), 200

