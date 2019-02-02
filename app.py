from flask import Flask, jsonify, render_template, request,redirect,flash
import pandas as pd
import numpy as np
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)
df = pd.read_csv('survey.csv')


@app.route('/')
def base():
    return render_template('main.html')


@app.route('/index')
def index():
    return render_template('index.html')



# def filter_route():
#     return render_template('filter.html')
#
# def filter():
#     params = request.get_json()
#     return jsonify(filterfunc(params, df2))


if __name__=='__main__':
    app.run()
