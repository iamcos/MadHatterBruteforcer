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
import history
from history import BotScripts, MarketData, Plot
from history import

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

	for i, b in enumerate(configs):
		print(i, b)
		bb = b


		setup_bot = haasomeClient.customBotApi.setup_mad_hatter_bot(
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
			try:
			 print(do.errorCode, do.errorMessage, 'Length')
			except :
			 pass
		if current_bot.bBands["Devup"] != bb.bBands["Devup"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid, EnumMadHatterIndicators.BBANDS, 1, bb.bBands["Devup"]
			)
			try:
			 print(do.errorCode, do.errorMessage, 'Devup')
			except :
			 pass
		if current_bot.bBands["Devdn"] != bb.bBands["Devdn"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid, EnumMadHatterIndicators.BBANDS, 2, bb.bBands["Devdn"]
			)
			try:
			 print(do.errorCode, do.errorMessage, 'Devdn')
			except :
			 pass
		if current_bot.bBands["MaType"] != bb.bBands["MaType"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid,
				EnumMadHatterIndicators.BBANDS,
				3,
				bb.bBands["MaType"],
			)
			try:
			 print(do.errorCode, do.errorMessage, 'MaType')
			except :
			 pass
		if current_bot.bBands["AllowMidSell"] != bb.bBands["AllowMidSell"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid,
				EnumMadHatterIndicators.BBANDS,
				5,
				bb.bBands["AllowMidSell"],
			)
			try:
			 print(do.errorCode, do.errorMessage, 'AllowMidSell')
			except :
			 pass
		if current_bot.bBands["RequireFcc"] != bb.bBands["RequireFcc"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid,
				EnumMadHatterIndicators.BBANDS,
				6,
				bb.bBands["RequireFcc"],
			)
			try:
			 print(do.errorCode, do.errorMessage, 'RequireFcc')
			except :
			 pass
		if current_bot.rsi["RsiLength"] != bb.rsi["RsiLength"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid, EnumMadHatterIndicators.RSI, 0, bb.rsi["RsiLength"]
			)
			try:
			 print(do.errorCode, do.errorMessage, 'RsiLength')
			except :
			 pass
		if current_bot.rsi["RsiOverbought"] != bb.rsi["RsiOverbought"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid,
				EnumMadHatterIndicators.RSI,
				1,
				bb.rsi["RsiOverbought"],
			)
			try:
			 print(do.errorCode, do.errorMessage, 'RsiOverbought')
			except :
			 pass
		if current_bot.rsi["RsiOversold"] != bb.rsi["RsiOversold"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid, EnumMadHatterIndicators.RSI, 2, bb.rsi["RsiOversold"]
			)
			try:
			 print(do.errorCode, do.errorMessage, 'RsiOversold')
			except :
			 pass
		if current_bot.macd["MacdFast"] != bb.macd["MacdFast"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid, EnumMadHatterIndicators.MACD, 0, bb.macd["MacdFast"]
			)
			try:
			 print(do.errorCode, do.errorMessage, 'MacdFast')
			except :
			 pass
		if current_bot.macd["MacdSlow"] != bb.macd["MacdSlow"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid, EnumMadHatterIndicators.MACD, 1, bb.macd["MacdSlow"]
			)
			try:
			 print(do.errorCode, do.errorMessage, 'MacdSlow')
			except :
			 pass

		if current_bot.macd["MacdSign"] != bb.macd["MacdSign"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid, EnumMadHatterIndicators.MACD, 2, bb.macd["MacdSign"]
			)
			try:
			 print(do.errorCode, do.errorMessage, 'MacdSign')
			except :
			 pass

		ticks = iiv.readinterval(current_bot)
		bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
			current_bot.accountId,
			current_bot.guid,
			int(ticks),
			current_bot.priceMarket.primaryCurrency,
			current_bot.priceMarket.secondaryCurrency,
			current_bot.priceMarket.contractName,
		)
		try:
			print("bt", bt.errorCode, bt.errorMessage)
			btr = bt.result
			roi = btr.roi

			print(roi)
			results.append(btr)
		except:
			pass
		

		
		delete = haasomeClient.customBotApi.remove_custom_bot(current_bot.guid)
	


	return results

