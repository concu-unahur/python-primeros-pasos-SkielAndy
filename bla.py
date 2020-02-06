import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

def dormir():
    logging.info("empezando desde funcion")
    time.sleep(1)
    logging.info("finalizando desde funcion")

t1 = threading.Thread(target=dormir , name= "tread desde funcion")
t1.start()

class Unthread(threading.Thread): 
    #Entre los parentesis va la superclase de la que hereda.
    def __init__(self):
        super().__init__() # inicializa el init de la super clase
        self.name= "threadClase"

    def run(self):
        logging.info("empezando desde clase")
        time.sleep(1)
        logging.info("finalizando desde clase")

t2 = Unthread()
t2.start() 
#Esto se ejecuta llamando al run de la clase .Si no hay run , no hace nada.