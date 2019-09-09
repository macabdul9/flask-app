
from flask import request
from flask_restful import Resource
import logging as logger

from .model import predict


import praw


class Task(Resource):


	def get(self):
		logger.debug('inside get method')
		return {"message":"inside get method"}, 200 #HTTP Status CODE OK

	def post(self):
		logger.debug('inside post method')

		req = request.get_json()

		url = req['url']

		result = predict(url)

		logger.debug(url)
		return {'result':result}, 200
	

	def put(self):
		logger.debug('inside put method')
		return {"message":"inside put method"}, 200 #HTTP Status CODE OK
	
	def delete(self):
		logger.debug('inside delete method')
		return {"message":"inside delete method"}, 200 #HTTP Status CODE OK
