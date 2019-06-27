from __future__ import print_function, unicode_literals
import regex
from haasomeapi.HaasomeClient import HaasomeClient
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError
import configserver
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType

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

style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})
ip, secret = configserver.validateserverdata()
haasomeClient = HaasomeClient(ip, secret)
currentBotGuid = '4091ed4f-6f40-4be5-bd59-ceb343acad72'
basebotconfig = haasomeClient.customBotApi.get_custom_bot(currentBotGuid, EnumCustomBotType.BASE_CUSTOM_BOT).result


def selectparametertochange():
	questions = [
		{'type': 'list','name': 'selectedparameter','message': 'Select parameter to change by using keys up and down then hit return',
		'choices': 
		[{'name': 'Bot time interval: '+str(basebotconfig.interval)+'minutes', 'value':'interval'},
		{'name': 'bBands MaType: '+str(basebotconfig.bBands['MaType']), 'value': 'MaType'},
		{'name': 'bBands Length: '+str(basebotconfig.bBands['Length']), 'value':'Length'},
		{'name': 'bBands Dev Up: '+str(basebotconfig.bBands['Devup']), 'value':'Devup'},
		{'name': 'bBands Dev Down: '+str(basebotconfig.bBands['Devdn']),'value':'Devdn'},
		{'name': 'Rsi Length: '+str(basebotconfig.rsi['RsiLength']) , 'value':'RsiLength'},
		{'name': 'Rsi Buy: '+str(basebotconfig.rsi['RsiOversold']), 'value': 'RsiOversold'},
		{'name': 'Rsi Sell: '+str(basebotconfig.rsi['RsiOverbought']), 'value':'RsiOverbought'},
		{'name': 'MACD Fast: '+str(basebotconfig.macd['MacdFast']), 'value':'MacdFast'},
		{'name': 'MACD Slow: ' +str(basebotconfig.macd['MacdSlow']), 'value': 'MacdSlow'},
		{'name': 'MACD Signal: '+str(basebotconfig.macd['MacdSign']), 'value':'MacdSign'}]}]
	return questions

# selectedparam = prompt(selectparametertochange())
# print(selectedparam['selectedparameter'])

def getmissingmarketdata():
	basebotconfig = haasomeClient.customBotApi.get_custom_bot(currentBotGuid, EnumCustomBotType.BASE_CUSTOM_BOT).result
	marketdata = []
	marketobject = haasomeClient.marketDataApi.get_price_markets(basebotconfig.priceMarket.priceSource)
	marketobjectr = marketobject.result
	for i,v  in enumerate(marketobjectr):
		if marketobjectr[i].primaryCurrency == basebotconfig.priceMarket.primaryCurrency and marketobjectr[i].secondaryCurrency == basebotconfig.priceMarket.secondaryCurrency:
			marketdata = marketobjectr[i]
			print(marketdata)

	

	configuremadhatter = haasomeClient.customBotApi.setup_mad_hatter_bot2(basebotconfig.name,basebotconfig.guid,basebotconfig.accountId, basebotconfig.priceMarket.primaryCurrency,basebotconfig.priceMarket.secondaryCurrency, marketdata.contractName, basebotconfig.leverage, basebotconfig.customTemplate, basebotconfig.coinPosition, marketdata.tradeFee, basebotconfig.amountType, basebotconfig.currentTradeAmount, basebotconfig.useTwoSignals, basebotconfig.disableAfterStopLoss, basebotconfig.interval, basebotconfig.includeIncompleteInterval,basebotconfig.mappedBuySignal, basebotconfig.mappedSellSignal)
	# print('Configured MAD HATTER', configuremadhatter.errorCode, configuremadhatter.errorMessage)
	return marketdata


