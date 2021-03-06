import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

cant= 3
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
logging.info(f'cant vale {cant}')
t1.start()
logging.info(f'cant vale {cant}')
t2.start()
logging.info(f'cant vale {cant}')
