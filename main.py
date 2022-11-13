import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
ID = ''
PASSWORD = ''
PROMISED_DOWN = 150
PROMISED_UP = 10

chrome_driver = 'D:/chrome driver/chromedriver.exe'

speed_url = 'https://www.speedtest.net/'


class TwitterBot:

    def __init__(self, driver_path):

        self.driver = webdriver.Chrome(executable_path=driver_path)

        self.DOWN_SPEED = 0
        self.UP_SPEED = 0
        sleep(15)

    def get_internet_speed(self):
        global PROMISED_UP, PROMISED_DOWN
        self.driver.get(speed_url)
        press = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        press.click()
        sleep(30)
        press_cross = self.driver.find_element_by_xpath('')
        press_cross.click()
        sleep(120)
        down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/'
                                                 'div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/'
                                                 'div[2]/div[1]/div[2]/div/div[2]/span')
        self.DOWN_SPEED = float(down.text)

        up = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
            'div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        self.UP_SPEED = float(up.text)

        print(f'Down Speed: {self.DOWN_SPEED}\nUp Speed: {self.UP_SPEED}')

        if self.DOWN_SPEED < PROMISED_DOWN or self.UP_SPEED < PROMISED_UP:
            return True

    def tweet(self):
        self.driver.get('https://twitter.com')
        sleep(30)
        button = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/a/div/span/span')
        button.click()
        sleep(5)
        number_login = self.driver.find_element_by_xpath('/html/body/div/div/div/div/'
                                                         'main/div/div/div/div[1]/div/div[3]/a')
        number_login.click()

        try:
            number = self.driver.find_element_by_xpath(
                '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
            number.send_keys(ID)
            password = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
            password.send_keys(PASSWORD)
            password.send_keys(Keys.ENTER)

        except selenium.common.exceptions.NoSuchElementException:
            try:
                login_button = self.driver.find_element_by_xpath('/html/body/div/div/'
                                                                 'div/div/main/div/div/'
                                                                 'div/div[1]/div/div[3]/a[2]')
            except selenium.common.exceptions.NoSuchElementException:

                sleep(5)
                number = self.driver.find_element_by_xpath(
                    '//*[@id="layers"]/div/div/div/div/div/div/div[2]/'
                    'div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/'
                    'label/div/div[2]/div/input')
                number.send_keys(ID)
                number.send_keys(Keys.ENTER)
                sleep(5)
                password = self.driver.find_element_by_xpath(
                    '//*[@id="layers"]/div[2]/div/div/div/div/div/'
                    'div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/'
                    'div[2]/div/label/div/div[2]/div/input')
                password.send_keys(PASSWORD) #your password
            else:
                number = self.driver.find_element_by_xpath(
                    '/html/body/div/div/div/div[2]/main/div/div/'
                    'div[2]/form/div/div[1]/label/div/'
                    'div[2]/div/input')
                number.send_keys(ID) #your id
                password = self.driver.find_element_by_xpath(
                    '//*[@id="react-root"]/div/div/div[2]'
                    '/main/div/div/div[2]/form/div/div[2]/'
                    'label/div/div[2]/div/input')
                password.send_keys(PASSWORD) #your password
                password.send_keys(Keys.ENTER)

            password.send_keys(Keys.ENTER)
        sleep(10)
        tweeting = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/'
                                                     'div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div'
                                                     '/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div'
                                                     '/div/div/div')
        tweeting.send_keys(f'Dear provider\n {self.DOWN_SPEED} is less than promised download speed of '
                           f'{PROMISED_DOWN}\n'
                           f'and\n{self.UP_SPEED} is less than promised upload speed of {PROMISED_UP} ')
        TWEET = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/'
                                                  'div[2]/div/div[2]/''div[1]/div/div/div/div[2]/'
                                                  'div[3]/div/div/div[2]/div[3]')
        TWEET.click()


bot = TwitterBot(chrome_driver)

to_tweet = bot.get_internet_speed()

if to_tweet:
    bot.tweet()
