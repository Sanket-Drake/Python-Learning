from threading import Timer
import time
import sys
from time import sleep
import mraa
import requests

sys.stdout.write("Initializing UART...")				
u=mraa.Uart(0)
print("...done")
print("Setting UART parameters: baudrate 57600, 8N1, no flow control")
u.setBaudRate(57600)
u.setMode(8, mraa.UART_PARITY_NONE, 1)
u.setFlowcontrol(False, False)

list1 = [];
command_sensor = [0x24]				
msg = bytearray(command_sensor)

def loop():
	u.write(msg)
	print "asked"
	sleep(2)
	if u.dataAvailable(100):
		while u.dataAvailable():
			data_byte = u.readStr(1)
			value = int(data_byte.encode('hex'), 16)
			print "value : " , value
			#sleep(1)
			list1.append(value);
	print list1
	sleep(10)

while True:
	# Start a neverending loop waiting for data to arrive.
	# Press Ctrl+C to get out of it

	loop()
