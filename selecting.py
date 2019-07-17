from __future__ import print_function, unicode_literals
import regex
from decimal import Decimal
from haasomeapi.HaasomeClient import HaasomeClient
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError
import configserver
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
from licensing.models import *
from licensing.methods import Key, Helpers

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
			{'name': 'Change BT range', 'value': 'therange'},
			{'name': 'bBands Length: '+str(basebotconfig.bBands['Length']), 'value':'Length'},
			{'name': 'bBands Dev Up: '+str(basebotconfig.bBands['Devup']), 'value':'Devup'},
			{'name': 'bBands Dev Down: '+str(basebotconfig.bBands['Devdn']),'value':'Devdn'},
			{'name': 'Rsi Length: '+str(basebotconfig.rsi['RsiLength']) , 'value':'RsiLength'},
			{'name': 'Rsi Buy: '+str(basebotconfig.rsi['RsiOversold']), 'value': 'RsiOversold'},
			{'name': 'Rsi Sell: '+str(basebotconfig.rsi['RsiOverbought']), 'value':'RsiOverbought'},
			{'name': 'MACD Fast: '+str(basebotconfig.macd['MacdFast']), 'value':'MacdFast'},
			{'name': 'MACD Slow: ' +str(basebotconfig.macd['MacdSlow']), 'value': 'MacdSlow'},
			{'name': 'MACD Signal: '+str(basebotconfig.macd['MacdSign']), 'value':'MacdSign'},
			{'name': 'All Coins:', 'value':'allcoins'},
			{'name': 'Changing time interval: ', 'value': 'setTimeInterval'},
			{'name': 'Full autotuning', 'value': 'fullauto'},
			{'name': 'exit', 'value': 'exit' }]}]
		return questions

def startconfiguring(therange):
	while True:
		answers = prompt(selectparametertochange())
		if answers['selectedparameter'] == 'interval':
			tune_timeinterval()
		if answers['selectedparameter'] == 'MaType':
			pass
		if answers['selectedparameter'] == 'Length':
			tuneLength(therange)
		if answers['selectedparameter'] == 'Devup':
			tuneDevup(therange)
		if answers['selectedparameter'] == 'Devdn':
			tuneDevdn(therange)
		if answers['selectedparameter'] == 'RsiLength':
				tuneRsiLength(therange)
		if answers['selectedparameter'] == 'RsiOversold':
				tuneRsiOversold(therange)
		if answers['selectedparameter'] == 'RsiOverbought':
				tuneRsiOverbought(therange)
		if answers['selectedparameter'] == 'MacdFast':
			tuneMacdFast(therange)
		if answers['selectedparameter'] == 'MacdSlow':
			tuneMacdSlow(therange)
		if answers['selectedparameter'] == 'MacdSign':
			tuneMacdSignal(therange)
		if answers['selectedparameter'] == 'allcoins':
			results = probeallmarkets()
		if answers['selectedparameter'] == 'setTimeInterval':
			pass
			#btinterval = settimeinterval()
		if answers['selectedparameter'] == 'fullauto':
			# tune_timeinterval2()
			# for x in range(3):
			for x in range(2):
					tuneRsiLength(therange)
					tuneRsiOversold(therange)
					tuneRsiOverbought(therange)

					for x in range(2):
						tuneLength(therange)
						tuneDevdn(therange)
						tuneDevdn(therange)
		if answers['selectedparameter'] == 'therange':
			therange = settherange()
		if answers['selectedparameter'] == 'exit':
			break

def tunersi(therange):
	for x in range(therange):
		tuneRsiLength(therange)


def connectionstring():
	ip, secret = configserver.validateserverdata()
	haasomeClient = HaasomeClient(ip, secret)
	return haasomeClient
	



