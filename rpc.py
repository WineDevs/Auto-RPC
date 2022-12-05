from resources import *
from pypresence import Presence,exceptions
from utils import pause
import time
client_id = '1048337473614393344'
try:
    RPC = Presence(client_id)
except exceptions.DiscordNotFound:
    print(Discord_Not_Found_Error)
    pause()
    quit()

RPC.connect()#Connect to Discord


print(RPC_Connected_Info)


def set_rpc(app: str, use_stopwatch=False,custom_name=None):
    start_time=time.time()
    if app!='none':
        print('Switch to: '+app.capitalize())
        if not use_stopwatch:
            RPC.update(details=f"I'm in {app.capitalize()}!",large_image=f'{app}_logo',large_text=app.capitalize())
        if use_stopwatch:
            RPC.update(details=f"I'm in {app.capitalize()}!",large_image=f'{app}_logo',large_text=app.capitalize(),start=start_time)

        if custom_name!=None and use_stopwatch:
            RPC.update(details=f"I'm in {custom_name}!", large_image=f'{app}_logo', large_text=app.capitalize(),start=start_time)
        elif custom_name!=None and not use_stopwatch:
            RPC.update(details=f"I'm in {custom_name}!",large_image=f'{app}_logo', large_text=app.capitalize())
            
    else:
        print('Switch to: '+app.capitalize())
        RPC.update(details=Auto_RPC_None_Warning, large_image=f'{app}_logo', large_text=app.capitalize())
