import ibmiotf.device
from time import sleep
import json

# Trying to establish a connection
try:
	options = {
	"org": "org",
	"id": "device_id",
	"auth-method": "token",
	"auth-token": "password"
	}
	client = ibmiotf.device.Client(options)
except ibmiotf.ConnectionException  as e:
	print(str(e))
	# sys.exit()

#Checking connection before sending a data
client.connect()
send_payload =  { "data": { "time": "1466168010", "sensor1": "47", "sensor2": "207", "sensor3": "20"} }
try:
	client.publishEvent("data", "json", send_payload)
except exceptions.TypeError:
	print "data not sent"
print "data sent"
# client.commandCallback = myCommandCallback
while True:
	sleep(1)
