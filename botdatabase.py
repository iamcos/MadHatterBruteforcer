

import botsellector
import configparser_cos
import configserver
import json
from io import StringIO
import base64, zlib, gzip

from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
import pickle

import jsonpickle
from haasomeapi.HaasomeClient import HaasomeClient
ip, secret = configserver.validateserverdata()
haasomeClient = HaasomeClient(ip, secret)



class BotDB:
	def __init__(self, bot, dbfile):
		self.bot = botlist
		self.dbfile = dbfile

	def save_bot(bot,dbfile):
				frozen = jsonpickle.encode(bot)
				with open(dbfile,'ab') as botsconfig_file:
					pickle.dump(frozen, botsconfig_file)

	def save_bots(botlist,dbfile):
			frozenobjlist = []
			for i, bot in enumerate(botlist):
				frozen = jsonpickle.encode(bot)
				frozenobjlist.append(frozen)
			with open(dbfile,'wb') as botsconfig_file:
					pickle.dump(frozenobjlist, botsconfig_file)

	def load_botlist(dbfile):
		restored = []
		with open(dbfile, 'rb') as botsconfig_file:
			botlist = pickle.load(botsconfig_file)
			for i in botlist:
				unfreeze = jsonpickle.decode(i)	
				# print(unfreeze.name, unfreeze.priceMarket.primaryCurrency,unfreeze.priceMarket.secondaryCurrency,)
				restored.append(unfreeze)
		return restored

def jsavebot(bot,file):
	with open(file,'w') as f:
		botstring = json.dump(bot,f)
		print(botstring)

def print_bot_as_string(bot):
		toremove = ['accountId','botLogBook','groupName','guid','messageProfile','notes','name','activated','activatedSince','amountDecimals',''] # need to do the opposite
		data = jsonpickle.encode(bot)
		
		print(data)

def make_bot_from_string(string):
	pass
def jsavebots(botlist,file):
	frozenobjlist = []
	for i, bot in enumerate(botlist):
		frozen = json.dumps(bot)
		frozenobjlist.append(frozen)
	with open(file,'w') as f:
		json.dump(frozenobjlist,f)

def jloadbots(file):
		with open(file,'r') as f:
			bots = json.load(f)
			return

def print_keys(kl):
		if kl == i.bBands.keys():
			for key in kl:
				print('config.bBands[\''+key+'\']')
		if kl == i.macd.keys():
			for key in kl:
				print('config.macd[\''+key+'\']')
		if kl == i.rsi.keys():
			for key in kl:
				print('config.rsi[\''+key+'\']')

def main():
	# botsagain = jloadbots('bots.db')
	# print(botsagain)
	# botlist = botsellector.botlist(haasomeClient)
	# for i in botlist:
	# 	print(i.priceMarket.primaryCurrency, i.priceMarket.secondaryCurrency, i.roi)
	bot = botsellector.getallbots(haasomeClient)
	print_bot_as_string(bot)





if __name__ == '__main__':
	main()



