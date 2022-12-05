import win32gui, win32process, win32con, psutil
from time import sleep as wait
from threading import Thread
from resources import logo
from ctypes import WinDLL
from utils import *
from rpc import *
import webbrowser
import PIL.Image
import platform
import requests
import pystray
import os

if platform.system().lower() != 'windows':
    print("Sorry, this program doesn't support Linux systems")
    quit()

if not os.path.isdir('./assets'):
    os.mkdir('./assets')
if not os.path.isfile('./assets/auto_rpc_logo.png'):
    with open('./assets/auto_rpc_logo.png','wb') as lg:
        lg.write(logo)

def active_window_process_name():
    try:
        pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
        return(psutil.Process(pid[-1]).name())
    except:
        pass

apps = None#This for IDE to remove errors
exec('apps = '+requests.get('https://raw.githubusercontent.com/purpl3-yt/trash-bin/main/apps.py').text)#apps

#vars
currect_window = ''
stop = False
show = True
debug = False
delay = 3
#Main program
class Main(Thread):
    def run(self):
        global currect_window,stop,debug
        while True:
            if stop:
                break
            window = active_window_process_name()
            if debug:
                print(window,'X: '+str(getMousePosition()['x']),'Y: '+str(getMousePosition()['y']))
            
            try:
                if currect_window!=str(window.lower()):
                    print('Foreground window process: '+window)
                    currect_window=window.lower()
                    dict_window = apps[str(window.lower())]
                    try:
                        window_custom_name = apps[str(window.lower())][2]
                    except IndexError:
                        set_rpc(dict_window[0],dict_window[1])
                    else:
                        set_rpc(dict_window[0],dict_window[1],window_custom_name)    
            except KeyError:
                set_rpc('none')
            wait(int(delay))

main = Main()#define

kernel32 = WinDLL('kernel32')
user32 = WinDLL('user32')
hWnd = kernel32.GetConsoleWindow()

def Hide():
    user32.ShowWindow(hWnd, win32con.SW_HIDE)
def Show():
    user32.ShowWindow(hWnd, win32con.SW_SHOW)

def Creator():
    webbrowser.open('https://github.com/purpl3-yt')

image = PIL.Image.open('./assets/auto_rpc_logo.png')

icon = pystray.Icon('Neural', image, menu=pystray.Menu(
    pystray.MenuItem('Hide',Hide),
    pystray.MenuItem('Show',Show),
    pystray.MenuItem('Creator',Creator)
))

def run_icon(icon):
    icon.run()


def MainMenu():
    global delay,stop,debug
    print(getlogo()+'\n')
    pause()
    while True:
        cls()
        if stop:
            break
        mode = str(input('1) Start \n2) Settings\nSelect: '))

        if mode in ['y','true','yes','1','да','н']:
            input('To stop press ctrl+c or close window! ')
            cls()
            main.start()
            break

        elif mode in ['set','settings','2','ыуеештпы','ыуе']:
            print('Settings!')
            while True:
                cls()
                settings = str(input('''
1) Delay
2) Debug
3) Exit
Enter: '''))

                if settings=='1':
                    print('Default: 3\nCurrent: '+str(delay))
                    new_delay = input('New delay: ')
                    if new_delay.isdigit():
                        delay=new_delay
                        pause()
                    else:
                        print('Enter digits!')
                        pause()
                elif settings=='2':
                    if debug:
                        debug=False
                        print('Debug off')
                        pause()
                    elif not debug:
                        debug=True
                        print('Debug on')
                        pause()
                elif settings=='3':
                    break


if __name__ == '__main__':
    ticon = Thread(target=run_icon,args=(icon,))
    ticon.daemon = True
    ticon.start()

    TMainMenu = Thread(target=MainMenu)
    TMainMenu.start()