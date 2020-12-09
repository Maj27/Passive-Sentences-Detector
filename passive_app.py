# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 16:11:00 2020

@author: majed.aljefri
"""
#app.py
from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json
import string
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

model_file = 'C:/Side Projects/Learning Branch/model.pickle'


app = Flask(__name__)
model, vec, selection = p.load(open(model_file, 'rb'))


@app.route('/')
#def home():
#    return render_template('index.html')

@app.route('/predict_api/', methods=['POST'])
def predict_api():
    new_sentence = request.get_json(force = True)
    prediction = new_prediction(new_sentence, model, vec, selection)
    
    return jsonify(prediction)

def get_tages2 (sent):
    
    words_ = nltk.word_tokenize(sent)
    words = [] 
    for word in words_: # Go through every word in your tokens list
        if (word not in string.punctuation):  # remove punctuation
            words.append(word)
        
    tokens = nltk.pos_tag(words)
    tags = [i[1] for i in tokens]
    
    return ' '.join(tags)

def new_prediction(sentence,model, vec, selection):
   
    tags = np.array(str(get_tages2(sentence)))
    features = vec.transform(tags.ravel())
   
    features = selection.transform(features[0]) 
    if model.predict(features):
        return 'Active'
    else:
        return 'Passive'
    
if __name__ == '__main__':
    app.run(debug=True)