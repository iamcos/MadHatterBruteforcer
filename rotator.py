# from licensing.models import *
# from licensing.methods import Key, Helpers
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
import configparser_cos as cp
import configparser
import operator
from decimal import Decimal
import time
from inspect import getmembers

import os
def getch():
	if os.name == 'nt':
		import msvcrt
		def getch():
			return msvcrt.getch().decode()
	else:
		import sys, tty, termios
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		def getch():
			try:
				tty.setraw(sys.stdin.fileno())
				ch = sys.stdin.read(1)
			finally:
				termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
			return ch

char = getch.getch()
print('Keyboard shortcunts: \n for selecting Bollinger bands\n w:bbl e:bbup )
if (char =="q"):
	print('bbands l selected')
	indicator = 	[EnumMadHatterIndicators.BBANDS, 0]
	print('SET selected: ', setbbl.errorCode, setbbl.errorMessage)

	elif (char == "w"):
		print('bbands devup selected')
		indicator = 	[EnumMadHatterIndicators.BBANDS, 1]

	elif (char == "e"):
		print('bbands devdn selected')
		indicator = [EnumMadHatterIndicators.BBANDS, 2]

	elif (char == "a"):
		print('RSI l selected')
		indicator = [EnumMadHatterIndicators.RSI, 0]

	elif (char == "s"):
			print('RSI Buy selected')
		indicator = [EnumMadHatterIndicators.RSI, 1]
	elif (char == "s"):
			print('RSI Sell selected')
		indicator = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
		currentBotGuid, EnumMadHatterIndicators.RSI, 2, newparam)
	elif (char == "z"):
			print('MACD Fast selected')
		indicator = 	haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
		currentBotGuid, EnumMadHatterIndicators.MACD, 0, MACDFast)
	elif (char == "x"):
		print('MACD Slow selected')
		indicator = 	haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
	currentBotGuid, EnumMadHatterIndicators.MACD, 1, MACDFast)
		elif (char == "c"):
				print('MACD Signal selected')
			indicator = 	haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
		currentBotGuid, EnumMadHatterIndicators.MACD, 2, MACDFast)
		
		
	elif (not char):
					print("No char")
	elif (char == "a"):
					print("Left pressed")
					time.sleep(button_delay)

	

	elif (char == "w"):
					print("Up pressed")
					time.sleep(button_delay)

	elif (char == "s"):
					print("Down pressed")
					time.sleep(button_delay)

	elif (char == "1"):
					print("Number 1 pressed")
					time.sleep(button_delay)



# import only system from os 
from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 
  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
try:
		input = raw_input
except NameError:
		pass


class madHatter:

		def __init__(self):
				self

		def setrsi(buy, length, sell):

				buy = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						currentBotGuid, EnumMadHatterIndicators.RSI, 1, buy)

				length = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						currentBotGuid, EnumMadHatterIndicators.RSI, 0, length)

				sell = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						currentBotGuid, EnumMadHatterIndicators.RSI, 2, sell)

def configuremhsafety(currentBotGuid, sellStep, buyStep, stopLoss):
	sellStep == 0
	buyStep == 0
	sellStep = haasomeClient.customBotApi.set_mad_hatter_safety_parameter(
			currentBotGuid, EnumMadHatterSafeties.PRICE_CHANGE_TO_SELL, sellStep)
	buyStep = haasomeClient.customBotApi.set_mad_hatter_safety_parameter(
			currentBotGuid, EnumMadHatterSafeties.PRICE_CHANGE_TO_BUY, buyStep)
	stopLoss = haasomeClient.customBotApi.set_mad_hatter_safety_parameter(
			currentBotGuid, EnumMadHatterSafeties.STOP_LOSS, stopLoss)

def configuremh(currentBotGuid, bbLength, bbDevUp, bbDevDown, bbMAType, fcc, rm, mms, RSILength, RSIBuy, RSISell, MACDSlow, MACDFast, MACDSignal):
	
				bbLength = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						currentBotGuid, EnumMadHatterIndicators.BBANDS, 0, bbLength)

				bbDevUp = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						currentBotGuid, EnumMadHatterIndicators.BBANDS, 1, bbDevUp)

				bbDevDown = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						currentBotGuid, EnumMadHatterIndicators.BBANDS, 2, bbDevDown)

				bbMAType = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						currentBotGuid, EnumMadHatterIndicators.BBANDS, 3, bbMAType)

				RSILength = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						currentBotGuid, EnumMadHatterIndicators.RSI, 0, RSILength)

				RSIBuy = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						currentBotGuid, EnumMadHatterIndicators.RSI, 1, RSIBuy)

				RSSell = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						currentBotGuid, EnumMadHatterIndicators.RSI, 2, RSISell)

				MACDFast = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						currentBotGuid, EnumMadHatterIndicators.MACD, 0, MACDFast)

				MACDSlow = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						currentBotGuid, EnumMadHatterIndicators.MACD, 1, MACDSlow)
				MACDSignal = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						currentBotGuid, EnumMadHatterIndicators.MACD, 2, MACDSignal)

				fcc = fcc
				if fcc == 1:
						fcc = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
								currentBotGuid, EnumMadHatterIndicators.BBANDS, 5, True)
				elif fcc == 0:
						fcc = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
								currentBotGuid, EnumMadHatterIndicators.BBANDS, 5, false)
				else:
						fcc = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
								currentBotGuid, EnumMadHatterIndicators.BBANDS, 5, fcc)

				rm = rm
				if rm == 1:
						rm = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
								currentBotGuid, EnumMadHatterIndicators.BBANDS, 6, True)
				elif rm == 0:
						rm = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
								currentBotGuid, EnumMadHatterIndicators.BBANDS, 6, False)
				else:
						rm = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
								currentBotGuid, EnumMadHatterIndicators.BBANDS, 6, rm)

				mms = mms
				if mms == 1:
						mms = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
								currentBotGuid, EnumMadHatterIndicators.BBANDS, 7, True)
				elif mms == 0:
						mms = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
								currentBotGuid, EnumMadHatterIndicators.BBANDS, 7, false)
				else:
						mms = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
								currentBotGuid, EnumMadHatterIndicators.BBANDS, 7, mms)
				return currentBotGuid

