Builds off [Roger Whitson](https://github.com/rogerwhitson/Markov-Tweet)'s work in [Markov-Tweet](https://github.com/rogerwhitson/Markov-Tweet). Updated to automate and simplify the process of creating a bot as well as replace now-defunct libraries. Also, allows for Arabic text.

To use:
* pip install tweepy
* Update the values in 'DO_ME_twitter_keys' and save as keys.py
* Update Markov_Tweet.py with the handle you wish to emulate.
* python Markov_Tweet.py 


Essentially, this bot differs from the original in that it's designed to emulate existing Twitter users effortlessly. No need to compile training data or multi-step procedures. Given the handle, it will autodump the last 3240 of that user in csv, remove retweets and convert it into a text file. It will then run the Markov Chain model on it and automatically tweet the result out to the account detailed in keys.py
