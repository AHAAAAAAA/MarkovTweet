Builds off [Roger Whitson](https://github.com/rogerwhitson/Markov-Tweet)'s work in [Markov-Tweet](https://github.com/rogerwhitson/Markov-Tweet). Updated to automate and simplify the process of emulating a twitter user's style as well as replacing now-defunct libraries. Also, allows for Arabic text.

To use:
* `pip install tweepy`
* Update the values in 'DO_ME_twitter_keys' and save as keys.py
* Update Markov_Tweet.py with the handle you wish to emulate.
* `python Markov_Tweet.py `


Essentially, this bot differs from the original in that it's designed to emulate existing Twitter users effortlessly. No need to compile training data or multi-step procedures. Given the handle, it will:
* Autodump the last 3240 tweets of that user in csv
* Remove retweets+mentions
* Convert it into a text file
* Feed that into a MCMC model
* Tweet a single status out to your account. 

This can be modified to emulate a single user, skipping the new tweetdumps and conversions, by simply commenting out lines 19-20. You can add `python Markov_Tweet.py` to your CronJob to run regularly as a bot after 1 run. (Please don't tweetdump daily)

TODO:- Get a better damn MCMC model. Too little data and a broken model makes for very repetitive, nonsense tweets.
