import regex
import shelve 
from __future__ import print_function, unicode_literals
from decimal import Decimal
from haasomeapi.HaasomeClient import HaasomeClient
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError
import configserver
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
from licensing.models import *
from licensing.methods import Key, Helpers
import createroiset

import numpy as np

import time
from haasomeapi.apis.AccountDataApi import AccountDataApi
from haasomeapi.apis.ApiBase import ApiBase
from haasomeapi.apis.MarketDataApi import MarketDataApi
from haasomeapi.dataobjects.accountdata.BaseOrder import BaseOrder
from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot
from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot
from haasomeapi.dataobjects.marketdata.Market import Market
from haasomeapi.dataobjects.util.HaasomeClientResponse import \
    HaasomeClientResponse
from haasomeapi.enums.EnumCurrencyType import EnumCurrencyType
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from haasomeapi.enums.EnumFundPosition import EnumFundPosition
from haasomeapi.enums.EnumMadHatterIndicators import EnumMadHatterIndicators
from haasomeapi.enums.EnumMadHatterSafeties import EnumMadHatterSafeties
from haasomeapi.enums.EnumOrderType import EnumOrderType
from haasomeapi.enums.EnumPriceSource import EnumPriceSource


def backtestrange(parameter: int, btrange: int, step: int):
	parameter = parameter
	btrange = btrange
	step = step
	therange = []
	startrange = btrange - btrange*step
	nextvalue = startrange + step
	therange.append(startrange)

	rangesteps = ''

	for x in range(rangesteps):
		nextvalue += step
		therange.append(nextvalue)
	return therange
		

def tuneRsiLength():
		btinterval = 2500
		firstbt = 0
		
		print('tuning rsi lenghth')
		btroilist = []
		basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
		RsiLength = basebotconfig.rsi['RsiLength']
		RsiOversold = basebotconfig.rsi['RsiOversold']
		RsiOverbought = basebotconfig.rsi['RsiOverbought']
		bBandsLength = basebotconfig.bBands['Length']
		devup = basebotconfig.bBands['Devup']
		devdn = basebotconfig.bBands['Devdn']
		setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(guid, EnumMadHatterIndicators.RSI, 0	, RsiLength)
		bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
		# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
		btr = bt.result
		print(btr.roi, 'RSI Length: ',RsiLength)
		btroitarget = btr.roi
		btroilist.append([btr.roi, RsiLength])
		while btr.roi < btroitarget:
			if btroilist[-1][0] < btr.roi:
				RsiOversoldup = RsiOversold+3
				lengthup =  bBandsLength+3
				RsiOverboughtdn = RsiOverbought-1
			if btroilist[-1][0] > btr.roi:
				RsiOversolddown = RsiOversold-13
				RsiOverboughtup = RsiOverbought+1
				lengthdown =  bBandsLength-3
			if btroilist[-1][0] > btr.roi:


			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(guid, EnumMadHatterIndicators.RSI, 1	, RsiOversold)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, 'RSI OVERSOLD: ',RsiOversold)
			btroilist.append([btr.roi, RsiOversold])
			RsiOversold 

		for x in range(5):
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(guid, EnumMadHatterIndicators.RSI, 0	, RsiLength)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi, 'RSI Length: ',RsiLength)
				btroilist.append([btr.roi, RsiLength])
				RsiLength +=1
	
		print(btroilist)

		while True:
			
			b = btroilist
			if b[0][1]>b[1][1]:
					if b[1][1]<b[2][1] or b[1][1]>b[2][1]:
						if b[2][1]>b[3][1]:
							btroilist.reverse()
							setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(guid, EnumMadHatterIndicators.RSI, 0	, RsiLength)
							bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
							# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
							btr = bt.result
							print(btr.roi, 'RSI Length: ',RsiLength)
							btroilist.reverse()
							btroilist.append([btr.roi, RsiLength])
							RsiLength +=1
							btroilist.reverse()
			if b[0][1]<b[1][1]:
					if b[1][1]<b[2][1]:
						if b[2][1]<b[3][1]:
							btroilist.reverse()
							setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(guid, EnumMadHatterIndicators.RSI, 0	, RsiLength)
							bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
							# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
							btr = bt.result
							print(btr.roi, 'RSI Length: ',RsiLength)
							btroilist.reverse()
							btroilist.append([btr.roi, RsiLength])
							RsiLength -=1
							btroilist.reverse()
					print(btroilist)
			if b[0][1]==b[1][1]:
				if b[1][1]==b[2][1]:
					if b[2][1]==b[3][1]:
						print('btroilist')


		if one == None:
			db.update['one'] = roi
		if one != None:
			db.update['two'] = db['one']
		if three != None:
			db.update['three'] = db['two']
		if four != None:
				db.update['four'] = db['three']
		if five != None:
				db.update['five'] = db['four']
		db.update['five'] = db['four']
		db.update['four'] = db['three']
		db.update['three'] = db['two']
		db.update['two'] = db['one']
		db.update['one'] = btr.roi
		return db
		




def connectionstring():
	ip, secret = configserver.validateserverdata()
	haasomeClient = HaasomeClient(ip, secret)
	return haasomeClient

guid = '1c69309c-677b-4484-bc48-a77ae4ab7494'
haasomeClient = connectionstring()
therange = backtestrange(5.0, 0.5, 2)
print(therange)
tuneRsiLength()