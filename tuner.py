from haasomeapi.HaasomeClient import HaasomeClient
import botsellector
import configparser_cos
import configserver
import interval
import interval as iiv

from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
from haasomeapi.enums.EnumMadHatterIndicators import EnumMadHatterIndicators
from haasomeapi.enums.EnumMadHatterSafeties import EnumMadHatterSafeties
from decimal import Decimal


def connect():
		ip, secret = configserver.validateserverdata()
		haasomeClient = HaasomeClient(ip, secret)
		return haasomeClient

haasomeClient = connect()

def getindicators(bot):
		basebotconfig = haasomeClient.customBotApi.get_custom_bot(bot.guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
		#bbands stuff
		bBands = basebotconfig.bBands
		rsi = 	 basebotconfig.rsi
		macd =  basebotconfig.macd
		return bBands, rsi, macd

bb, rsi, macd =		getindicators()
# print(bb, rsi, macd)

def setl(l):
			for i in enumerate(rsiconfig):
				if i[1] == l and i[2] == s and i[3] == b:
					pass
				else:
					setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.RSI, 0	, l)
					bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
					btr = bt.result
					print(btr.roi, 'RSI: ', l, s, b)
					rsiconfig.append([btr.roi,l,s,b])

def sets(s):
		for i,x in enumerate(rsiconfig):
				if i[1] == l and i[2] == s and i[3] == b:
					pass
				else:
					setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
									guid, EnumMadHatterIndicators.RSI, 1	, s)
					bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
					btr = bt.result
					print(btr.roi, 'RSI: ', l, s, b)
					rsiconfig.append([btr.roi,l,s,b])

def setb(b):
			for i,x in enumerate(rsiconfig):
				if i[1] == l and i[2] == s and i[3] == b:
					pass
				else:
					setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.RSI, 2	, b)
					bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
					btr = bt.result
					print(btr.roi, 'RSI: ', l, s, b)
					rsiconfig.append([btr.roi,l,s,b])



#### RSI TUNING ###

def tuneRsiLength(therange, guid, btinterval):
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


def tuneRsiOversold(therange, guid, btinterval):
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




def tuneRsiOverbought(therange, guid, btinterval):
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

def tuneDevdn(therange, guid, btinterval):
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
		if currentvalue >0:
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


def tuneDevup(therange, guid, btinterval):
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
			if currentvalue >0:
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




def tuneLength(therange, guid, btinterval):
			btroilist = []
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.bBands['Length']
			initvalue = currentvalue
			if currentvalue >=2:
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
					if currentvalue >= 2:
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
			if currentvalue <=1:
					etl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
								guid, EnumMadHatterIndicators.BBANDS, 0, 2)
### MACD TUNER STARTS ###

def tuneMacdSlow(therange, guid, btinterval):
	btroilist = []
	basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
	currentvalue = basebotconfig.macd['MacdSlow']
	initvalue = currentvalue
	for x in range(therange):
		if currentvalue > 0:
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


def tuneMacdFast(therange, guid, btinterval):
		btroilist = []
		basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
		currentvalue = basebotconfig.macd['MacdFast']
		initvalue = currentvalue
		for x in range(therange):
			if currentvalue > 0:
					
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




def tuneMacdSignal(therange, guid, btinterval):
			btroilist = []
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.macd['MacdSign']
			initvalue = currentvalue
			for x in range(therange):
				if currentvalue > 0:
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
		
