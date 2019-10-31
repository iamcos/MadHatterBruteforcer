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
import concurrent.futures

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
ip, secret = configserver.validateserverdata()
haasomeClient = HaasomeClient(ip, secret)


def create_new_custom_bot(newbot, example_bot):
    print(example_bot.name)
    new = haasomeClient.customBotApi.new_custom_bot(
        example_bot.accountId,
        newbot.botType,
        "IMP: " + newbot.name,
        newbot.priceMarket.primaryCurrency,
        newbot.priceMarket.secondaryCurrency,
        newbot.priceMarket.contractName,
    )
    print('new ',new.errorCode, new.errorMessage)
    BotDB.set_safety_parameters(newbot, example_bot)
    newr = new.result
    # print(newr)
    return newr

def recreate_stored_bots(bot, configs, haasomeClient):
    current_bot = haasomeClient.customBotApi.clone_custom_bot_simple(bot.accountId, bot.guid, 'temp: '+bot.name).result
    results = []
    # print(configs[0][0])
    for i, b in enumerate(configs):

        
        configured = haasomeClient.customBotApi.setup_mad_hatter_bot(
            botName = current_bot.name,
            botGuid=current_bot.guid,
            accountGuid=current_bot.accountId,
            primaryCoin=current_bot.priceMarket.primaryCurrency,
            secondaryCoin=current_bot.priceMarket.secondaryCurrency,
            contractName=bb.priceMarket.contractName,
            leverage=current_bot.leverage,
            templateGuid=bb.customTemplate,
            position=bb.coinPosition,
            fee=current_bot.currentFeePercentage,
            tradeAmountType=current_bot.amountType,
            tradeAmount=current_bot.currentTradeAmount,
            useconsensus=bb.useTwoSignals,
            disableAfterStopLoss=bb.disableAfterStopLoss,
            interval=bb.interval,
            includeIncompleteInterval=bb.includeIncompleteInterval,
            mappedBuySignal=bb.mappedBuySignal,
            mappedSellSignal=bb.mappedSellSignal,
        )

        if current_bot.bBands["Length"] != bb.bBands["Length"]:
            do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                current_bot.guid,
                EnumMadHatterIndicators.BBANDS,
                0,
                bb.bBands["Length"],
            )
            # try:
            #   print(do.errorCode, do.errorMessage, 'Length')
            # except :
            #   pass
        if current_bot.bBands["Devup"] != bb.bBands["Devup"]:
            do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                current_bot.guid, EnumMadHatterIndicators.BBANDS, 1, bb.bBands["Devup"]
            )
            # try:
            #   print(do.errorCode, do.errorMessage, 'Devup')
            # except :
            #   pass
        if current_bot.bBands["Devdn"] != bb.bBands["Devdn"]:
            do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                current_bot.guid, EnumMadHatterIndicators.BBANDS, 2, bb.bBands["Devdn"]
            )
            # try:
            #   print(do.errorCode, do.errorMessage, 'Devdn')
            # except :
            #   pass
        if current_bot.bBands["MaType"] != bb.bBands["MaType"]:
            do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                current_bot.guid,
                EnumMadHatterIndicators.BBANDS,
                3,
                bb.bBands["MaType"],
            )
            # try:
            #   print(do.errorCode, do.errorMessage, 'MaType')
            # except :
            #   pass
        if current_bot.bBands["AllowMidSell"] != bb.bBands["AllowMidSell"]:
            do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                current_bot.guid,
                EnumMadHatterIndicators.BBANDS,
                5,
                bb.bBands["AllowMidSell"],
            )
            # try:
            #   print(do.errorCode, do.errorMessage, 'AllowMidSell')
            # except :
            #   pass
        if current_bot.bBands["RequireFcc"] != bb.bBands["RequireFcc"]:
            do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                current_bot.guid,
                EnumMadHatterIndicators.BBANDS,
                6,
                bb.bBands["RequireFcc"],
            )
            # try:
            #   print(do.errorCode, do.errorMessage, 'RequireFcc')
            # except :
            #   pass
        if current_bot.rsi["RsiLength"] != bb.rsi["RsiLength"]:
            do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                current_bot.guid, EnumMadHatterIndicators.RSI, 0, bb.rsi["RsiLength"]
            )
            # try:
            #   print(do.errorCode, do.errorMessage, 'RsiLength')
            # except :
            #   pass
        if current_bot.rsi["RsiOverbought"] != bb.rsi["RsiOverbought"]:
            do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                current_bot.guid,
                EnumMadHatterIndicators.RSI,
                1,
                bb.rsi["RsiOverbought"],
            )
            # try:
            #   print(do.errorCode, do.errorMessage, 'RsiOverbought')
            # except :
            #   pass
        if current_bot.rsi["RsiOversold"] != bb.rsi["RsiOversold"]:
            do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                current_bot.guid, EnumMadHatterIndicators.RSI, 2, bb.rsi["RsiOversold"]
            )
            # try:
            #   print(do.errorCode, do.errorMessage, 'RsiOversold')
            # except :
            #   pass
        if current_bot.macd["MacdFast"] != bb.macd["MacdFast"]:
            do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                current_bot.guid, EnumMadHatterIndicators.MACD, 0, bb.macd["MacdFast"]
            )
            # try:
            #   print(do.errorCode, do.errorMessage, 'MacdFast')
            # except :
            #   pass
        if current_bot.macd["MacdSlow"] != bb.macd["MacdSlow"]:
            do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                current_bot.guid, EnumMadHatterIndicators.MACD, 1, bb.macd["MacdSlow"]
            )
            # try:
            #   print(do.errorCode, do.errorMessage, 'MacdSlow')
            # except :
            #   pass

        if current_bot.macd["MacdSign"] != bb.macd["MacdSign"]:
            do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                current_bot.guid, EnumMadHatterIndicators.MACD, 2, bb.macd["MacdSign"]
            )
            # try:
            #   print(do.errorCode, do.errorMessage, 'MacdSign')
            # except :
            #   pass

        ticks = iiv.readinterval(current_bot)
        bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
            current_bot.accountId,
            current_bot.guid,
            ticks,
            current_bot.priceMarket.primaryCurrency,
            current_bot.priceMarket.secondaryCurrency,
            current_bot.priceMarket.contractName,
        )
        try:
            print("bt", bt.errorCode, bt.errorMessage)
        except:
            pass
        btr = bt.result
        roi = btr.roi
        print(roi)
        results.append(btr)
        delete = haasomeClient.customBotApi.remove_custom_bot(current_bot.guid)
        # try:
        #   print('delete', delete.errorCode, delete.errorMessage)
        # except :
        #   pass

        # print(results)
  
  
        return results

