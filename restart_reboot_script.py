#Restarting a system from a command line event 
from threading import Timer
import time
import sys
from time import sleep
import mraa
import requests
from wireless import Wireless
import os
import subprocess

def rebootscript():
    print "rebooting system"
    command = "/sbin/reboot"
    subprocess.call(command, shell = True)

def restart():
    command = "reboot"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print output
    os.system("reboot")


def loop():
	rebootscript()
	print "going down for restart"
	sleep(8)


while True:
	# Start a neverending loop waiting for data to arrive.
	# Press Ctrl+C to get out of it

	loop()
