import twitterbot as tb
import secrets,posts, sys
import numpy as np

# TODO: Youtube
#https://www.youtube.com/watch?v=7ovFudqFB0Q&t=691s&ab_channel=DevEd


#sessions_count = int(sys.argv[1])
session_count = np.random.randint(5, 9)
credentials = secrets.get_credentials()

# Bot1 credentials
bot1_email = credentials.get("email1")
bot1_username = credentials.get("username1")
bot1_password = credentials.get("password1")

#Bot2 credentials
bot2_email = credentials.get("email2")
bot2_username = credentials.get("username2")
bot2_password = credentials.get("password2")

if __name__ == "__main__":

    # initialize the bot1/bot2 with your credentials and log in Twitter
    bot2 = tb.Twitterbot(bot2_username, bot2_password)
    bot2.login()

    # Walking around
    #bot2.go_home(h_step=50, h_speed=np.random.randint(7, 9), h_interval=np.random.randint(100, 200))
    #bot2.go_profile(p_step=30, p_speed=np.random.randint(6, 9), p_interval=np.random.randint(100, 200))
    #bot2.go_notif(n_step=30, n_speed=np.random.randint(6, 9), n_interval=np.random.randint(200, 250))

    'Visit hashtags/like/tweet/retweet/message'
    #bot2.send_message()
    #bot2.visit_random_hashtags(hotflag_l=False, hotflag_r=False, lateflag=True, latelikes=3)
    #mytweet = posts.get_post()
    #bot2.post_tweet(mytweet)


'''==== Single Collab / 2 bots =====
Start time 09:00 - RUN:
collab_hours = 8 hours

login_count = [2, 4]
tweet_count = [4, 6]

if [tweet_count / login_count] == qaliqli, then: ceil -> floor -> ceil -> floor ..... remanining
if [tweet_count / login_count] == tam, randomly +-1 ..... remaining


max_login_hours = collab_hours / [login_count(Bot1) + login_count(Bot2)]
single_login_interval = max_login_hours * [60%-85%]
last_login_interval =  sum(single_login_interval)

1) randomly pick bot = Bot1
    first login of Bot1
    tweet of Bot1

2) pick another bot = Bot2
3) pick another bot = Bot1
'''

'''if __name__ == "__main__":
    for _ in range(session_count):
        if session_count == 1:
           #bot = tb.Twitterbot(credentials['email'], credentials['password'])
           #bot.login()

            # TODO: ================================ Single Login Activities ==========================================

            # TODO: FIRST
            if np.random.rand() < 0.85: print("go_home") #bot.go_home(h_step=50, h_speed=np.random.randint(7, 9), h_interval=np.random.randint(900, 1200))

            choice = np.random.randint(0, 2)
            if choice == 0:
                if np.random.rand() < 0.5:  print("go_profile") #bot.go_profile(p_step=30, p_speed=np.random.randint(6, 9), p_interval=np.random.randint(600, 700))
                if np.random.rand() < 0.7:  print("go_notif") #bot.go_notif(n_step=30, n_speed=np.random.randint(6, 9), n_interval=np.random.randint(350, 500))
            else:
                if np.random.rand() < 0.7:  print("go_notif")  # bot.go_notif(n_step=30, n_speed=np.random.randint(6, 9), n_interval=np.random.randint(350, 500))
                if np.random.rand() < 0.5:  print("go_profile")  # bot.go_profile(p_step=30, p_speed=np.random.randint(6, 9), p_interval=np.random.randint(600, 700))


            # TODO: SECOND
                interval = single_login_interval / tweet_count
                wait for single_login_interval * [25-35% ]'''
