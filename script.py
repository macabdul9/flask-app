
# #importing libraries
# import os
# import numpy as np
# import flask
# import pickle
# from flask import Flask, render_template, request

# #creating instance of the class
# app=Flask(__name__)

# #to tell flask what url shoud trigger the function index()
# @app.route('/')
# @app.route('/index')
# def index():
#     return flask.render_template('index.html')

# if __name__ == "__main__":
# 	port = int(os.environ.get("PORT", 5000))
# 	app.run(debug=True, port=port)

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
