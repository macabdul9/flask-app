
# # #importing libraries
# # import os
# # import numpy as np
# # import flask
# # import pickle
# # from flask import Flask, render_template, request

# # #creating instance of the class
# # app=Flask(__name__)

# # #to tell flask what url shoud trigger the function index()
# # @app.route('/')
# # @app.route('/index')
# # def index():
# #     return flask.render_template('index.html')

# # if __name__ == "__main__":
# # 	port = int(os.environ.get("PORT", 5000))
# # 	app.run(debug=True, port=port)


# # REST API
# # from flask import Flask, jsonify, request

# # app = Flask(__name__)




# # @app.route('/', methods=['GET', 'POST'])
# # def index():
# # 	if(request.method == 'POST'):
# # 		some_json = request.get_json()
# # 		return jsonify({'you sent':some_json}), 201
# # 	else:
# # 		return jsonify({'about':'Hello World'})

# # @app.route('/multi/<int:num>', methods=['GET'])
# # def get_multiply(num):
# # 	return jsonify({'result':num*10})


# # if __name__=='__main__':
# # 	app.run(debug=True)


# # to avoid the warnings
# import warnings
# warnings.filterwarnings('ignore')



# from keras.preprocessing.text import Tokenizer
# from keras.preprocessing.sequence import pad_sequences

# from keras.models import Sequential
# from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D

# import shutil
# import os
# import re
# import praw
# import pickle

# # REST API with RESTFUL

# import numpy as np
# from flask import Flask, request, jsonify
# from flask_restful import Resource, Api

# app =Flask(__name__)
# api = Api(app)

# class HelloWorld(Resource):
# 	def get(self):
# 		return {'about':"Abdul Waheed"}
# 		# return {'result:':num*np.random.randn(10).tolist()}

# 	def post(self):
# 		some_json = request.get_json()
#  		return {'you sent':some_json}, 201

# class Multi(Resource):
# 	def get(self, name):
# 		# return {'result:':num*np.random.randn(10).tolist()}
# 		reddit = praw.Reddit(client_id='xVeb5-ej49aBDg', client_secret='HLuuBB0e1upw1pbZ-oUFtrBplFY', user_agent='reddit-scrap', username='macabdul9', password='Sudo$0#1')
# 		subm = reddit.submission(id=name)
# 		title = subm.title
# 		return {'post title':title}


# # # The maximum number of words to be used. (most frequent)
# # MAX_NB_WORDS = 50000

# # # Max number of words in each complaint.
# # MAX_SEQUENCE_LENGTH = 100

# # # This is fixed.
# # EMBEDDING_DIM = 100


# # idx_to_flair = {
# # 		0: 'AskIndia', 1: 'Business/Finance', 2: 'Food', 3: 'Non-Political', 4: 'Not in English.', 5: 'Photography',
# # 	 	6: 'Policy/Economy', 7: 'Politics',8: 'Science/Technology', 9: 'Sports', 10: '[R]eddiquette'
# # 	 }

# # REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
# # BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')



# # with open('word_counts.pkl', 'rb') as fp:
# #   	word_counts = pickle.load(fp)
# # with open('word_docs.pkl', 'rb') as fp:
# #   	word_docs = pickle.load(fp)
# # with open('word_index.pkl', 'rb') as fp:
# #   	word_index = pickle.load(fp)

# # tokenizer = Tokenizer()
# # tokenizer.word_counts = word_counts
# # tokenizer.word_docs = word_docs
# # tokenizer.word_index = word_index



# class Prediction(Resource):


# 	# def text_cleaning(text):
 
# 	#     #stopword = set(stopwords.words('english'))
# 	#     text = text.lower()
	    
# 	#     text = REPLACE_BY_SPACE_RE.sub(' ', text) # replace REPLACE_BY_SPACE_RE symbols by space in text. substitute the matched string in REPLACE_BY_SPACE_RE with space.
#  #    	text = BAD_SYMBOLS_RE.sub('', text) # remove symbols which are in BAD_SYMBOLS_RE from text. substitute the matched string in BAD_SYMBOLS_RE with nothing.
	    
# 	#     return text

# 	# def preprocessing(text):
# 	# 	pass
		



# 	def create_n_compile(self):
# 		model = Sequential()
# 		model.add(Embedding(MAX_NB_WORDS, EMBEDDING_DIM, input_length=X.shape[1]))
# 		#model.add(SpatialDropout1D(0.2))
# 		model.add(LSTM(64))
# 		model.add(Dense(11, activation='softmax'))
# 		model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# 		return model


# 	def prediction(self, x):
# 		model = self.create_n_compile()

# 		model.load_weights('weights.h5')


# 		result = model.predict(x)

# 		return idx_to_flair[result]


# 	def get(self, s_id):

# 		reddit = praw.Reddit(client_id='xVeb5-ej49aBDg', client_secret='HLuuBB0e1upw1pbZ-oUFtrBplFY', user_agent='reddit-scrap', username='macabdul9', password='Sudo$0#1')
# 		try:
# 			subm = reddit.submission(id=s_id)
# 		except Exception as e:
# 			result = "Invalid URL !"
# 			return {'predicted flair ':result}

# 		title = subm.title
# 		flair = subm.link_flair_text
# 		permalink = subm.permalink

# 		return {
# 		'result':title,
# 		'flair' : flair,
# 		'url':'https://www.reddit.com'+permalink
# 		}





# api.add_resource(HelloWorld, '/')


# api.add_resource(Multi, '/category-finder/<string:name>')



# api.add_resource(Prediction, '/predict/<string:s_id>')



# if __name__ == '__main__':
# 	app.run(debug=True)
		







# Python Flask CRUD REST APP in 30 Minutes https://www.youtube.com/watch?v=j2v2r6ByjJI

from flask import Flask, render_template, url_for, request

import logging as logger

logger.basicConfig(level="DEBUG")

flaskApp = Flask(__name__)




@flaskApp.route('/')
def index():
    return render_template('/index.html')


@flaskApp.route('/hello')
def hello():
    return render_template('hello.html')




if __name__=="__main__":

	from api import *
	logger.debug('Starting the Application')
	flaskApp.run(debug=True)

