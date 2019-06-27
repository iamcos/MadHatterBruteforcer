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

def selectparametertochange():
		basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
		questions = [
			{'type': 'list','name': 'selectedparameter','message': 'Select parameter to change by using keys up and down then hit return',
			'choices': 
			[{'name': 'Bot time interval: '+str(basebotconfig.interval)+' minutes', 'value':'interval'},
			{'name': 'bBands MaType: '+str(basebotconfig.bBands['MaType']), 'value': 'MaType'},
			{'name': 'bBands Length: '+str(basebotconfig.bBands['Length']), 'value':'Length'},
			{'name': 'bBands Dev Up: '+str(basebotconfig.bBands['Devup']), 'value':'Devup'},
			{'name': 'bBands Dev Down: '+str(basebotconfig.bBands['Devdn']),'value':'Devdn'},
			{'name': 'Rsi Length: '+str(basebotconfig.rsi['RsiLength']) , 'value':'RsiLength'},
			{'name': 'Rsi Buy: '+str(basebotconfig.rsi['RsiOversold']), 'value': 'RsiOversold'},
			{'name': 'Rsi Sell: '+str(basebotconfig.rsi['RsiOverbought']), 'value':'RsiOverbought'},
			{'name': 'MACD Fast: '+str(basebotconfig.macd['MacdFast']), 'value':'MacdFast'},
			{'name': 'MACD Slow: ' +str(basebotconfig.macd['MacdSlow']), 'value': 'MacdSlow'},
			{'name': 'MACD Signal: '+str(basebotconfig.macd['MacdSign']), 'value':'MacdSign'},
			{'name': 'Changing time interval: ', 'value': 'setTimeInterval'},
			{'name': 'Full autotuning', 'value': 'fullauto'},
			{'name': 'exit', 'value': 'exit' }]}]
		return questions

def startconfiguring():
	while True:
		answers = prompt(selectparametertochange())
		if answers['selectedparameter'] == 'interval':
			tune_timeinterval()
		if answers['selectedparameter'] == 'MaType':
			pass
		if answers['selectedparameter'] == 'Length':
			setLength()
		if answers['selectedparameter'] == 'Devup':
			setDevup()
		if answers['selectedparameter'] == 'Devdn':
			setDevdn()
		if answers['selectedparameter'] == 'RsiLength':
			setRsiLength()
		if answers['selectedparameter'] == 'RsiOversold':
				setRsiOversold()
		if answers['selectedparameter'] == 'RsiOverbought':
				setRsiOverbought()
		if answers['selectedparameter'] == 'MacdFast':
			setMacdFast()
		if answers['selectedparameter'] == 'MacdSlow':
			setMacdSlow()
		if answers['selectedparameter'] == 'MacdSign':
			setMacdSign()
		if answers['selectedparameter'] == 'stopLoss':
			pass
		if answers['selectedparameter'] == 'setTimeInterval':
			btinterval = settimeinterval()
		if answers['selectedparameter'] == 'fullauto':
			# tune_timeinterval2()
			for x in range(3):
				tuneRsiLength()
				tuneRsiOverbought()
				tuneRsiOversold()
				tuneLength()
				tuneDevup()
				tuneDevdn()
				tuneMacdFast()
				tuneMacdSlow()
				tuneMacdSignal()
		if answers['selectedparameter'] == 'exit':
			break




