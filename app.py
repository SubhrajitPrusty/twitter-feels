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

