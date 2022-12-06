import os,sys,glob
out_folder = './out'
main_script = './main.py'

#Build script from our launcher, https://github.com/WineDevs/Wine-Launcher

def build():
    #os.system(sys.path[0]+'\\venv\\Scripts\\activate.bat')#use venv to low exe size
    os.system(f'pyinstaller --noconfirm --onefile --console --clean --distpath "{out_folder}" --icon "./assets/auto_rpc_logo.ico" --name "Auto_RPC"  "{main_script}"')

def clear_cache():#delete unused files
    all_specs = glob.glob('./*.spec')
    for spec in all_specs:
        os.remove(spec)
    os.remove('./build')

if '__main__' == __name__:
    build()#build
    clear_cache()#clear cache etc