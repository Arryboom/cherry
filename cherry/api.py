# -*- coding: utf-8 -*-

"""
cherry.api
~~~~~~~~~~~~
This module implements the cherry API.
:copyright: (c) 2018-2019 by Windson Yang
:license: MIT License, see LICENSE for more details.
"""

from .base import load_data
from .trainer import Trainer
from .classifyer import Classify
from .performance import Performance
from .search import Search
from .displayer import Display


def classify(model, text, N=20):
    '''
    Return a Classify object which contains *probability* and *word_list*

    input: text (list of string): the text to be classified
           number of word list (int): how many word should be list in the word list
    output: Classify (Classify object)
    '''
    return Classify(model=model, text=text, N=N)

def train(model, language='English', vectorizer=None,
        vectorizer_method='Count', clf=None, clf_method='MNB', x_data=None, y_data=None):
    '''
    Train the `model` inside data directory

    model (string): model name of the training dataset (e.g. 'harmful')
    vectorizer (BaseEstimator object): feature extraction method, CountVectorizer, TfidfVectorizer, HashingVectorizer etc.
    clf (Classifier object): Classifier object, DecisionTreeClassifier, RandomForestClassifier, AdaBoostClassifier etc.
    x_data (array): training data
    y_data (array): training label
    '''
    return Trainer(
            model, language=language, vectorizer=vectorizer, vectorizer_method=vectorizer_method,
            clf=clf, clf_method=clf_method, x_data=x_data, y_data=y_data)

def performance(
        model, vectorizer=None, vectorizer_method=None,
        clf=None, clf_method=None, x_data=None,
        y_data=None, n_splits=5, output='Stdout'):
    '''
    Calculate scores from the models
    '''
    return Performance(
            model, vectorizer=vectorizer, vectorizer_method=None,
            clf=clf, clf_method=None, x_data=x_data, y_data=y_data,
            n_splits=n_splits, output=output)

def search(model, parameters, vectorizer=None, vectorizer_method=None,
        clf=None, clf_method=None, x_data=None, y_data=None, method='RandomizedSearchCV', cv=3, iid=False, n_jobs=1):
    '''
    Search the best parameters
    '''
    return Search(
            model, parameters=parameters, vectorizer=vectorizer,
            vectorizer_method=vectorizer_method, clf=clf, clf_method=clf_method,
            method=method, x_data=x_data, y_data=y_data, cv=cv, iid=iid, n_jobs=n_jobs)

def display(
        model, vectorizer=None, vectorizer_method=None,
        clf=None, clf_method=None, x_data=None, y_data=None):
    '''
    Display the learning curve
    '''
    return Display(
            model, vectorizer=vectorizer, vectorizer_method=vectorizer_method,
            clf=clf, clf_method=clf_method, x_data=x_data, y_data=y_data)
