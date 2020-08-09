# -----------------------------------------------------------------PORTRAY----------------------------------------------------------------------#


#                                                                       AUTHORS

#                                                       PRABHAV SINGH -> prabhavsingh55221@gmail.com
#                                                       RIDAM SRIVASTAVA -> ridam2k@gmail.com

#                                                                    TEAM ILLUMINATI


#__________________________________________________________________APPLICATION_______________________________________________________________

import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
import yake


'''
Setting up FLASK INSTANCE
'''
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
from main import predictor
from trends import articles

@app.route('/')
def home():
    '''
    Home Page
    '''
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    '''
    PREDICTOR
    '''

    int_features = [x for x in request.form.values()]
    choice = int_features[0]
    query = int_features[1]
    count = int(int_features[2])
    predictor(choice, query, count)

    top = pd.read_pickle('static/Sample_Results/TOP.pkl')
    bottom = pd.read_pickle('static/Sample_Results/BOTTOM.pkl')


    '''
    Using Custom Keyword Extractor to Load Keywords.
    '''

    top["Keywords"] = 'None'
    bottom["Keywords"] = 'None'
    language = "en"
    max_ngram_size = 1
    deduplication_thresold = 0.9
    deduplication_algo = 'seqm'
    windowSize = 1
    numOfKeywords = 2


    # FOR TOP
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_thresold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)
    for i in range(len(top)):
        if (top["Description"][i] == ''):
            top["Keywords"][i] = 'None'
            continue
        keywords = custom_kw_extractor.extract_keywords(top["Description"][i])
        if (len(keywords) == 0):
            top["Keywords"][i] = 'None'
            continue
        if (len(keywords) == 1):
            top["Keywords"][i] = str(keywords[0][0])
            continue
        top["Keywords"][i] = str(keywords[0][0]) + ', ' + str(keywords[1][0])

    # FOR BOTTOM
    for i in range(len(bottom)):
        if (bottom["Description"][i] == ''):
            bottom["Keywords"][i] = 'None'
            continue
        keywords = custom_kw_extractor.extract_keywords(bottom["Description"][i])
        if (len(keywords) == 0):
            bottom["Keywords"][i] = 'None'
            continue
        if (len(keywords) == 1):
            bottom["Keywords"][i] = str(keywords[0][0])
            continue
        bottom["Keywords"][i] = str(keywords[0][0]) + ', ' + str(keywords[1][0])

    return render_template('ecommresults.html', details = choice + ' - ' + query, top = top, bottom = bottom)

@app.route('/results',methods=['POST'])
def results():

    predictor('NORDSTROM', 'jeans')
    return

@app.route('/analyse',methods=['POST'])
def analyse():

    '''
    Analysis for articles.
    '''

    int_features = [x for x in request.form.values()]
    website = int_features[0]
    product = int_features[1]
    articles(website, product)

    top5 = pd.read_pickle('static/Sample_Results/top5articles.pkl')
    prods = pd.read_pickle('static/Sample_Results/top5prods.pkl')

    return render_template('inner-page.html', details = website + ' - ' + product, arts = top5, prods = prods)

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0')