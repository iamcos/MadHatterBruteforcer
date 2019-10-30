# from licensing.models import *
# from licensing.methods import Key, Helpers
import configparser
import csv
import datetime
import fileinput
import json
import logging
import multiprocessing
import operator
import os
import re
import sys
import threading
import time
from datetime import datetime
from decimal import Decimal
from inspect import getmembers
from pathlib import Path
from time import gmtime, sleep, strftime
from typing import List
from multiprocessing.pool import ThreadPool
import asyncio

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

import _thread
import botsellector
import configparser_cos
import configserver
import expiration
import interval as iiv
from botdatabase import BotDB


async def recreate_stored_bots(bot, configs, haasomeClient):
    results = []
    for i, b in enumerate(configs):
        botname = "TestBot"
        newb = haasomeClient.customBotApi.clone_custom_bot_simple(
            bot.accountId, str(bot.guid), "newname"
        ).result
        configured = haasomeClient.customBotApi.setup_mad_hatter_bot(
            botname,
            botGuid=newb.guid,
            accountGuid=newb.accountId,
            primaryCoin=newb.priceMarket.primaryCurrency,
            secondaryCoin=newb.priceMarket.secondaryCurrency,
            contractName=b.priceMarket.contractName,
            leverage=newb.leverage,
            templateGuid=b.customTemplate,
            position=b.coinPosition,
            fee=newb.currentFeePercentage,
            tradeAmountType=newb.amountType,
            tradeAmount=newb.currentTradeAmount*100,
            useconsensus=b.useTwoSignals,
            disableAfterStopLoss=b.disableAfterStopLoss,
            interval=b.interval,
            includeIncompleteInterval=b.includeIncompleteInterval,
            mappedBuySignal=b.mappedBuySignal,
            mappedSellSignal=b.mappedSellSignal,
        )

        if newb.bBands["Length"] != b.bBands["Length"]:
            do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                newb.guid,
                EnumMadHatterIndicators.BBANDS,
                0,
                configs[i].bBands["Length"],
            )
            # try:
            #   print(do.errorCode, do.errorMessage, 'Length')
            # except :
            #   pass
        if newb.bBands["Devup"] != b.bBands["Devup"]:
            do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                newb.guid, EnumMadHatterIndicators.BBANDS, 1, configs[i].bBands["Devup"]
            )
            # try:
            #   print(do.errorCode, do.errorMessage, 'Devup')
            # except :
            #   pass
        if newb.bBands["Devdn"] != b.bBands["Devdn"]:
            do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                newb.guid, EnumMadHatterIndicators.BBANDS, 2, configs[i].bBands["Devdn"]
            )
            # try:
            #   print(do.errorCode, do.errorMessage, 'Devdn')
            # except :
            #   pass
        if newb.bBands["MaType"] != b.bBands["MaType"]:
            do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                newb.guid,
                EnumMadHatterIndicators.BBANDS,
                3,
                configs[i].bBands["MaType"],
            )
            # try:
            #   print(do.errorCode, do.errorMessage, 'MaType')
            # except :
            #   pass
        if newb.bBands["AllowMidSell"] != b.bBands["AllowMidSell"]:
            do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                newb.guid,
                EnumMadHatterIndicators.BBANDS,
                5,
                configs[i].bBands["AllowMidSell"],
            )
            # try:
            #   print(do.errorCode, do.errorMessage, 'AllowMidSell')
            # except :
            #   pass
        if newb.bBands["RequireFcc"] != b.bBands["RequireFcc"]:
            do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                newb.guid,
                EnumMadHatterIndicators.BBANDS,
                6,
                configs[i].bBands["RequireFcc"],
            )
            # try:
            #   print(do.errorCode, do.errorMessage, 'RequireFcc')
            # except :
            #   pass
        if newb.rsi["RsiLength"] != b.rsi["RsiLength"]:
            do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                newb.guid, EnumMadHatterIndicators.RSI, 0, configs[i].rsi["RsiLength"]
            )
            # try:
            #   print(do.errorCode, do.errorMessage, 'RsiLength')
            # except :
            #   pass
        if newb.rsi["RsiOverbought"] != b.rsi["RsiOverbought"]:
            do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                newb.guid,
                EnumMadHatterIndicators.RSI,
                1,
                configs[i].rsi["RsiOverbought"],
            )
            # try:
            #   print(do.errorCode, do.errorMessage, 'RsiOverbought')
            # except :
            #   pass
        if newb.rsi["RsiOversold"] != b.rsi["RsiOversold"]:
            do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                newb.guid, EnumMadHatterIndicators.RSI, 2, configs[i].rsi["RsiOversold"]
            )
            # try:
            #   print(do.errorCode, do.errorMessage, 'RsiOversold')
            # except :
            #   pass
        if newb.macd["MacdFast"] != b.macd["MacdFast"]:
            do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                newb.guid, EnumMadHatterIndicators.MACD, 0, configs[i].macd["MacdFast"]
            )
            # try:
            #   print(do.errorCode, do.errorMessage, 'MacdFast')
            # except :
            #   pass
        if newb.macd["MacdSlow"] != b.macd["MacdSlow"]:
            do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                newb.guid, EnumMadHatterIndicators.MACD, 1, configs[i].macd["MacdSlow"]
            )
            # try:
            #   print(do.errorCode, do.errorMessage, 'MacdSlow')
            # except :
            #   pass

        if newb.macd["MacdSign"] != b.macd["MacdSign"]:
            do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                newb.guid, EnumMadHatterIndicators.MACD, 2, configs[i].macd["MacdSign"]
            )
            # try:
            #   print(do.errorCode, do.errorMessage, 'MacdSign')
            # except :
            #   pass

        ticks = iiv.readinterval()
        bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
            newb.accountId,
            newb.guid,
            ticks,
            newb.priceMarket.primaryCurrency,
            newb.priceMarket.secondaryCurrency,
            newb.priceMarket.contractName,
        )
        try:
            print("bt", bt.errorCode, bt.errorMessage)
        except:
            pass
        btr = bt.result
        roi = btr.roi
        print(roi)
        results.append(newb)
        delete = haasomeClient.customBotApi.remove_custom_bot(newb.guid)
        # try:
        #   print('delete', delete.errorCode, delete.errorMessage)
        # except :
        #   pass

        # print(results)
    prevresults = BotDB.load_botlist("results.db")
    newresults = prevresults + results
    BotDB.save_bots(newresults)
    return results


