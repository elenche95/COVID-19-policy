#!/usr/bin/env python
# coding: utf-8

import tweepy, json
# importing API keys, this must be part of the git ignore
from keys import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open("may_tweets.txt", "a")
        # this option will overwrite all the current text, this other option will self.file = open("tweets.txt", "w")

    def on_status(self, status):
        tweet = status._json
        self.file.write( json.dumps(tweet) + '\n' )
        self.num_tweets += 1
        if self.num_tweets < 10000:
            return True
        else:
            return False
        self.file.close()

    def on_error(self, status):
        print(status)


l = MyStreamListener()

# Create your Stream object with authentication
stream = tweepy.Stream(auth , l)

# Filter Twitter Streams to capture data by the keywords: for now we are only looking at english tweets
stream.filter(track=['COVID','covid', 'COVID-19', 'covid-19', 'coronavirus', '"corona virus"'], languages=['en'])

