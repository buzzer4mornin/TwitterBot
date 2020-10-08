# Custom TwitterBot

Bot is created using SeleniumLibrary

All is implemented under single class with multiple functions, so everytime code is run, bot has flexibility via different random time intervals provided by input arguments.

Actions such as scroll/tweet/retweet/like/visit_hashtag can be combined with desirable time intervals between one another


## Possible upgrades:

============ Single Collab / 2 bots ============

Start time 09:00 - RUN!
collab_hours = 8 hours

Initiate for each Bot:
 - login_count = [2, 4]
 - tweet_count = [4, 6]
 - tweets per login : if [tweet_count / login_count] == qaliqli, then: ceil -> floor -> ceil -> floor ..... remanining   
                      if [tweet_count / login_count] == tam, then: randomly +-1 ..... remaining


max_login_hours = collab_hours / [login_count(Bot1) + login_count(Bot2)]
single_login_interval = max_login_hours * [60%-85%]

1) randomly pick bot, e.g => Bot1
    spend single_login_interval 
            
    log out 

2) pick another bot = Bot2
3) pick another bot = Bot1