# expiration date setting:
# expiration.setexpiration('2019-9-01')

class ReturningThread(threading.Thread):
    def run(self):
        try:
            if self._target:
                self._result = self._target(*self._args, **self._kwargs)
        finally:
            del self._target, self._args, self._kwargs

    def join(self):
        super().join()
        return self._result

def chunks(configs, cpu_cores):

    return [configs[i:i+cpu_cores] for i in range(0, len(configs), cpu_cores)]
    


def do_job(job_id, data_slice):
    for item in data_slice:
        print( "job", job_id, item)


def dispatch_jobs(configs, bot):
    threds_n = os.cpu_count()
    # print('there are ', threds_n, 'CPU Cores')
    # print(configs)
    total = len(configs)
    chunk_size = total / 1
    # slice = chunks(configs, int(chunk_size))
    slice = chunks(configs, int(chunk_size))
    # print('slice', len(slice))
    jobs = []
    
    for i, s in enumerate(slice):
        for config in s:
            # print(s)
            j = ReturningThread(target=recreate_stored_bots, args=(bot, s, haasomeClient))
            jobs.append(j)
            j.start()
    results = []
    
    for j in jobs:
        results.append(j.join())
  
    results2 = []
    for i in results:
        results2.append(i[0])
    return results2

if __name__ == "__main__":
    configserver.set_bt()
    results = []
    # haasomeClient = connect()
    bot = botsellector.get_mh_bot(haasomeClient)
    results = []
    botfile = BotDB.return_botlist_file()
    # print(botfile)
    configs = BotDB.load_botlist(botfile)
    
    # print(configs)
    # data = ['a', 'b', 'c', 'd']
    # chunks = chunks(configs, int(8))
    # print(len(chunks[1]))
    # print(chunks[0][0])
    # for i,c in enumerate(chunks):
    #     print('chunk', i)
    #     for b in c:
    #         b = BotDB.make_bot_from_string(b)
    #         print(b.name)
    bt_results = dispatch_jobs(configs,bot)
    bt_results = bt_results[:30]
   
 
    
    BotDB.save_botlist_to_file(bt_results)
    # print(rs)
    # for i in rs:
    #     print(i[0].roi)

20/10/19 10:00