def botsellector():
	allbots = haasomeClient.customBotApi.get_all_custom_bots().result
	for i, x in enumerate(allbots):
			print(i, x.name)
	botnum = input(
			'Type bot number to use from the list above and hit return. \n Your answer: ')
	botnumobj = allbots[int(botnum)]
	print(botnumobj.name +'is selected!')
	return botnumobj

def bottimeinterval():
	timeintervals = {'1 minutes':1,'2 minutes':2,'3 minutes':3,'4 minutes':4,'5 minutes':5,'6 minutes':6,'10 minutes':10,'12 minutes':12,'15 minutes':15,'20 minutes':20,'30 minutes':30,'45 minutes':45,'1 hour':60,'1.5 hours':90,'2 hours':120,'2.5 hours':150,'3 hours':180,'4 hours':240,'6 hours':360,'12 hours':720,'1 day':1440,'2 days':2880}
	print('Available time intervals for current bot are:')
	timeintext = list(timeintervals.keys())

	for i, k in enumerate(timeintext):
		print(i, k)
	userinput = input('type interval number to select it: ')
	selected = timeintext[int(userinput)]
	selectedintervalinminutes = timeintervals[selected]
	print(selected, 'set as time interval')
	return selectedintervalinminutes


def minutestobacktest():
		intervals = {'1H': 60, '2H': 120, '3H': 180, '4H': 240, '5H': 300, '6H': 360, '7H': 420, '8H': 480, '9H': 540, '10H': 600, '11H': 660, '12H': 720, '13H': 780, '14H': 840, '15H': 900, '16H': 960, '17H': 1020, '18H': 1080, '19H': 1140, '20H': 1200, '21H': 1260, '22H': 1320, '23H': 1380, '24H': 1440, '1D': 1440, '2D': 2880, '3D': 4320, '4D': 5760, '5D': 7200,
									'6D': 8640, '7D': 10080, '8D': 11520, '9D': 12960, '10D': 14400, '11D': 15840, '12D': 17280, '13D': 18720, '14D': 20160, '15D': 21600, '16D': 23040, '17D': 24480, '18D': 25920, '19D': 27360, '20D': 28800, '21D': 30240, '22D': 31680, '23D': 33120, '24D': 34560, '25D': 36000, '26D': 37440, '27D': 38880, '28D': 40320, '29D': 41760, '30D': 43200}
		user_resp = input(
				'Define backtesting interval: 1H-24H for hours, 1D-30D for days. \n Your answer: ')
		try:
			interval = intervals[user_resp]
		except KeyError:
			user_resp = input('Please re-enter your chouse exactly as 1H for 1 hour, 5D for 5 days and so on and hit return again \n Your answer: ')
			interval = intervals[user_resp]
		print('Backtesting interval is set to', user_resp,
					'which is exactly ', interval, 'minutes')
		return interval

configroi = list()
btresults = {}
prevroi = 0

templateguid = "LOCKEDLIMITORDERGUID"

# def backtest():
# 		backtestfor = minutestobacktest()
# 		bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountGuid, currentBotGuid,backtestfor, primarycurrency, secondarycurrency, contractname).result
# 		roi = bt.roi
# 		print(roi,'%',primarycurrency+'/'+secondarycurrency)
# 		return roi
# # def seq(currentsl, step):
# 	startsl = currentsl-1
# 	endsl = currentsl+1
# 	step = step
# 	n = int(round((endsl - startsl)/Decimal(step)))
#     if n > 1:
#         return([startsl + step*i for i in range(n+1)])
#     elif n == 1:
#         return([startsl])
#     else:
#         return([])



