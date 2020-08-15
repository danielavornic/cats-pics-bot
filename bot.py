import tweepy
import requests
import os
from time import sleep

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_KEY']
access_token_secret = os.environ['ACCESS_SECRET']
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def tweet():
    filename = 'cat.jpg'
    r = requests.get('https://api.thecatapi.com/v1/images/search')
    url = r.json()[0]['url']
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)
        api.update_with_media(filename)
        os.remove(filename)
    else:
        tweet()
    sleep(3600)

if __name__ == "__main__":
    while True:
        tweet()