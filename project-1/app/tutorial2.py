import tweepy

from authorization_tokens import *

# This will give access to Python's randomness-generating features.
import random

# This is making a new variable to hold the message that will be tweeted
message = ""

# Option 1: Select message randomly from a list of messages
# phrase_list = ["Hi my name is Gritty.", "I am a monster.", "I am organge and furry."]
# message = random.choice(phrase_list)

# Option 2: A simple Mad Lib
#string_template = "some people like {} but I like {}"
#word_list = ["hardboiled eggs", "shaving cream", "grapes", "thorns", "acrylic nails"]
#word1 = random.choice(word_list)
#word2 = random.choice(word_list)
#message = string_template.format(word1,word2)

# Option 3: Select from a list of possible Mad Libs
#template_list = [ "My name is {} and I like {}.", "Some people think I'm a {} but I'm actually a {}", "{} is the knockoff version of a {}"]
#word_list1 = ["dog", "cat", "zebra", "flamingo", "cannibal"]
#word_list2 = ["disaster", "menace", "heathen", "freak",]
#template = random.choice(template_list)
#word1 = random.choice(word_list1)
#word2 = random.choice(word_list2)
#message = template.format(word1,word2)

#Option 4: Using logic to make more intentional choices
string_template = "Hi there, I'm {}, master of {}"
word_list1 = ["Gritty", "Nicolas Cage"]
word_list2_a = ["monsters", "playing hockey", "scaring people"]
word_list2_b = ["movies", "acting", "saying 'woah'"]
word1 = random.choice(word_list1)
if word1 == "Gritty":
    word2 = random.choice(word_list2_a)
elif word1 == "Nicolas Cage":
    word2 = random.choice(word_list2_b)
message = string_template.format(word1,word2)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status(message)
print("Done.")