configs=[['27', '2', '2', '8', 'False', 'False', 'False', '17', '42', '72', '6', '81', '12'], ['21', '2', '2', '0', 'False', 'False', 'False', '34', '12', '71', '500', '100', '16'], ['7', '2', '2', '6', 'False', 'False', 'False', '18', '40', '51', '7', '23', '18'], ['71', '1', '1', 'D1', 'False', 'False', 'False', '46', '46', '69', '12', '61', '10'], ['23', '1', '1', '7', 'False', 'False', 'False', '33', '40', '56', '12', '26', '2'], ['5', '2', '2', '7', 'False', 'False', 'False', '9', '37', '70', '12', '24', '9'], ['25', '1', '1', '0', 'False', 'False', 'False', '19', '31', '62', '10', '398', '116'], ['18', '2.5', '1', '8', 'True', 'False', 'False', '4', '41', '70', '24', '52', '12'], ['21', '2.9', '1', '7', 'False', 'False', 'False', '2', '31', '80', '20', '40', '2'], ['21', '1', '1', '1', 'False', 'False', 'False', '12', '27', '69', '20', '120', '12'], ['15', '2.4', '1.1', '0', 'False', 'True', 'False', '7', '32', '75', '12', '24', '11'], ['20', '1', '1', '6', 'False', 'False', 'False', '4', '31', '61', '20', '40', '2'], ['33', '1', '1.3', '6', 'False', 'False', 'False', '26', '31', '54', '6', '81', '2'], ['34', '1.8', '1.5', '2', 'False', 'False', 'False', '24', '40', '64', '50', '100', '21'], ['19', '2.5', '0.9', '8', 'True', 'False', 'False', '5', '40', '81', '24', '52', '11'], ['10', '2.05', '0.3', '0', 'False', 'False', 'False', '5', '21', '81', '20', '120', '4'], ['18', '2', '1', '8', 'False', 'False', 'True', '4', '41', '81', '120', '12', '2'], ['35', '0.93', '1.57', 'D1', 'False', 'False', 'False', '16', '46', '69', '53', '41', '38'], ['25', '2.4', '1.6', '0', 'False', 'False', 'False', '12', '31', '69', '12', '30', '8'], ['7', '1.2', '1.3', '7', 'False', 'False', 'False', '6', '25', '81', '40', '159', '2'], ['22', '2.2', '2.1', '6', 'False', 'False', 'False', '18', '44', '61', '50', '100', '11'], ['18', '1.4', '1.9', '0', 'False', 'False', 'False', '3', '25', '55', '16', '23', '1'], ['21', '2.6', '2.2', '1', 'False', 'False', 'False', '9', '21', '81', '3', '8', '12'], ['21', '1', '1.1', '0', 'False', 'False', 'False', '30', '42', '61', '20', '40', '2'], ['2', '1', '1', '5', 'False', 'False', 'False', '5', '31', '71', '20', '40', '12'], ['3', '1', '1', 'T1', 'False', 'False', 'False', '21', '33', '69', '20', '100', '2'], ['19', '1.1', '1.5', '2', 'False', 'False', 'False', '8', '35', '73', '20', '40', '11'], ['10', '2', '1', '0', 'False', 'False', 'False', '9', '31', '79', '20', '80', '2'], ['17', '2', '2', '5', 'False', 'False', 'False', '8', '34', '64', '50', '120', '12'], ['21', '2.5', '1.5', '0', 'True', 'False', 'False', '6', '31', '77', '12', '26', '10'], ['56', '1.8', '1.8', '7', 'False', 'False', 'False', '61', '35', '63', '12', '117', '12'], ['21', '2.5', '1.172', '0', 'True', 'False', 'True', '6', '34', '76', '2', '40', '2'], ['12', '1', '1', '7', 'False', 'False', 'False', '15', '36', '62', '5', '55', '2'], ['3', '1.3', '0.5', '8', 'False', 'False', 'False', '5', '32', '67', '33', '66', '9'], ['10', '1.5', '1', '7', 'False', 'False', 'False', '10', '32', '77', '12', '26', '9'], ['21', '1', '1', '7', 'False', 'False', 'True', '21', '43', '56', '30', '60', '3'], ['10', '2', '2', '5', 'False', 'False', 'False', '2', '41', '55', '20', '40', '122'], ['20', '1', '1', '0', 'False', 'False', 'False', '4', '41', '71', '7', '23', '18'], ['7', '2.4', '1.57', '0', 'False', 'False', 'False', '6', '32', '77', '12', '26', '9'], ['51', '21', '1', '0', 'False', 'False', 'False', '2', '41', '51', '20', '40', '2'], ['53', '1.1', '0.9', 'D1', 'False', 'False', 'False', '14', '41', '71', '22', '24', '2'], ['45', '1', '1', '7', 'False', 'False', 'False', '9', '49', '81', '10', '52', '2'], ['12', '1', '1', '7', 'True', 'True', 'False', '21', '41', '65', '12', '26', '12'], ['21', '1', '1', '0', 'False', 'False', 'False', '40', '48', '51', '12', '24', '8'], ['30', '2', '1.3', '0', 'True', 'False', 'False', '4', '45', '78', '20', '80', '2'], ['2', '2', '2', '8', 'False', 'False', 'False', '10', '31', '64', '4', '8', '2'], ['18', '2.5', '1', '8', 'True', 'False', 'False', '3', '11', '65', '55', '180', '16'], ['19', '1.3', '1.8', '0', 'False', 'False', 'False', '18', '35', '61', '7', '23', '18'], ['65', '2.719', '2', '8', 'True', 'False', 'False', '5', '41', '78', '24', '52', '12'], ['14', '2', '2', '1', 'False', 'False', 'False', '6', '25', '66', '7', '49', '2'], ['53', '1.1', '0.92', 'D1', 'False', 'False', 'False', '12', '43', '71', '22', '26', '2'], ['20', '2.7', '2', '2', 'True', 'False', 'False', '5', '25', '77', '5', '10', '2'], ['29', '2.18', '2.79', '2', 'False', 'False', 'False', '41', '38', '70', '17', '41', '44'], ['26', '3.1', '2.06', 'D1', 'False', 'False', 'False', '15', '26', '58', '27', '56', '5'], ['20', '1.59', '0.77', '2', 'False', 'False', 'False', '6', '38', '81', '54', '56', '10'], ['31', '0.7', '0.7', '8', 'False', 'False', 'False', '7', '37', '67', '44', '81', '8'], ['41', '2', '1', '0', 'False', 'False', 'False', '10', '31', '64', '4', '8', '2']]


def doallpairs():
	
	backtestfor = minutestobacktest()
	pairslist = []
	# contractnamelist = []
	results = list()
	for i,v  in enumerate(allpairs):
		pairslist.append([v.secondaryCurrency, v.contractName, v.tradeFee, v.minimumTradeAmount])
		#safeHistoryGet(MarketEnum, v.primaryCurrency, v.secondaryCurrency, v.contractName, 4,backtestfor)
		backtest = haasomeClient.customBotApi.backtest_custom_bot_on_market(
					accountGuid, currentBotGuid,backtestfor, v.primaryCurrency, v.secondaryCurrency, v.contractName).result
		roi = backtest.roi
		results.append([roi, pairslist])
		print(roi, v.primaryCurrency, v.secondaryCurrency)
	
	# resultssorted = sorted(results, key=lambda x: x[0], reverse=False)
	
		str(secondarycurrency)


botType = EnumCustomBotType.MAD_HATTER_BOT
cp.verifyconfigfile()
ip, secret, threshold = cp.connectiondata()


haasomeClient = HaasomeClient(ip, secret)

