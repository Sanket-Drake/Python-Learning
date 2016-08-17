#Checking Internet Connection
from threading import Timer
import time
import sys
from time import sleep
import mraa
import requests
from wireless import Wireless

#wireless = Wireless()

def connected_to_internet(url='http://www.google.com/', timeout=1):
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("No internet connection available.")
    return False

def loop():
	#wifi.getEssid()
#	a = wireless.interfaces()
#	print a
	a = connected_to_internet()
	print a
	sleep(8)


while True:
	# Start a neverending loop waiting for data to arrive.
	# Press Ctrl+C to get out of it

	loop()
