# Custom TwitterBot

Bot is created using SeleniumLibrary

All is implemented under single class with multiple functions, so everytime code is run, bot has flexibility via different random time intervals provided by input arguments.

Actions such as scroll/tweet/retweet/like/visit_hashtag can be combined with desirable time intervals between one another


## Possible upgrades
======= Single Collab / 2 bots =======

Start time 09:00 - RUN!
collab_hours = 8 hours

Global Constraints:
- login_count = [2, 4]
- tweet_count = [4, 6]
- tweets_per_login = if [tweet_count / login_count] == qaliqli, then: ceil -> floor -> ceil -> floor ..... remanining =]] 
......................if [tweet_count / login_count] == tam, then: randomly +-1 ..... remaining                        || 
- max_login_hours = collab_hours / [login_count(Bot1) + login_count(Bot2)]                                             ||
- single_login_interval = max_login_hours * [60%-85%] =====================]]                                          ||
                                                  [[=======================||==========================================]]
Initiate Global Constraints for each Bot:         ||                       ||
bot1_login_count , bot1_tweet_count && bot1_tweets_per_login, bot1_single_login_interval
bot2_login_count , bot2_tweet_count && bot2_tweets_per_login, bot2_single_login_interval

1) randomly pick bot, e.g => Bot1
    Log in Bot1
    spend bot1_single_login_interval (randomized 60-85%)
             # TODO: FIRST
             # TODO: SECOND
             .
             .
             Total Tweets = bot1_tweets_per_login (ceil/floor of bot1_tweet_count/bot1_login_count)
             .
             note: decide interval between tweets !!
    log out 
2) Wait for [max_login_hours - bot1_single_login_interval]
2) Pick another bot = Bot2
     do same procedure
3) Wait for [max_login_hours - bot2_single_login_interval]
4) Pick another bot = Bot1
.
.
.
======================================================================

