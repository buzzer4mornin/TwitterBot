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
