import os,sys,shutil,time

os.chdir(sys.path[0])#cd to currect dir

if os.path.isfile('./main.exe'):
    os.remove('main.exe')#Delete previous build

def build():
    os.system('nuitka main.py')#build with nuitka

def clear():
    for f in ['main.cmd','main.build']:#Files
        if os.path.isfile(f):
            os.remove('./'+f)#Delete file
        elif os.path.isdir(f):
            shutil.rmtree(f)#Delete tree

def set_icon():
    os.system('rcedit.exe main.exe --set-icon "assets\\auto_rpc_logo.ico"')#add icon to exe

def rename():
    os.rename('./main.exe','./Auto_RPC.exe')#Rename exe

build()#Build
time.sleep(3)#Wait 3 seconds
clear()#delete unused folders, files
set_icon()#Set icon to exe
rename()#Rename exe file

#Auto Build?