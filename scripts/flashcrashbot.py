# from licensing.models import *
# from licensing.methods import Key, Helpers
from pynput import keyboard
from pathlib import Path
import csv
import fileinput
import json
import multiprocessing
import os
import sys
import time
from time import gmtime, sleep, strftime
from typing import List
import re
import numpy as np
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
from haasomeapi.HaasomeClient import HaasomeClient
import configparser_cos as cp
import configparser
import operator
from decimal import Decimal
import time
from inspect import getmembers

cp.verifyconfigfile()
ip, secret = cp.connectiondata()


# {
# "botGuid": botguid,
# "botName": botname,
# "accountGuid": accountguid,
# "primaryCoin": primarycoin,
# "secondaryCoin": secondarycoin,
# "fee": float(str(fee).replace(',', '.')),
# "basePrice": float(str(baseprice).replace(',', '.')),
# "priceSpreadType": EnumFlashSpreadOptions(priceSpreadType).name.capitalize(),
# "priceSpread": float(str(pricespread).replace(',', '.')),
# "percentageBoost": float(str(percentageboost).replace(',', '.')),
# "minPercentage": float(str(minpercentage).replace(',', '.')),
# "maxPercentage": float(str(maxpercentage).replace(',', '.')),
# "amountType": EnumCurrencyType(amounttype).name.capitalize(),
# "amountSpread": float(str(amountspread).replace(',', '.')),
# "buyAmount": float(str(buyamount).replace(',', '.')),
# "sellAmount":  float(str(sellamount).replace(',', '.')),
# "refillDelay": refilldelay,
# "safetyEnabled": str(safetyenabled).lower(),
# "safetyTriggerLevel": safetytriggerlevel,
# "safetyMoveInOut": str(safetymoveinout).lower(),
# "fttEnabled": str(followthetrend).lower(),
# "fttRange": followthetrendchannelrange,
# "fttOffset": followthetrendchanneloffset,
# "fttTimeout": followthetrendtimeout
# }


def getfcconfig(currentBotGuid):
    basebotconfig = haasomeClient.customBotApi.get_custom_bot(
        currentBotGuid, EnumCustomBotType.BASE_CUSTOM_BOT
    ).result
    fcdict = {}
    missingmarketdata = {}
    currentpricesource = []
    pricemarket = basebotconfig.priceMarket
    pricemarkets = haasomeClient.marketDataApi.get_price_markets(
        pricemarket.priceSource
    ).result

    for i, v in enumerate(pricemarkets):
        if (
            v.primaryCurrency == pricemarket.primaryCurrency
            and v.secondaryCurrency == pricemarket.secondaryCurrency
        ):
            # missingmarketdata.update({'mintradeammount':v.minimumTradeAmount, 'fee':v.tradeFee, 'pricesource': v.priceSource,'primarycoin': v.primaryCurrency,'secondarycoin': v.secondaryCurrency, 'contractname': v.contractName, 'displayname': v.displayName})
            missingmarketdata.update(
                {
                    "mintradeammount": v.minimumTradeAmount,
                    "fee": v.tradeFee,
                    "pricesource": v.priceSource,
                    "primarycoin": v.primaryCurrency,
                    "secondarycoin": v.secondaryCurrency,
                    "contractname": v.contractName,
                    "displayname": v.displayName,
                    "shortname": v.shortName,
                }
            )
            print(missingmarketdata, "\n\n\n")

    fcdict.update(
        {
            "botGuid": basebotconfig.guid,
            "botname": basebotconfig.name,
            "accountguid": basebotconfig.accountId,
            "primarycoin": missingmarketdata["primarycoin"],
            "secomdarycoin": missingmarketdata["secomdarycoin"],
            "fee": missingmarketdata["fee"],
            "baseprice": basebotconfig.basePrice,
            "pricespreadtype": basebotconfig.priceSpreadType,
            "percentageboost": basebotconfig.percentageBoost,
            "minpercentage": basebotconfig.minPercentage,
            "maxPercentage": basebotconfig.maxPercentage,
            "ammounttype": basebotconfig.amountType,
            "ammountspread": basebotconfig.amountSpread,
            "sellammount": basebotconfig.sellAmount,
            "refilldelay": basebotconfig.refillDelay,
            "safetyenabled": basebotconfig.safetyEnabled,
            "safetyTriggerLevel": basebotconfig.safetyTriggerLevel,
            "safetyMoveInOut": basebotconfig.safetyMoveInOut,
            "fttEnabled": basebotconfig.fttEnabled,
            "fttRange": basebotconfig.fttRange,
            "fttOffset": basebotconfig.fttOffset,
            "fttTimeout": basebotconfig.fttTimeout,
        }
    )

    print(missingmarketdata)
    indicators.update(
        {
            "timeinterval": basebotconfig.interval,
            "bbl": basebotconfig.bBands["Length"],
            "bbdevup": basebotconfig.bBands["Devup"],
            "bbdevdn": basebotconfig.bBands["Devdn"],
            "matype": basebotconfig.bBands["MaType"],
            "Deviation": basebotconfig.bBands["Deviation"],
            "rm": basebotconfig.bBands["ResetMid"],
            "ams": basebotconfig.bBands["AllowMidSell"],
            "fcc": basebotconfig.bBands["RequireFcc"],
            "rsil": basebotconfig.rsi["RsiLength"],
            "rsisell": basebotconfig.rsi["RsiOversold"],
            "rsibuy": basebotconfig.rsi["RsiOverbought"],
            "macdslow": basebotconfig.macd["MacdSlow"],
            "macdfast": basebotconfig.macd["MacdFast"],
            "macdsign": basebotconfig.macd["MacdSign"],
        }
    )
    print(indicators)
    basebotdict.update(
        {
            "accountguid": basebotconfig.accountId,
            "botGuid": basebotconfig.guid,
            "botname": basebotconfig.name,
            "tradeamount": basebotconfig.currentTradeAmount,
            "ammounttype": basebotconfig.amountType,
            "coinposition": basebotconfig.coinPosition,
            "consensus": basebotconfig.useTwoSignals,
            "customtemplate": basebotconfig.customTemplate,
            "icc": basebotconfig.includeIncompleteInterval,
            "mappedbuysignal": basebotconfig.mappedBuySignal,
            "mappedsellsignal": basebotconfig.mappedSellSignal,
            "sldisable": basebotconfig.disableAfterStopLoss,
            "leverage": basebotconfig.leverage,
            "contractname": missingmarketdata["contractname"],
        }
    )  #'minimumtradeammount': pricemarket.minimumTradeAmount
    print(basebotdict)

    return basebotconfig, indicators, basebotdict, missingmarketdata


getfcconfig(fdict[botGuid])
