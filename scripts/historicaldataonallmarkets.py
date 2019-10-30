from __future__ import print_function, unicode_literals
import regex
from decimal import Decimal
from haasomeapi.HaasomeClient import HaasomeClient
from pprint import pprint

# ffrom puinquirer import style_from_dict, Token, prompt
# ffrom puinquirer import Validator, ValidationError
import PyInquirer
import configserver
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType

from haasomeapi.apis.AccountDataApi import AccountDataApi
from haasomeapi.apis.ApiBase import ApiBase
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


### required data for script to work ###
ip, secret = configserver.validateserverdata()
haasomeClient = HaasomeClient(ip, secret)


def marketselector():
    pass


def listcoinsaschoice():
    pass


def listallaccounts():
    markets = []
    all = haasomeClient.accountDataApi.get_all_account_details().result
    for i, x in enumerate(all):
        markets.append([("name:") + str(+i) + "," + str("value: ") + str(x)])

    print(markets)
    return markets


# def chosemarket():
# 		questions = [
# 			{'type': 'list','name': 'chosenmarket','message': 'Choose market',
# 			'choices': listallaccounts()
# 		return questions


def makeconfigurenewmhbot():
    bot = haasomeClient.customBotApi.new_custom_bot()


# listallaccounts()

listallaccounts()
