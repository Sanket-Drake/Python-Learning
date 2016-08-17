import time
from time import sleep

def loop():
	timestamp = int(time.time())	#Getting epoch time stamp
	print timestamp
	sleep(5)

while True:
	loop()