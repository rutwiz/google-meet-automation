#Module Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#File Import
import Checker

#Some Initializations
xJOIN = "//*[@id=\"yDmH0d\"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]"
driver = None

#Option Config
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\rutwi\\AppData\\Local\\Google\\Chrome\\User Data")

#Driver Instance
def start():
    global driver
    driver = webdriver.Chrome(options=options)

#Open Google Meet
def openGmeet(link):
    driver.get(link)
    time.sleep(5)

    action = webdriver.ActionChains(driver)
    action.key_down(Keys.CONTROL).send_keys('d').send_keys('e').key_up(Keys.CONTROL).perform()

    join_button = driver.find_element_by_xpath(xJOIN)
    join_button.click()

def autoClose(endTime):
    Checker.loopTill(endTime)
    driver.quit()

