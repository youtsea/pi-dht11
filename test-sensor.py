# -*- coding: utf-8 -*-
from sensor.dht11 import HTSensor,ReadError
import time

while True:
    try:
        yolo = HTSensor(12)
        humidity, temperature = yolo.read()
        print "Humidity:%s, Temperature:%s" % (humidity,temperature)
    except ReadError:
        print "Read failed"
    finally:
	time.sleep(0.5)
        yolo.cleanup()
