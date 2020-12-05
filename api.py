"""This script handles setup of the sudoku api.
"""

import flask
from flask import jsonify

APP = flask.Flask(__name__)
APP.config["DEBUG"] = True

HEALTH = {
    "status": "UP"
}

@APP.route('/', methods=['GET'])
def health():
    """Serves a JSON object indicating that API is active.
    """

    return jsonify(HEALTH)

APP.run()
