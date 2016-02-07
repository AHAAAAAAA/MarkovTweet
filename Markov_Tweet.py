#!/usr/bin/python
# -*- coding: utf-8 -*-
from sys import argv
from markov_class import *
from keys import *
import tweepy
from tweetdump import *
from csvtotxt import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

outputf = "result.txt"
def main():
    #Change Order
    order = int(2)
    handle = "jack" #Put handle you want to emulate here
    get_all_tweets(handle) #COMMENT THIS OUT TO JUST READ FROM LAST READ USER
    csvtotext('tweets.csv', 'tweets.txt') #COMMENT THIS OUT TO JUST READ FROM LAST READ USER
    filetext = process_file('tweets.txt')

    # The number below is determined upon the maximum length of a tweet minus the maximum
    # length of a handle.
    markov = MarkovDict(filetext, order, 140)
    markov.read_text()
    output = markov.output_text()
    tweet_output(output)

# prompt to open file
def process_file(file):
    f = open(file)
    print "processed file"
    # read through the file
    filetext = f.read()
    f.close()
    return filetext

# Put your keys into "DO_ME_twitter_keys" file and rename the file to "keys.py"
def tweet_output(output):
    new = list(output)
    print "Status:" + output
    api.update_status(output)
    print "Tweeted!"


if __name__ == "__main__":
    main()
