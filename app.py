from flask import Flask, jsonify, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

df = pd.read_csv('survey.csv')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result')
def result():
    return render_template('result.html')


if __name__=='__main__':
    app.run()