botnumobj = botsellector()
pricemarket = botnumobj.priceMarket
accountGuid = botnumobj.accountId
currentBotGuid = botnumobj.guid
currentBotname = botnumobj.name
MarketEnum = pricemarket.priceSource
primarycurrency = pricemarket.primaryCurrency
secondarycurrency = pricemarket.secondaryCurrency
contractname = pricemarket.contractName
try:
	leverage = botnumobj.Leverage
except:
	leverage = Decimal(0.0)



def backtestingfrommemory(currentBotGuid):
	baseconfig = haasomeClient.customBotApi.get_custom_bot(currentBotGuid, EnumCustomBotType.BASE_CUSTOM_BOT).result
	settingsprev = []
	settingsstats = []
	backtestfor = minutestobacktest()
	print('Downloading backtsting history... Expect results anytime soon')
	for i, v in enumerate(configs):
		bot = configuremh(currentBotGuid,configs[i][0], configs[i][1], configs[i][2], configs[i][3], configs[i][4], configs[i][5],configs[i][6], configs[i][7], configs[i][8], configs[i][9], configs[i][10], configs[i][11], configs[i][12])
		configuremhsafety(currentBotGuid, 0, 0, 0)
		backtest = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountGuid, currentBotGuid, backtestfor, primarycurrency, secondarycurrency, contractname).result
		roi = backtest.roi
		prevroi = roi
		settings = configs[i][0], configs[i][1], configs[i][2], configs[i][3], configs[i][4], configs[i][5],configs[i][6], configs[i][7], configs[i][8], configs[i][9], configs[i][10], configs[i][11], configs[i][12]
		configroi.append([configs[i][0], configs[i][1], configs[i][2], configs[i][3], configs[i][4], configs[i][5],	configs[i][6], configs[i][7], configs[i][8], configs[i][9], configs[i][10], configs[i][11], configs[i][12], roi])
		settingsprev = settings
		print('ROI:', roi, 'Bot configuration :', configs[i][0], configs[i][1], configs[i][2], configs[i][3], configs[i][4], configs[i][5],configs[i][6], configs[i][7], configs[i][8], configs[i][9], configs[i][10], configs[i][11], configs[i][12])
		btresults[roi] = settings
		botconfig = haasomeClient.customBotApi.get_custom_bot(currentBotGuid, EnumCustomBotType.MAD_HATTER_BOT).result
		botorders = botconfig.completedOrders
	with open('btresults.csv', 'w', ) as csvfile:
		fieldnames = ['price','ammountFilled', 'unixAddedTime']
		csvwriter = csv.DictWriter(csvfile,fieldnames=fieldnames)
		csvwriter.writeheader()
		for i, v in enumerate(botorders):
			csvwriter.writerow({'price': v.price, 'ammountFilled':v.amountFilled,'unixAddedTime':v.unixAddedTime})
	filename = primarycurrency+'/'+secondarycurrency+'.csv'
	with open(filename, 'wb', newline='') as csvfile:
		fieldnames = ['n', 'bbLength', 'bbDevUp', 'bbDevDown', 'bbMAType', 'fcc', 'rm', 'mms', 'RSILength', 'RSIBuy', 'RSISell', 'MACDSlow', 'MACDFast', 'MACDSignal', 'roi']
		csvwriter = csv.DictWriter(csvfile,fieldnames=fieldnames)
		csvwriter.writeheader()
		for i, v in enumerate(configroi):
			csvwriter.writerow({'n': i ,'bbLength':configroi[i][0], 'bbDevUp':configroi[i][1], 'bbDevDown':configroi[i][2],'bbMAType':configroi[i][3], 'fcc':configroi[i][4], 'rm':configroi[i][5], 'mms':configroi[i][6], 'RSILength':configroi[i][7], 'RSIBuy':configroi[i][8],'RSISell':configroi[i][9], 'MACDSlow':configroi[i][10],'MACDFast':configroi[i][11], 'MACDSignal':configroi[i][12], 'roi':roi})

	configroiorted = sorted(configroi, key=lambda x: x[13], reverse=False)
	for i,v in enumerate(configroiorted):
		print(i, 'ROI: ', v[13])
	botstocreate = int(input('Type number of how any bots yo would like to create?'))
	for bots in range(0,botstocreate):
		i = int(input('Type bot number to create'))
		botname = str(primarycurrency) + str(' / ') + \
		str(secondarycurrency) + str(' Roi ') + str(configroiorted[i][13])
		newbot = haasomeClient.customBotApi.new_custom_bot(accountGuid, botType, botname, primarycurrency, secondarycurrency, contractname).result
		print('newbot guuid', newbot.guid)
		currentBotGuid = newbot.guid
		setup_newbot = configuremh(currentBotGuid,configroiorted[i][0], configroiorted[i][1], configroiorted[i][2], configroiorted[i][3], configroiorted[i][4], configroiorted[i][5], configroiorted[i][6], configroiorted[i][7], configroiorted[i][8], configroiorted[i][9], configroiorted[i][10], configroiorted[i][11], configroiorted[i][12])
		configuremhsafety(currentBotGuid, 0, 0, 0)
		print(botname, 'has been created')

