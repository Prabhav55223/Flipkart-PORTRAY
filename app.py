import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
from main import predictor
from trends import articles

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [x for x in request.form.values()]
    choice = int_features[0]
    query = int_features[1]
    predictor(choice, query)

    top = pd.read_pickle('static/Sample_Results/TOP.pkl')
    bottom = pd.read_pickle('static/Sample_Results/BOTTOM.pkl')

    return render_template('ecommresults.html', details = choice + ' - ' + query, top = top, bottom = bottom)

@app.route('/analyse',methods=['POST'])
def analyse():

    int_features = [x for x in request.form.values()]
    website = int_features[0]
    product = int_features[1]
    articles(website, product)

    top5 = pd.read_pickle('static/Sample_Results/top5articles.pkl')
    prods = pd.read_pickle('static/Sample_Results/top5prods.pkl')

    return render_template('inner-page.html', details = website + ' - ' + product, arts = top5, prods = prods)


@app.route('/results',methods=['POST'])
def results():

    predictor('NORDSTROM', 'jeans')
    return

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0')