def tune_timeinterval():
	basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.MAD_HATTER_BOT).result
	marketdata = []
	marketobject = haasomeClient.marketDataApi.get_price_markets(basebotconfig.priceMarket.priceSource)
	marketobjectr = marketobject.result
	for i,v  in enumerate(marketobjectr):
		if marketobjectr[i].primaryCurrency == basebotconfig.priceMarket.primaryCurrency and marketobjectr[i].secondaryCurrency == basebotconfig.priceMarket.secondaryCurrency:
			marketdata = marketobjectr[i]
	intervals = {'0 minutes': 0,'1 minutes':1,'2 minutes':2,'3 minutes':3,'4 minutes':4,'5 minutes':5,'6 minutes':6,'10 minutes':10,'12 minutes':12,'15 minutes':15,'20 minutes':20,'30 minutes':30,'45 minutes':45,'1 hour':60,'1.5 hours':90,'2 hours':120,'2.5 hours':150,'3 hours':180,'4 hours':240,'6 hours':360,'12 hours':720,'1 day':1440,'2 days':2880}
	intervalindex = []
	intervalkeys = list(intervals.keys())
	intervalvalues = list(intervals.values())
	for n, i in enumerate(intervalvalues):
		if i == basebotconfig.interval:
			intervalindex = n
			answers = {'selection': None}
			print('Current bot interval: ', intervalindex, ' Minutes')
			while answers['selection'] != 'back':
				action = [
					{
						'type':'list',
						'name':'selection',
						'message': 'Chose your next move: ',
						'choices': ['increse', 'decrease', 'back']}]
				if answers['selection'] == 'increse': 
							basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
							configuremadhatter = haasomeClient.customBotApi.setup_mad_hatter_bot2(basebotconfig.name,basebotconfig.guid,basebotconfig.accountId, basebotconfig.priceMarket.primaryCurrency,basebotconfig.priceMarket.secondaryCurrency, marketdata.contractName, basebotconfig.leverage, basebotconfig.customTemplate, basebotconfig.coinPosition, marketdata.tradeFee, basebotconfig.amountType, basebotconfig.currentTradeAmount, basebotconfig.useTwoSignals, basebotconfig.disableAfterStopLoss, intervalvalues[intervalindex], basebotconfig.includeIncompleteInterval,basebotconfig.mappedBuySignal, basebotconfig.mappedSellSignal)
							intervalindex += 1
							print(configuremadhatter.result.interval,'minutes')
							bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, marketdata.contractName)
							# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
							btr = bt.result
							print(btr.roi)
				elif answers['selection'] == 'decrease': 
							basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
							configuremadhatter = haasomeClient.customBotApi.setup_mad_hatter_bot2(basebotconfig.name,basebotconfig.guid,basebotconfig.accountId, basebotconfig.priceMarket.primaryCurrency,basebotconfig.priceMarket.secondaryCurrency, marketdata.contractName, basebotconfig.leverage, basebotconfig.customTemplate, basebotconfig.coinPosition, marketdata.tradeFee, basebotconfig.amountType, basebotconfig.currentTradeAmount, basebotconfig.useTwoSignals, basebotconfig.disableAfterStopLoss, intervalvalues[intervalindex], basebotconfig.includeIncompleteInterval,basebotconfig.mappedBuySignal, basebotconfig.mappedSellSignal)
							intervalindex -= 1
							print(configuremadhatter.result.interval, 'minutes')
							bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, marketdata.contractName)
							# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
							btr = bt.result
							print(btr.roi)
				elif answers['selection'] == 'back': 
					break
				answers = prompt(action)


### BBands tuning and setup ###

def setLength():
	answers = {'selection': None}
	while answers['selection'] != 'back':
		action = [
						{
							'type':'list',
							'name':'selection',
							'message': 'Chose your next move: ',
							'choices': ['increse', 'decrease', 'increase 10 steps','decrease 10 steps', 'back']}]
					
		if answers['selection'] == 'increse':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentl = basebotconfig.bBands['Length']
			currentl +=1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.BBANDS, 0, currentl)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi,' ', currentl)
		elif answers['selection'] == 'decrease':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentl = basebotconfig.bBands['Length']
			currentl -=1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.BBANDS, 0, currentl)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi,' ', currentl)

		elif answers['selection'] == 'increase 10 steps':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentl = basebotconfig.bBands['Length']
			for x in range(10):
				currentl +=1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.BBANDS, 0, currentl)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi,' ', currentl)

		elif answers['selection'] == 'decrease 10 steps':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentl = basebotconfig.bBands['Length']
			for x in range(10):
				currentl -=1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.BBANDS, 0, currentl)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi,' ', currentl)
		answers = prompt(action)

