import twitterbot as tb
import secrets,posts, sys
import numpy as np


#hashtag = sys.argv[1]

credentials = secrets.get_credentials()


# initialize the bot with your credentials and log in Twitter
bot = tb.Twitterbot(credentials['email'], credentials['password'])
bot.login()

# initialize the bot with your credentials
#bot = tb.Twitterbot(credentials['email'], credentials['password'], mytweet)
# loging in
#bot.login()
# calling like_retweet function
# bot.like_retweet(hashtag)
#bot.post_tweet()
