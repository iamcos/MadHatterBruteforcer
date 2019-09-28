

import botsellector
import configparser_cos
import configserver
import json
from pbwrap import Pastebin
from io import StringIO
from pathlib import Path
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

	def save_bot(bot):
				frozen = jsonpickle.encode(bot)
				filename = 'bot.json'
				currentfile = Path(str(filename))
				currentfile.touch(exist_ok=True)
				with open(filename,'wb') as botsconfig_file:
					pickle.dump(frozen, botsconfig_file)
				return frozen

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

	def load_bot_from_file():
			filename = 'bot.json'
			with open(filename, 'rb') as botsconfig_file:
				bot = pickle.load(botsconfig_file)
				unfreeze = jsonpickle.decode(bot)
				return unfreeze

def bot_to_string(bot):
		# toremove = ['accountId','botLogBook','groupName','guid','messageProfile','notes','name','activated','activatedSince','amountDecimals',''] # need to do the opposite
		data = jsonpickle.encode(bot)
		print(data)
		return data

def make_bot_from_string(string):
	data = jsonpickle.decode(string)
	print(data)
	return data
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

def create_new_custom_bot(inputbot,example_bot):
	if inputbot.botType >=1:
		# string = input('copy and paste Mad Hatter Bot string here to have it crecreated.')
		new = haasomeClient.customBotApi.new_custom_bot(example_bot.accountId, inputbot.botType, 'imported '+inputbot.name, inputbot.priceMarket.primaryCurrency, inputbot.priceMarket.secondaryCurrency, inputbot.priceMarket.contractName)
		print(new.errorCode, new.errorMessage)
	elif inputbot.botType == 0:
		# string = input('copy and paste Trade bot Bot string here to have it crecreated.')
		new = haasomeClient.tradeBotApi.new_trade_bot(example_bot.accountId, 'imported '+inputbot.name, inputbot.priceMarket.primaryCurrency, inputbot.priceMarket.secondaryCurrency, inputbot.priceMarket.contractName,inputbot.leverage,'')
		print('error: ',new.errorCode, new.errorMessage)

def to_pastebin(botdata):
	
	api_dev_key = '807da6e50a40294f2f4b04a9dc221eb4'
	
	username = 'TradingBotsbyCos'
	password = 'lKwutRq!cYE6P8&k1#'
	url = Pastebin.create_papi_paste_code=botdata, api_paste_private=0, api_paste_name=None, api_paste_expire_date=None, api_paste_format=None)
	print(url)

def main():
	
	bot = botsellector.getallbots(haasomeClient)
	print('This is a simple script that uses a single file named bot.json for easy storage and sharing of Custom bots and Trade Bots. Its simple: select a bot to save, select save - bot saved to bot.json file. On another machine, select example bot, hit load bot and the bot will be recreated based on example bot account data.')
	print('1. Save a single bot to file')
	print('2. Load bot from file')

	user_response = input('Type number here: ')
	if user_response == '1':
		
		botdata = BotDB.save_bot(bot)
		tada = to_pastebin(botdata)

	if user_response == '2':
		botstr = BotDB.load_bot_from_file()
		bot2 = create_new_custom_bot(botstr, bot)


	# bot = botsellector.getallbots(haasomeClient)
	# string =	bot_to_string(bot)
	# bot2 = make_bot_from_string(string)
	# print(bot2.botType)
	# clone = create_new_custom_bot(bot2, bot)



if __name__ == '__main__':
	main()



