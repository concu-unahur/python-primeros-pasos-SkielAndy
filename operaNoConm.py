import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

num= 0
def sumarUno():
    global num
    num+=1
def multiplicarPor2():
    global num
    num=num*2

r1= threading.Thread(target= sumarUno,name="hilo de suma")
r2= threading.Thread(target= multiplicarPor2,name="hilo de multiplicacion")
r1.start()
r2.start()
print(f'el resultado es {num}')