def create_trial():
	trial_key = Key.create_trial_key("WyI1NzkyIiwibDV5QVVDV2VmQ08zYmNmbE9GWHdyVFFNK2hzb0l6YldPOVhUY0hQVSJd", 3941, Helpers.GetMachineCode())
	if trial_key[0] == None:
				print("An error occurred: {0}".format(trial_key[1]))


	pubKey = "<RSAKeyValue><Modulus>sGbvxwdlDbqFXOMlVUnAF5ew0t0WpPW7rFpI5jHQOFkht/326dvh7t74RYeMpjy357NljouhpTLA3a6idnn4j6c3jmPWBkjZndGsPL4Bqm+fwE48nKpGPjkj4q/yzT4tHXBTyvaBjA8bVoCTnu+LiC4XEaLZRThGzIn5KQXKCigg6tQRy0GXE13XYFVz/x1mjFbT9/7dS8p85n8BuwlY5JvuBIQkKhuCNFfrUxBWyu87CFnXWjIupCD2VO/GbxaCvzrRjLZjAngLCMtZbYBALksqGPgTUN7ZM24XbPWyLtKPaXF2i4XRR9u6eTj5BfnLbKAU5PIVfjIS+vNYYogteQ==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"

	res = Key.activate(token="WyI1NzkyIiwibDV5QVVDV2VmQ08zYmNmbE9GWHdyVFFNK2hzb0l6YldPOVhUY0hQVSJd",\
																				rsa_pub_key=pubKey,\
																				product_id=3941, key=trial_key[0], \
																					)
																				# machine_code=Helpers.GetMachineCode())

	if res[0] == None: #or not Helpers.IsOnRightMachine(res[0])
					print("An error occurred: {0}".format(res[1]))
	else:
					print("Success")
					
					license_key = res[0]
					print("Feature 1: " + str(license_key.f1))
					print("License expires: " + str(license_key.expires))
	return trial_key

def verifylicense(trial_key):
	RSAPubKey = "<RSAKeyValue><Modulus>nz/GmQrJsY53isJ23svQM9ewz2E/rZI+mdhWV+YxIDn7fljNN5MBw7UPGcAUARQkPfpUPpkGEKjmBHvQh5jk5yvcuzIVNNlfew3PkmbnkZbjREM6PzvZumC8QYK2p4zrdLFlt7SfLZWiRNVnT2dO4ssnsxmv//V8IKVwX8dkEg8mXmviAU/VTQC4o+MJG0Lqinu76X241pJDHiWRGIErpBgUw455hRByEpkQvjBdVclIPhyhn46Kf5ZUQ3CImjaKkTkUTDkmSW8ieYUa4A3xe4JFgCBgfMWaX5CU5X3tuGL05ZO4jDoda2jdtWdsemq/uQykh+dsfxBSYHtQPLHTHw==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
	auth = "WyI1NzkyIiwibDV5QVVDV2VmQ08zYmNmbE9GWHdyVFFNK2hzb0l6YldPOVhUY0hQVSJd"

	result = Key.activate(token=auth,\
																				rsa_pub_key=RSAPubKey,\
																				product_id=3349, \
																				key="ICVLD-VVSZR-ZTICT-YKGXL",\
																					)
																				# machine_code=Helpers.GetMachineCode())

	if result[0] == None: #or not Helpers.IsOnRightMachine(res[0]):
					# an error occurred or the key is invalid or it cannot be activated
					# (eg. the limit of activated devices was achieved)
					print("The license does not work: {0}".format(result[1]))
	else:
					# everything went fine if we are here!
					print("The license is valid!")


def allmarketshistory():
	basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.MAD_HATTER_BOT).result
	marketdata = []
	historyresult = ' '
	results = []
	marketobject = haasomeClient.marketDataApi.get_price_markets(basebotconfig.priceMarket.priceSource)
	marketobjectr = marketobject.result
	for i,v  in enumerate(marketobjectr):
		gethistory = haasomeClient.marketDataApi.get_history_from_market(v,basebotconfig.interval,btinterval)
		print('History for ', v.primaryCurrency, v.secondaryCurrency, gethistory.EnumErrorCode)	
		print(gethistory.re)