import datetime
def findbtperiod():
	backtestfor = minutestobacktest()
	history = safeHistoryGet(MarketEnum, primarycurrency, secondarycurrency, "", 1,backtestfor*2)
	candles = history.result
	percentagetocheck = int(50)
	print(len(candles))
	timeframeinminutes = int(interval)
	percentagetocheckstep = int(5)

	percentageUpDownFinal = int((int(percentagetocheck)/100 * int(timeframeinminutes)))

	candlesToCheck = []

	highestCandleFromTestRange = None
	lowestCandleFromTestRange = None

	# Get the candles to check
	print("Calculating candles to test for best start time")

	for x in range(int(percentageUpDownFinal)+1):
					if x == 0:
									candlesToCheck.append(candles[timeframeinminutes])
					else:
									candlesToCheck.append(candles[timeframeinminutes-x])
									candlesToCheck.append(candles[timeframeinminutes+x])

	highestCandleFromTestRange = candlesToCheck[0]
	lowestCandleFromTestRange = candlesToCheck[0]

	for candle in candlesToCheck:
					if candle.close > highestCandleFromTestRange.close:
									highestCandleFromTestRange = candle

					if candle.close < lowestCandleFromTestRange.close:
									lowestCandleFromTestRange = candle

	print("Lowest Candle Price Found: " + str(lowestCandleFromTestRange.close))
	print("Highest Candle Price Found: " + str(highestCandleFromTestRange.close))

	stepCandleAmount = int(5/100 * percentageUpDownFinal)

	sortedCandles = sorted(candlesToCheck, key=operator.attrgetter('close'))

	tasks = {}
	botResults = {}
	for x in range (5):

					newBacktestLength = int((datetime.datetime.utcnow() - sortedCandles[stepCandleAmount*x].timeStamp).total_seconds() / 60) 
					task = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountGuid, currentBotGuid, newBacktestLength, primarycurrency, secondarycurrency, contractname).result
					roi = task.roi

					tasks[newBacktestLength] = roi

	while len(botResults) != len(tasks):
					for k, v in tasks.items():
									result = v
									if result != None:
													botResults[k] = result
	print('')
	print("Tested coin pair: " + primarycurrency + "/" + secondarycurrency)
	print("Ran with the following settings")
	print("Percentage To Check: " + str(percentagetocheck))
	print("Percentage To Step " + str(percentagetocheckstep))
	print('')
	bestSettings = list(botResults.values())[0]
	bestLength = list(botResults.keys())[0]

	for k,v in botResults.items():
				if v > bestSettings:
								bestSettings = v
								bestLength = k

				print("Result Length:" + str(k) + " Settings:" + str(v))

	print('')
	print("Smart scalper task finished")
	return "HPRV: " + str(lowestCandleFromTestRange.close) + " LPRV:" + str(highestCandleFromTestRange.close) + " CL:" + str(bestLength) + " BSP:" + str(candles[bestLength].close) + " Settings: " + str(bestSettings)



def safeHistoryGet(pricesource: EnumPriceSource, primarycoin: str, secondarycoin: str, contractname: str,backtestfor: int, depth: int):
				history = None
				historyResult = False
				failCount = 0

				while historyResult == False:
								history = haasomeClient.marketDataApi.get_history(pricesource, primarycoin, secondarycoin, contractname,backtestfor, depth)
								if len(history.result) > 1:
												historyResult = True
								else:
												failCount = failCount + 1
												time.sleep(1)

								if failCount == 10:
												historyResult = True


				return history

def getmhindicators(currentBotGuid):
		basebotconfig = haasomeClient.customBotApi.get_custom_bot(currentBotGuid, EnumCustomBotType.BASE_CUSTOM_BOT).result
		indicators = basebotconfig.bBands['Length'], basebotconfig.bBands['Devup'],basebotconfig.bBands['Devdn'],basebotconfig.bBands['MaType'],basebotconfig.bBands['Deviation'],basebotconfig.bBands['ResetMid'],basebotconfig.bBands['AllowMidSell'],basebotconfig.bBands['RequireFcc'],basebotconfig.rsi['RsiLength'], basebotconfig.rsi['RsiOversold'], basebotconfig.rsi['RsiOverbought'], basebotconfig.macd['MacdSlow'],basebotconfig.macd['MacdFast'], basebotconfig.macd['MacdSign']
		return indicators
		print(indicators)


def getbasebotconfig(currentBotGuid):
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(currentBotGuid, EnumCustomBotType.BASE_CUSTOM_BOT).result

			botname = basebotconfig.name
			pricemarket = basebotconfig.priceMarket
			primarycoin = pricemarket.primaryCurrency
			secondarycoin = pricemarket.secondaryCurrency
			fee = basebotconfig.currentFeePercentage
			tradeamount = basebotconfig.currentTradeAmount
			ammounttype = basebotconfig.amountType
			coinposition = basebotconfig.coinPosition
			consensus = basebotconfig.useTwoSignals
			customtemplate= basebotconfig.customTemplate
			icc = basebotconfig.includeIncompleteInterval
			mappedbuysignal = basebotconfig.mappedBuySignal
			mappedsellsignal = basebotconfig.mappedSellSignal
			sldisable = basebotconfig.disableAfterStopLoss
			leverage = basebotconfig.leverage

			return botname, primarycoin, secondarycoin, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, icc, mappedbuysignal, mappedsellsignal, leverage


def settimeinterval(currentBotGuid, timeinterval):
	
	timeintervals = [['1 minutes',1],['2 minutes',2],['3 minutes',3],['4 minutes',4],['5 minutes',5],['6 minutes',6],['10 minutes',10],['12 minutes',12],['15 minutes',15],['20 minutes',20],['30 minutes',30],['45 minutes',45],['1 hour',60],['1.5 hours',90],['2 hours',120],['2.5 hours',150],['3 hours',180],['4 hours',240],['6 hours',360],['12 hours',720],['1440 day',1440],['2880 days',2880]]
	basebotconfig = haasomeClient.customBotApi.get_custom_bot(currentBotGuid, EnumCustomBotType.BASE_CUSTOM_BOT).result
	initialinterval = basebotconfig.interval
	pricemarket = basebotconfig.priceMarket
	contractname = pricemarket.contractName
	timeinterval = basebotconfig.interval

	timeintervalnum = ''
	for i,k  in enumerate(timeintervals):
		if k[1] == timeinterval:
			timeintervalnum = i
	selectedinterval = timeintervals[timeintervalnum][0]

	botname, primarycoin, secondarycoin, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, icc, mappedbuysignal, mappedsellsignal, leverage = getbasebotconfig(currentBotGuid)
	configbot = haasomeClient.customBotApi.setup_mad_hatter_bot(accountGuid, currentBotGuid, botname, primarycoin, secondarycoin, customtemplate, contractname, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, timeinterval, icc, mappedbuysignal, mappedsellsignal, float(leverage))
	# print('settimeinterval: ', configurebot.errorCode, configurebot.errorMessage)



