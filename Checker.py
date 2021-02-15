'''Parse Timetable'''

from datetime import datetime
import time

daysOfWeek = {'M':0, 'T':1, 'W':2, 'Th':3, 'F':4, 'S':6} #Sunday Skipped

def checkClass():
    now = datetime.now()
    DAY = now.weekday() # Monday-Sunday = 0-6
    TIME = now.strftime("%H%M") # 24-format HHMM

    data = open("timetable.txt").read()
    classes = data.split('\n')

    for course in classes:
        details = course.split(';')
        if(int(TIME) >= int(details[3]) and int(TIME) <= int(details[4])):
            class_days = details[2].split(' ')
            for day in class_days:
                if(daysOfWeek[day] == DAY):
                    return details[0], details[1], details[4]

    return None, None, None

def loopTill(endTime):
    isClassOver = False
    while(not isClassOver):
        time.sleep(5)
        now = datetime.now()
        TIME = now.strftime("%H%M")

        if(int(TIME) >= int(endTime)):
            isClassOver = True
    return