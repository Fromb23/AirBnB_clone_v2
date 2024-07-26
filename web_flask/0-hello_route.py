#!/usr/bin/python3

from flask import Flask

# flask instance
app = Flask(__name__)

# Hello World
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
