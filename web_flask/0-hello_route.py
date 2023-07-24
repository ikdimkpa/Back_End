#!/usr/bin/python3
"""
Python script that starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)

# The code below displays "Hello HBNB!" when accessing the root URL
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

if __name__ == '__main__':
    # The code below runs the Flask app, listening on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)
