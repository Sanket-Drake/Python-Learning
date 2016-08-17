from threading import Timer
import time
import sys
from time import sleep
import mraa  

i2c = mraa.I2c(0)  
i2c.address(0x10)


def loop():
	d = i2c.writeByte(65)
	print "d : ",(str(d))
	sleep(5)

while True:
	# Start a neverending loop waiting for data to arrive.
	# Press Ctrl+C to get out of it

	loop()
