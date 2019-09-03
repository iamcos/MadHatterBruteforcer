import configparser 
import pickle
from collections import defaultdict
from pathlib import Path
from haasomeapi.HaasomeClient import HaasomeClient

import botsellector
import configdict
import configserver
import init
import interval as ivv
import os
import re 
import sys
import ranges as Ranges
ip, secret = init.connect()
haasomeClient = HaasomeClient(ip, secret)

def btindiator(bot, indicator_guid, haasomeClient):
	ticks = ivv.readinterval()()

def get_options(indicator_guid, bot):	
	print('\n',bot.indicators[indicator_guid].indicatorTypeShortName, 'avialable parameters:')
	indicator_options = []
	for option in bot.indicators[str(indicator_guid)].indicatorInterface:
	
		indicator_options.append([option.title, option.value, indicator_guid, bot.guid, ])
	for option in indicator_options:
		print('	',option[0], option[1])
	print('\n')
	return indicator_options



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


def paramconfiguration(dict):	
	dictionary = {}
	config = configparser.ConfigParser()
	file = config.read.configparser('indicator_preconfigurations.ini')
	for section in config.sections():
		dictionary[section] = {}
		for option in config.options(section):
			dictionary[section][option] = config.get(section, option)


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
def main():
	ranges = Ranges.forindicators()
	bot = botsellector.getalltradebots(haasomeClient)
	indicator_configs = configparser.ConfigParser()
	indicator_configs.read('indicatorranges.ini')
	indicators = indicator_configs.sections()
	print(indicators)
	
	new = indicatorstodict(bot)
	indicators = new.keys()
	opts = []
	for i in indicators:
			configs = []
			if indicator_configs.has_section(i) == True:
				print('Indicator Settings for ', i,' exist ')
				for option in indicator_configs.options(i):
					configs.append(option)
			print('the config', configs)
				


					 

	# dupes = mix.keys() & new.keys()
	# for i in dupes:
	# 	if i in ind_configs:
	# 		for b, d in ind_configs[i].items():
	# 			 if d != None:
	# 					for k, v in ind_ranges[i].items():
	# 						if k == b:
	# 							start = ind_ranges[i][k][0]
	# 							end = ind_ranges[i][k][1]
	# 							step = ind_ranges[i][k][2]
	# 							print(start, end, step)

	# print(ind_configs)

				
			
	# print(ind_configs_enum)

	# print(new)


def indicatorstodict(botty):

	bot = haasomeClient.tradeBotApi.get_trade_bot(botty.guid).result
	indicator_options = {}
	for indicator in bot.indicators:
			params2 = {}
			for param in bot.indicators[str(indicator)].indicatorInterface:
				params2[param.title] = param.value
			indicator_options[bot.indicators[indicator].indicatorTypeShortName] = params2
	return indicator_options


class MyParser(configparser.ConfigParser):
    def as_dict(self):
        d = dict(self._sections)
        for k in d:
            d[k] = dict(self._defaults, **d[k])
            d[k].pop('__name__', None)
        return d

	
def read(file):
    f = MyParser()
    f.read("indicators.ini")
    d = f.as_dict()
    return d

def writeConfig(dict, filename):
	c = configparser.ConfigParser()
	c.sections()


	for key1, value1 in dict.items():
		c.add_section(key1)
		i = 0
		if value1.keys != 0:
			for key2, value2 in value1.items():
				if value2 != None: 
					c.set(str(key1), str(key2), value2)
		
		# print(c.items)
		
	with open(filename, 'w') as configfile:
					c.write(configfile)			
		




main()