def probeallmarkets():
	basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.MAD_HATTER_BOT).result
	marketdata = []
	etalonroi = basebotconfig.roi*0.8
	historyresult = None
	results = []
	marketobject = haasomeClient.marketDataApi.get_price_markets(basebotconfig.priceMarket.priceSource)
	marketobjectr = marketobject.result
	for i,v  in enumerate(marketobjectr):
		settradeammount = v.minimumTradeAmount*10
		configuremadhatter = haasomeClient.customBotApi.setup_mad_hatter_bot2(basebotconfig.name,basebotconfig.guid,basebotconfig.accountId, basebotconfig.priceMarket.primaryCurrency,basebotconfig.priceMarket.secondaryCurrency, v.contractName, basebotconfig.leverage, basebotconfig.customTemplate, basebotconfig.coinPosition, v.tradeFee, basebotconfig.amountType, settradeammount*10, basebotconfig.useTwoSignals, basebotconfig.disableAfterStopLoss, basebotconfig.interval, basebotconfig.includeIncompleteInterval,basebotconfig.mappedBuySignal, basebotconfig.mappedSellSignal)
		# gethistory = haasomeClient.marketDataApi.get_history_from_market(v,basebotconfig.interval,btinterval)
		# historyresult = gethistory.errorCode
		bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,v.primaryCurrency, v.secondaryCurrency, v.contractName)
		btr = bt.result
		results.append([btr.roi,v.primaryCurrency, v.secondaryCurrency, v.contractName])
		print([v.primaryCurrency, v.secondaryCurrency, btr.roi])
	resultssorted = sorted(results, key=lambda x: x[0], reverse=True)
	for i, x in enumerate(resultssorted)[10]:
		if x[0] >= etalonroi:
			newbot = haasomeClient.customBotApi.clone_custom_bot(basebotconfig.accountId,basebotconfig.guid,EnumCustomBotType.MAD_HATTER_BOT,x[i][1]+x[i][2]+x[i][0],x[i][1],x[i][2],x[i][3])
			print('bot for ', x[1], x[2], 'created')

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
							
							bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, marketdata.contractName)
							# # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
							btr = bt.result
							print(btr.roi, ' at', configuremadhatter.result.interval, 'minutes')
							intervalindex += 1
				elif answers['selection'] == 'decrease': 
							basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
							configuremadhatter = haasomeClient.customBotApi.setup_mad_hatter_bot2(basebotconfig.name,basebotconfig.guid,basebotconfig.accountId, basebotconfig.priceMarket.primaryCurrency,basebotconfig.priceMarket.secondaryCurrency, marketdata.contractName, basebotconfig.leverage, basebotconfig.customTemplate, basebotconfig.coinPosition, marketdata.tradeFee, basebotconfig.amountType, basebotconfig.currentTradeAmount, basebotconfig.useTwoSignals, basebotconfig.disableAfterStopLoss, intervalvalues[intervalindex], basebotconfig.includeIncompleteInterval,basebotconfig.mappedBuySignal, basebotconfig.mappedSellSignal)
							intervalindex -= 1
							bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, marketdata.contractName)
							# # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
							btr = bt.result
							print(btr.roi, ' at', configuremadhatter.result.interval, 'minutes')
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
			# # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi,' ', currentl, 'bBands Length')
		elif answers['selection'] == 'decrease':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentl = basebotconfig.bBands['Length']
			currentl -=1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.BBANDS, 0, currentl)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			# # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi,' ', currentl,'bBands Length')

		elif answers['selection'] == 'increase 10 steps':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentl = basebotconfig.bBands['Length']
			for x in range(10):
				currentl +=1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.BBANDS, 0, currentl)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				# # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
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
				# # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
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
			# # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi,' ', currentl)
		elif answers['selection'] == 'decrease':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentl = basebotconfig.bBands['Devup']
			currentl -=0.1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.BBANDS, 1, currentl)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			# # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
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
				# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
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
				# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
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
			# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi,' ', currentl)
		elif answers['selection'] == 'decrease':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentl = basebotconfig.bBands['Devdn']
			currentl -=0.1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.BBANDS, 2, currentl)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
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
				# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
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
				# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
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
			# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
		elif answers['selection'] == 'decrease':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.rsi['RsiLength']
			currentvalue -=1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.RSI, 0, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
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
				# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
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
				# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
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
			# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
		elif answers['selection'] == 'decrease':
			# basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			# currentvalue = basebotconfig.rsi['RsiOversold']
			currentvalue -=1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.RSI, 1, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
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
				# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
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
				# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
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
				# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi, currentvalue)
			elif answers['selection'] == 'decrease':
				# basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
				# currentvalue = basebotconfig.rsi['RsiOverbought']
				currentvalue -=1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.RSI, 2, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
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
					# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
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
					# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
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
			# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi,' ', currentvalue)
		elif answers['selection'] == 'decrease':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.macd['MacdFast']
			currentvalue -=1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.MACD, 0, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
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
				# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
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
				# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
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
			# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi,' ', currentvalue)
		elif answers['selection'] == 'decrease':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.macd['MacdSlow']
			currentvalue -=1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.MACD, 1, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
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
				# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
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
				# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
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
						# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
						btr = bt.result
						print(btr.roi,' ', currentvalue)
					elif answers['selection'] == 'decrease':
						basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
						currentvalue = basebotconfig.macd['MacdSign']
						currentvalue -=1
						setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
									guid, EnumMadHatterIndicators.MACD, 2, currentvalue)
						bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
						# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
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
							# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
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
							# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
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

	if int(intervalindex) >=0 and int(intervalindex) <= 12:
		print(intervalindex)
		configuremadhatter = haasomeClient.customBotApi.setup_mad_hatter_bot2(basebotconfig.name,basebotconfig.guid,basebotconfig.accountId, basebotconfig.priceMarket.primaryCurrency,basebotconfig.priceMarket.secondaryCurrency, marketdata.contractName, basebotconfig.leverage, basebotconfig.customTemplate, basebotconfig.coinPosition, marketdata.tradeFee, basebotconfig.amountType, basebotconfig.currentTradeAmount, basebotconfig.useTwoSignals, basebotconfig.disableAfterStopLoss, intervalvalues[intervalindex], basebotconfig.includeIncompleteInterval,basebotconfig.mappedBuySignal, basebotconfig.mappedSellSignal)
		
		print(configuremadhatter.result.interval,'minutes')
		bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, marketdata.contractName)
		# # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
		btr = bt.result
		paramroi.append([btr.roi,intervalvalues[intervalindex]])
		print(btr.roi)
		intervalindex += 1
	while initialinterval > 1 and initialinterval <=10:
		configuremadhatter = haasomeClient.customBotApi.setup_mad_hatter_bot2(basebotconfig.name,basebotconfig.guid,basebotconfig.accountId, basebotconfig.priceMarket.primaryCurrency,basebotconfig.priceMarket.secondaryCurrency, marketdata.contractName, basebotconfig.leverage, basebotconfig.customTemplate, basebotconfig.coinPosition, marketdata.tradeFee, basebotconfig.amountType, basebotconfig.currentTradeAmount, basebotconfig.useTwoSignals, basebotconfig.disableAfterStopLoss, intervalvalues[intervalindex], basebotconfig.includeIncompleteInterval,basebotconfig.mappedBuySignal, basebotconfig.mappedSellSignal)
		print(configuremadhatter.errorCode, configuremadhatter.errorMessage)
		print(configuremadhatter.result.interval,'minutes')
		bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, marketdata.contractName)
		# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
		btr = bt.result
		print(btr.roi)
		paramroi.append([btr.roi,intervalvalues[intervalindex]])
		initialinterval -= 1


		paramroisorted = sorted(paramroi, key=lambda x: x[0], reverse=True)
		print(paramroisorted)
		configuremadhatter = haasomeClient.customBotApi.setup_mad_hatter_bot2(basebotconfig.name,basebotconfig.guid,basebotconfig.accountId, basebotconfig.priceMarket.primaryCurrency,basebotconfig.priceMarket.secondaryCurrency, marketdata.contractName, basebotconfig.leverage, basebotconfig.customTemplate, basebotconfig.coinPosition, marketdata.tradeFee, basebotconfig.amountType, basebotconfig.currentTradeAmount, basebotconfig.useTwoSignals, basebotconfig.disableAfterStopLoss, paramroisorted[0][1], basebotconfig.includeIncompleteInterval,basebotconfig.mappedBuySignal, basebotconfig.mappedSellSignal)
		print('best time interval has been set')


