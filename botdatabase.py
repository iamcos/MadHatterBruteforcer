
from haasomeapi.HaasomeClient import HaasomeClient
import botsellector
import configparser_cos
import configserver

from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
import pickle

import jsonpickle
ip, secret = configserver.validateserverdata()
haasomeClient = HaasomeClient(ip, secret)




class BotDB:
	def __init__(self, bot, dbfile):
		self.bot = botlist
		self.dbfile = dbfile

	def save_bots(botlist,dbfile):
			frozenobjlist = []
			for i, bot in enumerate(botlist):
				print(bot.name, bot.priceMarket.primaryCurrency)
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


# do = BotDB.save_bots(botlist,'bots.db')

# bots = BotDB.load_botlist('bots.db')

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
	botlist = botsellector.botlist(haasomeClient)
	for i in botlist:
		print(i.priceMarket.primaryCurrency, i.priceMarket.secondaryCurrency, i.roi)

# def configuremh(bot, newbot):
if __name__ == '__main__':
	main()



