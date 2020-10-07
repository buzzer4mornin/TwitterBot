from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import pyautogui
'''Uncomment the below line when running in linux'''
# from pyvirtualdisplay import Display
import time, os


class Twitterbot:

    def __init__(self, email, password, quote):

        """Constructor

        Arguments:
            email {string} -- registered twitter email
            password {string} -- password for the twitter account
        """

        self.email = email
        self.password = password
        self.quote = quote
        # initializing chrome options
        chrome_options = Options()

        # adding the path to the chrome driver and
        # integrating chrome_options with the bot
        self.bot = webdriver.Chrome(
            executable_path=os.path.join(os.getcwd(), 'chromedriver'),
            options=chrome_options
        )

    def login(self):
        """
            Method for signing in the user
            with the provided email and password.
        """

        bot = self.bot
        # fetches the login page
        bot.maximize_window()

        bot.get('https://twitter.com/login')
        # adjust the sleep time according to your internet speed

        # TODO: DONE BY ME
        bot.implicitly_wait(10)
        #time.sleep(10)

        email = bot.find_element_by_css_selector(
            '#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-13qz1uu > form > div > div:nth-child(6) > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1udh08x > div > input'
        )
        password = bot.find_element_by_css_selector(
            '#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-13qz1uu > form > div > div:nth-child(7) > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1udh08x > div > input'
        )

        # sends the email to the email input
        email.send_keys(self.email)
        # sends the password to the password input
        password.send_keys(self.password)
        # executes RETURN key action
        password.send_keys(Keys.RETURN)

        #TODO: DONE BY ME
        bot.implicitly_wait(50)
        time.sleep(2)



    def like_retweet(self, hashtag):

        """
        This function automatically retrieves
        the tweets and then likes and retweets them

        Arguments:
            hashtag {string} -- twitter hashtag
        """

        bot = self.bot
        bot.implicitly_wait(50)
        # fetches the latest tweets with the provided hashtag
        bot.get(
            'https://twitter.com/search?q=%23' + \
            hashtag + '&src=typed_query&f=live'
        )

        time.sleep(3)

        # using set so that only unique links
        # are present and to avoid unnecessary repetition
        links = set()

        # obtaining the links of the tweets
        for _ in range(2):
            # executing javascript code
            # to scroll the webpage
            bot.execute_script(
                'window.scrollTo(0, document.body.scrollHeight)'
            )

            time.sleep(4)

            # using list comprehension
            # for adding all the tweets link to the set
            # this particular piece of code might
            # look very complicated but the only reason
            # I opted for list comprehension because is
            # lot faster than traditional loops
            [
                links.add(elem.get_attribute('href')) \
                for elem in bot.find_elements_by_xpath("//a[@dir ='auto']")
            ]

            # traversing through the generated links
        for link in links:
            # opens individual links
            bot.get(link)
            time.sleep(4)

            try:
                '''# retweet button selector
                bot.find_element_by_css_selector(
                    '.css-18t94o4[data-testid ="retweet"]'
                ).click()'''
                # initializes action chain
                actions = ActionChains(bot)
                # sends RETURN key to retweet without comment
                actions.send_keys(Keys.RETURN).perform()

                # like button selector
                bot.find_element_by_css_selector(
                    '.css-18t94o4[data-testid ="like"]'
                ).click()
                # adding higher sleep time to avoid
                # getting detected as bot by twitter
                time.sleep(10)
            except:
                time.sleep(2)

                # fetches the main homepage
        bot.get('https://twitter.com/')

    def post_tweet(self):
        bot = self.bot
        bot.implicitly_wait(50)
        bot.maximize_window()

        # TODO: first way
        tweet = bot.find_element_by_css_selector("br[data-text='true']")
        time.sleep(2)
        tweet.send_keys(self.quote)
        time.sleep(2)
        #tweet.send_keys(Keys.COMMAND + Keys.ENTER)

        #TODO: second way
        #tweet = bot.find_element_by_css_selector(".notranslate > div:nth-child(1) > div:nth-child(1)")
        #tweet = tweet.find_element_by_xpath("./div")
        #tweet.click()
        #tweet.send_keys("#StopArmenia")
        #time.sleep(2)
        #tweet.send_keys(Keys.COMMAND + Keys.ENTER)

        bot.save_screenshot('1111.png')



        #TODO: for Google Collab
        ''' def post_tweet(self):
        bot = self.bot
        bot.implicitly_wait(50)
        bot.maximize_window()
        
        tweet = bot.find_element_by_css_selector("br[data-text='true']")
        time.sleep(2)
        tweet.send_keys("tweetMessage")
        time.sleep(2)
        button = bot.find_element_by_css_selector("div[data-testid='tweetButtonInline']")
        button.click()
        time.sleep(2)

        bot.save_screenshot('screenshot.png')'''
