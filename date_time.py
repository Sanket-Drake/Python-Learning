#Experiment with time data
from threading import Timer
import time
import sys
from time import sleep
import mraa
import requests
import os
import subprocess
from datetime import datetime , date , time

def restart():
	command = "date +%X"
	import subprocess
	process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
	output = process.communicate()[0]
	print output
	print "date" ,output[0],output[1],output[3],output[4]
	print (int(output[0])*10+int(output[1]))+4
	#s=os.system("date")
	#print "date" , s
	today = datetime.now()
	print today
	tt = today.timetuple()
	#sleep(10)
	today = datetime.now()
	print today
	tt = today.timetuple()
	print tt
	if(tt[4]>30):
		mins=tt[4]-30
		hours=tt[3]+1
	else:
		mins=tt[4]+30
	if(tt[3]>18):
		hours=tt[3]-19
	else:
		hours=tt[3]+5
	print hours,":",mins
	for it in tt:
		print it


def loop():
	restart()
	print "going down for restart"
	sleep(8)


while True:
	# Start a neverending loop waiting for data to arrive.
	# Press Ctrl+C to get out of it

	loop()