#### RSI tuning 3 params together ###
def tunersi():
	rsiconfig = []
	basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
	l = basebotconfig.rsi['RsiLength']
	s = basebotconfig.rsi['RsiOversold']
	b = basebotconfig.rsi['RsiOverbought'] 
	
	def setl(l):
		setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.RSI, 0	, l)
		bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
		btr = bt.result
		print(btr.roi, 'RSI: ', l, s, b)
		rsiconfig.append([btr.roi,l,s,b])
		return btr.roi

	def sets(s):
		setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.RSI, 1	, s)
		bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
		btr = bt.result
		print(btr.roi, 'RSI: ', l, s, b)
		rsiconfig.append([btr.roi,l,s,b])
		return btr.roi
	
	def setb(b):
		setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.RSI, 2	, b)
		bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
		btr = bt.result
		print(btr.roi, 'RSI: ', l, s, b)
		rsiconfig.append([btr.roi,l,s,b])
		return btr.roi

	if rsiconfig[0][0] == 0 or rsiconfig[0][0] == Decimal(0.0):
		l -= 1
		setl(l)
		s += 1
		sets(s)
		b -= 1
		setb(b)
		if rsiconfig[1][0] > rsiconfig[2][0] and rsiconfig[0][0] >= rsiconfig[1][0]:
			for x in range(2):
				l +=1
				setl(l)
				for x in range(2):
					s += 1
					sets(s)
					b-=1
					setb(b)
				l -=1
				setl(l)
				for x in range(2):
					s += 1
					sets(s)
					b-=1
					setb(b)

