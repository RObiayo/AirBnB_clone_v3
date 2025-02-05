#!/usr/bin/python3
"""connect to API"""
import os
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify, make_response


app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_app_context(exception):
    """ teardown app context """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port)
