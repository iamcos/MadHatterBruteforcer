from __future__ import print_function, unicode_literals
import regex
from haasomeapi.HaasomeClient import HaasomeClient
from pprint import pprint
# ffrom puinquirer import style_from_dict, Token, prompt
# ffrom puinquirer import Validator, ValidationError
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

questions = [
	{'type': 'list','name': 'selectedparameter','message': 'Select parameter to change by using keys up and down then hit return',
	'choices': 
	[{'name':'1H','value':60},{'name':'2H','value':120},{'name':'3H', 'value':180},{'name':'4H','value':240},{'name':'5H','value':300} ,{'name':'6H','value':360},{'name':'7H','value':420},{'name':'8H','value':480},{'name':'9H','value':540},{'name':'10H','value':600},{'name':'11H','value':660},{'name':'12H','value':720},{'name':'13H','value':780},{'name':'14H','value':840},{'name':'15H','value':900},{'name':'16H','value':960},{'name':'17H','value':1020},{'name':'18H','value':1080},{'name':'19H','value':1140},{'name':'20H','value':1200},{'name':'21H','value':1260},{'name':'22H','value':1320},{'name':'23H','value':1380},{'name':'24H','value':1440},{'name':'1D','value':1440},{'name':'2D','value':2880},{'name':'3D','value':4320},{'name':'4D','value':5760},{'name':'5D','value':7200},{'name':'6D','value':8640},{'name':'7D','value':10080},{'name':'8D','value':11520},{'name':'9D','value':12960},{'name':'10D','value':14400},{'name':'11D','value':15840},{'name':'12D','value':17280},{'name':'13D','value':18720},{'name':'14D','value':20160},{'name':'15D','value':21600},{'name':'16D','value':23040},{'name':'17D','value':24480},{'name':'18D','value':25920},{'name':'19D','value':27360},{'name':'20D','value':28800},{'name':'21D','value':30240},{'name':'22D','value':31680},{'name':'23D','value':33120},{'name':'24D','value':34560},{'name':'25D','value':36000},{'name':'26D','value':37440},{'name':'27D','value':38880},{'name':'28D','value':40320},{'name':'29D','value':41760},{'name':'30D','value':43200}]}]

answer = prompt(questions)