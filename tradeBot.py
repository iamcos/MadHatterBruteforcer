from haasomeapi.apis.TradeBotApi import TradeBotApi
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import \
    IndicatorOption
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from haasomeapi.HaasomeClient import HaasomeClient
import interval
import init
import haasomeapi.enums.EnumIndicator as EnumIndicator
import numpy as np
import time
interval = interval.inticks(2019,8,22,1)
ip, secret = init.connect()
haasomeClient = HaasomeClient(ip, secret)



def getTradeBots(haasomeClient):
	alltradebots = haasomeClient.tradeBotApi.get_all_trade_bots()
	if alltradebots.errorCode != EnumErrorCode.SUCCESS:
		return alltradebots.errorCode, alltradebots.errorMessage
	else: 
		return alltradebots.result

def returnTradeBotObject(haasomeClient,alltradebots):
	for i, bot in enumerate(alltradebots):
		print(i, bot.name, bot.priceMarket.primaryCurrency+'\\'+bot.priceMarket.secondaryCurrency, len(bot.completedOrders),' orders')
	user_response = input('\nType in bot number to select it: ')
	currentbot = alltradebots[int(user_response)]
	return currentbot

def tuneindicatorseperately(haasomeClient, bot, interval):
	# interval =int(interval.inticks(2019,8,22,1))
	for guid in bot.indicators: 
		newbot = haasomeClient.tradeBotApi.new_trade_bot(bot.accountId, bot.botname+' temp', bot.priceMarket.primaryCurrency, bot.priceMarket.secondaryCurrency, bot.priceMarket.contractName, bot.leverage, bot.priceMarket.groupName).result
		cloeindicator = haasomeClient.tradeBotApi.clone_indicator(bot.guid, guid, newbot.guid)
		newbot = haasomeClient.tradeBotApi.setup_trade_bot(newbot.accountid, newbot.guid, newbot.botname, newbot.priceMarket.primaryCurrency, newbot.priceMarket.secondaryCurrency, newbot.priceMarket.contractName,newbot.leverage, newbot.groupName, newbot.consensusMode, True)
		newbot = haasomeClient.tradeBotApi.setup_spot_bot_trade_amount(newbot.guid, newbot.currentPositionPl, bot.currentTradeAmount, bot.lastBuyPrice, bot.lastSellPrice, bot.buyOrderTemplateId, bot.sellOrderTemplateId, bot.highFrequencyUpdates, bot.goAllIn, bot.openOrderTimeout, bot.templateTimeout,bot.originalTradeAmount, bot.limitOrderType, bot.useHiddenOrders, bot.currentFeePercentage)

def botconfig(haasomeClient,bot):
	safeties = []
	indicators = []
	insurances = []

		# Printing Safeties data
	print('\n',len(bot.safeties),' Safeties')
	for guid in bot.safeties:
		print(bot.safeties[guid].safetyName)
		safeties.append([guid, bot.safeties[guid].safetyName])
	#printing Safeties interface data
		for interface in bot.safeties[guid].safetyInterface:
					print(interface.title, interface.value, interface.options)
	
		# Printing indicator data
	print('\n',len(bot.indicators),' Indicators')
	for guid in bot.indicators:

		indicators.append([guid, bot.indicators[guid].indicatorName])
		# print(EnumIndicator.EnumIndicator(bot.indicators[guid].indicatorType))
			# Printing indicator interface data
		for interface in bot.indicators[guid].indicatorInterface:
				# print(interface.__dict__)
				# print(interface.fieldType)
				print(interface.title) #interface.value , interface.options
	print('\n')

	# Print Insurance data
	print('\n',len(bot.insurances), ' Insurances')
	for guid in bot.insurances:
			print(bot.insurances[guid].insuranceTypeFullName, guid)
			insurances.append([guid, bot.insurances[guid].insuranceTypeFullName])
	# print Insurance interface data
			for interface in bot.insurances[guid].insuranceInterface:
					print(interface.title, interface.value, interface.options) 
	print('\n')
	return safeties, indicators, insurances	





