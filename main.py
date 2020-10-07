import twitterbot as tb
import secrets,posts, sys

# fetches the hashtag from command line argument
# -- hashtag = sys.argv[1]
# fetches the credentials dictionary
# using get_credentials function



credentials = secrets.get_credentials()
print(credentials)
mytweet = posts.get_post()

# initialize the bot with your credentials
#bot = tb.Twitterbot(credentials['email'], credentials['password'], mytweet)
# loging in
#bot.login()
# calling like_retweet function
# bot.like_retweet(hashtag)
#bot.post_tweet()
