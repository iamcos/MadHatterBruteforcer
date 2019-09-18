from haasomeapi.apis.TradeBotApi import TradeBotApi
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import \
    IndicatorOption
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from haasomeapi.HaasomeClient import HaasomeClient
from haasomeapi.enums.EnumCoinPosition import EnumCoinPosition
from haasomeapi.enums.EnumLimitOrderPriceType import EnumLimitOrderPriceType
import interval as iiv 
import init
import haasomeapi.enums.EnumIndicator as EnumIndicator
import numpy as np
import time
import botsellector
import multiprocessing as mp



ip, secret = init.connect()
haasomeClient = HaasomeClient(ip, secret)



def indicatorsintobots(haasomeClient, bot, interval):
	ticks = iiv.readinterval()
	newbots = []
	createdbots = []
	indicators = []
	
	for guid in bot.indicators: 
		newbotname = bot.name+' '+bot.indicators[guid].indicatorTypeShortName+' temp'
		newbot = haasomeClient.tradeBotApi.clone_trade_bot(bot.accountId, bot.guid, newbotname, bot.priceMarket.primaryCurrency, bot.priceMarket.secondaryCurrency, bot.priceMarket.contractName, bot.leverage, False, False, False, True, True).result
		cloeindicator = haasomeClient.tradeBotApi.clone_indicator(bot.guid, guid, newbot.guid).result
	
		gettradebot = haasomeClient.tradeBotApi.get_trade_bot(newbot.guid).result
		for guid in gettradebot.indicators:
			print('Indicator name: ',gettradebot.indicators[guid].indicatorTypeShortName)
			for i, options in enumerate(gettradebot.indicators[str(guid)].indicatorInterface):
				indicators.append(i)
			for interface in gettradebot.indicators[str(guid)].indicatorInterface:
								print(interface.__dict__)
								# print(interface.fieldType)
								print(interface.title, interface.value , interface.options)
			
			print('length is : ', len(indicators))
			results = []
			if gettradebot.indicators[guid].indicatorTypeShortName == 'Aroon':
				 for xxx in np.arange(2, 12, 2):
						change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(gettradebot.guid, guid, 2, xxx)
						bt = haasomeClient.tradeBotApi.backtest_trade_bot(gettradebot.guid, ticks)
						printerrors(bt, 'bt')
						printerrors(change, 'change')
						print(bt.result.roi)
						for x in np.arange(10, 50, 10):
							change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(gettradebot.guid, guid, 0, x)
							bt = haasomeClient.tradeBotApi.backtest_trade_bot(gettradebot.guid, ticks)
							printerrors(bt, 'bt')
							printerrors(change, 'change')
							print(bt.result.roi)
							for xx in np.arange(20, 100, 10):
								change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(gettradebot.guid, guid, 1, xx)
								bt = haasomeClient.tradeBotApi.backtest_trade_bot(gettradebot.guid, ticks)
								printerrors(bt, 'bt')
								printerrors(change, 'change')
								print(bt.result.roi)	
								results.append([bt.result.roi, x, xx, xxx])
			elif gettradebot.indicators[guid].indicatorTypeShortName == 'CRSI': #missing ROC
				 for l in np.arange(2, 40, 2):
						change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(gettradebot.guid, guid, 0, l)
						bt = haasomeClient.tradeBotApi.backtest_trade_bot(gettradebot.guid, ticks)
						printerrors(bt, 'bt')
						printerrors(change, 'change')
						print(bt.result.roi)
						for b in np.arange(10, 40, 2):
							change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(gettradebot.guid, guid, 3, b)
							bt = haasomeClient.tradeBotApi.backtest_trade_bot(gettradebot.guid, ticks)
							printerrors(bt, 'bt')
							printerrors(change, 'change')
							print(bt.result.roi)
							for s in np.arange(65, 81, 2):
								change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(gettradebot.guid, guid, 4, s)
								bt = haasomeClient.tradeBotApi.backtest_trade_bot(gettradebot.guid, ticks)
								printerrors(bt, 'bt')
								printerrors(change, 'change')
								print(bt.result.roi)	
								for lud in np.arange(2, 5, 1):
										change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(gettradebot.guid, guid, 1, lud)
										bt = haasomeClient.tradeBotApi.backtest_trade_bot(gettradebot.guid, ticks)
										printerrors(bt, 'bt')
										printerrors(change, 'change')
										print(bt.result.roi)	
										results.append([bt.result.roi, l, lud, b, s])
			elif gettradebot.indicators[guid].indicatorTypeShortName == None:
				
				return bot