def bt_bot_configs2(bot, configs, haasomeClient):
	results = []
	

	
	for bb in (configs):
		current_bot = haasomeClient.customBotApi.clone_custom_bot_simple(bot.accountId, bot.guid, 'temp: '+bot.name).result
		setup_bot = haasomeClient.customBotApi.setup_mad_hatter_bot(
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
	).result

		if current_bot.bBands["Length"] != bb.bBands["Length"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid,
				EnumMadHatterIndicators.BBANDS,
				0,
				bb.bBands["Length"],
			)
			try:
			 print(do.errorCode, do.errorMessage, 'Length')
			except :
			 pass
		if current_bot.bBands["Devup"] != bb.bBands["Devup"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid, EnumMadHatterIndicators.BBANDS, 1, bb.bBands["Devup"]
			)
			try:
			 print(do.errorCode, do.errorMessage, 'Devup')
			except :
			 pass
		if current_bot.bBands["Devdn"] != bb.bBands["Devdn"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid, EnumMadHatterIndicators.BBANDS, 2, bb.bBands["Devdn"]
			)
			try:
			 print(do.errorCode, do.errorMessage, 'Devdn')
			except :
			 pass
		if current_bot.bBands["MaType"] != bb.bBands["MaType"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid,
				EnumMadHatterIndicators.BBANDS,
				3,
				bb.bBands["MaType"],
			)
			try:
			 print(do.errorCode, do.errorMessage, 'MaType')
			except :
			 pass
		if current_bot.bBands["AllowMidSell"] != bb.bBands["AllowMidSell"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid,
				EnumMadHatterIndicators.BBANDS,
				5,
				bb.bBands["AllowMidSell"],
			)
			try:
			 print(do.errorCode, do.errorMessage, 'AllowMidSell')
			except :
			 pass
		if current_bot.bBands["RequireFcc"] != bb.bBands["RequireFcc"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid,
				EnumMadHatterIndicators.BBANDS,
				6,
				bb.bBands["RequireFcc"],
			)
			try:
			 print(do.errorCode, do.errorMessage, 'RequireFcc')
			except :
			 pass
		if current_bot.rsi["RsiLength"] != bb.rsi["RsiLength"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid, EnumMadHatterIndicators.RSI, 0, bb.rsi["RsiLength"]
			)
			try:
			 print(do.errorCode, do.errorMessage, 'RsiLength')
			except :
			 pass
		if current_bot.rsi["RsiOverbought"] != bb.rsi["RsiOverbought"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid,
				EnumMadHatterIndicators.RSI,
				1,
				bb.rsi["RsiOverbought"],
			)
			try:
			 print(do.errorCode, do.errorMessage, 'RsiOverbought')
			except :
			 pass
		if current_bot.rsi["RsiOversold"] != bb.rsi["RsiOversold"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid, EnumMadHatterIndicators.RSI, 2, bb.rsi["RsiOversold"]
			)
			try:
			 print(do.errorCode, do.errorMessage, 'RsiOversold')
			except :
			 pass
		if current_bot.macd["MacdFast"] != bb.macd["MacdFast"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid, EnumMadHatterIndicators.MACD, 0, bb.macd["MacdFast"]
			)
			try:
			 print(do.errorCode, do.errorMessage, 'MacdFast')
			except :
			 pass
		if current_bot.macd["MacdSlow"] != bb.macd["MacdSlow"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid, EnumMadHatterIndicators.MACD, 1, bb.macd["MacdSlow"]
			)
			try:
			 print(do.errorCode, do.errorMessage, 'MacdSlow')
			except :
			 pass

		if current_bot.macd["MacdSign"] != bb.macd["MacdSign"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid, EnumMadHatterIndicators.MACD, 2, bb.macd["MacdSign"]
			)
			try:
			 print(do.errorCode, do.errorMessage, 'MacdSign')
			except :
			 pass

		ticks = iiv.readinterval(current_bot)
		bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
			current_bot.accountId,
			current_bot.guid,
			int(ticks),
			current_bot.priceMarket.primaryCurrency,
			current_bot.priceMarket.secondaryCurrency,
			current_bot.priceMarket.contractName,
		)
		print("bt", bt.errorCode, bt.errorMessage)
		# print(len(bt.resuls.completedOrders))
		btr = bt.result
		roi = btr.roi

		print(roi)
		results.append(btr)
		delete = haasomeClient.customBotApi.remove_custom_bot(current_bot.guid)
	
	# 20/10/19 10:00

	BotDB.save_botlist_to_file(results)

	return results

def configure_bot(current_bot, setup_bot):
	current_bot = haasomeClient.customBotApi.clone_custom_bot_simple(bot.accountId, bot.guid, 'temp: '+bot.name).result
	setup_bot = haasomeClient.customBotApi.setup_mad_hatter_bot(
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
	mappedSellSignal=bb.mappedSellSignal,).result
	print('Bot haas been configured')
	return setup_bot

