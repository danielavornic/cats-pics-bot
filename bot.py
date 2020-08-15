import tweepy
import requests
import os
from time import sleep

consumer_key = 'lnYxJ2kGKKWQnKUyn4omuNCLj' 
consumer_secret = 'fRDKspUvcUQEklWhCXeZJi2Et58FwDhtOV71fTNIr5Pc1XtIy0' 
access_token = '1285590029776097280-xRUcCQ4nEEiYYTG6Vj4be1FcinnKR3' 
access_token_secret = 'NZU2wmq3Uz0egyu1xKH92eIFbpoPUNZV2VB53dRWjYBU8' 
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