def bttimeintervals(currentBotGuid, accountGuid):
	timeintervals = (['1 minutes',1],['2 minutes',2],['3 minutes',3],['4 minutes',4],['5 minutes',5],['6 minutes',6],['10 minutes',10],['12 minutes',12],['15 minutes',15],['20 minutes',20],['30 minutes',30],['45 minutes',45],['1 hour',60],['1.5 hours',90],['2 hours',120],['2.5 hours',150],['3 hours',180],['4 hours',240],['6 hours',360],['12 hours',720],['1 day',1440],['2 days',2880])
	# print('Available time intervals for current bot are:')
	
	basebotconfig = haasomeClient.customBotApi.get_custom_bot(currentBotGuid, EnumCustomBotType.BASE_CUSTOM_BOT).result
	botname, primary
	coin, secondarycoin, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, icc, mappedbuysignal, mappedsellsignal, leverage = getbasebotconfig(currentBotGuid)
	initialinterval = basebotconfig.interval
	pricemarket = basebotconfig.priceMarket
	contractname = pricemarket.contractName
	timeinterval = basebotconfig.interval
	backtestfor = minutestobacktest()
	
	btresults = []
	for l in range(0,26):
		print(timeintervals[l][1])
		configbot = haasomeClient.customBotApi.setup_mad_hatter_bot(basebotconfig.accountId, basebotconfig.guid, botname, primarycoin, secondarycoin, customtemplate, contractname, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, timeintervals[l][1], icc, mappedbuysignal, mappedsellsignal, float(leverage))
		print('configurebot', configbot.errorCode, configbot.errorMessage)
		bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId,basebotconfig.guid,backtestfor, primarycoin, secondarycoin, ' ')
		btr = bt.result
		# btresults.append([btr.roi,k[0],k[1]])
	# tresultssorted = sorted(btresults, key=lambda x: x[0], reverse=True)
	# print(btresultssorted[0][1],'gives best roi of: ',btresultssorted[0][0])
	# userinput = input('would you like to set it? y/n \n Your answer: ')
	# for i, k in enumerate(timeintervals):
	# 	selectedinterval = int(k[1])
	# 	configbot = haasomeClient.customBotApi.setup_mad_hatter_bot(basebotconfig.accountId, basebotconfig.guid, botname, primarycoin, secondarycoin, customtemplate, ' ', coinposition, fee, ammounttype, tradeamount, consensus, sldisable, selectedinterval, icc, mappedbuysignal, mappedsellsignal, float(leverage))
	# 	print('configurebot', configbot.errorCode, configbot.errorMessage)
	# 	bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId,basebotconfig.guid,backtestfor, primarycoin, secondarycoin, ' ')
	# 	btr = bt.result
	# 	print('backtest:' , bt.errorCode, bt.errorMessage)
	# 	print(btr.roi,'for timeInterval: ', k[0])
	# 	btresults.append([btr.roi,k[0],k[1]])
	# btresultssorted = sorted(btresults, key=lambda x: x[0], reverse=True)
	# print(btresultssorted[0][1],'gives best roi of: ',btresultssorted[0][0])
	# userinput = input('would you like to set it? y/n \n Your answer: ')
	# if userinput == 'y':
	# 	configurebot = settimeinterval(currentBotGuid, btresultssorted[0][2])
	# 	print(btresultssorted[0][1], 'time interval has been set!')
	# if userinput == 'n':
	# 	configurebot = settimeinterval(currentBotGuid, initialinterval)
	# 	print(initialinterval, 'time interval has been restored!')

def bbtbbdev(currentBotGuid):
	currentconfig = getmhindicators(currentBotGuid)
	basebotconfig = haasomeClient.customBotApi.get_custom_bot(currentBotGuid, EnumCustomBotType.BASE_CUSTOM_BOT).result
	pricemarket = basebotconfig.priceMarket
	contractname = pricemarket.contractName
	timeinterval = basebotconfig.interval
	botname, primarycoin, secondarycoin, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, icc, mappedbuysignal, mappedsellsignal, leverage = getbasebotconfig(currentBotGuid)
	#configurebot = haasomeClient.customBotApi.setup_mad_hatter_bot(accountGuid, currentBotGuid, botname, primarycoin, secondarycoin, contractname, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, timeinterval, icc, mappedbuysignal, mappedsellsignal, leverage)
	#print('configurebot', configurebot.errorCode, configurebot.errorMessage)
	backtestfor = minutestobacktest()

	btresults = []
	devuprange = np.arange(0.7,3.0,0.5)
	devdnrange = np.arange(0.7,3.0,0.5)
	i = 0
	for devup in devuprange:
		i += 1
		print(i, 'up: ',devup)
		setdevup = setbbDevUp(currentBotGuid, devup)
		i += 1
		for devdn in devdnrange:
			i += 1
			print(i, 'down: ', devdn)
			setbbDevDown(currentBotGuid, devdn)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountGuid,currentBotGuid,backtestfor, primarycoin, secondarycoin, contractname)
			btr = bt.result
			print(devup, devdn, btr.roi)
			btresults.append([btr.roi,devup, devdn])
	btresultssorted = sorted(btresults, key=lambda x: x[0], reverse=True)
	for i in range(10):
		print(btresultssorted[i][1], btresultssorted[i][2],'ROI ',btresultssorted[i][0])


