import praw

def predict(url):

		reddit = praw.Reddit(client_id='xVeb5-ej49aBDg', client_secret='HLuuBB0e1upw1pbZ-oUFtrBplFY', user_agent='reddit-scrap', username='macabdul9', password='Sudo$0#1')
		try:
			subm = reddit.submission(url=url)
		except Exception as e:
			result = "Invalid URL !"
			return {'predicted flair ':result}

		title = subm.title
		flair = subm.link_flair_text
		permalink = subm.permalink
		_id = subm.id

		return {
		'title':title,
		'flair':flair,
		'_id': _id,
		'url':'https://www.reddit.com'+permalink
		}