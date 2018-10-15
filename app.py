import requests
from dotenv import load_dotenv
import os
import json
from requests_oauthlib import OAuth1


load_dotenv() # load environments

APIKEY = os.getenv("APIKEY")
APISECRET = os.getenv("APISECRET")
TOKEN = os.getenv("TOKEN")
TOKENSECRET = os.getenv("TOKENSECRET")

day = 'today'

LINK = f'https://api.twitter.com/1.1/search/tweets.json?q={day}&count=100'

auth = OAuth1(APIKEY, APISECRET, TOKEN, TOKENSECRET)

r = requests.get(LINK, auth=auth)

print(r)
rjson = r.json()

# print(json.dumps(rjson, indent=4, sort_keys=True))

statuses = rjson['statuses']
# print( json.dumps(statuses, indent=4))
print(f"Number of statuses : {len(statuses)}")

for tweet in statuses:
	text = tweet['text']
	print(text.count(":)"))