#### RSI TUNING ###

def tuneRsiLength(therange: float):
	print('tuning rsi lenghth')
	btroilist = []
	basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
	currentvalue = basebotconfig.rsi['RsiLength']
	initvalue = currentvalue
	for x in range(int(therange)):
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.RSI, 0	, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, ' at RSI Length: ', currentvalue)
			btroilist.append([btr.roi, currentvalue])
			currentvalue +=1

	currentvalue = btroilist[0][1]
	for x in range(int(therange)):
		if currentvalue > 0:
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(guid, EnumMadHatterIndicators.RSI, 0	, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi, 'RSI Length: ',currentvalue)
				btroilist.append([btr.roi, currentvalue])
				currentvalue -=1
		
		if currentvalue <= 0:
			pass
	
	btroilistsorted = sorted(btroilist, key=lambda x: x[0], reverse=True)
	print(btroilistsorted)
	
	setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
	guid, EnumMadHatterIndicators.RSI, 0, btroilistsorted[0][1])


def tuneRsiOversold(therange):
		btroilist = []
		basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
		currentvalue = basebotconfig.rsi['RsiOversold']
		initvalue = currentvalue
		if currentvalue > 0:
			for x in range(therange):
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.RSI, 1, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi,'RSI Buy', currentvalue)
				btroilist.append([btr.roi, currentvalue])
				currentvalue +=1
			currentvalue = initvalue-1
			for x in range(therange):
				if currentvalue >0:
					setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
								guid, EnumMadHatterIndicators.RSI, 1, currentvalue)
					bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
					# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
					btr = bt.result
					print(btr.roi,'RSI Buy',currentvalue)
					btroilist.append([btr.roi, currentvalue])
					currentvalue -=1
			btroilistsorted = sorted(btroilist, key=lambda x: x[0], reverse=True)
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
					guid, EnumMadHatterIndicators.RSI, 1	, btroilistsorted[0][1])




