#Experiment with class and objects and File read/write
from threading import Timer
import time
import sys
from time import sleep
import mraa
import requests
from wireless import Wireless
from pythonwifi.iwlibs import Wireless
import cPickle as pickle

#f = open ('testfile.txt','rwb')

class Data(object):
	name = "obj"
	def __init__(self, x,y,z):
		self.a=x
		self.b=y
		self.c=z

sanket = Data(1,2,3)
 
def loop():
	#wifi.getEssid()
#	a = wireless.interfaces()
#	print a
	
	#print sanket.c
	lists = []

	with open('testfile.txt', 'wb') as output:
	
		company1 = Data(32,56,21)
		pickle.dump(company1, output, pickle.HIGHEST_PROTOCOL)

		company1 = Data(3,5,9)
		pickle.dump(company1, output, pickle.HIGHEST_PROTOCOL)

		company1 = Data(13,15,9)
		pickle.dump(company1, output, pickle.HIGHEST_PROTOCOL)

		company1 = Data(23,25,9)
		pickle.dump(company1, output, pickle.HIGHEST_PROTOCOL)

		company1 = Data(33,35,9)
		pickle.dump(company1, output, pickle.HIGHEST_PROTOCOL)

		company1 = Data(43,45,9)
		pickle.dump(company1, output, pickle.HIGHEST_PROTOCOL)

	del company1
	#del company2

	with open('testfile.txt', 'rb') as input:
		eof = 0
		index = 0
		while(eof==0):
			try:
				lists.append(pickle.load(input))
				print(lists[index].a)  # -> banana
				print(lists[index].b)  # -> 40
				index+=1
			except EOFError:
				eof=1
				print " Eof Dectected"
		print "all printed"

		for index in range(len(lists)):
			del lists[0];
		#lists.append(pickle.load(input))
		#print(lists[0].a)  # -> banana
		#print(lists[0].b)  # -> 40

		#company2 = pickle.load(input)
		#print(company2.a) # -> spam
		#print(company2.b)  # -> 42
	
		#try:
		#	company3 = pickle.load(input)
		#except EOFError:
		#	print " Eof Dectected"

		#print(company3.a) # -> spam
		#print(company3.b)  # -> 42

	sleep(5)



while True:
	# Start a neverending loop waiting for data to arrive.
	# Press Ctrl+C to get out of it

	loop()