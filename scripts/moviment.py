import urllib2, json, time, sys, os, time
from uuid import getnode as get_mac
import threading, RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
PIN_MOVIMIENTO = int(sys.argv[1])
GPIO.setup(PIN_MOVIMIENTO, GPIO.IN)

url = "http://"+ip+"/data/add"
data = {
        "fichero": os.path.basename(__file__),
        "mac": get_mac()
        }
espera_nuevo_aviso = float(sys.argv[2])


def Movimiento_Infrarojos(espera_nuevo_aviso):
        while True:
                if GPIO.input(PIN_MOVIMIENTO):
                        time.sleep(0.5)
                        print "Movimiento"
                        time.sleep(espera_nuevo_aviso)
                else:
                        time.sleep(1)
                        

if __name__ == "__main__":
        Movimiento_Infrarojos(espera_nuevo_aviso)