def setDevup():
	answers = {'selection': None}
	while answers['selection'] != 'back':
		action = [
						{
							'type':'list',
							'name':'selection',
							'message': 'Chose your next move: ',
							'choices': ['increse', 'decrease', 'increase 10 steps','decrease 10 steps', 'back']}]
					
		if answers['selection'] == 'increse':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentl = basebotconfig.bBands['Devup']
			currentl +=0.1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.BBANDS, 1, currentl)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi,' ', currentl)
		elif answers['selection'] == 'decrease':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentl = basebotconfig.bBands['Devup']
			currentl -=0.1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.BBANDS, 1, currentl)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi,' ', currentl)

		elif answers['selection'] == 'increase 10 steps':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentl = basebotconfig.bBands['Devup']
			for x in range(10):
				currentl +=0.1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.BBANDS, 1, currentl)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi,' ', currentl)

		elif answers['selection'] == 'decrease 10 steps':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentl = basebotconfig.bBands['Devup']
			for x in range(10):
				currentl -=0.1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.BBANDS, 1, currentl)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi,' ', currentl)
		answers = prompt(action)

def setDevdn():
	answers = {'selection': None}
	while answers['selection'] != 'back':
		action = [
						{
							'type':'list',
							'name':'selection',
							'message': 'Chose your next move: ',
							'choices': ['increse', 'decrease', 'increase 10 steps','decrease 10 steps', 'back']}]
					
		if answers['selection'] == 'increse':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentl = basebotconfig.bBands['Devdn']
			currentl +=0.1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.BBANDS, 2, currentl)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi,' ', currentl)
		elif answers['selection'] == 'decrease':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentl = basebotconfig.bBands['Devdn']
			currentl -=0.1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.BBANDS, 2, currentl)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi,' ', currentl)

		elif answers['selection'] == 'increase 10 steps':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentl = basebotconfig.bBands['Devdn']
			for x in range(10):
				currentl +=0.1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.BBANDS, 2, currentl)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi,' ', currentl)

		elif answers['selection'] == 'decrease 10 steps':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentl = basebotconfig.bBands['Devdn']
			for x in range(10):
				currentl -=0.1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.BBANDS, 2, currentl)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi,' ', currentl)
		answers = prompt(action)


### RSI PART starts now ###

def setRsiLength():
	answers = {'selection': None}
	while answers['selection'] != 'back':
		action = [
						{
							'type':'list',
							'name':'selection',
							'message': 'Chose your next move: ',
							'choices': ['increse', 'decrease', 'increase 10 steps','decrease 10 steps', 'back']}]
					
		if answers['selection'] == 'increse':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.rsi['RsiLength']
			currentvalue +=1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.RSI, 0	, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
		elif answers['selection'] == 'decrease':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.rsi['RsiLength']
			currentvalue -=1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.RSI, 0, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)

		elif answers['selection'] == 'increase 10 steps':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.rsi['RsiLength']
			for x in range(10):
				currentvalue +=1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.RSI, 0, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi, currentvalue)

		elif answers['selection'] == 'decrease 10 steps':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.rsi['RsiLength']
			for x in range(10):
				currentvalue -=1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.RSI, 0, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi, currentvalue)
		answers = prompt(action)

