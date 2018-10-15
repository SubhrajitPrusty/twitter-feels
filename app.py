import requests
from dotenv import load_dotenv
import os
import json
from requests_oauthlib import OAuth1


load_dotenv() # load environments


def query(topic):
	APIKEY = os.getenv("APIKEY")
	APISECRET = os.getenv("APISECRET")
	TOKEN = os.getenv("TOKEN")
	TOKENSECRET = os.getenv("TOKENSECRET")

	SEARCH_LINK = f'https://api.twitter.com/1.1/search/tweets.json?q={topic}&count=100&result_type=recent'

	auth = OAuth1(APIKEY, APISECRET, TOKEN, TOKENSECRET)

	r = requests.get(SEARCH_LINK, auth=auth)

	if r.status_code == 200:
		rjson = r.json()

		# print(json.dumps(rjson, indent=4, sort_keys=True))

		statuses = rjson['statuses']
		# print( json.dumps(statuses, indent=4))
		print(f"Number of statuses : {len(statuses)}")

		print(f"{topic} : {sum([tweet['text'].count(topic) for tweet in statuses])}")


query('happy')
query('sad')
