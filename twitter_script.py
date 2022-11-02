from script import main
import tweepy
from os import environ
from time import sleep
from dotenv import load_dotenv

# implementar a parte do twitter
load_dotenv()

api = tweepy.Client(
    consumer_key=f"{environ['CONSUMER_KEY']}",
    consumer_secret=f"{environ['CONSUMER_SECRET']}",
    access_token=f"{environ['ACCESS_TOKEN']}",
    access_token_secret=f"{environ['ACCESS_TOKEN_SECRET']}",
)

artigo = main()

try:
    api.create_tweet(text=f"{artigo['titulo']}\n{artigo['texto']}\n{artigo['url']}")
    print("Tweet criado")
except:
    print("Deu errado")