def bbtrsil(currentBotGuid):
	currentconfig = getmhindicators(currentBotGuid)
	basebotconfig = haasomeClient.customBotApi.get_custom_bot(currentBotGuid, EnumCustomBotType.BASE_CUSTOM_BOT).result
	pricemarket = basebotconfig.priceMarket
	contractname = pricemarket.contractName
	timeinterval = basebotconfig.interval
	botname, primarycoin, secondarycoin, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, icc, mappedbuysignal, mappedsellsignal, leverage = getbasebotconfig(currentBotGuid)
	#configurebot = haasomeClient.customBotApi.setup_mad_hatter_bot(accountGuid, currentBotGuid, botname, primarycoin, secondarycoin, contractname, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, timeinterval, icc, mappedbuysignal, mappedsellsignal, leverage)
	#print('configurebot', configurebot.errorCode, configurebot.errorMessage)
	btresults = []
	initrsil = currentconfig[8]
	backtestfor = minutestobacktest()
	for l in range(2,21):
		setrsil = setRSILength(currentBotGuid,l)
		bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountGuid,currentBotGuid,backtestfor, primarycoin, secondarycoin, contractname)
		btr = bt.result
		print('backtest:' , bt.errorCode, bt.errorMessage)
		print(l, btr.roi)
		btresults.append([btr.roi,l])
	btresultssorted = sorted(btresults, key=lambda x: x[0], reverse=True)
	print(btresultssorted[0][1],'gives best roi of: ',btresultssorted[0][0])

def bbtrsifinetune(currentBotGuid):
		currentconfig = getmhindicators(currentBotGuid)
		basebotconfig = haasomeClient.customBotApi.get_custom_bot(currentBotGuid, EnumCustomBotType.BASE_CUSTOM_BOT).result
		pricemarket = basebotconfig.priceMarket
		contractname = pricemarket.contractName
		timeinterval = basebotconfig.interval
		botname, primarycoin, secondarycoin, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, icc, mappedbuysignal, mappedsellsignal, leverage = getbasebotconfig(currentBotGuid)
		#configurebot = haasomeClient.customBotApi.setup_mad_hatter_bot(accountGuid, currentBotGuid, botname, primarycoin, secondarycoin, contractname, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, timeinterval, icc, mappedbuysignal, mappedsellsignal, leverage)
		#print('configurebot', configurebot.errorCode, configurebot.errorMessage)
		btresults = []
		initrsil = currentconfig[8]
		newrsil =  initrsil
		backtestfor = minutestobacktest()
		for l in range(0,3):
			newrsil  += 1
			setRSILength(currentBotGuid,newrsil)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountGuid,currentBotGuid,backtestfor, primarycoin, secondarycoin, contractname)
			btr = bt.result
			print('backtest:' , bt.errorCode, bt.errorMessage)
			print(newrsil, btr.roi)
			btresults.append([btr.roi,newrsil])
		newrsil =  initrsil
		for l in range(0,3):
			newrsil  -= 1
			setRSILength(currentBotGuid,newrsil)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountGuid,currentBotGuid,backtestfor, primarycoin, secondarycoin, contractname)
			btr = bt.result
			print('backtest:' , bt.errorCode, bt.errorMessage)
			print(newrsil, btr.roi)
			btresults.append([btr.roi,newrsil])
		btresultssorted = sorted(btresults, key=lambda x: x[0], reverse=True)
		print(btresultssorted[0][1],'gives best roi of: ',btresultssorted[0][0])

def bbtbbl(currentBotGuid):
	currentconfig = getmhindicators(currentBotGuid)
	basebotconfig = haasomeClient.customBotApi.get_custom_bot(currentBotGuid, EnumCustomBotType.BASE_CUSTOM_BOT).result
	pricemarket = basebotconfig.priceMarket
	contractname = pricemarket.contractName
	timeinterval = basebotconfig.interval
	botname, primarycoin, secondarycoin, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, icc, mappedbuysignal, mappedsellsignal, leverage = getbasebotconfig(currentBotGuid)
	#configurebot = haasomeClient.customBotApi.setup_mad_hatter_bot(accountGuid, currentBotGuid, botname, primarycoin, secondarycoin, contractname, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, timeinterval, icc, mappedbuysignal, mappedsellsignal, leverage)
	#print('configurebot', configurebot.errorCode, configurebot.errorMessage)
	btresults = []
	initbbl = currentconfig[0]
	backtestfor = minutestobacktest()
	for l in range(5,50):
		setbbl = setbbLength(currentBotGuid,l)
		bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountGuid,currentBotGuid,backtestfor, primarycoin, secondarycoin, contractname)
		btr = bt.result
		print('backtest:' , bt.errorCode, bt.errorMessage)
		print(l, btr.roi)
		btresults.append([btr.roi,l])
	btresultssorted = sorted(btresults, key=lambda x: x[0], reverse=True)
	print(btresultssorted[0][1],'gives best roi of: ',btresultssorted[0][0])
	


def steptimeinterval(currentBotGuid, accountGuid):
	timeintervals = [['1 minutes',1],['2 minutes',2],['3 minutes',3],['4 minutes',4],['5 minutes',5],['6 minutes',6],['10 minutes',10],['12 minutes',12],['15 minutes',15],['20 minutes',20],['30 minutes',30],['45 minutes',45],['1 hour',60],['1.5 hours',90],['2 hours',120],['2.5 hours',150],['3 hours',180],['4 hours',240],['6 hours',360],['12 hours',720],['1 day',1440],['2 days',2880]]
	# print('Available time intervals for current bot are:')
	if (char == None):
		print('current timeinterval is set to: ', timeinterval)
	basebotconfig = haasomeClient.customBotApi.get_custom_bot(currentBotGuid, EnumCustomBotType.BASE_CUSTOM_BOT).result
	
	timeinterval = basebotconfig.interval
	timeintervalnum = ''
	for i,k  in enumerate(timeintervals):
		if k[1] == timeinterval:
			print(i,k[0],'textline')
			timeintervalnum = i
	selectedinterval = timeintervals[timeintervalnum][1]
	selectedintervaltext = timeintervals[timeintervalnum][0]
	backtestfor = minutestobacktest()
	
	char = getch()
	if (char =="u"):
		print('increasing value')
		configurebot = settimeinterval(currentBotGuid, selectedinterval)
		bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountGuid,currentBotGuid,backtestfor, pricemarket.primaryCurrency, pricemarket.secondaryCurrency, '')
		btr = bt.result
		timeintervalnum +=1
		selectedinterval = timeintervals[timeintervalnum][1]
		selectedintervaltext = timeintervals[timeintervalnum][0]
		print('backtest:' , bt.errorCode, bt.errorMessage)
		print(btr.roi, selectedintervaltext)
		again = input('type u to increase interval, d to decrease for else\n Your answer: ')
	if (char =="d"):
		configurebot = settimeinterval(currentBotGuid, selectedinterval)
		bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountGuid,currentBotGuid,backtestfor, pricemarket.primaryCurrency, pricemarket.secondaryCurrency, '')
		btr = bt.result
		timeintervalnum -=1
		selectedinterval = timeintervals[timeintervalnum][1]
		selectedintervaltext = timeintervals[timeintervalnum][0]
		print('backtest:' , bt.errorCode, bt.errorMessage)
		print(btr.roi, selectedintervaltext)
		again = input('type u to increase interval, d to decrease')

