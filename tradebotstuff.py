from __future__ import print_function, unicode_literals
import regex
from decimal import Decimal
from haasomeapi.HaasomeClient import HaasomeClient
from pprint import pprint
# ffrom puinquirer import style_from_dict, Token, prompt
# ffrom puinquirer import Validator, ValidationError
import configserver
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
from licensing.models import *
from licensing.methods import Key, Helpers
import tuner

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
import connectionstring
import setbtrange
import startconfiguring
import botsellector
### required data for script to work ###

guid = '1a526bcf-ab76-479f-bb53-ae81b571fc60'
elementguid = '6448eebf-0718-4b37-a019-1372d0e2d657'

def gettradebot(guid):
	bot = haasomeClient.tradeBotApi.get_trade_bot(guid).result
	# for key, value in indicatorlist.items():
	# 	# print('indicator: ',key, 'otherstuff:', value['title'])
	# 	indicator.append([key])
	# print(indicator)
	return bot


		

		
	# indicators = bot.indicators[elementguid].indicatorInterface
	# print(indicators[0].title,indicators[0].value, indicators[0].options)


# def setupindicator(guid):
	# indicator = haasomeClient.tradeBotApi.edit_bot_indicator_settings(botguid: str, elementguid: str, pricesource: EnumPriceSource, primarycoin: str,secondarycoin: str, contractname: str, interval: int, charttype: EnumPriceChartType, delay: int)


def listalltradebots():
	allbots = haasomeClient.tradeBotApi.get_all_trade_bots().result

	
	for i, b in enumerate(allbots):
		print(i, b.name, b.guid)

haasomeClient = connectionstring.connectionstring()

listalltradebots()
bot = gettradebot(guid)
indicatorlist = bot.indicators
# print(bot, indicatorlist)
indicators = indicatorlist
ivtg
for k, v in indicators.items():
	iv = []
	# print( '\n\n----- FIRST LINE ---- \n\n',k, '\n\n',v.indicatorName, '\n\n', v.indicatorInterface[0].title,v.indicatorInterface[0].value, v.indicatorInterface[0].options)
	print('\n\n',v.indicatorName,'\n')
	 iv.append(v.indicatorName)
	for i in v.indicatorInterface:
			print( i.value,':',i.title)
			iv.append(i.value)
			if i.options == None:
				# print('No Options')
				pass
			else:
				print('Options are:')
				for i, v in enumerate(i.options):
					print(k[i], '\n\n')
		ivtg.append(indicator)
	print(values)