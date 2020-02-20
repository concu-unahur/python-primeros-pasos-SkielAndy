import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

cant= 1
lock = threading.Lock()
def sumarUno():
    global cant
    global lock
    lock.acquire()
    try:
        cant += 1
    finally:
       lock.release()
def multPorDos():
    global cant
    global lock
    lock.acquire()
    try:
        cant *= 2
    finally:
        lock.release() 
def divPorDos():
    global cant
    global lock
    lock.acquire()
    try:
        cant /= 2
    finally:
        lock.release()
t1 = threading.Thread(target=divPorDos)
t2 = threading.Thread(target=sumarUno)
t3 = threading.Thread(target=sumarUno)
t4 = threading.Thread(target=sumarUno)
t5 = threading.Thread(target=divPorDos)
logging.info(f'cant vale {cant}')
t1.start()
logging.info(f'cant vale {cant}')
t2.start()
logging.info(f'cant vale {cant}')
t3.start()
logging.info(f'cant vale {cant}')
t4.start()
logging.info(f'cant vale {cant}')
t5.start()
logging.info(f'cant vale {cant}')