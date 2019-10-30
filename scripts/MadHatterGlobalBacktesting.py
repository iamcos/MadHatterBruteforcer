from haasomeapi.apis.MarketDataApi import MarketDataApi
from haasomeapi.dataobjects.accountdata.BaseOrder import BaseOrder
from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot
from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot
from haasomeapi.dataobjects.marketdata.Market import Market
from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse
from haasomeapi.enums.EnumCurrencyType import EnumCurrencyType
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from haasomeapi.enums.EnumFundPosition import EnumFundPosition
from haasomeapi.enums.EnumMadHatterIndicators import EnumMadHatterIndicators
from haasomeapi.enums.EnumMadHatterSafeties import EnumMadHatterSafeties
from haasomeapi.enums.EnumOrderType import EnumOrderType
from haasomeapi.enums.EnumPriceSource import EnumPriceSource
from decimal import Decimal
from random import sample
import random
import mh_indicators_dict
import init
import botsellector
import interval as iiv
import numpy as np
import csv
from pathlib import Path


# import os.path
haasomeClient = init.connect()
# useful = ['rsil','rsib','rsis','bbl','devup','devdn','macdfast','macdslow','macdsign']
# useful2 = bot.rsi["RsiLength"],bot.rsi["RsiOversold"],bot.rsi["RsiOverbought"],bot.bBands['Length'],bot.bBands['Devup'],bot.bBands['Devdn'],bot.macd['MacdFast'],bot.macd['MacdSlow'],bot.macd['MacdSign']

def opposite_direction(direction):

		if direction == 'up':
			direction = 'down'
		else: 
		 direction = 'up'
		return direction


def direction_mon(indicator, direction, bt_r):
	flip = 0
	print(len(bt_r))
	try:
		if bt_r[0][0] == bt_r[1][0]:
			if bt_r[2][0] == bt_r[1][0]:
				direction = opposite_direction(direction)
				flip +=1
		if len(bt_r) >= 10:
			indicator = random_indicator()

		if flip == 4:
			flip = 0
			indicator = random_indicator()
	except IndexError:
			pass
	return indicator, direction

def frange(start, end=None, inc=None):
    "A range function, that does accept float increments..."

    if end == None:
        end = start + 0.0
        start = 0.0

    if inc == None:
        inc = 1.0

    L = []
    while 1:
        next = start + len(L) * inc
        if inc > 0 and next >= end:
            break
        elif inc < 0 and next <= end:
            break
        L.append(next)
        
    return L

