from flask import Flask, jsonify, render_template, request,redirect,flash
import pandas as pd
import numpy as np
from flask_cors import CORS, cross_origin
import json

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


@app.route('/filter', methods=['POST'])
def filter_spec():
    params = json.loads(request.get_json())
    for attrib in params:
        params[attrib] = int(params[attrib])*0.4
    df2=df
    print(df2.shape)
    for attrib in params:
        print(attrib)
        df2 = df2[df2[attrib]<params[attrib]+0.5]
        df2 = df2[df2[attrib]>params[attrib]-0.5]
    dogList = set(df2['Breed'])
    print(dogList)
    return render_template('filter.html', msg = dogList)


    # df1 = df.groupby("BreedEntity").agg({key: "mean" for key in list(df)[2:]})
    # return jsonify(filterfunc(params, df1))


if __name__=='__main__':
    app.run()