def tune(haasomeClient, bots, indicators, int):

		for i, b in zip(indicators, bots):
			change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(b.guid, i, field, value)
		

def tuneTradeBot2(haasomeClient,bot):
		
		for guid in bot.indicators: 
			print(guid)
			for interface in guid:
					print(interface, interface.title)
					if interface.title == 'Length':
							backtesting(int(5), int(50), int(interface.step), bot, str(key), int(i), haasomeClient, interval)
					elif interface.title == 'RSI Length':
							backtesting(int(5), int(50), int(interface.step), bot, str(key), int(i), haasomeClient, interval)
					elif interface.title == 'Lookback':
							backtesting(int(5), int(50), int(interface.step), bot, str(key), int(i), haasomeClient, interval)
					elif interface.title == 'Buy Level':
								backtesting(int(10), int(50), int(interface.step), bot, str(key), int(i), haasomeClient, interval)
					elif interface.title == 'Sell Level':
								backtesting(int(50), int(90), int(interface.step), bot, str(key), int(i), haasomeClient, interval)
					elif interface.title == 'Short length':
								backtesting(int(2), int(50), int(interface.step), bot, str(key), int(i), haasomeClient, interval)
					elif interface.title == 'Middle length':
								backtesting(int(2), int(50), int(interface.step), bot, str(key), int(i), haasomeClient, interval)
					elif interface.title == 'Long length':
								backtesting(int(50), int(100), int(interface.step), bot, str(key), int(i), haasomeClient, interval)
					elif interface.title == 'Swing':
								backtesting(int(0), int(0), int(interface.step), bot, str(key), int(i), haasomeClient, interval)
					elif interface.title == 'Fast K':
								backtesting(int(2), int(20), int(interface.step), bot, str(key), int(i), haasomeClient, interval)
					elif interface.title == 'Fast D':
								backtesting(int(2), int(20), int(interface.step), bot, str(key), int(i), haasomeClient, interval)
					elif interface.title == 'Dev.Up':
									backtesting(float(0), float(3), float(interface.step), bot, str(key), int(i), haasomeClient, interval)
					elif interface.title == 'Dev.Down':
								backtesting(float(0), float(3), float(interface.step), bot, str(key), int(i), haasomeClient, interval)
					elif interface.title == 'U/D Length':
								backtesting(int(0), int(10), int(interface.step), bot, str(key), int(i), haasomeClient, interval)
					elif interface.title == 'ROC':
								backtesting(int(80), int(120), int(interface.step), bot, str(key), int(i), haasomeClient, interval)
					else:
								backtesting(int(0), int(120), int(interface.step), bot, str(key), int(i), haasomeClient, interval)

def backtesting(start, stop, step, bot,indicator, field, haasomeClient, interval):

	interface = []
	prevbtr = []
	for value in np.arange(start, stop, step):
			change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(bot.guid, indicator, field, value)
			change2 = haasomeClient.tradeBotApi.edit_bot_indicator_settings(bot.guid, indicator, field, value).result
			print(bot.guid, indicator, field, value)
			print('Backtesting: ',change.errorCode, change.errorMessage)
			bt = haasomeClient.tradeBotApi.backtest_trade_bot(bot.guid, interval).result
			btr = bot.roi
			print(btr, value)
			if btr == prevbtr:
				pass
			else:
				interface.append([btr, value])
	int2 = sorted(interface, key=lambda x: x[0], reverse=False)
	change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(bot.guid, indicator, 0, int2[-1][1])


def printerrors(variable, text):
		print(str(text),variable.errorCode, variable.errorMessage)


def main():
	pool = mp.Pool(mp.cpu_count())
	bot = botsellector.getalltradebots(haasomeClient)
	# newbots = indicatorsintobots(haasomeClient,bot,1)

	#Multiprocessing try
	newbots = pool.apply(indicatorsintobots(haasomeClient,bot,5))
	print(newbots)
	# botconfig(haasomeClient,newbots)
	# print(newbots, newindicators)
	# tuneTradeBot2(haasomeClient, newbots)


if __name__ == '__main__':
	main()