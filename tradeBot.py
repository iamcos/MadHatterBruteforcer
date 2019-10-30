from haasomeapi.apis.TradeBotApi import TradeBotApi
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import (
    IndicatorOption,
)
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from haasomeapi.enums.EnumErrorCode import EnumErrorCode

from haasomeapi.enums.EnumCoinPosition import EnumCoinPosition
from haasomeapi.enums.EnumLimitOrderPriceType import EnumLimitOrderPriceType
import interval as iiv
import configserver
import haasomeapi.enums.EnumIndicator2 as EnumIndicator
import numpy as np
import pandas as pd
import time
import botsellector
import multiprocessing as mp
from decimal import Decimal
from haasomeapi.HaasomeClient import HaasomeClient
ip, secret = configserver.validateserverdata()
haasomeClient = HaasomeClient(ip, secret)

def multiprocess(bot, guid):
    newbotname = bot.name + " " + bot.indicators[guid].indicatorTypeShortName + " temp"
    newbot = haasomeClient.tradeBotApi.clone_trade_bot(
        bot.accountId,
        bot.guid,
        newbotname,
        bot.priceMarket.primaryCurrency,
        bot.priceMarket.secondaryCurrency,
        bot.priceMarket.contractName,
        bot.leverage,
        False,
        False,
        False,
        True,
        True,
    ).result
    cloeindicator = haasomeClient.tradeBotApi.clone_indicator(
        bot.guid, guid, newbot.guid
    ).result

    gettradebot = haasomeClient.tradeBotApi.get_trade_bot(newbot.guid).result
    for guid in gettradebot.indicators:
        # print('Indicator name: ',gettradebot.indicators[guid].indicatorTypeShortName)
        for i, options in enumerate(
            gettradebot.indicators[str(guid)].indicatorInterface
        ):
            indicators.append(i)
        for interface in gettradebot.indicators[str(guid)].indicatorInterface:
            # print(interface.title, interface.value , interface.options)
            print(interface.value.type)


def new_bot_for_every_indicator(haasomeClient, bot, interval):
    ticks = iiv.readinterval(1)
    newbots = []
    createdbots = []
    indicators = []
    options = []

    for guid in bot.indicators:
        newbotname = (
            bot.name + " " + bot.indicators[guid].indicatorTypeShortName + " temp"
        )
        newbot = haasomeClient.tradeBotApi.clone_trade_bot(
            bot.accountId,
            bot.guid,
            newbotname,
            bot.priceMarket.primaryCurrency,
            bot.priceMarket.secondaryCurrency,
            bot.priceMarket.contractName,
            bot.leverage,
            False,
            False,
            False,
            True,
            True,
        ).result
        cloeindicator = haasomeClient.tradeBotApi.clone_indicator(
            bot.guid, guid, newbot.guid
        ).result
        newbots.append(newbot)
    return newbots


def get_indicators(bot):
    indicators = {}
    for indicator in bot.indicators:
        indicators[bot.indicators[indicator].indicatorTypeShortName] = indicator
    return indicators

def select_indicator(indicators):
    keys = list(indicators.keys())
    print(indicators.keys())
    for i, indicator in enumerate(keys):
        print(i, indicator)
    response = input('Type indicator number to select it: ')
    # print(keys[int(response)])
    # print(indicators[response])
    print(indicators[str(keys[int(response)])])
    return indicators[str(keys[int(response)])]
       

def get_interfaces(bot, indicator):
    # interfaces = {}
    interfaces = {}
    # for indicator in bot.indicators[indicator].indicatorInterface:
    for i,indicator in enumerate(bot.indicators[indicator].indicatorInterface):
        # print(indicator.title, indicator.value, indicator.options)
        interfaces[i] = {'title':indicator.title, 'value':indicator.value, 'options':indicator.options}
    # print(interfaces)
    return interfaces

def select_interface(bot, indicator, interfaces):
    interface = {}
    # print(interfaces)
    for i, interface in enumerate(interfaces):
        print(interface, '.',interfaces[i]['title'],':', interfaces[i]['value'])
    response = input('Type parameter number to select it: ')
    # print(interfaces[int(response)])
    print(bot.indicators[indicator].indicatorInterface[int(response)])

def add_indicator(bot, indicator):
    try:
        add = haasomeClient.tradeBotApi.add_indicator(bot.guid, indicator)
        # print(add.errorCode, add.errorMessage)
        print(add.errorCode, add.errorMessage)
        try: 
            print(EnumIndicator.EnumIndicator(indicator))
        except:
            print('something didnt work out')

    except ValueError or KeyError:
        pass


def to_dataframe(bot):
    interfaces = get_indicator_interfaces(bot)
    # print(interfaces)
    df = pd.DataFrame.from_dict(interfaces, orient="index")
    print(df)


def backtest_single_indicator_bot(bot):
    results = []
    indicators = get_indicator_interfaces(bot)

    # 				for i+1 in enumerate(indicators[indicator].keys()):

    # 	for title, value in indicators[indicator].items():
    # 	indicators[indicator].keys()
    # 					if title == 'Short length':
    # 						print('value',value)
    # 						start = 5
    # 						stop =  20
    # 						step =  1
    # 						try:
    # 							for x in np.arange(start,stop,step):
    # 							# print(indicator,indicators[indicator])
    # 								# ticks = iiv.readinterval(bot.indicators[indicator].timer)
    # 								ticks = iiv.readinterval(1)
    # 								print(title, x)
    # 								change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(bot.guid, indicator,list(indicators[indicator].keys()).index(key) , x)
    # 								bt = haasomeClient.tradeBotApi.backtest_trade_bot(bot.guid, ticks)
    # 								printerrors(bt)
    # 								printerrors(change)
    # 								print(bt.result.roi)
    # 								results.append([bt.result.roi, x])
    # 						except ZeroDivisionError:
    # 							pass
    # 					else:
    # 						pass
    # results = sorted(results, key=lambda x: x[1], reverse=False)
    # change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(bot.guid,results[0][1] , 0, x)


def printerrors(variable):
    print(variable.errorCode, variable.errorMessage)


def main1():
    pool = mp.Pool(mp.cpu_count())
    bot = botsellector.getalltradebots(haasomeClient)
    intt = get_indicator_interfaces(bot)
    # dd = to_dataframe(bot)

def add_all_indicators_to_bot():

    bot = botsellector.get_trade_bot(haasomeClient)
    for x in range(71):
        add_indicator(bot, x)

def main2():
    bot = botsellector.getalltradebots(haasomeClient)
    indicators = get_indicators(bot)
    indicator_guid = select_indicator(indicators)
    # print(indicator_guid)
    interfaces = get_interfaces(bot, indicator_guid)
    interface = select_interface(bot, indicator_guid, interfaces)


if __name__ == "__main__":
    # add_all_indicators_to_bot()
    main2()
