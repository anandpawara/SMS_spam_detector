from flask import Flask, render_template, request
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Hello World</h1>'


if __name__ == '__main__':
    app.run()