def setRsiOversold():
	answers = {'selection': None}
	while answers['selection'] != 'back':
		basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
		currentvalue = basebotconfig.rsi['RsiOversold']
		action = [
						{
							'type':'list',
							'name':'selection',
							'message': 'Chose your next move: ',
							'choices': ['increse', 'decrease', 'increase 10 steps','decrease 10 steps', 'back']}]	
		if answers['selection'] == 'increse':
			
			currentvalue +=1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.RSI, 1, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
		elif answers['selection'] == 'decrease':
			# basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			# currentvalue = basebotconfig.rsi['RsiOversold']
			currentvalue -=1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.RSI, 1, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)

		elif answers['selection'] == 'increase 10 steps':
			# basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			# currentvalue = basebotconfig.rsi['RsiOversold']
			for x in range(10):
				currentvalue +=1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.RSI, 1, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi, currentvalue)

		elif answers['selection'] == 'decrease 10 steps':
			# basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			# currentvalue = basebotconfig.rsi['RsiOversold']
			for x in range(10):
				currentvalue -=1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.RSI, 1, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi, currentvalue)
		answers = prompt(action)



def setRsiOverbought():
		answers = {'selection': None}
		while answers['selection'] != 'back':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.rsi['RsiOverbought']
			action = [
						{
							'type':'list',
							'name':'selection',
							'message': 'Chose your next move: ',
							'choices': ['increse', 'decrease', 'increase 10 steps','decrease 10 steps', 'back']}]	
			if answers['selection'] == 'increse':
				currentvalue +=1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.RSI, 2, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi, currentvalue)
			elif answers['selection'] == 'decrease':
				# basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
				# currentvalue = basebotconfig.rsi['RsiOverbought']
				currentvalue -=1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.RSI, 2, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi, currentvalue)

			elif answers['selection'] == 'increase 10 steps':
				# basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
				# currentvalue = basebotconfig.rsi['RsiOverbought']
				for x in range(10):
					currentvalue +=1
					setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
								guid, EnumMadHatterIndicators.RSI, 2, currentvalue)
					bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
					print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
					btr = bt.result
					print(btr.roi, currentvalue)

			elif answers['selection'] == 'decrease 10 steps':
				# basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
				# currentvalue = basebotconfig.rsi['RsiOverbought']
				for x in range(10):
					currentvalue -=1
					setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
								guid, EnumMadHatterIndicators.RSI, 2, currentvalue)
					bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
					print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
					btr = bt.result
					print(btr.roi, currentvalue)
			answers = prompt(action)


### MACD Configuration strings ###

def setMacdFast():
	answers = {'selection': None}
	while answers['selection'] != 'back':
		action = [
						{
							'type':'list',
							'name':'selection',
							'message': 'Chose your next move: ',
							'choices': ['increse', 'decrease', 'increase 10 steps','decrease 10 steps', 'back']}]
					
		if answers['selection'] == 'increse':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.macd['MacdFast']
			currentvalue +=1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.MACD, 0, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi,' ', currentvalue)
		elif answers['selection'] == 'decrease':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.macd['MacdFast']
			currentvalue -=1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.MACD, 0, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi,' ', currentvalue)

		elif answers['selection'] == 'increase 10 steps':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.macd['MacdFast']
			for x in range(10):
				currentvalue +=1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.MACD, 0, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi,' ', currentvalue)

		elif answers['selection'] == 'decrease 10 steps':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.macd['MacdFast']
			for x in range(10):
				currentvalue -=1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.MACD, 0, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi,' ', currentvalue)
		answers = prompt(action)


def setMacdSlow():
	answers = {'selection': None}
	while answers['selection'] != 'back':
		action = [
						{
							'type':'list',
							'name':'selection',
							'message': 'Chose your next move: ',
							'choices': ['increse', 'decrease', 'increase 10 steps','decrease 10 steps', 'back']}]
					
		if answers['selection'] == 'increse':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.macd['MacdSlow']
			currentvalue +=1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.MACD, 1, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi,' ', currentvalue)
		elif answers['selection'] == 'decrease':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.macd['MacdSlow']
			currentvalue -=1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.MACD, 1, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi,' ', currentvalue)

		elif answers['selection'] == 'increase 10 steps':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.macd['MacdSlow']
			for x in range(10):
				currentvalue +=1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.MACD, 1, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi,' ', currentvalue)

		elif answers['selection'] == 'decrease 10 steps':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.macd['MacdSlow']
			for x in range(10):
				currentvalue -=1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.MACD, 1, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi,' ', currentvalue)
		answers = prompt(action)


