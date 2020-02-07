import threading
import time
import logging

from tiempo import Contador

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

# la función para usar para el thread
def dormir():
    time.sleep(1)
#forma hecha clasica por nosotros

'''tiempo=0
for i in range(10):
    t=Contador()
    t.iniciar()
    i=threading.Thread(target=dormir , name= "tread desde funcion")
    i.start()
    i.join()
    t.finalizar()
    t.imprimir()
    tiempo+=t.numero()
print('pasaron en total',tiempo,'segundos')'''

#forma del profesor, mucho mas simple

y=Contador()
y.iniciar()
lista=[]#lista vacia
for i in range(10):
    i=threading.Thread(target=dormir , name= "tread desde funcion")
    i.start()
    lista.append(i)
    #i.join()
for thread in lista:
    thread.join()
y.finalizar()
y.imprimir()
