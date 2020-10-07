import twitterbot as tb
import secrets,posts, sys
import numpy as np


#hashtag = sys.argv[1]

credentials = secrets.get_credentials()


# initialize the bot with your credentials and log in Twitter
bot = tb.Twitterbot(credentials['email'], credentials['password'])
bot.login()

#bot.random_scroll()
#bot.go_home()
#bot.go_profile()
#bot.go_notif()
#bot.visit_random_hashtags(hotflag_l=True, hotflag_r=False, lateflag=True)
mytweet = posts.get_post()
bot.post_tweet(mytweet)