def tuneRsiOverbought(therange):
			btroilist = []
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.rsi['RsiOverbought']
			initvalue = currentvalue
			if currentvalue >0:	
				for x in range(therange):
					setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
								guid, EnumMadHatterIndicators.RSI, 2, currentvalue)
					bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
					# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
					btr = bt.result
					print(btr.roi, btr.roi, 'RSI sell :', currentvalue)
					btroilist.append([btr.roi, currentvalue])
					currentvalue +=1
				currentvalue = initvalue-1
				for x in range(therange):
					if currentvalue >0:
						setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
									guid, EnumMadHatterIndicators.RSI, 2, currentvalue)
						bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
						# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
						btr = bt.result
						print(btr.roi, btr.roi, 'RSI Sell: ', currentvalue)
						btroilist.append([btr.roi, currentvalue])
						currentvalue -=1
				btroilistsorted = sorted(btroilist, key=lambda x: x[0], reverse=True)
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
					guid, EnumMadHatterIndicators.RSI, 2	, btroilistsorted[0][1])

###BBANDS Tuner ###

def tuneDevdn(therange):
	btroilist = []
	basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
	currentvalue = round(Decimal(basebotconfig.bBands['Devdn']),2)
	initvalue = currentvalue
	if currentvalue >0:
		for x in range(therange):
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.BBANDS, 2	, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi,'Devdn: ', currentvalue)
				btroilist.append([btr.roi, currentvalue])
				currentvalue +=round(Decimal(0.1),2)
		currentvalue = initvalue-round(Decimal(0.1),2)
		for x in range(therange):
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(guid, EnumMadHatterIndicators.BBANDS, 2	, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi,'Devdn: ', currentvalue)
				btroilist.append([btr.roi, currentvalue])
				currentvalue -=round(Decimal(0.1),2)
		btroilistsorted = sorted(btroilist, key=lambda x: x[0], reverse=True)


	setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				guid, EnumMadHatterIndicators.BBANDS, 2	, btroilistsorted[0][1])
	print(btroilistsorted[0][1])


def tuneDevup(therange):
		btroilist = []
		basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
		currentvalue = round(Decimal(basebotconfig.bBands['Devup']),2)
		initvalue = currentvalue
		if currentvalue >0:
			for x in range(therange):
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.BBANDS, 1, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi,'Devup: ', currentvalue)
				btroilist.append([btr.roi, currentvalue])
				currentvalue +=round(Decimal(0.1),2)
			currentvalue = round(initvalue-Decimal(0.1),2)
			for x in range(therange):
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.BBANDS, 1, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi,'Devup: ', currentvalue)
				btroilist.append([btr.roi, currentvalue])
				currentvalue -=round(Decimal(0.1),2)
			btroilistsorted = sorted(btroilist, key=lambda x: x[0], reverse=True)
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
					guid, EnumMadHatterIndicators.BBANDS, 1	, btroilistsorted[0][1])




def tuneLength(therange):
			btroilist = []
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.bBands['Length']
			initvalue = currentvalue
			if currentvalue >0:
				for x in range(therange):
					setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
								guid, EnumMadHatterIndicators.BBANDS, 0, currentvalue)
					bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
					# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
					btr = bt.result
					print(btr.roi,'bBands Length ', currentvalue)
					btroilist.append([btr.roi, currentvalue])
					currentvalue +=1
				currentvalue = initvalue-1
				for x in range(therange):
					if currentvalue > 0:
							
						setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
									guid, EnumMadHatterIndicators.BBANDS, 0 ,currentvalue)
						bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
						# # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
						btr = bt.result
						print(btr.roi, 'bBands Length', currentvalue)
						btroilist.append([btr.roi, currentvalue])
						currentvalue -=1
				btroilistsorted = sorted(btroilist, key=lambda x: x[0], reverse=True)
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
					guid, EnumMadHatterIndicators.BBANDS, 0	, btroilistsorted[0][1])

### MACD TUNER STARTS ###

