from flask import Flask, render_template, url_for, request, jsonify
from flask_pymongo import PyMongo

import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib

from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://macab:<Sudo$0#1>@datatset-shard-00-00-c4vhw.mongodb.net:27017,datatset-shard-00-01-c4vhw.mongodb.net:27017,datatset-shard-00-02-c4vhw.mongodb.net:27017/test?ssl=true&replicaSet=datatset-shard-0&authSource=admin&retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/',  methods=['GET', 'POST', 'PUT', "DELETE"])
def gppd(): 
    if request.method=='POST':
        return jsonify({'name':"post request"}), 200
    if request.method=='PUT':
        return jsonify({'name':"put request"}), 200
    if request.method=='DELETE':
        return jsonify({'name':"delete request"}), 200
    if request.method=='GET':
        return jsonify({'name':"get request"}), 200



# @app.route('/predict',methods=['POST'])
# def predict():
#     df = pd.read_csv('spam.csv',encoding='latin-1')
#     df.drop(['Unnamed: 2','Unnamed: 3','Unnamed: 4'], axis=1,
#             inplace = True)
#     df['label'] = df['class'].map({'ham':0,'spam':1})
#     X= df['message']
#     y = df['label']
    
    
#     #Extract feature with CountVectorize
#     cv = CountVectorizer()
#     X = cv.fit_transform(X)
#     from sklearn.model_selection import train_test_split
#     X_train, X_test, y_train, y_test = train_test_split(X,y,
#                                                         test_size=0.33,
#                                                         random_state=42)
#     from sklearn.naive_bayes import MultinomialNB
#     clf = MultinomialNB()
#     clf.fit(X_train,y_train)
#     print(clf.score(X_test,y_test))
    
    
#     if request.method == "POST":
#         message = request.form['message']
#         data = [message]
#         vect = cv.transform(data).toarray()
#         pred = clf.predict(vect)

#     return render_template('home.html', prediction = pred)
    
if __name__ == '__main__':
    app.run(debug=True)