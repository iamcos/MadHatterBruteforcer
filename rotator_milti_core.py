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

import numpy as np
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
from haasomeapi.HaasomeClient import HaasomeClient

import _thread
import botsellector
import configparser_cos
import configserver
import expiration
import interval as iiv
from botdatabase import BotDB


def recreate_stored_bots(bot, configs, haasomeClient):
	results = []
	for i, b in enumerate(configs):
			botname = 'TestBot'
			newb = haasomeClient.customBotApi.clone_custom_bot_simple(bot.accountId, str(bot.guid),'newname').result
			configured = haasomeClient.customBotApi.setup_mad_hatter_bot(botname, botGuid=newb.guid, accountGuid=newb.accountId, primaryCoin=newb.priceMarket.primaryCurrency, secondaryCoin=newb.priceMarket.secondaryCurrency, contractName=b.priceMarket.contractName, leverage =newb.leverage,templateGuid=b.customTemplate, position= b.coinPosition, fee=newb.currentFeePercentage, tradeAmountType=newb.amountType, tradeAmount=newb.currentTradeAmount, useconsensus=b.useTwoSignals, disableAfterStopLoss=b.disableAfterStopLoss, interval=b.interval, includeIncompleteInterval=b.includeIncompleteInterval,mappedBuySignal=b.mappedBuySignal, mappedSellSignal=b.mappedSellSignal)

			if newb.bBands['Length']!= b.bBands['Length']:
				do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				newb.guid, EnumMadHatterIndicators.BBANDS, 0, configs[i].bBands['Length'])
				# try:    
				#   print(do.errorCode, do.errorMessage, 'Length')
				# except :
				#   pass
			if newb.bBands['Devup']!= b.bBands['Devup']:
				do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				newb.guid, EnumMadHatterIndicators.BBANDS, 1, configs[i].bBands['Devup'])
				# try:    
				#   print(do.errorCode, do.errorMessage, 'Devup')
				# except :
				#   pass
			if newb.bBands['Devdn']!= b.bBands['Devdn']:
				do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				newb.guid, EnumMadHatterIndicators.BBANDS, 2, configs[i].bBands['Devdn'])
				# try:    
				#   print(do.errorCode, do.errorMessage, 'Devdn')
				# except :
				#   pass
			if newb.bBands['MaType']!= b.bBands['MaType']:
				do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				newb.guid, EnumMadHatterIndicators.BBANDS, 3, configs[i].bBands['MaType'])
				# try:    
				#   print(do.errorCode, do.errorMessage, 'MaType')
				# except :
				#   pass
			if newb.bBands['AllowMidSell']!= b.bBands['AllowMidSell']:
				do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				newb.guid, EnumMadHatterIndicators.BBANDS, 5, configs[i].bBands['AllowMidSell'])
				# try:    
				#   print(do.errorCode, do.errorMessage, 'AllowMidSell')
				# except :
				#   pass
			if newb.bBands['RequireFcc']!= b.bBands['RequireFcc']:
				do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				newb.guid, EnumMadHatterIndicators.BBANDS, 6, configs[i].bBands['RequireFcc'])
				# try:    
				#   print(do.errorCode, do.errorMessage, 'RequireFcc')
				# except :
				#   pass
			if newb.rsi['RsiLength']!= b.rsi['RsiLength']:
				do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				newb.guid, EnumMadHatterIndicators.RSI, 0, configs[i].rsi['RsiLength'])
				# try:    
				#   print(do.errorCode, do.errorMessage, 'RsiLength')
				# except :
				#   pass
			if newb.rsi['RsiOverbought']!= b.rsi['RsiOverbought']:
				do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				newb.guid, EnumMadHatterIndicators.RSI, 1, configs[i].rsi['RsiOverbought'])
				# try:    
				#   print(do.errorCode, do.errorMessage, 'RsiOverbought')
				# except :
				#   pass
			if newb.rsi['RsiOversold']!= b.rsi['RsiOversold']:
				do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				newb.guid, EnumMadHatterIndicators.RSI, 2, configs[i].rsi['RsiOversold'])
				# try:    
				#   print(do.errorCode, do.errorMessage, 'RsiOversold')
				# except :
				#   pass
			if newb.macd['MacdFast']!= b.macd['MacdFast']:
				do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				newb.guid, EnumMadHatterIndicators.MACD, 0, configs[i].macd['MacdFast'])
				# try:    
				#   print(do.errorCode, do.errorMessage, 'MacdFast')
				# except :
				#   pass
			if newb.macd['MacdSlow']!= b.macd['MacdSlow']:
				do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
					newb.guid, EnumMadHatterIndicators.MACD, 1, configs[i].macd['MacdSlow'])
				# try:    
				#   print(do.errorCode, do.errorMessage, 'MacdSlow')
				# except :
				#   pass

			if newb.macd['MacdSign']!= b.macd['MacdSign']:
				do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				newb.guid, EnumMadHatterIndicators.MACD, 2, configs[i].macd['MacdSign'])
				# try:    
				#   print(do.errorCode, do.errorMessage, 'MacdSign')
				# except :
				#   pass

			ticks = iiv.readinterval(bot.interval)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(newb.accountId, newb.guid, ticks, newb.priceMarket.primaryCurrency, newb.priceMarket.secondaryCurrency, newb.priceMarket.contractName)
			try:    
				print('bt', bt.errorCode, bt.errorMessage)
			except :
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
	prevresults = BotDB.load_botlist('results.db')
	newresults = prevresults+results
	BotDB.save_bots(newresults,'results.db')
	return results