def set_bot_indicators(current_bot, config):
		
		if current_bot.bBands["Length"] != config.bBands["Length"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
			current_bot.guid,
			EnumMadHatterIndicators.BBANDS,
			0,
			config.bBands["Length"],
		)
		try:
			print(do.errorCode, do.errorMessage, 'Length')
		except :
			pass
		if current_bot.bBands["Devup"] != config.bBands["Devup"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid, EnumMadHatterIndicators.BBANDS, 1, config.bBands["Devup"]
			)
			try:
			 print(do.errorCode, do.errorMessage, 'Devup')
			except :
			 pass
		if current_bot.bBands["Devdn"] != config.bBands["Devdn"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid, EnumMadHatterIndicators.BBANDS, 2, config.bBands["Devdn"]
			)
			try:
			 print(do.errorCode, do.errorMessage, 'Devdn')
			except :
			 pass
		if current_bot.bBands["MaType"] != config.bBands["MaType"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid,
				EnumMadHatterIndicators.BBANDS,
				3,
				config.bBands["MaType"],
			)
			try:
			 print(do.errorCode, do.errorMessage, 'MaType')
			except :
			 pass
		if current_bot.bBands["AllowMidSell"] != config.bBands["AllowMidSell"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid,
				EnumMadHatterIndicators.BBANDS,
				5,
				config.bBands["AllowMidSell"],
			)
			try:
			 print(do.errorCode, do.errorMessage, 'AllowMidSell')
			except :
			 pass
		if current_bot.bBands["RequireFcc"] != config.bBands["RequireFcc"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid,
				EnumMadHatterIndicators.BBANDS,
				6,
				config.bBands["RequireFcc"],
			)
			try:
			 print(do.errorCode, do.errorMessage, 'RequireFcc')
			except :
			 pass
		if current_bot.rsi["RsiLength"] != config.rsi["RsiLength"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid, EnumMadHatterIndicators.RSI, 0, config.rsi["RsiLength"]
			)
			try:
			 print(do.errorCode, do.errorMessage, 'RsiLength')
			except :
			 pass
		if current_bot.rsi["RsiOverbought"] != config.rsi["RsiOverbought"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid,
				EnumMadHatterIndicators.RSI,
				1,
				config.rsi["RsiOverbought"],
			)
			try:
			 print(do.errorCode, do.errorMessage, 'RsiOverbought')
			except :
			 pass
		if current_bot.rsi["RsiOversold"] != config.rsi["RsiOversold"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid, EnumMadHatterIndicators.RSI, 2, config.rsi["RsiOversold"]
			)
			try:
			 print(do.errorCode, do.errorMessage, 'RsiOversold')
			except :
			 pass
		if current_bot.macd["MacdFast"] != config.macd["MacdFast"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid, EnumMadHatterIndicators.MACD, 0, config.macd["MacdFast"]
			)
			try:
			 print(do.errorCode, do.errorMessage, 'MacdFast')
			except :
			 pass
		if current_bot.macd["MacdSlow"] != config.macd["MacdSlow"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid, EnumMadHatterIndicators.MACD, 1, config.macd["MacdSlow"]
			)
			try:
			 print(do.errorCode, do.errorMessage, 'MacdSlow')
			except :
			 pass

		if current_bot.macd["MacdSign"] != config.macd["MacdSign"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid, EnumMadHatterIndicators.MACD, 2, config.macd["MacdSign"]
			)
			try:
			 print(do.errorCode, do.errorMessage, 'MacdSign')
			except :
			 pass
		

		print('bot haas cofigured and configured')
		return do.result


def bt_bot_configs(bot,configs,haasomeClient):
	for bb in configs:
		result = configure_bot(bot,bb, haasomeClient)
		result2 = set_bot_indicators(result)



def find_good_safety(bot, haasomeClient):
	best_roi = bot.roi
	print(best_roi)
	ticks = iiv.readinterval()
	stoploss = []
	if bot.platformType == 0:
		for x in np.arange(1.5,3.0,0.2):
			stopLoss = haasomeClient.customBotApi.set_mad_hatter_safety_parameter(
			
			bot.guid, EnumMadHatterSafeties.STOP_LOSS, round(x,2))
			backtest = haasomeClient.customBotApi.backtest_custom_bot_on_market(bot.accountId, bot.guid, ticks, bot.priceMarket.primaryCurrency, bot.priceMarket.secondaryCurrency, bot.priceMarket.contractName)
			backtestr = backtest.result
			roi = backtestr.roi
			print('Stoploss', round(x,2), ': ', roi)
			stoploss.append([roi,round(x,2)])
	if bot.platformType == 2:
		for x in np.arange(0.0,200.0,10.0):
			stopLoss = haasomeClient.customBotApi.set_mad_hatter_safety_parameter(
			bot.guid, EnumMadHatterSafeties.STOP_LOSS, round(x,2))
			backtest = haasomeClient.customBotApi.backtest_custom_bot_on_market(bot.accountId, bot.guid, ticks, bot.priceMarket.primaryCurrency, bot.priceMarket.secondaryCurrency, bot.priceMarket.contractName)
			backtestr = backtest.result
			roi = backtestr.roi
			print('Stoploss', x, ': ', roi)
			stoploss.append([roi,round(x,2)])
	
	sortedstoploss = sorted(stoploss, key=lambda x: x[0], reverse=True)
	if sortedstoploss[0][1] >= best_roi:
		stopLoss = haasomeClient.customBotApi.set_mad_hatter_safety_parameter(
			bot.guid, EnumMadHatterSafeties.STOP_LOSS, sortedstoploss[0][1])
	else: 
		stopLoss = haasomeClient.customBotApi.set_mad_hatter_safety_parameter(
			bot.guid, EnumMadHatterSafeties.STOP_LOSS, 0)