def tuneMacdSlow(therange):
	btroilist = []
	basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
	currentvalue = basebotconfig.macd['MacdSlow']
	initvalue = currentvalue
	for x in range(therange):
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.MACD, 1	, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi,'MacdSlow :', currentvalue)
			btroilist.append([btr.roi, currentvalue])
			currentvalue +=2
	currentvalue = initvalue-1
	for x in range(therange):
		if currentvalue >= 2:
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(guid, EnumMadHatterIndicators.MACD,1	, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi,'MacdSlow :',  currentvalue)
				btroilist.append([btr.roi, currentvalue])
				currentvalue -=2
		if currentvalue <= 0: 
			pass
	btroilistsorted = sorted(btroilist, key=lambda x: x[0], reverse=True)
	setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				guid, EnumMadHatterIndicators.MACD,1	, btroilistsorted[0][1])


def tuneMacdFast(therange):
		btroilist = []
		basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
		currentvalue = basebotconfig.macd['MacdFast']
		initvalue = currentvalue
		for x in range(therange):
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.MACD, 0, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
			btroilist.append([btr.roi,'MacdFast :',  currentvalue])
			currentvalue +=1
		currentvalue = initvalue-1
		for x in range(therange):
			if currentvalue >=2:
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.MACD, 0, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi,'MacdFast :',  currentvalue)
				btroilist.append([btr.roi, currentvalue])
				currentvalue -=1
		btroilistsorted = sorted(btroilist, key=lambda x: x[0], reverse=True)
		setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
					guid, EnumMadHatterIndicators.MACD, 0	, btroilistsorted[0][1])




def tuneMacdSignal(therange):
			btroilist = []
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.macd['MacdSign']
			initvalue = currentvalue
			for x in range(therange):
					setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
								guid, EnumMadHatterIndicators.MACD, 2, currentvalue)
					bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
					# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
					btr = bt.result
					print(btr.roi, 'MacdSignal :', currentvalue)
					btroilist.append([btr.roi, currentvalue])
					currentvalue +=1

			currentvalue = initvalue-1
			for x in range(therange):
				if currentvalue >=3:
					setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
								guid, EnumMadHatterIndicators.MACD, 2, currentvalue)
					bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
					# print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
					btr = bt.result
					print(btr.roi, 'MacdSignal :',  currentvalue)
					btroilist.append([btr.roi, currentvalue])
					currentvalue -=1
		

def setbasicbotparameters():
	basebotconfig = haasomeClient.customBotApi.get_custom_bot(botnumobj.guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
	haasomeClient.customBotApi.set_mad_hatter_safety_parameter(
	basebotconfig.guid, EnumMadHatterSafeties.STOP_LOSS, 0)
	haasomeClient.customBotApi.set_mad_hatter_safety_parameter(
	basebotconfig.guid, EnumMadHatterSafeties.PRICE_CHANGE_TO_BUY, 0)
	haasomeClient.customBotApi.set_mad_hatter_safety_parameter(
	basebotconfig.guid, EnumMadHatterSafeties.PRICE_CHANGE_TO_SELL, 0)
	print('for the purposes of backtesting, STOPLOSS, %change to buy and sell has been set to zero')
	haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						basebotconfig.guid, EnumMadHatterIndicators.BBANDS, 6, False)
	haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						basebotconfig.guid, EnumMadHatterIndicators.BBANDS, 7, False)
	haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						basebotconfig.guid, EnumMadHatterIndicators.BBANDS, 8, False)
	print('FCC, Midell, Reset middle have been disabled for the same purposes')
### Helper classes ###

def settherange():
		therange = int(input('Write the N% of backtests to be done at each operation. The recomended values are 3, 6, 12, 20'))
		return int(therange)


### required data for script to work ###

haasomeClient = connectionstring()

botnumobj = botsellector()
guid = botnumobj.guid
btinterval = settimeinterval()
setbasicbotparameters()

# answers = prompt(selectparametertochange())
therange = settherange()
info = startconfiguring(therange)
print(info)
