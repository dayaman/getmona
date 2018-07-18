import threading
from time import sleep
from getmona.models import init
from getmona.seeds import addpair
from getmona.zaifapi import start_threading
from getmona.ueshita import loop_get
from getmona.tweet import get_reply

def create_models():
    init()
    addpair()
    
def preparation():
    threading_a = threading.Thread(target=start_threading)
    threading_b = threading.Thread(target=loop_get)
    threading_c = threading.Thread(target=get_reply)
    threading_a.start()
    sleep(2)
    threading_b.start()
    threading_c.start()

