from sys import argv
from markov_class import *
from keys import *
import twitter

script = argv
inputfile = argv

def main():
    order = int(2)
    handle = "HandleHEre"

    filetext = process_file()

    # The number below is determined upon the maximum length of a tweet minus the maximum
    # length of a handle.
    markov = MarkovDict(filetext, order, 123)
    markov.read_text()
    output = markov.output_text()
    print output
    tweet_output(output)

# prompt to open file
def process_file():
    f = open("blake.txt")
    # read through the file
    filetext = f.read()
    f.close()
    return filetext

# Put your keys into "DO_ME_twitter_keys" file and rename the file to "keys.py"
def tweet_output(output):
    api = twitter.Api(consumer_key='ConsumerKeyHere',
                      consumer_secret='ConsumerSecretHere',
                      access_token_key='AccessTokenHere',
                      access_token_secret='AccessTokenSecretHere')

    status = api.PostUpdate(output)


if __name__ == "__main__":
    main()