def backtestconfiguredmh():
	basebotconfig = haasomeClient.customBotApi.get_custom_bot(currentBotGuid, EnumCustomBotType.MAD_HATTER_BOT).result
	marketdata = getmissingmarketdata()
	
	intervals = {'0 minutes': 0,'1 minutes':1,'2 minutes':2,'3 minutes':3,'4 minutes':4,'5 minutes':5,'6 minutes':6,'10 minutes':10,'12 minutes':12,'15 minutes':15,'20 minutes':20,'30 minutes':30,'45 minutes':45,'1 hour':60,'1.5 hours':90,'2 hours':120,'2.5 hours':150,'3 hours':180,'4 hours':240,'6 hours':360,'12 hours':720,'1 day':1440,'2 days':2880}
	intervalindex = []
	intervalkeys = list(intervals.keys())
	intervalvalues = list(intervals.values())
	for n, i in enumerate(intervalvalues):
		if i == basebotconfig.interval:
			intervalindex = n
			print('selected interval: ', intervalindex, ' Minutes')

			action = [
				{
					'type':'list',
					'name':'selection',
					'message': 'Lets do something',
					'choices': ['increse', 'decrease', 'back']}]
		
			if answers['selection'] != 'back':
				answers = prompt(action)
				if answers['selection'] == 'increse': 
						basebotconfig = haasomeClient.customBotApi.get_custom_bot(currentBotGuid, EnumCustomBotType.BASE_CUSTOM_BOT).result
						configuremadhatter = haasomeClient.customBotApi.setup_mad_hatter_bot2(basebotconfig.name,basebotconfig.guid,basebotconfig.accountId, basebotconfig.priceMarket.primaryCurrency,basebotconfig.priceMarket.secondaryCurrency, marketdata.contractName, basebotconfig.leverage, basebotconfig.customTemplate, basebotconfig.coinPosition, marketdata.tradeFee, basebotconfig.amountType, basebotconfig.currentTradeAmount, basebotconfig.useTwoSignals, basebotconfig.disableAfterStopLoss, intervalvalues[intervalindex], basebotconfig.includeIncompleteInterval,basebotconfig.mappedBuySignal, basebotconfig.mappedSellSignal)
						intervalindex += 1
						print(configuremadhatter.result)
						bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, marketdata.contractName)
						print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
						btr = bt.result
						print(btr.roi)
				elif answers['selection'] == 'decrease': 
						basebotconfig = haasomeClient.customBotApi.get_custom_bot(currentBotGuid, EnumCustomBotType.BASE_CUSTOM_BOT).result
						configuremadhatter = haasomeClient.customBotApi.setup_mad_hatter_bot2(basebotconfig.name,basebotconfig.guid,basebotconfig.accountId, basebotconfig.priceMarket.primaryCurrency,basebotconfig.priceMarket.secondaryCurrency, marketdata.contractName, basebotconfig.leverage, basebotconfig.customTemplate, basebotconfig.coinPosition, marketdata.tradeFee, basebotconfig.amountType, basebotconfig.currentTradeAmount, basebotconfig.useTwoSignals, basebotconfig.disableAfterStopLoss, intervalvalues[intervalindex], basebotconfig.includeIncompleteInterval,basebotconfig.mappedBuySignal, basebotconfig.mappedSellSignal)
						intervalindex -= 1
						print(configuremadhatter.result)
						bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, marketdata.contractName)
						print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
						btr = bt.result
						print(btr.roi)
			elif selected['selection'] == 'bBands Length':
					action = [
				{
					'type':'list',
					'name':'selection',
					'message': 'Lets do something',
					'choices': ['increse', 'decrease', 'back']}]
			answers = {'selection': None}
			if answers['selection'] != 'back':
				answers = prompt(action)
				if answers['selection'] == 'increse': 
					basebotconfig = haasomeClient.customBotApi.get_custom_bot(currentBotGuid, EnumCustomBotType.BASE_CUSTOM_BOT).result
					currentbbl = basebotconfig.bBands['Length']
					increasebbl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
    	basebotconfig.guid, EnumMadHatterIndicators.BBANDS, 0, currentbbl+1).result
					bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, marketdata.contractName)
					print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
					btr = bt.result
					print(btr.roi)
				elif answers['selection'] == 'decrease':
					basebotconfig = haasomeClient.customBotApi.get_custom_bot(currentBotGuid, EnumCustomBotType.BASE_CUSTOM_BOT).result
					currentbbl = basebotconfig.bBands['Length']
					increasebbl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
    	basebotconfig.guid, EnumMadHatterIndicators.BBANDS, 0, currentbbl-1).result
					bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, marketdata.contractName)
					print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
					btr = bt.result
					print(btr.roi)
			elif selected['selection'] == 'back':
					selected = prompt(selectparameter)
					print(selected)


backtestconfiguredmh()
