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