def tuneTradeBot(haasomeClient,bot, interval):

	for guid in bot.indicators: 
		# print(bot.indicators[guid].indicatorType)
		if bot.indicators[guid].indicatorType == 32:
				interface = []
				prevbtr = []
				for value in np.arange(3, 30, 1):
					change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(bot.guid, guid, 0, value)
					# print(change.errorCode, change.errorMessage)
					bt = haasomeClient.tradeBotApi.backtest_trade_bot(bot.guid, interval)
					btr = bt.result.roi
					print(btr, value)
					if btr == prevbtr:
						pass	
					else:
						interface.append([btr, value])
				
				
				int2 = sorted(interface, key=lambda x: x[0], reverse=False)
				print(interface)
				change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(bot.guid, guid, 0, int2[-1][1])
				
				for value in np.arange(2, 40, 1):
					change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(bot.guid, guid, 1, value)
					# print(change.errorCode, change.errorMessage)
					bt = haasomeClient.tradeBotApi.backtest_trade_bot(bot.guid, interval)
					btr = bt.result.roi
					print(btr, value)
					interface.append([btr, value])
				
				int2 = sorted(interface, key=lambda x: x[0], reverse=False)
				print(interface)
				change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(bot.guid, guid, 1, int2[-1][1])
				for value in np.arange(60, 80, 1):
					change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(bot.guid, guid, 2, value)
						# print(change.errorCode, change.errorMessage)
					bt = haasomeClient.tradeBotApi.backtest_trade_bot(bot.guid, interval)
					btr = bt.result.roi
					print(btr, value)
					interface.append([btr, value])
				int2 = sorted(interface, key=lambda x: x[0], reverse=False)
				print(interface)
				change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(bot.guid, guid, 2, int2[-1][1])
		# if bot.indicators[guid].indicatorType == 0:
		# 		#Aroon
		# 	for interface in bot.indicators[guid].indicatorInterface:
					
		# 				backtesting(5, 50, 2, bot, guid, interface, interval, haasomeClient)		
		# if bot.indicators[guid].indicatorType == 2:
		# 		#Aroon
		# 	for interface in bot.indicators[guid].indicatorInterface:
		# 				backtesting(5, 50, 2, bot, guid, interface, interval, haasomeClient)	
		# else:
		# 	interface = []
				
		# 	for value in np.arange(3, 100, 5):
		# 		change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(bot.guid, guid, i, value)
		# 		# print(change.errorCode, change.errorMessage)
		# 		bt = haasomeClient.tradeBotApi.backtest_trade_bot(bot.guid, interval)
		# 		btr = bt.result.roi
		# 		print(btr, value)
		# 		interface.append([btr, value])
		# 	int2 = sorted(interface, key=lambda x: x[0], reverse=False)
		# 	print(interface)
		# 	change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(bot.guid, guid, i, int2[-1][1])

def tuneTradeBot2(haasomeClient,bot):
	for key in bot.indicators: 
		for i, interface in enumerate(bot.indicators[key].indicatorInterface[i]):
				print(bot.indicators[key].indicatorInterface, interface.title)
				print(key, interface.__dict__, i, bot.indicators)
				if interface.title == 'Length':
						backtesting(int(5), int(50), int(interface.step), bot, str(key), int(i), haasomeClient, interval)
				elif interface.title == 'RSI Length':
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
							backtesting(0, 100, interface.step, bot, str(key), int(i), haasomeClient, interval)

def backtesting(start, stop, step, bot,indicator, field, haasomeClient, interval):

	interface = []
	prevbtr = []
	for value in np.arange(start, stop, step):
			change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(bot.guid, indicator, field, value)
			change2 = haasomeClient.tradeBotApi.edit_bot_indicator_settings(bot.guid, indicator, field, value).result
			print(bot.guid, indicator, field, value)
			print('Backtesting: ',change.errorCode, change.errorMessage)
			bt = haasomeClient.tradeBotApi.backtest_trade_bot(bot.guid, interval).result
			# print(bt.__dict__)
			btr = bot.roi
			print(btr, value)
			if btr == prevbtr:
				pass
			else:
				interface.append([btr, value])
	int2 = sorted(interface, key=lambda x: x[0], reverse=False)
	# print(interface)
	change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(bot.guid, indicator, 0, int2[-1][1])


def printerrors(variable, text):
		print(str(text),variable.errorCode, variable.errorMessage)

def tuneoneindicator(haasomeClient, bot):
	perindicatorbot = []
	for guid in bot.indicators: 
		new = haasomeClient.tradeBotApi.clone_trade_bot(bot.accountId, bot.guid, bot.name+' '+bot.indicators[guid].indicatorTypeShortName+' temp', bot.priceMarket.primaryCurrency, bot.priceMarket.secondaryCurrency, bot.priceMarket.contractName, bot.leverage, False, False, False, True, True)
		print(new.errorCode, new.errorMessage)
		newbot = new.result
		
		cloeindicator = haasomeClient.tradeBotApi.clone_indicator(bot.guid, str(guid), newbot.guid)
		printerrors(cloeindicator, 'clone indicator')
		perindicatorbot.append(newbot)
		tuneTradeBot2(haasomeClient, newbot)
	return perindicatorbot

def main():

	alltradebots = getTradeBots(haasomeClient)
	
	bot = returnTradeBotObject(haasomeClient,alltradebots)
	it = tuneoneindicator(haasomeClient, bot)

	tuneTradeBot2(haasomeClient, it[0])

	
	# backtesting(2,20,1,bot,'62f8788e-14ac-4f52-b15f-55c106954384',0, haasomeClient, interval)


if __name__ == '__main__':
	main()