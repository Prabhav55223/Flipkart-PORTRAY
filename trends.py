import nltk
import os
from datetime import datetime
import warnings
import gc
import sys
import urllib.request
import pandas as pd
import time 
import json
import glob
import pickle
import random
from pathlib import Path
import editdistance
import string
from sklearn.preprocessing import MinMaxScaler
import io
import itertools
import networkx as nx
import re
import networkx
from rake_nltk import Rake
from nltk.tokenize import word_tokenize, sent_tokenize
import numpy as np
import numpy as np
import pandas as pd
import itertools
from tqdm import tqdm

apparel= {
    'tshirt' : ['tee', 'tshirt', 'T-shirt',' t shirt', 'teeshirt'],
    'footwear' : ['shoes', 'sandal', 'sandals', 'shoes', 'footwear', 'slipper','Croc', 'Sandals'],
    'jewellery' : ['jewellery'],
    'dress' : ['dress', 'dresses', 'sundress', 'sundresses'],
    'skirt': ['skirt', 'skirts', 'maxi'],
    'bag': ['bag', 'bags', 'purse', 'purses', 'wallet', 'wallets']
}

def normal(tagged):
    return [(item[0].replace('.', ' '), item[1]) for item in tagged]

def filter_for_tags(tagged, tags=['NNP']):
    """Semantic Filter Based on POS."""
    return [item for item in tagged if item[1] in tags]

def unique_ever(iterable, key=None):
    
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in [x for x in iterable if x not in seen]:
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element

def build_graph(nodes):
    """Return a networkx graph instance.
    :param nodes: List of hashables that represent the nodes of a graph.
    """
    gr = nx.Graph()  
    gr.add_nodes_from(nodes)
    nodePairs = list(itertools.combinations(nodes, 2))

    for pair in nodePairs:
        firstString = pair[0]
        secondString = pair[1]
        levDistance = editdistance.eval(firstString, secondString)
        gr.add_edge(firstString, secondString, weight=levDistance)

    return gr

def extract_key_phrases(text):
    word_tokens = nltk.word_tokenize(text)

    tagged = nltk.pos_tag(word_tokens)
    textlist = [x[0] for x in tagged]

    tagged = filter_for_tags(tagged)
    tagged = normal(tagged)

    unique_word_set =unique_ever([x[0] for x in tagged])
    word_set_list = list(unique_word_set)

    graph = build_graph(word_set_list)

    calculated_page_rank = nx.pagerank(graph, weight='weight')
    keyphrases = sorted(calculated_page_rank, key=calculated_page_rank.get,
                        reverse=True)
    one_third = 50
    keyphrases = keyphrases[0:50]

    modified_key_phrases = set([])
    dealt_with = set([])
    i = 0
    j = 1
    while j < len(textlist):
        first = textlist[i]
        second = textlist[j]
        if first in keyphrases and second in keyphrases:
            keyphrase = first + ' ' + second
            modified_key_phrases.add(keyphrase)
            dealt_with.add(first)
            dealt_with.add(second)
        else:
            if first in keyphrases and first not in dealt_with:
                    modified_key_phrases.add(first)
            if j == len(textlist) - 1 and second in keyphrases and \
                    second not in dealt_with:
                modified_key_phrases.add(second)

        i = i + 1
        j = j + 1

    return list(modified_key_phrases)

def todf(vogue):
    df1=pd.DataFrame.from_dict(vogue)
    row=[]
    for entry in df1.columns:
        row.append(entry)
    
    df1.loc[len(df1)]= row
    cols=[]
    for i in range(len(df1.loc[0])):
        cols.append(str(i))
    
    df1.columns= cols
    df= df1.T
    df.columns= ['Date', 'Tags', 'Text', 'Links', 'Title']
    cols = list(df.columns)
    a, b = cols.index('Date'), cols.index('Title')
    cols[b], cols[a] = cols[a], cols[b]
    df = df[cols]
    cols = list(df.columns)
    a, b = cols.index('Date'), cols.index('Tags')
    cols[b], cols[a] = cols[a], cols[b]
    df = df[cols]
    return df

def convert_date(text):
    datetime_object = datetime.strptime(text, '%d %B %Y')
    return datetime_object

def dscore(df):
    df['Date'] = df.Date.apply(convert_date)
    df = df.sort_values(by='Date').reset_index(drop=True)      
    lis = []
    for i in range(len(df)):
        lis.append(i)
    df["DScore"] = pd.Series(lis)
    return df

def endorse(text, title, tags):
    temp= text+title+tags
    res= extract_key_phrases(temp)
    return len(res)
def escore(df):
#     df['EScore']= ""
    df['EScore'] = df.apply(lambda row : endorse(row['Text'], row['Title'], row['Tags']), axis = 1)
    return df

scaler = MinMaxScaler(feature_range = (0,10))

def normalize(df):
    column_names_to_normalize = ['DScore', 'EScore']
    x = df[column_names_to_normalize].values
    x_scaled = scaler.fit_transform(x)
    df_temp = pd.DataFrame(x_scaled, columns=column_names_to_normalize, index =df.index)
    df[column_names_to_normalize] = df_temp
    return df

def filter_for_tags(tagged, tags=['NN', 'JJ']):
    """Semantic Filter Based on POS."""
    return [item for item in tagged if item[1] in tags]

def clean(rev): 
    lis = []
    for i in rev:
        i = re.sub(r'[^\w\s\']','',i)
        i = i.replace("\n", " ")
        lis.append(i)
    return lis