def tuningsystem(bot, indicator, direction):
	ticks = iiv.readinterval()

	indicators_dict = {'rsil':{'currentvalue':bot.rsi["RsiLength"], 'enumstring': 1, 'field':0, 'range': list(range(0,100,1))}, 'rsis':{'currentvalue':int(bot.rsi["RsiOversold"]), 'enumstring':1, 'field':1, 'range': list(range(0,100,1))},'rsib':{'currentvalue':int(bot.rsi["RsiOverbought"]), 'enumstring':1, 'field':2, 'range': list(range(0,100,1))}, 'bbl':{'currentvalue':bot.bBands['Length'], 'enumstring':2, 'field':0, 'range': list(range(0,100,1))}, 'devup':{'currentvalue':bot.bBands['Devup'], 'enumstring':2, 'field':2, 'range': list(frange(0.1,3.1,0.1))}, 'devdn':{'currentvalue':bot.bBands['Devdn'], 'enumstring':2, 'field':2, 'range': list(frange(0.1,3.1,0.1))}, 'macdfast':{'currentvalue':bot.macd['MacdFast'], 'enumstring':0, 'field':0, 'range': list(range(0,100,1))},'macdslow':{'currentvalue':bot.macd['MacdSlow'], 'enumstring':0, 'field':1, 'range': list(range(0,100,1))},'macdsign':{'currentvalue':bot.macd['MacdSign'], 'enumstring':0, 'field':2, 'range': list(range(0,100,1))}}

	# print(indicator)
	print(indicators_dict[indicator])
	start = indicators_dict[indicator]['currentvalue']
	print(start)
	start1 = start
	backtesting = True
	bt_results = []

	
	ranges = {}
	indicators = ['rsil','rsib','rsis','bbl','devup','devdn','macdfast','macdslow','macdsign']

	for i, x in enumerate(mh_indicators_dict.ranges()):
		ranges[str(indicators[i])] = [x]
	
	
	while backtesting:
		
		# start = indicators_dict[indicator]['currentvalue']
		bt_result = []
		bt_sorted = []

		if type(start) == int :
			try:
					while len(ranges[indicator][0])>=0 and start <= ranges[indicator][0][-1]:
						
						if direction == 'up':
								step = 1
								start = start+step
								if start > ranges[indicator][0][-1]:
									direction = 'down'
								print( "This number is a int")
								print(start)
								# print('l', len(ranges[indicator][0]))
								# print('list',ranges[indicator][0])

								for i,x in enumerate(ranges[indicator][0]):
									if start == x:
										ranges[indicator][0].remove(start)
										# print('length',len(ranges[indicator][0]))
										bot1 = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(bot.guid,EnumMadHatterIndicators(indicators_dict[indicator]['enumstring']),indicators_dict[indicator]['field'], start)
										print(bot1.errorCode,bot1.errorMessage)
										bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(bot.accountId,bot.guid,ticks,bot.priceMarket.primaryCurrency,bot.priceMarket.secondaryCurrency,bot.priceMarket.contractName)
										print(bt.errorCode,bt.errorMessage)
										print('ROI',bt.result.roi)

										bt_results.append([bt.result.roi, start])
										print(bt_results)
										bt_sorted = sorted(bt_results, key=lambda x: x[0], reverse=True)
										print('sorted',bt_sorted)
										direction_mon(indicator,direction,bt_sorted)
										# indicator,direction = direction_mon(indicator,direction, bt_sorted)

						elif direction =='down':
									step = 1
									start = start-step
									print( "This number is a int")
									print(start)
									# print('l', len(ranges[indicator][0]))
									# print('list',ranges[indicator][0])

									for x in ranges[indicator][0]:
										if start == x:
											ranges[indicator][0].remove(start)
											# print('length',len(ranges[indicator][0]))
											bot1 = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(bot.guid,EnumMadHatterIndicators(indicators_dict[indicator]['enumstring']),indicators_dict[indicator]['field'], start)
											print(bot1.errorCode,bot1.errorMessage)
											bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(bot.accountId,bot.guid,ticks,bot.priceMarket.primaryCurrency,bot.priceMarket.secondaryCurrency,bot.priceMarket.contractName)
											print(bt.errorCode,bt.errorMessage)
											print('ROI',bt.result.roi)
											bt_results.append([bt.result.roi, start])
											print(bt_results)
											bt_sorted = sorted(bt_results, key=lambda x: x[0], reverse=True)
											print('sorted',bt_sorted)
											direction_mon(indicator,direction,bt_sorted)
											# indicator,direction = direction_mon(indicator,direction, bt_sorted)

					else:
						pass
						print(ranges[indicator][0][0],ranges[indicator][0][-1])
						indicator = random.sample(indicators,1)
						break
			except IndexError:
				indicator = random.sample(indicators,1)
				break

		elif type(start) == float :

			try:
					while len(ranges[indicator][0])>=0 and round(start,2) <= ranges[indicator][0][-1]:
						print(indicator)
						if direction == 'up':
								step = 0.1
								start = round(start,2)+step
								if start > ranges[indicator][0][-1]:
									direction = 'down'
								print( "This number is a float")
								print(round(start,2))
								# # print('l', len(ranges[indicator][0]))3
								# print('list',ranges[indicator][0])

								for i,x in enumerate(ranges[indicator][0]):
									if round(start,2) == x:
										ranges[indicator][0].remove(round(start,2))
										# print('length',len(ranges[indicator][0]))
										bot1 = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(bot.guid,EnumMadHatterIndicators(indicators_dict[indicator]['enumstring']),indicators_dict[indicator]['field'], round(start,2))
										print(bot1.errorCode,bot1.errorMessage)
										bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(bot.accountId,bot.guid,ticks,bot.priceMarket.primaryCurrency,bot.priceMarket.secondaryCurrency,bot.priceMarket.contractName)
										print(bt.errorCode,bt.errorMessage)
										print('ROI',bt.result.roi)
										bt_results.append([bt.result.roi, round(start,2)])
										bt_sorted = sorted(bt_results, key=lambda x: x[0], reverse=True)
										print('sorted',bt_sorted)
										direction_mon(indicator,direction,bt_sorted)
										# indicator,direction = direction_mon(indicator,direction, bt_sorted)


								else:
										bt_results.clear()
										bot1 = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(bot.guid,EnumMadHatterIndicators(indicators_dict[indicator]['enumstring']),indicators_dict[indicator]['field'], bt_sorted[0][0])
										print(bot1.errorCode,bot1.errorMessage)
										indicator = random_indicator()
										break

						elif direction =='down':
									step = 0.1
									start = round(start,2)-step
									print( "This number is a float")
									print(round(start,2))
									# print('l', len(ranges[indicator][0]))
									# print('list',ranges[indicator][0])

									for x in ranges[indicator][0]:
										if round(start,2) == x:
											ranges[indicator][0].remove(round(start,2))
											# print('length',len(ranges[indicator][0]))
											bot1 = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(bot.guid,EnumMadHatterIndicators(indicators_dict[indicator]['enumstring']),indicators_dict[indicator]['field'], round(start,2))
											print(bot1.errorCode,bot1.errorMessage)
											bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(bot.accountId,bot.guid,ticks,bot.priceMarket.primaryCurrency,bot.priceMarket.secondaryCurrency,bot.priceMarket.contractName)
											print(bt.errorCode,bt.errorMessage)
											print('ROI',bt.result.roi)
											bt_results.append([bt.result.roi, start])
											print(bt_results)
											bt_sorted = sorted(bt_results, key=lambda x: x[0], reverse=True)
											print('sorted',bt_sorted)
											direction_mon(indicator,direction,bt_sorted)
											# indicator,direction = direction_mon(indicator,direction, bt_sorted)

									else:
										bt_results.clear()
										bot1 = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(bot.guid,EnumMadHatterIndicators(indicators_dict[indicator]['enumstring']),indicators_dict[indicator]['field'], bt_sorted[0][0])
										print(bot1.errorCode,bot1.errorMessage)
										indicator = random_indicator()
										break
			except IndexError:
					indicator = random.sample(indicators,1)
					break


def random_indicator():
	indicators = ['rsil','rsib','rsis','bbl','devup','devdn','macdfast','macdslow','macdsign']
	indicator = random.sample(indicators,1)[0]
	# print(indicator)
	return indicator

def main():

	bot = botsellector.getallmhbots(haasomeClient)
	indicator = random_indicator()

	while True:
		tuningsystem(bot,indicator,'up')
	# indicator_play(bot)


if __name__ == "__main__":
	main()
