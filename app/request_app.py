#!/usr/bin/python
"""
    Sript that starts a Flask web application
 """
from flask import Flask, request, jsonify
from datetime import datetime
import logging
import os
import sys

app = Flask(__name__)


host = os.getenv('HOST', '0.0.0.0')
port = os.getenv('PORT', 5000)


@app.route("/", methods=["GET", "POST"])
def check_headers():
    """
    Function to check Accept Headers
    Returns message depending on Accept Headers in GET Request
    """
    if request.method == "GET":
        if request.headers.get("Accept") == "application/json":
            create_logger()
            return '{"message": "Good morning"}'
        else:
            create_logger()
            return "<p>Hello, World</p>"
    elif request.method == "POST":
        create_logger()
        return "This is a POST request"


def create_logger():
    """
    Creates log for each request made on the Debug log level
    Log in dict format: {timestamp: request url}
    """
    timestamp = str(datetime.now())
    request_url = str(request.url)
    logging.basicConfig(level=logging.DEBUG)
    logging.debug({timestamp: request_url})


if __name__ == '__main__':
    app.run(host=host, port=port)
