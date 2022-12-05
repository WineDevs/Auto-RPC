from ctypes import windll, Structure, c_long, byref
import time
import os,re

def pause():
    os.system('pause')

def cls():
    os.system('cls')

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

def getMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return {'x': pt.x, 'y': pt.y}

def ifAfk(seconds_to_check: int):#Return true if user in afk, else false
    last_x = getMousePosition()['x']
    last_y = getMousePosition()['y']
    for wait in range(seconds_to_check):
        time.sleep(1)
        x = getMousePosition()['x']
        y = getMousePosition()['y']

    if x in range(last_x-10,last_x+10) and y in range(last_y-10,last_y+10):#If user in afk
        return True
    else:
        return False

def getlogo():
    return '''
    _   _   _ _____ ___    ____  ____   ____ 
   / \ | | | |_   _/ _ \  |  _ \|  _ \ / ___|
  / _ \| | | | | || | | | | |_) | |_) | |    
 / ___ \ |_| | | || |_| | |  _ <|  __/| |___ 
/_/   \_\___/  |_| \___/  |_| \_\_|    \____|
By Purpl3
'''
