from haasomeapi.HaasomeClient import HaasomeClient
import configparser_cos as cp

class Connect:
	
	def __init__(self, ip, secret):
		pass

	# Verifying config file settings at launch
	def verify_config():
		configverified = False
		if configverified == False:
			cp.verifyconfigfile()
			configverified = True
	
	#Compiling the connectionstring
	def connect():
		haasomeClient = HaasomeClient(ip, secret)