def connect():
    ip, secret = configserver.validateserverdata()
    haasomeClient = HaasomeClient(ip, secret)
    return haasomeClient


# expiration date setting:
# expiration.setexpiration('2019-9-01')

def slice_data(data, nprocs):
    
    aver, res = divmod(len(data), nprocs)
    nums = []
    for proc in range(nprocs):
        if proc < res:
            nums.append(aver + 1)
        else:
            nums.append(aver)
    count = 0
    slices = []
    for proc in range(nprocs):
        slices.append(data[count: count+nums[proc]])
        count += nums[proc]
    return slices


async def main():

    # results = []
    # botType = EnumCustomBotType.MAD_HATTER_BOT
    haasomeClient = connect()
    bot = botsellector.getallmhbots(haasomeClient)
    # results = []
    configs = BotDB.load_botlist("bots.db")
    tasks = slice_data(configs,2)
    jobs = []
    for item in tasks:
        task = asyncio.ensure_future(recreate_stored_bots(bot,item[:1],haasomeClient))
        jobs.append(task)
    await asyncio.gather(*jobs)
    ticks = iiv.readinterval()
    # for i in jobs:
    #     print(i.result()[0].roi)
    filename = (
            str(bot.priceMarket.primaryCurrency)
            + "\\"
            + str(bot.priceMarket.secondaryCurrency)
            + " "
            + str(ticks)
            + ".db")

    botresults = BotDB.load_botlist(filename)
    for i in botresults:
        print(i.roi)


if __name__ == "__main__":
    _start = time.time()
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(main())
    loop.run_until_complete(future)
    print(f"Execution time: { time.time() - _start }")
    loop.close()
    
   