def writetimeinterval(currentBotGuid):
		basebotconfig = haasomeClient.customBotApi.get_custom_bot(currentBotGuid, EnumCustomBotType.BASE_CUSTOM_BOT).result
		timeinterval = basebotconfig.interval
		print(timeinterval,' is timeinterval')

def main(currentBotGuid):
	user_resp2 = input(
		'What would you like to do with selected bot? \n 1.Find good config.\n 2. Quick bruteforce bollingerbaands length. \n 3.Quick rough bruteforce bollingerbaands deviatios \n 6 bbtrsil')
			#\n4. Interactive time interval backtesting \n 5. Test bot for every time interval \n \n Your answer: 
	if user_resp2 == '1':
		configroiorted = backtestingfrommemory(currentBotGuid
		)
		createbotsfrombtresults()
	elif user_resp2 == '2':
		bbtbbl(currentBotGuid)
	elif user_resp2 == '3':
		bbtbbdev(currentBotGuid)
	elif user_resp2 == '4':
		steptimeinterval(currentBotGuid,accountGuid)
	elif user_resp2 == '5':
		bttimeintervals(currentBotGuid, accountGuid)
	elif user_resp2 == '6':
		bbtrsifinetune(currentBotGuid)	
	elif user_resp2 == '7':
		backtestfor = minutestobacktest()
		timeinterval = input('type time interval number')
		history = haasomeClient.marketDataApi.get_history(MarketEnum, primarycurrency, secondarycurrency, contractname, timeinterval,backtestfor).result
		print(history)
		with open('history.csv', 'w', newline='') as csvfile:
				fieldnames = ['timeStamp','unixTimeStamp','open','highValue','lowValue','close','volume','currentBuyValue','currentSellValue']
				csvwriter = csv.DictWriter(csvfile,fieldnames=fieldnames)
				csvwriter.writeheader()
				for i, v in enumerate(history):
					csvwriter.writerow({'timeStamp': str(v.timeStamp),'unixTimeStamp': str(v.unixTimeStamp), 'open': float(v.open), 'highValue':  float(v.highValue), 'lowValue': float(v.lowValue),'close' : float(v.close),'volume': float(v.volume),'currentBuyValue': str(v.currentBuyValue),'currentSellValue': float(v.currentSellValue)})
# def btbblrange():

def setstopLoss(currentBotGuid, stopLoss):
	haasomeClient.customBotApi.set_mad_hatter_safety_parameter(
			currentBotGuid, EnumMadHatterSafeties.STOP_LOSS, stopLoss)

def setbbLength(currentBotGuid ,bbLength):
	setbbl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
			currentBotGuid, EnumMadHatterIndicators.BBANDS, 0, bbLength)
	print('SET BBL: ', setbbl.errorCode, setbbl.errorMessage)

def setbbDevUp(currentBotGuid,bbDevUp ):
	haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
			currentBotGuid, EnumMadHatterIndicators.BBANDS, 1, bbDevUp)
def setbbDevDown(currentBotGuid, bbDevDown):
	haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
			currentBotGuid, EnumMadHatterIndicators.BBANDS, 2, bbDevDown)

def setbbMAType(currentBotGuid, bbMAType):
	haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
			currentBotGuid, EnumMadHatterIndicators.BBANDS, 3, bbMAType)

def setfcc(currentBotGuid, fcc):
	haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
					currentBotGuid, EnumMadHatterIndicators.BBANDS, 5, fcc)

def setrm(currentBotGuid, rm):
	haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
					currentBotGuid, EnumMadHatterIndicators.BBANDS, 6, rm)

def setmms(currentBotGuid, mms):
	haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
					currentBotGuid, EnumMadHatterIndicators.BBANDS, 7, mms)

def setRSILength(currentBotGuid, RSILength):
	haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
			currentBotGuid, EnumMadHatterIndicators.RSI, 0, RSILength)

def setRSIBuy(currentBotGuid, RSIBuy):
	haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
			currentBotGuid, EnumMadHatterIndicators.RSI, 1, RSIBuy)

def setRSSell(currentBotGuid, RSSell):
	haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
			currentBotGuid, EnumMadHatterIndicators.RSI, 2, RSISell)

def setMACDFast(currentBotGuid, MACDFast):
	haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
			currentBotGuid, EnumMadHatterIndicators.MACD, 0, MACDFast)

def setMACDSlow(currentBotGuid, MACDSlow):
	haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
			currentBotGuid, EnumMadHatterIndicators.MACD, 1, MACDSlow)
def setMACDSignal(currentBotGuid, MACDSignal):
	haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
			currentBotGuid, EnumMadHatterIndicators.MACD, 2, MACDSignal)



main(currentBotGuid)