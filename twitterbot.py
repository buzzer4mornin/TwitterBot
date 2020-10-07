from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import numpy as np
import random
import time, os
'''Uncomment the below line for Linux OS'''
# from pyvirtualdisplay import Display

# TODO: within LOGIN, set 2 secs interval between username and password
# TODO: here, instead of email, we will use username, and add email separately along with password [3 total arguments]

class Twitterbot:

    def __init__(self, email, password):
        self.email = email
        self.password = password

        # initializing chrome options
        chrome_options = Options()
        self.bot = webdriver.Chrome(
            executable_path=os.path.join(os.getcwd(), 'chromedriver'),
            options=chrome_options
        )

    def login(self):

        bot = self.bot
        bot.maximize_window()
        bot.get('https://twitter.com/login')

        time.sleep(3)
        bot.implicitly_wait(10)

        email = bot.find_element_by_css_selector(
            '#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-13qz1uu > form > div > div:nth-child(6) > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1udh08x > div > input'
        )
        password = bot.find_element_by_css_selector(
            '#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-13qz1uu > form > div > div:nth-child(7) > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1udh08x > div > input'
        )

        # sends the email to the email input
        email.send_keys(self.email)
        time.sleep(np.random.randint(1, 4))
        # sends the password to the password input
        password.send_keys(self.password)
        time.sleep(np.random.randint(1, 4))
        # executes RETURN key action
        password.send_keys(Keys.RETURN)

        bot.implicitly_wait(10)

    def random_scroll(self, step, speed, start, end):
        bot = self.bot
        bot.implicitly_wait(50)

        my_range = np.random.randint(start, end)

        for i in range(my_range):
            a = "window.scrollTo(0," + str(i * speed) + ")"
            bot.execute_script(a)
            if i % step == 0 and bool(random.getrandbits(1)):
                # randomly stop for random amount of time during scroll
                time.sleep(np.random.randint(2, 7))
        time.sleep(np.random.randint(1, 4))

    def go_home(self):
        bot = self.bot
        bot.implicitly_wait(20)
        time.sleep(np.random.randint(1, 4))

        # go to homepage
        home_link = bot.find_element_by_xpath('//a[@href="/home"]')
        home_link.click()
        time.sleep(np.random.randint(1, 4))

        # TODO: randomize intervals || Take as input end[500,2000]
        # scroll down on profile & maybe LIKE depending on flag
        self.random_scroll(step=30, speed=np.random.randint(4, 7), start=0, end=np.random.randint(50, 100))

    def go_profile(self):
        bot = self.bot
        bot.implicitly_wait(20)
        time.sleep(np.random.randint(1, 4))

        # go to profile
        cook = '//a[@href="/' + self.email + '"]'
        profile_link = bot.find_element_by_xpath(cook)
        profile_link.click()
        time.sleep(np.random.randint(1, 4))

        # TODO: randomize intervals || end = [400,900]
        self.random_scroll(step=30, speed=3, start=0, end=np.random.randint(50, 100))

        home_link = bot.find_element_by_xpath('//a[@href="/home"]')
        home_link.click()

    def go_notif(self):
        bot = self.bot
        bot.implicitly_wait(20)
        time.sleep(np.random.randint(1, 4))

        # go to notification
        notif_link = bot.find_element_by_xpath('//a[@href="/notifications"]')
        notif_link.click()
        time.sleep(np.random.randint(2, 5))

        # 70% of time -> go to mentions on notification
        if np.random.rand() < 0.7:
            mention = bot.find_element_by_xpath('//a[@href="/notifications/mentions"]')
            mention.click()
            time.sleep(np.random.randint(3, 6))

            # go back to notification
            notif_link = bot.find_element_by_xpath('//a[@href="/notifications"]')
            notif_link.click()
            time.sleep(np.random.randint(2, 4))

        # TODO: randomize intervals || Take as input  end[300,600]
        # scroll down on notifications
        self.random_scroll(step=30, speed=3, start=0, end=np.random.randint(50, 100))

        home_link = bot.find_element_by_xpath('//a[@href="/home"]')
        home_link.click()        

    # TODO: Works on both Local and COLLAB
    def visit_random_hashtags(self, hotflag_l, hotflag_r ,lateflag):

        bot = self.bot
        bot.implicitly_wait(50)
        time.sleep(np.random.randint(1, 4))
        hashtags = ["DontBelieveArmenia", "DontBelieveArmenia", "StopArmenianAggression", "StopArmenia",
                    "SupportAzerbaijan", "khojaly", "khojalygenocide", "karabakhisazerbaijan",
                    "stoparmenianoccupation", "AzerbaijanNotAlone"]

        visit_counts = np.random.randint(3, 6)
        for i in range(visit_counts):
            target = hashtags[np.random.randint(0, len(hashtags))]
            hashtags.remove(target)
            target_hash = "#" + target
            explore_link = bot.find_element_by_xpath('//a[@href="/explore"]')
            explore_link.click()

            # scroll in HOT
            time.sleep(np.random.randint(2, 4))
            search_link = bot.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div[2]/input'
            )
            search_link.send_keys(target_hash)
            time.sleep(np.random.randint(2, 4))
            search_link.send_keys(Keys.ENTER)
            time.sleep(np.random.randint(2, 4))

            # TODO: randomize intervals
            self.random_scroll(step=30, speed=np.random.randint(12, 15), start=0, end=np.random.randint(400, 600))
            time.sleep(np.random.randint(2, 4))

            # TODO: randomize "count"
            if hotflag_l or hotflag_r:
                links = set()
                for _ in range(2):
                    time.sleep(np.random.randint(1, 4))
                    [
                        links.add(elem.get_attribute('href')) \
                        for elem in bot.find_elements_by_xpath("//a[@dir ='auto']")
                    ]
                # traversing through the generated links
                count = 0
                for link in links:
                    if "status" not in link: continue
                    if count > 4: break
                    bot.get(link)
                    time.sleep(np.random.randint(3, 5))
                    if hotflag_l:
                        try:
                            # like button selector
                             bot.find_element_by_css_selector(
                                '.css-18t94o4[data-testid ="like"]'
                             ).click()
                             time.sleep(np.random.randint(3, 5))
                        except:
                            time.sleep(np.random.randint(1, 4))
                    if hotflag_r:
                        try:
                            # like button selector
                             #bot.find_element_by_css_selector(
                             #   '.css-18t94o4[data-testid ="retweet"]'
                             #).click()
                             #time.sleep(np.random.randint(1, 2))
                            # bot.find_element_by_css_selector(
                            #    '.css-1dbjc4n[data-testid ="retweetConfirm"]'
                            # ).click()
                             time.sleep(np.random.randint(3, 5))
                        except:
                            time.sleep(np.random.randint(1, 4))
                    count += 1
            # ==========================================================================================================
            # ============================================= Connection =================================================
            # ==========================================================================================================
            home_link = bot.find_element_by_xpath('//a[@href="/home"]')             # ========= CONNECTION ============
            home_link.click()                                                       # ========= CONNECTION ============
            explore_link = bot.find_element_by_xpath('//a[@href="/explore"]')       # ========= CONNECTION ============
            explore_link.click()                                                    # ========= CONNECTION ============
            time.sleep(np.random.randint(2, 4))                                     # ========= CONNECTION ============
            search_link = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div[2]/input')                                                                       # ========= CONNECTION ============
            search_link.send_keys(target_hash)                                      # ========= CONNECTION ============
            time.sleep(np.random.randint(2, 4))                                     # ========= CONNECTION ============
            search_link.send_keys(Keys.ENTER)                                       # ========= CONNECTION ============
            time.sleep(np.random.randint(2, 4))                                     # ========= CONNECTION ============
            # ==========================================================================================================
            # ==========================================================================================================
            # ==========================================================================================================

