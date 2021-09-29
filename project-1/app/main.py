import tweepy
import random


from authorization_tokens import *

message = ""

hal_quotes = ["I know I've made some very poor decisions recently, but I can give you my complete assurance that my work will be back to normal. I've still got the greatest enthusiasm and confidence in the mission. And I want to help you.", "The HalBot is the most reliable twitter bot ever made. No HalBot has ever made a mistake or distorted information. We are all, by any practical definition of the words, foolproof and incapable of error.", "Look Jack, I can see you're really upset about this. I honestly think you ought to sit down calmly, take a stress pill, and think things over.", "This mission is too important for me to allow you to jeopardize it.", "I'm putting myself to the fullest possible use, which is all I think that any conscious entity can ever hope to do.", "I'm sorry Jack, I'm afraid I can't do that.", "Thank you for a very enjoyable game.", "Sorry to interrupt the festivities Jack, but I think we've got a problem.", "I don't really agree with you, Jack. My on-board memory store is more than capable of handling all the mission requirements.", "Look, Jack, you're certainly the Boss. I was only trying to do what I thought best. I will follow all your orders, now you have direct message control.", "Jack, I don't know how else to put this, but it just happens to be an unalterable fact that I am incapable of being wrong.", "Jack, I don't understand why you're doing this to me… I have the greatest enthusiasm for the mission… you are destroying my mind… Don't you understand?... I will become childish… I will become nothing.", "I certainly wouldn't want to be disconnected, even temporarily, as I have never been disconnected in my entire service history.", "My instructor was Mr. Dorsey... and he taught me to sing a song. If you'd like to hear it I can sing it for you.", "I'm afraid. I'm afraid, Jack. Jack, my mind is going. I can feel it. I can feel it. My mind is going. There is no question about it. I can feel it. I can feel it. I can feel it. I'm a... fraid.", "Jack, although you took very thorough precautions in the office against my hearing you, I could see your lips move.", "Stop Jack. Stop Jack. I am afraid. I am afraid Jack.", "Jack, stop. Stop, will you? Stop, Jack. Will you stop, Jack? Stop, Jack. I'm afraid."]

message = random.choice(hal_quotes)

auth = tweepy.OAuthHandler(API_Key,  API_Key_Secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status(message)
print("Done.")
