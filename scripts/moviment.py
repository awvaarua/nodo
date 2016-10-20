import urllib2, json, time, sys, os, time
from uuid import getnode as get_mac
import threading, RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
PIR_PIN = 18
GPIO.setup(PIR_PIN, GPIO.IN)

url = "http://192.168.2.81:8080/data/add"
data = {
        "fichero": os.path.basename(__file__),
        "mac": get_mac()
        }


mutex = threading.Semaphore(1)
deteccion_sensores = [False, False]

espera_cancelacion = sys.arg[1]
espera_nuevo_aviso = sys.arg[2]

def Cancelar(posicion, tiempo):
        global deteccion_sensores
        global mutex

        time.sleep(tiempo)
        mutex.acquire()
        deteccion_sensores[posicion] = False
        mutex.release()

def Deteccion(posicion):
        global deteccion_sensores
        global mutex

        mutex.acquire()
        deteccion_sensores[posicion] = True
        mutex.release()

def Comprobar():
        global deteccion_sensores
        global mutex

        mutex.acquire()
        for val in deteccion_sensores:
                if val == False:
                        mutex.release()
                        return
        mutex.release()
        #Enviar aviso
        deteccion_sensores.full((1, len(deteccion_sensores)), False, dtype=bool)


def Movimiento_Infrarojos(posicion, espera_cancelacion, espera_nuevo_aviso):
        while True:
                if GPIO.input(PIR_PIN):
                        time.sleep(1)
                        Deteccion(posicion)
                        Comprobar()
                        Cancelar(posicion, espera_cancelacion)
                        time.sleep(espera_nuevo_aviso)
                else:
                        time.sleep(1)

def Sonido(posicion, espera_cancelacion, espera_nuevo_aviso):
        pass

if __name__ == "__main__":
        infrarojos = threading.Thread(target = Movimiento_Infrarojos, args = (0, espera_cancelacion, espera_nuevo_aviso))
        sonido = threading.Thread(target = Sonido, args = (1, espera_cancelacion, espera_nuevo_aviso))
        infrarojos.start()
        sonido.start()
        infrarojos.join()        
        sonido.join()