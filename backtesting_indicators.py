import configparser 
import pickle
from collections import defaultdict
from pathlib import Path
from haasomeapi.HaasomeClient import HaasomeClient
import csv
import botsellector
import configdict
import configserver
import init
import interval as ivv
import os
import re 
import sys
import pandas as pd
import ranges as Ranges
ip, secret = init.connect()
haasomeClient = HaasomeClient(ip, secret)

def btindiator(bot, indicator_guid, haasomeClient):
	ticks = ivv.readinterval()()
	change_param = 	haasomeClient.tradeBotApi.edit_bot_indicator_settings(bot.guid, indicator_guid, field_n, value)
	backtest = haasomeClient.tradeBotApi.backtest_trade_bot(bot.guid, ticks)

	if gettradebot.indicators[guid].indicatorTypeShortName == 'CRSI': #missing ROC
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
							change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(gettradebot.guid, guid, 4, ll)
							bt = haasomeClient.tradeBotApi.backtest_trade_bot(gettradebot.guid, ticks)
							printerrors(bt, 'bt')
							printerrors(change, 'change')
							print(bt.result.roi)	
							for lud in np.arange(2, 5, 1):
									change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(gettradebot.guid, guid, 1, ll)
									bt = haasomeClient.tradeBotApi.backtest_trade_bot(gettradebot.guid, ticks)
									printerrors(bt, 'bt')
									printerrors(change, 'change')
									print(bt.result.roi)	
									results.append([bt.result.roi, l, lud, b, s])


def dict2ini(d, root):
    for k, v in d.items():
        if isinstance(v, dict):
            _key = '%s.%s' % (root, k) if root else k
            if v:
                dict2ini(v, _key)
            else:
                res[_key] = {}
        elif isinstance(v, (int, float)):
            res[root] = {k:v}

def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

def enum_dict(dict):
		dict_enum_list = []
		i = 0
		for k, v in dict.items():
			i2=0
			for k1,v1 in v.items():
				dict_enum_list.append([k, i2, v1])
				i2+=1
			i+=1
		i =0
		return dict_enum_list


def modify_indicator(bot, haasomeClient, indicator_guid,field,value):

	modifyparam =  haasomeClient.tradeBotApi.edit_bot_indicator_settings(bot_guid = bot.guid, elementguid=indicator_guid, field=field, value=value)

def dropnested(alist):
    outputdict = {}
    for dic in alist:
        for key, value in dic.items():
            if isinstance(value, dict):
                for k2, v2, in value.items():
                    outputdict[k2] = outputdict.get(k2, []) + [v2]
            else:
                outputdict[key] = outputdict.get(key, []) + [value]
    return outputdict    



def indicatorparametersdata(bot, haasomeClient):
		indicators_all = ['Aroon','Aroon Oscillator','AO','BOP','Blind indicator','Bollinger Bands','Bollinger Bands %B','Bollinger Bands %W','Bollinger Bands (Legacy)','Candle Pattern finder','CMO','CRSI','Coppock Curve','DPO','DC','DEMA','Dynamic Buy/Sell','Elliot','EMA','FastRSI','Fibonacci','Fixed Buy/Sell','Fractal','Ichimoku Clouds','KAMA','Keltner Channels','Momentum','MFI','MACD','ROC','RS','RSI','SAR','SMA','SlowRSI','Small Fractal','Stochastic','Stoch-RSI','Stochastic^2','Timed Blind','TD','TRIMA','TRIX','TEMA','UO','WMA','Williams %R']
		
		todict = indicatorstodict2(bot)
		indicators_bot = todict.keys()
		for indicator, data in todict.items():
			pass

