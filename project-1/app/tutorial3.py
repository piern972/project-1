import tweepy
import random

from authorization_tokens import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

message = ""

# Option 5: Basic search
#search_results = api.search(q="Nicki Minaj filter:safe", lang="en")
#random_tweet = random.choice(search_results)
#random tweet is an object which is a variable that has
#many values, or properties, which you can access with dot notation
#print( dir(random_tweet) )

import pprint
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(random_tweet._json)

#text = random_tweet.full_text
#message = text.replace("Nicki Minaj", "Woman who's cousin's fiance made her anti-vax,")
#print(message)

#Option 6: Mentions
#mentions = api.mentions_timeline()
#mention_tweet = random.choice(mentions)
#thanks = "I'm a radical gratitude bot. Thank you for the mention."
#message = "@" + mention_tweet.user.screen_name + thanks
#api.update_status(message, in reply to status_id=mention_tweet.id)

#Option 7: External API
mentions = api.mentions_timeline()
mention_tweet = random.choice(mentions)
mention_tweet_words = mention_tweet.text.split()
word = random.choice(mention_tweet_words)
rhyming_wors_list = pronouncing.rhymes(word)
rhyme word = random.choice(rhyming_word_list)

template = "You say {}, I say {}."
message = template.format(word,rhyme_word)

message = "@" + message
api.update_status(message, in_reply_to_status_id=mention_tweet.id)

#api.update_status(message)
print("Done.")