def setMacdSign():
			answers = {'selection': None}
			while answers['selection'] != 'back':
					action = [
						{
							'type':'list',
							'name':'selection',
							'message': 'Chose your next move: ',
							'choices': ['increse', 'decrease', 'increase 10 steps','decrease 10 steps', 'back']}]
					
					if answers['selection'] == 'increse':
						basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
						currentvalue = basebotconfig.macd['MacdSign']
						currentvalue +=1
						setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
									guid, EnumMadHatterIndicators.MACD, 2, currentvalue)
						bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
						print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
						btr = bt.result
						print(btr.roi,' ', currentvalue)
					elif answers['selection'] == 'decrease':
						basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
						currentvalue = basebotconfig.macd['MacdSign']
						currentvalue -=1
						setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
									guid, EnumMadHatterIndicators.MACD, 2, currentvalue)
						bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
						print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
						btr = bt.result
						print(btr.roi,' ', currentvalue)

					elif answers['selection'] == 'increase 10 steps':
						basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
						currentvalue = basebotconfig.macd['MacdSign']
						for x in range(10):
							currentvalue +=1
							setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
										guid, EnumMadHatterIndicators.MACD, 2, currentvalue)
							bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
							print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
							btr = bt.result
							print(btr.roi,' ', currentvalue)

					elif answers['selection'] == 'decrease 10 steps':
						basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
						currentvalue = basebotconfig.macd['MacdSign']
						for x in range(10):
							currentvalue -=1
							setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
										guid, EnumMadHatterIndicators.MACD, 2, currentvalue)
							bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
							print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
							btr = bt.result
							print(btr.roi,' ', currentvalue)
					answers = prompt(action)

### Helper classes ###

### Bot Selector ###

def botsellector():
  allbots = haasomeClient.customBotApi.get_all_custom_bots().result
  for i, x in enumerate(allbots):
        print(i, x.name, 'ROI : ',x.roi) #bottypedict[x.botType] to bring bot type into view
  botnum = input(
    'Type bot number to use from the list above and hit return. \n Your answer: ')
  try:
    botnumobj = allbots[int(botnum)]
  except ValueError:
     botnum = input(
    'Wrong symbol. Can only use numbers. Type bot number indecated at the start of the string here: ')
  except IndexError: 
    botnum = input(
    'Bot number is out of range. Type the number that is present on the list and hit enter: ')
  finally:
    botnumobj = allbots[int(botnum)]
  print(botnumobj.name +'is selected!')
  return botnumobj



### Backtesting interval being redefined ###

def settimeinterval():
   intervals = {'1H': 60, '2H': 120, '3H': 180, '4H': 240, '5H': 300, '6H': 360, '7H': 420, '8H': 480, '9H': 540, '10H': 600, '11H': 660, '12H': 720, '13H': 780, '14H': 840, '15H': 900, '16H': 960, '17H': 1020, '18H': 1080, '19H': 1140, '20H': 1200, '21H': 1260, '22H': 1320, '23H': 1380, '24H': 1440, '1D': 1440, '2D': 2880, '3D': 4320, '4D': 5760, '5D': 7200, '6D': 8640, '7D': 10080, '8D': 11520, '9D': 12960, '10D': 14400, '11D': 15840, '12D': 17280, '13D': 18720, '14D': 20160, '15D': 21600, '16D': 23040, '17D': 24480, '18D': 25920, '19D': 27360, '20D': 28800, '21D': 30240, '22D': 31680, '23D': 33120, '24D': 34560, '25D': 36000, '26D': 37440, '27D': 38880, '28D': 40320, '29D': 41760, '30D': 43200}
   user_resp = input(
      'Define backtesting interval: 1H-24H for hours, 1D-30D for days. \n Your answer: ')
   try:
    interval = intervals[user_resp]
   except KeyError:
    user_resp = input('Please re-enter your chouse exactly as 1H for 1 hour, 5D for 5 days and so on and hit return again \n Your answer: ')
    interval = intervals[user_resp]
   print('Backtesting interval is set to', user_resp,
       'which is exactly ', interval, 'minutes')
   return interval