def makebots(bot, haasomeClient,botType, roilist):
	x = input(' Type a number of of bots you would like to create from the top')
	for i in range(x):
			ticks = iiv.readinterval()
			botname = str(bot.priceMarket.primaryCurrency) + str(' / ') + \
				str(bot.priceMarket.secondaryCurrency) + str(' Roi ') + str(roilist[i][13])
			newbotfrommarket = haasomeClient.customBotApi.new_custom_bot(bot.accountId, botType, botname, bot.priceMarket.primaryCurrency, bot.priceMarket.secondaryCurrency, bot.priceMarket.contractName).result
			setup_newbot = haasomeClient.customBotApi.setup_mad_hatter_bot(botname, newbotfrommarket.guid, newbotfrommarket.accountId,bot.priceMarket.primaryCurrency,bot.priceMarket.secondaryCurrency, bot.priceMarket.contractName, bot.leverage,  bot.customTemplate,  bot.fundsPosition,  bot.currentFeePercentage,  bot.amountType, bot.currentTradeAmount, bot.useTwoSignals, bot.disableAfterStopLoss, bot.interval,bot.includeIncompleteInterval, bot.mappedBuySignal, bot.mappedSellSignal).result
			guid = newbotfrommarket.guid
			setup_newbotfrommarket = configuremh(haasomeClient, guid,roilist[i][0], roilist[i][1], roilist[i][2], roilist[i][3], roilist[i][4], roilist[i][5], roilist[i][6], roilist[i][7], roilist[i][8], roilist[i][9], roilist[i][10], roilist[i][11], roilist[i][12])
			sellStep = haasomeClient.customBotApi.set_mad_hatter_safety_parameter(
			newbotfrommarket.guid, EnumMadHatterSafeties.PRICE_CHANGE_TO_SELL, bot.priceChangeToSell)
			buyStep = haasomeClient.customBotApi.set_mad_hatter_safety_parameter(
			newbotfrommarket.guid, EnumMadHatterSafeties.PRICE_CHANGE_TO_BUY, bot.priceChangeToBuy)
			stopLoss = haasomeClient.customBotApi.set_mad_hatter_safety_parameter(
			newbotfrommarket.guid, EnumMadHatterSafeties.STOP_LOSS, bot.stopLoss)
			print(botname, 'has been created')
			find_good_safety(newbotfrommarket, haasomeClient)
			backtest = haasomeClient.customBotApi.backtest_custom_bot(setup_newbot.guid, ticks)

def intro():
	

	print('1. Backtest a bot with set of configs from a file')
	print('2. Change BT period')
	print('3. Analyze and create bots stored in files, be it saved bt results or of another machine')
	print('4. Find a good safety for a bot ')
	response = input('Type number of action here: ')
	while True:
		if response == '1':
			bot = botsellector.get_mh_bot(haasomeClient)
			botlistfile = BotDB.return_botlist_file()
			configs = BotDB.load_botlist(botlistfile)
			# print(configs[:10])
			results = bt_bot_configs(bot, configs,haasomeClient)
			BotDB.save_botlist_to_file(results)
		elif response =='2':
			configserver.set_bt()
		elif response == '3':
			bot = botsellector.get_mh_bot(haasomeClient)
			botlistfile = BotDB.return_botlist_file()
			bots = BotDB.load_botlist(botlistfile)
			history.plot_bots(bots)
			makebots(bot, haasomeClient,botType, roilist)

		elif response == '4':
			bot = botsellector.get_mh_bot(haasomeClient)
		else:
			pass


def main():
	configserver.set_bt()
	bot = botsellector.get_mh_bot(haasomeClient)
	botlistfile = BotDB.return_botlist_file()
	configs = BotDB.load_botlist(botlistfile)
	# print(configs[:10])
	results = bt_bot_configs(bot, configs,haasomeClient)
	


if __name__ == '__main__':
	intro()