#A python program and library to check wifi connection status

from threading import Timer
import time
import sys
from time import sleep
import mraa
import requests
#from wireless import Wireless
from pythonwifi.iwlibs import Wireless

wifi = Wireless('apcli0')

#wireless = Wireless()

def connected_to_internet(url='http://www.google.com/', timeout=5):
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("No internet connection available.")
    return False

def loop():
	#wifi.getEssid()
	#a = wireless.interfaces()
	#print a
	a = wifi.getEssid()
	if(a != ""):
		print "WIFI",a
	if(a == ""):
		print "NO WIFI",a
	sleep(8)


while True:
	# Start a neverending loop waiting for data to arrive.
	# Press Ctrl+C to get out of it

	loop()