### Trying full auto algo ###

def fullauto():
	basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
	basebotconfig.interval
	basebotconfig.bBands['MaType']
	basebotconfig.bBands['Length']
	basebotconfig.bBands['Devup']
	basebotconfig.bBands['Devdn']
	basebotconfig.rsi['RsiLength']
	basebotconfig.rsi['RsiOversold']
	basebotconfig.rsi['RsiOverbought']
	basebotconfig.macd['MacdFast']
	basebotconfig.macd['MacdSlow']
	basebotconfig.macd['MacdSign']


def tune_timeinterval2():
	basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
	marketdata = []
	marketobject = haasomeClient.marketDataApi.get_price_markets(basebotconfig.priceMarket.priceSource)
	marketobjectr = marketobject.result
	for i,v  in enumerate(marketobjectr):
		if marketobjectr[i].primaryCurrency == basebotconfig.priceMarket.primaryCurrency and marketobjectr[i].secondaryCurrency == basebotconfig.priceMarket.secondaryCurrency:
			marketdata = marketobjectr[i]

	intervals = {'0 minutes': 0,'1 minutes':1,'2 minutes':2,'3 minutes':3,'4 minutes':4,'5 minutes':5,'6 minutes':6,'10 minutes':10,'12 minutes':12,'15 minutes':15,'20 minutes':20,'30 minutes':30,'45 minutes':45,'1 hour':60,'1.5 hours':90,'2 hours':120,'2.5 hours':150,'3 hours':180,'4 hours':240,'6 hours':360,'12 hours':720,'1 day':1440,'2 days':2880}
	initialinterval = basebotconfig.interval
	intervalindex = ' '
	intervalkeys = list(intervals.keys())
	intervalvalues = list(intervals.values())
	paramroi = []
	for n, i in enumerate(intervalvalues):
		if i == basebotconfig.interval:
			intervalindex = n
			print('Current bot interval: ', intervalindex, ' Minutes')

	while int(intervalindex) >=0 and int(intervalindex) <= 12:
		print(intervalindex)
		configuremadhatter = haasomeClient.customBotApi.setup_mad_hatter_bot2(basebotconfig.name,basebotconfig.guid,basebotconfig.accountId, basebotconfig.priceMarket.primaryCurrency,basebotconfig.priceMarket.secondaryCurrency, marketdata.contractName, basebotconfig.leverage, basebotconfig.customTemplate, basebotconfig.coinPosition, marketdata.tradeFee, basebotconfig.amountType, basebotconfig.currentTradeAmount, basebotconfig.useTwoSignals, basebotconfig.disableAfterStopLoss, intervalvalues[intervalindex], basebotconfig.includeIncompleteInterval,basebotconfig.mappedBuySignal, basebotconfig.mappedSellSignal)
		
		print(configuremadhatter.result.interval,'minutes')
		bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, marketdata.contractName)
		# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
		btr = bt.result
		intervalindex += 1
		paramroi.append([btr.roi,intervalvalues[intervalindex]])
		print(btr.roi)
	while initialinterval > 0 and initialinterval <=30:
		configuremadhatter = haasomeClient.customBotApi.setup_mad_hatter_bot2(basebotconfig.name,basebotconfig.guid,basebotconfig.accountId, basebotconfig.priceMarket.primaryCurrency,basebotconfig.priceMarket.secondaryCurrency, marketdata.contractName, basebotconfig.leverage, basebotconfig.customTemplate, basebotconfig.coinPosition, marketdata.tradeFee, basebotconfig.amountType, basebotconfig.currentTradeAmount, basebotconfig.useTwoSignals, basebotconfig.disableAfterStopLoss, intervalvalues[intervalindex], basebotconfig.includeIncompleteInterval,basebotconfig.mappedBuySignal, basebotconfig.mappedSellSignal)
		print(configuremadhatter.errorCode, configuremadhatter.errorMessage)
		print(configuremadhatter.result.interval,'minutes')
		bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, marketdata.contractName)
		print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
		btr = bt.result
		print(btr.roi)
		paramroi.append([btr.roi,intervalvalues[intervalindex]])
		initialinterval -= 1


		paramroisorted = sorted(paramroi, key=lambda x: x[0], reverse=True)
		print(paramroisorted)
		configuremadhatter = haasomeClient.customBotApi.setup_mad_hatter_bot2(basebotconfig.name,basebotconfig.guid,basebotconfig.accountId, basebotconfig.priceMarket.primaryCurrency,basebotconfig.priceMarket.secondaryCurrency, marketdata.contractName, basebotconfig.leverage, basebotconfig.customTemplate, basebotconfig.coinPosition, marketdata.tradeFee, basebotconfig.amountType, basebotconfig.currentTradeAmount, basebotconfig.useTwoSignals, basebotconfig.disableAfterStopLoss, paramroisorted[0][1], basebotconfig.includeIncompleteInterval,basebotconfig.mappedBuySignal, basebotconfig.mappedSellSignal)
		print('best time interval has been set')


