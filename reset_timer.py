# A manual restart Timer to avoid an infinite loop 
from threading import Timer
import time
import sys
from time import sleep
import mraa
import requests
import json
import os
import subprocess
from wireless import Wireless

#	Timer for data send on server
class RepeatedTimer(object):														
	def __init__(self, interval, function, *args, **kwargs):
		self._timer     = None
		self.interval   = interval
		self.function   = function
		self.args       = args
		self.kwargs     = kwargs
		self.is_running = False
		self.start()

	def _run(self):
		self.is_running = False
		self.start()
		self.function(*self.args, **self.kwargs)

	def start(self):
		if not self.is_running:
			self._timer = Timer(self.interval, self._run)
			self._timer.start()
			self.is_running = True

	def stop(self):
		self._timer.cancel()
		self.is_running = False

def timeout():
	print "restarting"

#   Initializing Continuous Iterating Timer
rt = RepeatedTimer(60, timeout)
rt.stop()
run = 0

def loop():
	global run
	run+=1
	print run
	sleep(15)
	rt.start()
	if(run==3):
		rt.stop()

	

while True:
	# Start a neverending loop waiting for data to arrive.
	# Press Ctrl+C to get out of it

	loop()
