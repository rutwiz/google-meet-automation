'''
Script to make you join whatever meet you have at that time with mic and cam muted
@Rutwij
'''

#Imports
import ctypes
import sys
import os

#File Imports
import Checker
import StartDriver

#Alert Box
def Mbox(text, style): #Style: (0 = Ok) (4 = Yes/No)
    return ctypes.windll.user32.MessageBoxW(0, text, "GMeet Opener", style)

#MAIN
course, link, endTime = Checker.checkClass()
if(course == None):
    Mbox("You have no class scheduled", 0)
else:
    StartDriver.start()
    StartDriver.openGmeet(link)
    text = "Joined meet link for " + course + ". Do you want to enable autoclose for this class at " + endTime + "?" 
    response = Mbox(text, 4)
    if(response == 6): #6 is the ID for YES. Check end of script for more info.
        StartDriver.autoClose(endTime)

sys.exit()

# ctypes messagebox return values
# MB_OK = 0
# MB_OKCANCEL = 1
# MB_YESNOCANCEL = 3
# MB_YESNO = 4
# IDOK = 0
# IDCANCEL = 2
# IDABORT = 3
# IDYES = 6
# IDNO = 7