def category(df):
    for i in range(len(df)):
        tshirt=0
        footwear=0
        jewellery=0
        dress=0
        skirt=0
        bag=0
        res = df['Title'][i].split()
        res = [word.lower() for word in res]
        df['Title'][i]=clean(res)
        for word in df['Title'][i]:
            if word in apparel['footwear']:
                footwear+=1
            if word in apparel['tshirt']:
                tshirt+=1
            if word in apparel['jewellery']:
                jewellery+=1
            if word in apparel['dress']:
                dress+=1
            if word in apparel['skirt']:
                skirt+=1
            if word in apparel['bag']:
                bag+=1
                
        if footwear== tshirt== jewellery==dress==skirt==bag:
            res=extract_key_phrases(df['Text'][i])
            res= list(res)
            new= []
            for word in res:
                small= word.split()
                new.append(small)
            tshirt=0
            footwear=0
            jewellery=0
            dress=0
            skirt=0
            bag=0
            for li in new:
                for word in li:
                    if word in apparel['footwear']:
                        footwear+=1
                    if word in apparel['tshirt']:
                        tshirt+=1
                    if word in apparel['jewellery']:
                        jewellery+=1
                    if word in apparel['dress']:
                        dress+=1
                    if word in apparel['skirt']:
                        skirt+=1
                    if word in apparel['bag']:
                        bag+=1
            df['tshirt'][i]=tshirt
            df['footwear'][i]=footwear
            df['jewellery'][i]=jewellery
            df['dress'][i]= dress
            df['skirt'][i]= skirt
            df['bag'][i]= bag
       
        else:
            df['tshirt'][i]=tshirt
            df['footwear'][i]=footwear
            df['jewellery'][i]=jewellery
            df['dress'][i]= dress
            df['skirt'][i]= skirt
            df['bag'][i]= bag
            
    return df

def clean_text(text):
    try:
        text= text.lower()
        res= text.split(" ")
    except:
        res=[]
    return res

def clean_list(str):
    res=[]
    for li in str:
        li = li.replace('-', ' ').split(' ')
        for word in li:
            res.append(word)
    return res

def similarity(nord, res_dict):
    for i in range(len(nord)):
        tscore=0
        dscore=0
        escore=0
        for j in range(len(res_dict['text'])):
            for word in res_dict['text'][j]:
                if word in nord['Name'][i]:
                    tscore+=1
                if word in nord['Description'][i]:
                    tscore+=1
            dscore= res_dict['dscore'][j]
            escore= res_dict['escore'][j]  
        nord['AScore'][i]= (tscore + dscore+ escore)/3
        
def normalize2(nord):
    column_names_to_normalize = ['AScore']
    x = nord[column_names_to_normalize].values
    x_scaled = scaler.fit_transform(x)
    nord_temp = pd.DataFrame(x_scaled, columns=column_names_to_normalize, index=nord.index)
    nord[column_names_to_normalize] = nord_temp
    return nord

def sortbyarticles(df):
    res1 = df
    lister = []
    for i in range(len(res1)):
        x = (res1["DScore"][i] + res1["EScore"][i])/2
        lister.append(x)
    res1["Scores"] = pd.Series(lister)
    res1 = res1.sort_values(by = "Scores", ascending = False).reset_index(drop = True)[:5]
    del res1["Tags"], res1["DScore"], res1["EScore"], df["Scores"]
    return res1 

def articles(website, product):

    nord= pd.read_csv('static/CSV/NORDSTROM_' + product + '.csv')
    file = 'static/PKL/' + website + '_articles.pkl'
    with open(file, 'rb') as f:
        vogue = pickle.load(f)
    
    df = todf(vogue)
    df = dscore(df)
    df = escore(df)
    res1 = sortbyarticles(df)
    res1.to_pickle('static/Sample_Results/top5articles.pkl')
    df['tshirt']  = "" 
    df['footwear']  = ""
    df['jewellery']  = ""
    df['dress']  = ""
    df['skirt']  = ""
    df['bag']  = ""
    df = category(df)
    df['Text'] = df.Text.apply(extract_key_phrases)
    df['Text']= df.Text.apply(clean_list)
    df['Category']= ['footwear', 'footwear', 'footwear', 'tshirt','jewellery', 'dress','none','dress','dress','dress','bag' ]
    nord['Name']= nord.Name.apply(clean_text)
    nord['Name']= nord.Name.apply(clean_list)
    nord['Description']= nord.Description.apply(clean_text)
    nord['Description']= nord.Description.apply(clean_list)

    #selecting category and building it's list
    res_dict={'text': [], 'dscore' : [], 'escore': []}
    relevant= df.loc[df['Category'] == product].reset_index()

    for i in range(len(relevant)):
        small= []
        for word in relevant['Text'][i]:
            small.append(word)
        res_dict['text'].append(small)
    res_dict['dscore'].append(relevant['DScore'][i])
    res_dict['escore'].append(relevant['EScore'][i])

    nord['AScore']= ""
    similarity(nord, res_dict)
    result = normalize2(nord)
    result = result.sort_values(by = "AScore", ascending = False)
    result = result[:5]
    result = result.reset_index(drop = True)
    del result["Rating"], result["Number of Ratings"], result["Reviews"], result["Current Views"], result["Description"], result["Discount"]
    result.to_pickle('static/Sample_Results/top5prods.pkl')
    return