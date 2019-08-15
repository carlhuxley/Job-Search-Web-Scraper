# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 11:19:28 2019

@author: JMN
"""
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

def clean_description(description):
    letters_only = re.sub("[^a-zA-Z0-9]", " ", description)                   
                       
    query = letters_only
    #need to improve the way markup is removed from descriptions! eg text-align
    markup = ['strong','gt','lt','li','ul','br','div','span','amp','b','nbsp', 
              'text','align','justify','p','style','font','weight']
    querywords = query.split()

    resultwords  = [word for word in querywords if word.lower() not in markup]
    description = ' '.join(resultwords)
    
    #description = description.lower()
    
    #bag_of_words = description.split()
    
    #bag_of_words = [ps.stem(word) for word in bag_of_words if not word in set(stopwords.words('english'))]
    
    #description = ' '.join(bag_of_words)
    
    return description

def create_corpus(jobs):
    corpus = []
   
    for j in jobs:
        corpus.append(j['Description'])
        
    return corpus

 #create bag of words model
def bag_of_words(corpus):
    from sklearn.feature_extraction.text import CountVectorizer
    cv = CountVectorizer(ngram_range=(1, 3), min_df = 2 )
    X = cv.fit_transform(corpus).toarray()
    #Show the words in the bag
    words = cv.get_feature_names()
    
    return words