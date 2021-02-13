'''
Script to make you join whatever meet you have at that time with mic and cam muted
@Rutwij
'''

#Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import ctypes

#Some Initializations
xJOIN = "//*[@id=\"yDmH0d\"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]"
daysOfWeek = {'M':0, 'T':1, 'W':2, 'Th':3, 'F':4, 'S':5} #Sunday Skipped

#Option Config
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\rutwi\\AppData\\Local\\Google\\Chrome\\User Data")

#Driver Instance
driver = webdriver.Chrome(options=options)

#Open Google Meet
def openGmeet(link):
    driver.get(link)
    time.sleep(5)

    action = webdriver.ActionChains(driver)
    action.key_down(Keys.CONTROL).send_keys('d').send_keys('e').key_up(Keys.CONTROL).perform()

    join_button = driver.find_element_by_xpath(xJOIN)
    join_button.click()

#Parse Timetable
def checkClass():
    now = datetime.now()
    DAY = now.weekday() # Monday-Sunday = 0-6
    TIME = now.strftime("%H%M") # 24-format HHMM

    data = open("timetable.txt").read()
    classes = data.split('\n')

    for course in classes:
        details = course.split(';')
        if(int(TIME) > int(details[3]) and int(TIME) < int(details[4])):
            class_days = details[2].split(' ')
            for day in class_days:
                if(daysOfWeek[day] == DAY):
                    return details[0], details[1]

    return None, None

#Alert Box
def Mbox(text):
    return ctypes.windll.user32.MessageBoxW(0, text, "GMeet Opener", 0)

#MAIN
course, link = checkClass()

if(course == None):
    driver.quit()
    Mbox("You have no class scheduled")
else:
    openGmeet(link)
    text = "Joined meet link for " + course + "."
    Mbox(text)