#### RSI TUNING ###

def tuneRsiLength():
	btroilist = []
	basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
	currentvalue = basebotconfig.rsi['RsiLength']
	initvalue = currentvalue
	for x in range(5):
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.RSI, 0	, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
			btroilist.append([btr.roi, currentvalue])
			currentvalue +=1
	currentvalue = initvalue-1
	for x in range(5):
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(guid, EnumMadHatterIndicators.RSI, 0	, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
			btroilist.append([btr.roi, currentvalue])
			currentvalue -=1
	btroilistsorted = sorted(btroilist, key=lambda x: x[0], reverse=True)
	setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				guid, EnumMadHatterIndicators.RSI, 0	, btroilistsorted[0][1])
	print(btroilistsorted[0][1])


def tuneRsiOversold():
		btroilist = []
		basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
		currentvalue = basebotconfig.rsi['RsiOversold']
		initvalue = currentvalue
		for x in range(5):
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.RSI, 1, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
			btroilist.append([btr.roi, currentvalue])
			currentvalue +=1
		currentvalue = initvalue-1
		for x in range(5):
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.RSI, 1, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
			btroilist.append([btr.roi, currentvalue])
			currentvalue -=1
		btroilistsorted = sorted(btroilist, key=lambda x: x[0], reverse=True)
		setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				guid, EnumMadHatterIndicators.RSI, 1	, btroilistsorted[0][1])




def tuneRsiOverbought():
			btroilist = []
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.rsi['RsiOverbought']
			initvalue = currentvalue
			for x in range(5):
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.RSI, 2, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi, currentvalue)
				btroilist.append([btr.roi, currentvalue])
				currentvalue +=1
			currentvalue = initvalue-1
			for x in range(5):
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.RSI, 2, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi, currentvalue)
				btroilist.append([btr.roi, currentvalue])
				currentvalue -=1
			btroilistsorted = sorted(btroilist, key=lambda x: x[0], reverse=True)
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				guid, EnumMadHatterIndicators.RSI, 2	, btroilistsorted[0][1])

###BBANDS Tuner ###

def tuneDevdn():
	btroilist = []
	basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
	currentvalue = basebotconfig.bBands['Devdn']
	initvalue = currentvalue
	for x in range(5):
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.BBANDS, 2	, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
			btroilist.append([btr.roi, currentvalue])
			currentvalue +=0.1
	currentvalue = initvalue-0.1
	for x in range(5):
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(guid, EnumMadHatterIndicators.BBANDS, 2	, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
			btroilist.append([btr.roi, currentvalue])
			currentvalue -=0.1
	btroilistsorted = sorted(btroilist, key=lambda x: x[0], reverse=True)
	setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				guid, EnumMadHatterIndicators.BBANDS, 2	, btroilistsorted[0][1])
	print(btroilistsorted[0][1])