def getindicatorranges(bot, haasomeClient):
			ticks = ivv.readinterval()
			todict = indicatorstodict2(bot)
			indicators_bot = todict.keys()
			for indicator, data in todict.items():

				if indicator =='Aroon' and indicator in indicators_bot:
						fd = 0
						start = 5
						end = 30
						step = 1
						for i in np.arange(5,30,1):
							change = haasomeClient.tradeBotApi.edit_bot_indicator_settings()
							bt = haasomeClient.tradeBotApi.backtest_trade_bot(bot.guid, ticks)
							print(bt.errorCode,bt.errorMessage)
							btr = bt.result
							print(btr.roi)

				elif indicator =='Aroon Oscillator' and indicator in indicators_bot:
					if fd == 0:
						start = 5
						end = 30
						step = 1

				elif indicator =='AO' and indicator in indicators_bot:
					if	fd == 0:
						start = 2
						end = 30
						step = 1

				elif indicator =='BOP' and indicator in indicators_bot:
					if fd == 0:
						start = 5
						end = 30
						step = 1


				elif indicator =='Blind indicator' and indicator in indicators_bot:
					print('BLIND INDICATOR IS UNSUPPORTED ATM')
					continue

				elif indicator =='Bollinger Bands' and indicator in indicators_bot:
					if fd == 0:
						start = 4
						end = 60
						step = 2
					elif fd == 1:
						start = 0.2
						end = 3.0
						step = 0.2
					elif fd == 2:
						start = 0.2
						end = 3.0
						step = 0.2

				elif indicator =='Bollinger Bands %B' and indicator in indicators_bot:
					if fd == 0:
						start = 4
						end = 60
						step = 2
					elif fd == 1:
						start = 0.2
						end = 3.0
						step = 0.2
					elif fd == 2:
						start = 0.2
						end = 3.0
						step = 0.2


				elif indicator =='Bollinger Bands %W' and indicator in indicators_bot:
					if fd == 0:
						start = 4
						end = 60
						step = 2
					elif fd == 1:
						start = 0.2
						end = 3.0
						step = 0.2
					elif fd == 2:
						start = 0.2
						end = 3.0
						step = 0.2


				elif indicator =='Bollinger Bands (Legacy)' and indicator in indicators_bot:
					if fd == 0:
						start = 4
						end = 60
						step = 2
					elif fd == 1:
						start = 0.2
						end = 3.0
						step = 0.2
					elif fd == 2:
						start = 0.2
						end = 3.0
						step = 0.2


				elif indicator =='Candle Pattern finder' and indicator in indicators_bot:
					print('candle pattern finder is not yet supported')
					continue				
	
				elif indicator =='CMO' and indicator in indicators_bot:
					if fd == 0:
						start = 2
						end = 40
						step = 2
					elif fd == 1:
						start = -10.0
						end = -2.0
						step = 1.0
					elif fd == 2:
						start = 2.0
						end = 10.0
						step = 1.0


				elif indicator =='CRSI' and indicator in indicators_bot:
					if fd == 0:
						start = 2
						end = 20
						step = 2
					elif fd == 1:
						start = 2
						end = 10
						step = 2
					elif fd == 2:
						start = 80
						end = 110
						step = 5
					elif fd == 3:
						start = 10
						end = 30
						step = 2
					elif fd == 4:
						start = 70
						end = 90
						step = 2


				elif indicator =='Coppock Curve' and indicator in indicators_bot:
					if fd == 0:
						start = 6
						end = 21
						step = 4
					elif fd == 1:
						start = 142
						end = 40
						step = 4
					elif fd == 2:
						start = 2
						end = 20
						step = 4
					elif fd == 3:
						start = -0.1
						end = -0.2
						step = 0.02
					elif fd == 4:
						start = 0.1
						end = 0.2
						step = 0.02

				elif indicator == 'DPO' and indicator in indicators_bot:
					if fd == 0:
						start = 8
						end = 16
						step = 2
					elif fd == 1:
						start = 19
						end = 36
						step = 2
					elif fd == 2:
						start = -0.1
						end = -0.2
						step = 0.02

				elif indicator =='DC' and indicator in indicators_bot:
					if fd == 0:
						start = 2
						end = 102
						step = 2
				elif indicator =='DEMA' and indicator in indicators_bot:
					if fd == 0:
						start = 10
						end = 60
						step = 5
					elif fd == 1:
						start = 20
						end = 80
						step = 5
					elif fd == 2:
						start = 2
						end = 12
						step = 2

				elif indicator =='Dynamic Buy/Sell' and indicator in indicators_bot:
					if fd == 0:
						start = 20
						end = 240
						step = 10

				elif indicator =='Elliot' and indicator in indicators_bot:
					if fd == 0:
						start = 5
						end = 80
						step = 5

				elif indicator =='EMA' and indicator in indicators_bot:
					if fd == 0:
						start = 4
						end = 21
						step = 2
					elif fd == 1:
						start = 8
						end = 42
						step = 2
					elif fd == 2:
						start = 0
						end = 0
						step = 0

				elif indicator =='FastRSI' and indicator in indicators_bot:
					if fd == 0:
						start = 6
						end = 30
						step = 2
					elif fd == 1:
						start = 2
						end = 10
						step = 1
					elif fd == 2:
						start = 10
						end = 45
						step = 2
					elif fd == 3:
						start = 59
						end = 81
						step = 2

				elif indicator =='Fibonacci' and indicator in indicators_bot:
					if fd == 0:
						start = 20
						end = 40
						step = 2
		

				elif indicator =='Fixed Buy/Sell' and indicator in indicators_bot:
					if fd == 0:
						start = 0
						end = 2.5
						step = 2
					elif fd == 1:
						start = 0
						end = 2.5
						step = 2
					elif fd == 2:
						start = 0.2
						end = 3.0
						step = 0.2

				elif indicator =='Fractal' and indicator in indicators_bot:
					print('fractal has no settings to displa')
					continue

				elif indicator =='Ichimoku Clouds' and indicator in indicators_bot:
					if fd == 0:
						start = 6
						end = 30
						step = 2
					elif fd == 1:
						start = 12
						end = 40
						step = 2
					elif fd == 2:
						start = 40
						end = 80
						step = 2
					elif fd == 3:
						start = 26
						end = 50
						step = 2
					print('Buy/Sell Triggers are not yet supported')

				elif indicator =='KAMA' and indicator in indicators_bot:
					if fd == 0:
						start = 4
						end = 21
						step = 2
					elif fd == 1:
						start = 8
						end = 42
						step = 2

				elif indicator =='Keltner Channels' and indicator in indicators_bot:
					if fd == 0:
						start = 2
						end = 20
						step = 2
					elif fd == 1:
						start = 0.1
						end = 2.0
						step = 0.1
					elif fd == 2:
						start = 2
						end = 20
						step = 2

				elif indicator =='Momentum' and indicator in indicators_bot:
					if fd == 0:
						start = 2
						end = 20
						step = 2
				elif indicator =='MFI' and indicator in indicators_bot:
					if fd == 0:
						start = 4
						end = 60
						step = 2
					elif fd == 1:
						start = 0.2
						end = 3.0
						step = 0.2
					elif fd == 2:
						start = 0.2
						end = 3.0
						step = 0.2

				elif indicator =='MACD' and indicator in indicators_bot:
					if fd == 0:
						start = 10
						end = 20
						step = 2
					elif fd == 1:
						start = 20
						end = 40
						step = 2
					elif fd == 2:
						start = 2
						end = 12
						step = 2

				elif indicator =='ROC' and indicator in indicators_bot:
					if fd == 0:
						start = 10
						end = 50
						step = 2
					elif fd == 1:
						start = -0.2
						end = -0.05
						step = 0.02
					elif fd == 2:
						start = 0.1
						end = 0.3
						step = 0.02

				elif indicator =='RS' and indicator in indicators_bot:
					if fd == 0:
						start = 18
						end = 40
						step = 2
		

				elif indicator =='RSI' and indicator in indicators_bot:
					if fd == 0:
						start = 2
						end = 60
						step = 2
					elif fd == 1:
						start = 10
						end = 40
						step = 3
					elif fd == 2:
						start = 59
						end = 80
						step = 4

				elif indicator =='SAR' and indicator in indicators_bot:
					if fd == 0:
						start = 4
						end = 40
						step = 2
					elif fd == 1:
						start = 0.1
						end = 0.2
						step = 0.02
				
				elif indicator =='SMA' and indicator in indicators_bot:
					if fd == 0:
						start = 10
						end = 30
						step = 4
					elif fd == 1:
						start = 20
						end = 40
						step = 4
					elif fd == 0:
						start = 0
						end = 0.1
						step = 0.02

				elif indicator =='SlowRSI' and indicator in indicators_bot:
					if fd == 0:
						start = 2
						end = 40
						step = 2
					elif fd == 1:
						start = 2
						end = 12
						step = 2
					elif fd == 2:
						start = 10
						end = 30
						step = 4
					elif fd == 3:
						start = 59
						end = 81
						step = 4

				elif indicator =='Small Fractal' and indicator in indicators_bot:
					print('Small fractal has no settings and will be skipped')
					continue
				elif indicator =='Stochastic' and indicator in indicators_bot:
					if fd == 0:
						start = 2
						end = 40
						step = 2
					elif fd == 1:
						start = 10
						end = 40
						step = 4
					elif fd == 2:
						start = 60
						end = 81
						step = 4

				elif indicator =='Stoch-RSI' and indicator in indicators_bot:
					if fd == 0:
						start = 2
						end = 20
						step = 2
					elif fd == 1:
						start = 2
						end = 10
						step = 2
					elif fd == 2:
						start = 80
						end = 110
						step = 5
					elif fd == 3:
						start = 10
						end = 30
						step = 2
					elif fd == 4:
						start = 70
						end = 90
						step = 2

				elif indicator =='Stochastic^2' and indicator in indicators_bot:
					if fd == 0:
						start = 2
						end = 40
						step = 2
					elif fd == 1:
						start = 10
						end = 40
						step = 4
					elif fd == 2:
						start = 60
						end = 81
						step = 4

				elif indicator =='Timed Blind' and indicator in indicators_bot:
					if fd == 0:
						start = 10
						end = 100
						step = 10

				elif indicator =='TD' and indicator in indicators_bot:
					if fd == 0:
						start = 2
						end = 15
						step = 2
					elif fd == 1:
						start = 4
						end = 20
						step = 2
					elif fd == 2:
						continue
					elif fd == 3:
						start = 3
						end = 18
						step = 2
					elif fd == 4:
						start = 3
						end = 20
						step = 2
					elif fd == 5:
						continue

	

				elif indicator =='TRIMA' and indicator in indicators_bot:
					if fd == 0:
						start = 2
						end = 20
						step = 2
					elif fd == 1:
						start = 4
						end = 40
						step = 2
		
				elif indicator =='TRIX' and indicator in indicators_bot:
					if fd == 0:
						start = 2
						end = 20
						step = 2
		

				elif indicator =='TEMA' and indicator in indicators_bot:
					if fd == 0:
						start = 2
						end = 20
						step = 2
					elif fd == 1:
						start = 20
						end = 40
						step = 2
					elif fd == 2:
						start = 0
						end = 0
						step = 0

				elif indicator =='UO' and indicator in indicators_bot:
					if fd == 0:
						start = 2
						end = 10
						step = 2
					elif fd == 1:
						start = 5
						end = 20
						step = 2
					elif fd == 2:
						start = 10
						end = 30
						step = 2

				elif indicator =='WMA' and indicator in indicators_bot:
					if fd == 0:
						start = 2
						end = 10
						step = 2
					elif fd == 1:
						start = 10
						end = 30
						step = 4
					elif fd == 2:
						start = 0
						end = 0.1
						step = 0.02

				elif indicator =='Williams %R' and indicator in indicators_bot:
					if fd == 0:
						start = 2
						end = 20
						step = 2
					elif fd == 1:
						start = -30
						end = -20
						step = 5
					elif fd == 2:
						start = -70
						end = -90
						step = 5
	

			
	
				# for paramname, data1 in todict[indicator].items():
				# 	# if paramname == 'Dev.Down':
			# print(paramname, pramstring, paramvalue
			# 				for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
			# 						print(paramname, pramstring, paramvalue)

	

	# for a, b in todict.items():
	# 	# print('PRINT(PARAMNAME,PRAMSTRING, PARAMVALUE)n',a,'PRINT(PARAMNAME,PRAMSTRING, PARAMVALUE)n')
	# 	for b, c in todict[a].items():
			
	# 		# print(a,b,c)

