from flask import Flask, jsonify, render_template, request,redirect,flash
import pandas as pd
import numpy as np
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)
df = pd.read_csv('survey.csv')


def filterfunc(fltparam,df):
    for param in fltparam:
        df = df[df[param] < float(fltparam[param]) + 2]
        df = df[float(fltparam[param]) - 2 < df[param]]
    return len(df)


@app.route('/')
def base():
    return render_template('main.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/index', methods=['POST'])
def filter_spec():
    params = request.get_json()
    print("in python function")
    print(params)
    return params


    # df1 = df.groupby("BreedEntity").agg({key: "mean" for key in list(df)[2:]})
    # return jsonify(filterfunc(params, df1))


if __name__=='__main__':
    app.run()