def tuneDevup():
		btroilist = []
		basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
		currentvalue = basebotconfig.bBands['Devup']
		initvalue = currentvalue
		for x in range(5):
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.BBANDS, 1, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
			btroilist.append([btr.roi, currentvalue])
			currentvalue +=0.1
		currentvalue = initvalue-0.1
		for x in range(5):
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.BBANDS, 1, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
			btroilist.append([btr.roi, currentvalue])
			currentvalue -=0.1
		btroilistsorted = sorted(btroilist, key=lambda x: x[0], reverse=True)
		setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				guid, EnumMadHatterIndicators.BBANDS, 1	, btroilistsorted[0][1])




def tuneLength():
			btroilist = []
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.bBands['Length']
			initvalue = currentvalue
			for x in range(5):
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.BBANDS, 0, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi, currentvalue)
				btroilist.append([btr.roi, currentvalue])
				currentvalue +=1
			currentvalue = initvalue-1
			for x in range(5):
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.BBANDS, 0 ,currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi, currentvalue)
				btroilist.append([btr.roi, currentvalue])
				currentvalue -=1
			btroilistsorted = sorted(btroilist, key=lambda x: x[0], reverse=True)
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				guid, EnumMadHatterIndicators.BBANDS, 0	, btroilistsorted[0][1])

### MACD TUNER STARTS ###

def tuneMacdSlow():
	btroilist = []
	basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
	currentvalue = basebotconfig.macd['MacdSlow']
	initvalue = currentvalue
	for x in range(5):
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.MACD, 1	, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
			btroilist.append([btr.roi, currentvalue])
			currentvalue +=1
	currentvalue = initvalue-1
	for x in range(5):
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(guid, EnumMadHatterIndicators.MACD,1	, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
			btroilist.append([btr.roi, currentvalue])
			currentvalue -=1
	btroilistsorted = sorted(btroilist, key=lambda x: x[0], reverse=True)
	setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				guid, EnumMadHatterIndicators.MACD,1	, btroilistsorted[0][1])
	print(btroilistsorted[0][1])


def tuneMacdFast():
		btroilist = []
		basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
		currentvalue = basebotconfig.macd['MacdFast']
		initvalue = currentvalue
		for x in range(5):
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.MACD, 0, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
			btroilist.append([btr.roi, currentvalue])
			currentvalue +=1
		currentvalue = initvalue-1
		for x in range(5):
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.MACD, 0, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
			btroilist.append([btr.roi, currentvalue])
			currentvalue -=1
		btroilistsorted = sorted(btroilist, key=lambda x: x[0], reverse=True)
		setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				guid, EnumMadHatterIndicators.MACD, 0	, btroilistsorted[0][1])




def tuneMacdSignal():
			btroilist = []
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.macd['MacdSign']
			initvalue = currentvalue
			for x in range(5):
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.MACD, 2, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi, currentvalue)
				btroilist.append([btr.roi, currentvalue])
				currentvalue +=1
			currentvalue = initvalue-1
			for x in range(5):
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.MACD, 2, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi, currentvalue)
				btroilist.append([btr.roi, currentvalue])
				currentvalue -=1
			btroilistsorted = sorted(btroilist, key=lambda x: x[0], reverse=True)
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				guid, EnumMadHatterIndicators.MACD, 2	, btroilistsorted[0][1])

### Helper classes ###


### required data for script to work ###
ip, secret = configserver.validateserverdata()
haasomeClient = HaasomeClient(ip, secret)
botnumobj = botsellector()
guid = botnumobj.guid
btinterval = 10000
# answers = prompt(selectparametertochange())
info = startconfiguring()
print(info)

