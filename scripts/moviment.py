import urllib2, json, time, sys, os
from uuid import getnode as get_mac
import RPi.GPIO as GPIO
import time
from time import gmtime, strftime
GPIO.setmode(GPIO.BCM)
PIR_PIN = 18
GPIO.setup(PIR_PIN, GPIO.IN)

data = {
        "fichero": os.path.basename(__file__),
        "mac": get_mac()
        }
url = "http://192.168.2.81:8080/data/add"

try:
    while True:
        if GPIO.input(PIR_PIN):
                time.sleep(1)
                req = urllib2.Request(url)
                req.add_header('Content-Type', 'application/json')
                response = urllib2.urlopen(req, json.dumps(data))
                time.sleep(0.5)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()