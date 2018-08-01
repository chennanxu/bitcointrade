from flask import jsonify
from ..libs.api import API
from .. import app


@app.route('/api/ticker/')
def ticker():
    return jsonify(API.get_trade())

