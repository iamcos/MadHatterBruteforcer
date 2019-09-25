from haasomeapi.apis.TradeBotApi import TradeBotApi
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import \
				IndicatorOption
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from haasomeapi.enums.EnumErrorCode import EnumErrorCode

from haasomeapi.enums.EnumCoinPosition import EnumCoinPosition
from haasomeapi.enums.EnumLimitOrderPriceType import EnumLimitOrderPriceType
import interval as iiv 

import haasomeapi.enums.EnumIndicator as EnumIndicator
import numpy as np
import pandas as pd
import time
import botsellector
import multiprocessing as mp
from decimal import Decimal



def multiprocess(bot,guid):
		newbotname = bot.name+' '+bot.indicators[guid].indicatorTypeShortName+' temp'
		newbot = haasomeClient.tradeBotApi.clone_trade_bot(bot.accountId, bot.guid, newbotname, bot.priceMarket.primaryCurrency, bot.priceMarket.secondaryCurrency, bot.priceMarket.contractName, bot.leverage, False, False, False, True, True).result
		cloeindicator = haasomeClient.tradeBotApi.clone_indicator(bot.guid, guid, newbot.guid).result
	
		gettradebot = haasomeClient.tradeBotApi.get_trade_bot(newbot.guid).result
		for guid in gettradebot.indicators:
			# print('Indicator name: ',gettradebot.indicators[guid].indicatorTypeShortName)
			for i, options in enumerate(gettradebot.indicators[str(guid)].indicatorInterface):
					indicators.append(i)
			for interface in gettradebot.indicators[str(guid)].indicatorInterface:
				# print(interface.title, interface.value , interface.options)
				print(interface.value.type)
			
def new_bot_for_every_indicator(haasomeClient, bot, interval):
	ticks = iiv.readinterval(1)
	newbots = []
	createdbots = []
	indicators = []
	options = []
	
	for guid in bot.indicators: 
		newbotname = bot.name+' '+bot.indicators[guid].indicatorTypeShortName+' temp'
		newbot = haasomeClient.tradeBotApi.clone_trade_bot(bot.accountId, bot.guid, newbotname, bot.priceMarket.primaryCurrency, bot.priceMarket.secondaryCurrency, bot.priceMarket.contractName, bot.leverage, False, False, False, True, True).result
		cloeindicator = haasomeClient.tradeBotApi.clone_indicator(bot.guid, guid, newbot.guid).result
		newbots.append(newbot)
	return newbots


def get_indicator_interfaces(bot):
	indicators = {}
	interfaces ={}
	indicator_ranges_by_name ={}
	interface_ranges_by_name = {}
	indicators_with_ranges = {}
	

	dataframes = {}
	

	for ii, v in enumerate(bot.indicators):
		interfaces ={}
		index = []
		values = []
		print('\n',bot.indicators[v].indicatorTypeShortName)
		# indicators[ii] = v
		for i,vv in enumerate(bot.indicators[v].indicatorInterface):
			print(i,vv.title, vv.value, vv.options)
			interfaces[vv.title] = vv.value
			indicators[v] = interfaces
			index.append(vv.title)
			values.append(vv.value)
			
		
def to_dataframe(bot):
	interfaces = get_indicator_interfaces(bot)
	# print(interfaces)
	df = pd.DataFrame.from_dict(interfaces,orient='index')
	print(df)

def backtest_single_indicator_bot(bot):
	results =[]
	indicators = get_indicator_interfaces(bot)
	
	# 				for i+1 in enumerate(indicators[indicator].keys()):

				
	# 	for title, value in indicators[indicator].items():
	# 	indicators[indicator].keys()
	# 					if title == 'Short length':
	# 						print('value',value)
	# 						start = 5
	# 						stop =  20
	# 						step =  1
	# 						try:
	# 							for x in np.arange(start,stop,step):
	# 							# print(indicator,indicators[indicator])
	# 								# ticks = iiv.readinterval(bot.indicators[indicator].timer)
	# 								ticks = iiv.readinterval(1)
	# 								print(title, x)
	# 								change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(bot.guid, indicator,list(indicators[indicator].keys()).index(key) , x)
	# 								bt = haasomeClient.tradeBotApi.backtest_trade_bot(bot.guid, ticks)
	# 								printerrors(bt)
	# 								printerrors(change)
	# 								print(bt.result.roi)
	# 								results.append([bt.result.roi, x])
	# 						except ZeroDivisionError:
	# 							pass
	# 					else:
	# 						pass
	# results = sorted(results, key=lambda x: x[1], reverse=False)
	# change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(bot.guid,results[0][1] , 0, x)
def printerrors(variable):
		print(variable.errorCode, variable.errorMessage)



def main():
	pool = mp.Pool(mp.cpu_count())
	bot = botsellector.getalltradebots(haasomeClient)
	intt = get_indicator_interfaces(bot)
	# dd = to_dataframe(bot)


if __name__ == '__main__':
	main()