def get_options(indicator_guid, bot):	
		indicator_options = []
		for option in bot.indicators[str(indicator_guid)].indicatorInterface:
			indicator_options.append([bot.indicators[indicator_guid].indicatorTypeShortName,option.title, option.value, indicator_guid, bot.guid])
		return indicator_options


	# print(new)
def get_indicator_config(bot, haasomeClient):
	indicator_configs = configparser.ConfigParser()
	indicator_configs.read('indicatorranges.ini')
	sections = indicator_configs.sections()
	for indicator in bot.indicators:
			indicatorname = 	bot.indicators[indicator].indicatorTypeShortName
			if indicatorname in sections:
				currentparams = get_options(indicator, bot)
				if indicatorname in currentparams:
					options = []
					params = []
					for option in indicator_configs.options(indicatorname):
						options.append(option.capitalize())
					# print(options)
						for param in options:
							print(indicatorname, param)
							# for value in param:
							# 	print(value)


def indicatorstodict(botty):

	bot = haasomeClient.tradeBotApi.get_trade_bot(botty.guid).result
	indicator_options = {}
	for indicator in bot.indicators:
			params2 = {}
			for param in bot.indicators[str(indicator)].indicatorInterface:
				params2[param.title] = param.value
			indicator_options[bot.indicators[indicator].indicatorTypeShortName] = params2
	return indicator_options

def indicatorstodict2(botty):
	indicator_configs = configparser.ConfigParser()
	indicator_configs.read('indicatorranges.ini')
	sections = indicator_configs.sections()
	bot = haasomeClient.tradeBotApi.get_trade_bot(botty.guid).result
	indicator_options = {}
	for indicator in bot.indicators:
			params2 = {}
			if bot.indicators[indicator].indicatorTypeShortName in sections:
				params3 = {}
				for param in bot.indicators[str(indicator)].indicatorInterface:
						params3['Value'] = param.value
						params3['Start'] = 0
						params3["Stop"] = 10
						params3['Range'] = 2
				params2[param.title] = params3
				indicator_options[bot.indicators[indicator].indicatorTypeShortName] = params2
				with open('indicators.py', 'wb') as f:
					pickle.dump(indicator_options,f)

	return indicator_options

def main():
	bot = botsellector.getalltradebots(haasomeClient)
	b2 = get_indicator_config(bot,haasomeClient)
	b3 = indicatorparametersdata(bot, haasomeClient)
	b4 = getindicatorranges(bot, haasomeClient)
	print('1',bot,'2', b2, '3', b3)


main()