def connect():
		ip, secret = configserver.validateserverdata()
		haasomeClient = HaasomeClient(ip, secret)
		return haasomeClient




#expiration date setting:
# expiration.setexpiration('2019-9-01')

def main():
	

	results = []
	botType = EnumCustomBotType.MAD_HATTER_BOT
	haasomeClient = connect()
	bot, botlist = botsellector.getallmhbots(haasomeClient)
	results = []
	configs = BotDB.load_botlist('bots.db')

	i = 0
	b = i-47
	i +=48
	t1 = multiprocessing.Process(target=recreate_stored_bots, args =(bot, configs[0:i], haasomeClient))
	i +=48
	b = i-47
	t2 = multiprocessing.Process(target=recreate_stored_bots, args =(bot, configs[b:i], haasomeClient))
	i +=48
	b = i-47
	t4 = multiprocessing.Process(target=recreate_stored_bots, args =(bot, configs[b:i], haasomeClient))
	i +=48
	b = i-47
	t3 = multiprocessing.Process(target=recreate_stored_bots, args =(bot, configs[b:i], haasomeClient))
	i +=48
	b = i-47
	t5 = multiprocessing.Process(target=recreate_stored_bots, args =(bot, configs[b:i], haasomeClient))
	i +=48
	b = i-47
	t6 = multiprocessing.Process(target=recreate_stored_bots, args =(bot, configs[b:i], haasomeClient))
	i +=48
	b = i-47
	t7 = multiprocessing.Process(target=recreate_stored_bots, args =(bot, configs[b:i], haasomeClient))
	i +=48
	b = i-47
	t8 = multiprocessing.Process(target=recreate_stored_bots, args =(bot, configs[b:i], haasomeClient))
	i +=48
	b = i-47
	t9 = multiprocessing.Process(target=recreate_stored_bots, args =(bot, configs[b:i], haasomeClient))
	i +=48
	b = i-47
	t10 = multiprocessing.Process(target=recreate_stored_bots, args =(bot, configs[b:i], haasomeClient))
	i +=48
	b = i-47
	t1.start() 
	t2.start()
	t3.start() 
	t4.start() 
	t5.start()
	t6.start() 
	t7.start() 
	t8.start()
	t9.start() 
	t10.start() 

	t1.join() 
	t2.join()
	t3.join() 
	t4.join() 
	t5.join()
	t6.join() 
	t7.join() 
	t8.join()
	t9.join() 
	t10.join() 
		

	print(resultslist)

if __name__ == '__main__':
	main()
