# from licensing.models import *
# from licensing.methods import Key, Helpers


import threading
import configparser
import csv
import datetime
import fileinput
import json
import multiprocessing
import operator
import os
import re
import sys
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

import botsellector
import configparser_cos
import configserver
import interval

class _Getch:
   """Gets a single character from standard input.  Does not echo to the
screen."""
   def __init__(self):
      try:
        self.impl = _GetchWindows()
      except ImportError:
        self.impl = _GetchUnix()

   def __call__(self): return self.impl()


class _GetchUnix:
   def __init__(self):
      import tty, sys

   def __call__(self):
      import sys, tty, termios
      fd = sys.stdin.fileno()
      old_settings = termios.tcgetattr(fd)
      try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
      finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
      return ch


class _GetchWindows:
   def __init__(self):
      import msvcrt

   def __call__(self):
      import msvcrt
      return msvcrt.getch()

getch = _Getch()

class madHatter:

   def __init__(self):
      self

   def setrsi(buy, length, sell):

      buy = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
        guid, EnumMadHatterIndicators.RSI, 1, buy)

      length = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
        guid, EnumMadHatterIndicators.RSI, 0, length)

      sell = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
        guid, EnumMadHatterIndicators.RSI, 2, sell)

def configuremhsafety(haasomeClient,guid, sellStep, buyStep, stopLoss):
  sellStep == 0
  buyStep == 0
  sellStep = haasomeClient.customBotApi.set_mad_hatter_safety_parameter(
    guid, EnumMadHatterSafeties.PRICE_CHANGE_TO_SELL, sellStep)
  buyStep = haasomeClient.customBotApi.set_mad_hatter_safety_parameter(
    guid, EnumMadHatterSafeties.PRICE_CHANGE_TO_BUY, buyStep)
  stopLoss = haasomeClient.customBotApi.set_mad_hatter_safety_parameter(
    guid, EnumMadHatterSafeties.STOP_LOSS, stopLoss)




def configuremh(haasomeClient,guid, bbLength, bbDevUp, bbDevDown, bbMAType, fcc, rm, mms, RSILength, RSIBuy, RSISell, MACDSlow, MACDFast, MACDSignal):
	

      bbLength = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
        guid, EnumMadHatterIndicators.BBANDS, 0, bbLength)

      bbDevUp = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
        guid, EnumMadHatterIndicators.BBANDS, 1, bbDevUp)

      bbDevDown = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
        guid, EnumMadHatterIndicators.BBANDS, 2, bbDevDown)

      bbMAType = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
        guid, EnumMadHatterIndicators.BBANDS, 3, bbMAType)

      RSILength = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
        guid, EnumMadHatterIndicators.RSI, 0, RSILength)

      RSIBuy = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
        guid, EnumMadHatterIndicators.RSI, 1, RSIBuy)

      RSSell = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
        guid, EnumMadHatterIndicators.RSI, 2, RSISell)

      MACDFast = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
        guid, EnumMadHatterIndicators.MACD, 0, MACDFast)

      MACDSlow = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
        guid, EnumMadHatterIndicators.MACD, 1, MACDSlow)
      MACDSignal = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
        guid, EnumMadHatterIndicators.MACD, 2, MACDSignal)

      fcc = fcc
      if fcc == 1:
        fcc = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
           guid, EnumMadHatterIndicators.BBANDS, 5, True)
      elif fcc == 0:
        fcc = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
           guid, EnumMadHatterIndicators.BBANDS, 5, false)
      else:
        fcc = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
           guid, EnumMadHatterIndicators.BBANDS, 5, fcc)

      rm = rm
      if rm == 1:
        rm = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
           guid, EnumMadHatterIndicators.BBANDS, 6, True)
      elif rm == 0:
        rm = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
           guid, EnumMadHatterIndicators.BBANDS, 6, False)
      else:
        rm = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
           guid, EnumMadHatterIndicators.BBANDS, 6, rm)

      mms = mms
      if mms == 1:
        mms = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
           guid, EnumMadHatterIndicators.BBANDS, 7, True)
      elif mms == 0:
        mms = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
           guid, EnumMadHatterIndicators.BBANDS, 7, false)
      else:
        mms = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
           guid, EnumMadHatterIndicators.BBANDS, 7, mms)



# def minutestobacktest():
#    intervals = {'1H': 60, '2H': 120, '3H': 180, '4H': 240, '5H': 300, '6H': 360, '7H': 420, '8H': 480, '9H': 540, '10H': 600, '11H': 660, '12H': 720, '13H': 780, '14H': 840, '15H': 900, '16H': 960, '17H': 1020, '18H': 1080, '19H': 1140, '20H': 1200, '21H': 1260, '22H': 1320, '23H': 1380, '24H': 1440, '1D': 1440, '2D': 2880, '3D': 4320, '4D': 5760, '5D': 7200, '6D': 8640, '7D': 10080, '8D': 11520, '9D': 12960, '10D': 14400, '11D': 15840, '12D': 17280, '13D': 18720, '14D': 20160, '15D': 21600, '16D': 23040, '17D': 24480, '18D': 25920, '19D': 27360, '20D': 28800, '21D': 30240, '22D': 31680, '23D': 33120, '24D': 34560, '25D': 36000, '26D': 37440, '27D': 38880, '28D': 40320, '29D': 41760, '30D': 43200}
#    user_resp = input(
#       'Define backtesting interval: 1H-24H for hours, 1D-30D for days. \n Your answer: ')
#    try:
#     interval = intervals[user_resp]
#    except KeyError:
#     user_resp = input('Please re-enter your chouse exactly as 1H for 1 hour, 5D for 5 days and so on and hit return again \n Your answer: ')
#     interval = intervals[user_resp]
#    print('Backtesting interval is set to', user_resp,
#        'which is exactly ', interval, 'minutes')
#    return interval

def minutestobacktest():
  try:
    ticks = interval.readinterval()
  except: 
    setbt = configserver.set_bt()
    ticks = interval.readinterval()
    print('BT tie interval is set to: ', ticks)
  return ticks





#configs=[['27', '2', '2', '8', 'False', 'False', 'False', '17', '42', '72', '6', '81', '12'], ['21', '2', '2', '0', 'False', 'False', 'False', '34', '12', '71', '500', '100', '16']]
#configs=[['27', '2', '2', '8', 'False', 'False', 'False', '17', '42', '72', '6', '81', '12'], ['21', '2', '2', '0', 'False', 'False', 'False', '34', '12', '71', '500', '100', '16'], ['7', '2', '2', '6', 'False', 'False', 'False', '18', '40', '51', '7', '23', '18'], ['71', '1', '1', 'D1', 'False', 'False', 'False', '46', '46', '69', '12', '61', '10'], ['23', '1', '1', '7', 'False', 'False', 'False', '33', '40', '56', '12', '26', '2'], ['5', '2', '2', '7', 'False', 'False', 'False', '9', '37', '70', '12', '24', '9'], ['25', '1', '1', '0', 'False', 'False', 'False', '19', '31', '62', '10', '398', '116'], ['18', '2.5', '1', '8', 'True', 'False', 'False', '4', '41', '70', '24', '52', '12'], ['21', '2.9', '1', '7', 'False', 'False', 'False', '2', '31', '80', '20', '40', '2'], ['21', '1', '1', '1', 'False', 'False', 'False', '12', '27', '69', '20', '120', '12'], ['15', '2.4', '1.1', '0', 'False', 'True', 'False', '7', '32', '75', '12', '24', '11'], ['20', '1', '1', '6', 'False', 'False', 'False', '4', '31', '61', '20', '40', '2'], ['33', '1', '1.3', '6', 'False', 'False', 'False', '26', '31', '54', '6', '81', '2'], ['34', '1.8', '1.5', '2', 'False', 'False', 'False', '24', '40', '64', '50', '100', '21'], ['19', '2.5', '0.9', '8', 'True', 'False', 'False', '5', '40', '81', '24', '52', '11'], ['10', '2.05', '0.3', '0', 'False', 'False', 'False', '5', '21', '81', '20', '120', '4'], ['18', '2', '1', '8', 'False', 'False', 'True', '4', '41', '81', '120', '12', '2'], ['35', '0.93', '1.57', 'D1', 'False', 'False', 'False', '16', '46', '69', '53', '41', '38'], ['25', '2.4', '1.6', '0', 'False', 'False', 'False', '12', '31', '69', '12', '30', '8'], ['7', '1.2', '1.3', '7', 'False', 'False', 'False', '6', '25', '81', '40', '159', '2'], ['22', '2.2', '2.1', '6', 'False', 'False', 'False', '18', '44', '61', '50', '100', '11'], ['18', '1.4', '1.9', '0', 'False', 'False', 'False', '3', '25', '55', '16', '23', '1'], ['21', '2.6', '2.2', '1', 'False', 'False', 'False', '9', '21', '81', '3', '8', '12'], ['21', '1', '1.1', '0', 'False', 'False', 'False', '30', '42', '61', '20', '40', '2'], ['2', '1', '1', '5', 'False', 'False', 'False', '5', '31', '71', '20', '40', '12'], ['3', '1', '1', 'T1', 'False', 'False', 'False', '21', '33', '69', '20', '100', '2'], ['19', '1.1', '1.5', '2', 'False', 'False', 'False', '8', '35', '73', '20', '40', '11'], ['10', '2', '1', '0', 'False', 'False', 'False', '9', '31', '79', '20', '80', '2'], ['17', '2', '2', '5', 'False', 'False', 'False', '8', '34', '64', '50', '120', '12'], ['21', '2.5', '1.5', '0', 'True', 'False', 'False', '6', '31', '77', '12', '26', '10'], ['56', '1.8', '1.8', '7', 'False', 'False', 'False', '61', '35', '63', '12', '117', '12'], ['21', '2.5', '1.172', '0', 'True', 'False', 'True', '6', '34', '76', '2', '40', '2'], ['12', '1', '1', '7', 'False', 'False', 'False', '15', '36', '62', '5', '55', '2'], ['3', '1.3', '0.5', '8', 'False', 'False', 'False', '5', '32', '67', '33', '66', '9'], ['10', '1.5', '1', '7', 'False', 'False', 'False', '10', '32', '77', '12', '26', '9'], ['21', '1', '1', '7', 'False', 'False', 'True', '21', '43', '56', '30', '60', '3'], ['10', '2', '2', '5', 'False', 'False', 'False', '2', '41', '55', '20', '40', '122'], ['20', '1', '1', '0', 'False', 'False', 'False', '4', '41', '71', '7', '23', '18'], ['7', '2.4', '1.57', '0', 'False', 'False', 'False', '6', '32', '77', '12', '26', '9'], ['51', '21', '1', '0', 'False', 'False', 'False', '2', '41', '51', '20', '40', '2'], ['53', '1.1', '0.9', 'D1', 'False', 'False', 'False', '14', '41', '71', '22', '24', '2'], ['45', '1', '1', '7', 'False', 'False', 'False', '9', '49', '81', '10', '52', '2'], ['12', '1', '1', '7', 'True', 'True', 'False', '21', '41', '65', '12', '26', '12'], ['21', '1', '1', '0', 'False', 'False', 'False', '40', '48', '51', '12', '24', '8'], ['30', '2', '1.3', '0', 'True', 'False', 'False', '4', '45', '78', '20', '80', '2'], ['2', '2', '2', '8', 'False', 'False', 'False', '10', '31', '64', '4', '8', '2'], ['18', '2.5', '1', '8', 'True', 'False', 'False', '3', '11', '65', '55', '180', '16'], ['19', '1.3', '1.8', '0', 'False', 'False', 'False', '18', '35', '61', '7', '23', '18'], ['65', '2.719', '2', '8', 'True', 'False', 'False', '5', '41', '78', '24', '52', '12'], ['14', '2', '2', '1', 'False', 'False', 'False', '6', '25', '66', '7', '49', '2'], ['53', '1.1', '0.92', 'D1', 'False', 'False', 'False', '12', '43', '71', '22', '26', '2'], ['20', '2.7', '2', '2', 'True', 'False', 'False', '5', '25', '77', '5', '10', '2'], ['29', '2.18', '2.79', '2', 'False', 'False', 'False', '41', '38', '70', '17', '41', '44'], ['26', '3.1', '2.06', 'D1', 'False', 'False', 'False', '15', '26', '58', '27', '56', '5'], ['20', '1.59', '0.77', '2', 'False', 'False', 'False', '6', '38', '81', '54', '56', '10'], ['31', '0.7', '0.7', '8', 'False', 'False', 'False', '7', '37', '67', '44', '81', '8'], ['41', '2', '1', '0', 'False', 'False', 'False', '10', '31', '64', '4', '8', '2']]
configs=[['10', '1', '1', '7', 'False', 'False', 'False', '3', '26', '81', '20', '120', '12'], ['10', '1', '1', '7', 'False', 'False', 'False', '3', '28', '62', '2', '100', '2'], ['10', '1', '1.1', '6', 'False', 'False', 'False', '8', '23', '73', '18', '119', '3'], ['10', '1', '1.4', '7', 'False', 'False', 'False', '28', '27', '67', '6', '91', '9'], ['10', '1.3', '1.3', '6', 'False', 'False', 'False', '7', '22', '74', '4', '80', '12'], ['10', '1.5', '1', '7', 'False', 'False', 'False', '10', '32', '77', '12', '26', '9'], ['10', '1.7', '1', '0', 'False', 'False', 'False', '3', '28', '71', '10', '120', '21'], ['10', '1.7', '1.5', '7', 'False', 'False', 'False', '3', '14', '60', '12', '24', '8'], ['10', '1.8', '1.5', '2', 'False', 'False', 'False', '11', '32', '75', '20', '28', '2'], ['10', '1.8', '1.5', '2', 'False', 'False', 'False', '7', '31', '81', '5', '12', '12'], ['10', '1.86', '1.94', '6', 'False', 'False', 'False', '21', '14', '67', '41', '130', '41'], ['10', '1.86', '1.94', '6', 'False', 'False', 'False', '8', '6', '67', '41', '130', '41'], ['10', '1.9', '2.1', '8', 'False', 'False', 'False', '22', '34', '68', '6', '51', '21'], ['10', '2', '1', '0', 'False', 'False', 'False', '9', '31', '79', '20', '80', '2'], ['10', '2', '1', '7', 'False', 'False', 'False', '37', '35', '67', '13', '42', '10'], ['10', '2', '1.7', '5', 'False', 'False', 'False', '6', '21', '81', '40', '50', '2'], ['10', '2', '2', '0', 'False', 'False', 'False', '23', '41', '78', '20', '120', '2'], ['10', '2', '2', '5', 'False', 'False', 'False', '2', '41', '55', '20', '40', '122'], ['10', '2', '2', '6', 'False', 'False', 'False', '5', '33', '81', '41', '130', '41'], ['10', '2', '2', '7', 'False', 'False', 'False', '7', '37', '61', '12', '44', '2'], ['10', '2', '2', '8', 'False', 'False', 'False', '2', '21', '81', '10', '100', '2'], ['10', '2.05', '0.3', '0', 'False', 'False', 'False', '5', '21', '81', '20', '120', '4'], ['10', '2.35', '2', '0', 'True', 'True', 'False', '6', '32', '77', '12', '26', '9'], ['10', '2.4', '1.57', '0', 'True', 'False', 'False', '4', '26', '79', '12', '30', '10'], ['10', '2.4', '1.57', '0', 'True', 'False', 'False', '6', '26', '79', '12', '30', '10'], ['10', '2.4', '1.57', '0', 'True', 'False', 'False', '6', '31', '77', '12', '26', '10'], ['10', '2.4', '1.57', '0', 'True', 'False', 'False', '6', '32', '77', '12', '26', '9'], ['10', '2.4', '3.2', '6', 'False', 'False', 'False', '6', '32', '77', '12', '26', '9'], ['11', '1', '1', '2', 'False', 'False', 'False', '8', '45', '75', '60', '120', '12'], ['11', '1.5', '1.3', '6', 'False', 'False', 'False', '20', '34', '50', '12', '24', '20'], ['11', '1.86', '1.94', '5', 'False', 'False', 'False', '5', '7', '67', '12', '50', '12'], ['11', '1.9', '1.9', '7', 'True', 'False', 'False', '25', '48', '61', '33', '77', '2'], ['11', '1.9', '1.9', '7', 'True', 'False', 'False', '9', '48', '61', '33', '77', '2'], ['11', '2', '1', '8', 'False', 'False', 'False', '13', '30', '60', '12', '24', '9'], ['11', '2', '1', '8', 'False', 'False', 'False', '8', '31', '81', '12', '24', '2'], ['11', '2.1', '1.9', '0', 'False', 'False', 'False', '4', '21', '81', '51', '120', '10'], ['12', '1', '1', '0', 'False', 'False', 'False', '12', '21', '71', '20', '40', '12'], ['12', '1', '1', '0', 'False', 'False', 'False', '4', '40', '51', '7', '23', '18'], ['12', '1', '1', '1', 'False', 'False', 'False', '4', '31', '65', '44', '80', '12'], ['12', '1', '1', '1', 'False', 'False', 'False', '5', '2', '81', '12', '71', '12'], ['12', '1', '1', '1', 'False', 'False', 'False', '6', '31', '51', '20', '120', '2'], ['12', '1', '1', '6', 'False', 'False', 'False', '5', '29', '76', '13', '30', '2'], ['12', '1', '1', '7', 'False', 'False', 'False', '15', '36', '62', '5', '55', '2'], ['12', '1', '1', '7', 'False', 'False', 'False', '17', '30', '79', '12', '24', '8'], ['12', '1', '1', '7', 'False', 'False', 'False', '3', '21', '81', '20', '80', '12'], ['12', '1', '1', '7', 'True', 'True', 'False', '21', '41', '65', '12', '26', '12'], ['12', '1', '1', '8', 'False', 'False', 'False', '23', '42', '67', '40', '120', '2'], ['12', '1', '1', '8', 'False', 'False', 'False', '6', '21', '71', '10', '120', '2'], ['12', '1', '1', '8', 'False', 'False', 'False', '6', '21', '71', '10', '20', '7'], ['12', '1', '1', 'D1', 'False', 'False', 'False', '15', '46', '59', '20', '120', '12'], ['12', '1', '1', 'D1', 'False', 'False', 'False', '31', '44', '61', '12', '12', '212'], ['12', '1', '1', 'T1', 'False', 'False', 'False', '11', '20', '81', '41', '120', '2'], ['12', '1', '1', 'T1', 'False', 'False', 'False', '5', '21', '61', '10', '40', '2'], ['12', '1', '1.7', '8', 'False', 'False', 'False', '4', '23', '71', '4', '83', '9'], ['12', '1.1', '1.1', '6', 'True', 'False', 'False', '10', '33', '70', '20', '50', '8'], ['12', '1.2', '2.87', '1', 'False', 'False', 'False', '43', '36', '60', '31', '40', '49'], ['12', '1.4', '1.8', '8', 'False', 'False', 'False', '3', '31', '51', '10', '120', '2'], ['12', '1.61', '1.1', '0', 'False', 'False', 'False', '28', '37', '72', '6', '86', '2'], ['12', '1.8', '1.5', '2', 'True', 'False', 'False', '11', '35', '73', '2', '40', '2'], ['12', '1.8', '1.9', '1', 'False', 'False', 'False', '15', '23', '61', '50', '100', '51'], ['12', '1.9', '0.5', '1', 'False', 'False', 'False', '5', '16', '78', '12', '26', '9'], ['12', '1.9', '1.9', '7', 'True', 'False', 'False', '25', '48', '61', '33', '77', '2'], ['12', '1.9', '2.5', '1', 'False', 'False', 'False', '5', '41', '78', '12', '26', '9'], ['12', '2', '0.5', '0', 'False', 'False', 'False', '10', '31', '64', '4', '8', '2'], ['12', '2', '1', '0', 'False', 'False', 'False', '4', '41', '71', '20', '80', '2'], ['12', '2', '1', '0', 'False', 'False', 'False', '5', '41', '71', '20', '80', '2'], ['12', '2', '1', '0', 'True', 'True', 'False', '4', '35', '81', '20', '120', '2'], ['12', '2', '1', '6', 'False', 'False', 'False', '3', '31', '61', '50', '100', '2'], ['12', '2', '1', '8', 'False', 'False', 'False', '2', '21', '81', '4', '20', '2'], ['12', '2', '1.6', '0', 'True', 'False', 'False', '12', '30', '61', '50', '100', '2'], ['12', '2', '2', '0', 'False', 'False', 'False', '4', '37', '78', '20', '80', '2'], ['12', '2', '2', '0', 'False', 'False', 'False', '5', '31', '77', '12', '26', '9'], ['12', '2', '2', '0', 'False', 'False', 'False', '94', '12', '71', '20', '80', '2'], ['12', '2', '2', '2', 'False', 'False', 'False', '3', '12', '75', '10', '40', '2'], ['12', '2', '2', '6', 'True', 'False', 'False', '11', '35', '69', '20', '120', '14'], ['12', '2', '2', '7', 'False', 'False', 'False', '53', '47', '53', '10', '20', '7'], ['12', '2', '2', '8', 'False', 'False', 'False', '10', '31', '64', '4', '8', '2'], ['12', '2', '2', 'D1', 'False', 'False', 'False', '4', '12', '75', '40', '120', '8'], ['12', '2.1', '0.9', '8', 'False', 'False', 'False', '11', '31', '69', '25', '60', '19'], ['12', '2.1', '1', '1', 'False', 'False', 'False', '5', '41', '78', '12', '26', '9'], ['12', '2.1', '1.4', '7', 'False', 'False', 'False', '5', '32', '74', '11', '24', '2'], ['12', '2.1', '1.4', '7', 'False', 'True', 'False', '5', '32', '74', '11', '24', '2'], ['12', '2.1', '1.8', '5', 'False', 'False', 'False', '9', '40', '74', '20', '120', '2'], ['12', '2.4', '1', '0', 'True', 'False', 'False', '12', '30', '61', '50', '100', '2'], ['12', '2.4', '1', '0', 'True', 'False', 'True', '3', '5', '78', '50', '100', '2'], ['12', '2.43', '1.92', '1', 'False', 'False', 'False', '24', '44', '66', '59', '26', '39'], ['12', '2.5', '1', '1', 'False', 'False', 'False', '7', '41', '79', '40', '80', '2'], ['12', '2.8', '2.5', '8', 'False', 'False', 'False', '21', '48', '64', '12', '55', '2'], ['12', '3', '1.6', '0', 'True', 'False', 'False', '40', '37', '76', '20', '120', '2'], ['12', '3', '2', '8', 'False', 'False', 'True', '6', '12', '70', '12', '24', '2'], ['12', '3', '3', '6', 'False', 'False', 'False', '13', '11', '71', '21', '120', '2'], ['12', '3.5', '0.7', '8', 'False', 'False', 'False', '8', '27', '75', '5', '231', '2'], ['13', '1', '1', '0', 'True', 'False', 'False', '3', '12', '81', '5', '10', '2'], ['13', '1', '2', '0', 'False', 'False', 'False', '2', '41', '77', '3', '120', '12'], ['13', '1.5', '1', '5', 'False', 'False', 'False', '6', '44', '72', '5', '20', '2'], ['13', '1.7', '1.99', '8', 'False', 'False', 'False', '21', '37', '63', '5', '30', '2'], ['13', '1.86', '1.6', '0', 'False', 'False', 'False', '5', '4', '80', '21', '100', '2'], ['13', '1.9', '1.8', '2', 'False', 'False', 'False', '12', '30', '67', '5', '30', '10'], ['13', '2.1', '1', '6', 'False', 'False', 'False', '7', '21', '75', '12', '26', '9'], ['13', '2.4', '1', '0', 'True', 'False', 'True', '6', '30', '77', '12', '26', '9'], ['13', '2.6', '2', '8', 'False', 'False', 'False', '3', '21', '71', '20', '120', '0'], ['14', '0.6', '2', '6', 'False', 'False', 'False', '18', '41', '51', '13', '26', '12'], ['14', '1', '2', '8', 'False', 'False', 'False', '12', '42', '66', '24', '52', '2'], ['14', '1.12', '1.2', '6', 'False', 'False', 'False', '3', '21', '81', '6', '81', '2'], ['14', '1.3', '1.6', '7', 'False', 'False', 'False', '3', '18', '71', '20', '30', '22'], ['14', '1.3', '1.6', '7', 'False', 'False', 'False', '3', '21', '71', '20', '30', '22'], ['14', '2', '2', '1', 'False', 'False', 'False', '6', '25', '66', '7', '49', '2'], ['14', '2', '2', '8', 'False', 'False', 'False', '18', '45', '70', '7', '23', '12'], ['15', '1', '1', '1', 'False', 'False', 'False', '12', '41', '61', '2', '4', '12'], ['15', '1', '1', '2', 'False', 'False', 'False', '3', '21', '71', '20', '80', '2'], ['15', '1', '1', '6', 'False', 'False', 'False', '11', '33', '71', '9', '23', '31'], ['15', '1', '1', '6', 'False', 'False', 'False', '4', '41', '71', '7', '23', '22'], ['15', '1', '1', 'D1', 'True', 'True', 'False', '14', '33', '56', '5', '22', '2'], ['15', '1', '1', 'T1', 'False', 'False', 'False', '21', '49', '57', '10', '16', '21'], ['15', '1.4', '1', '0', 'False', 'False', 'False', '3', '40', '51', '7', '23', '18'], ['15', '1.4', '1.4', '5', 'False', 'False', 'False', '3', '21', '44', '7', '120', '31'], ['15', '1.5', '1', '2', 'False', 'False', 'False', '11', '28', '51', '2', '40', '2'], ['15', '1.8', '2', '6', 'True', 'False', 'True', '13', '19', '70', '50', '80', '2'], ['15', '2', '1', '0', 'False', 'False', 'False', '41', '39', '66', '7', '111', '2'], ['15', '2', '1', '0', 'False', 'False', 'False', '6', '15', '75', '10', '26', '8'], ['15', '2', '1', '1', 'False', 'False', 'False', '2', '19', '55', '3', '8', '2'], ['15', '2', '1', '6', 'False', 'False', 'False', '11', '40', '51', '9', '19', '66'], ['15', '2', '2', '0', 'False', 'False', 'False', '18', '31', '61', '7', '23', '2'], ['15', '2', '2', '0', 'False', 'False', 'False', '18', '40', '51', '7', '23', '18'], ['15', '2', '2', '0', 'False', 'False', 'False', '18', '41', '61', '7', '23', '18'], ['15', '2', '2', '0', 'True', 'False', 'False', '18', '40', '51', '7', '23', '18'], ['15', '2', '2', '1', 'False', 'False', 'False', '18', '40', '51', '7', '23', '18'], ['15', '2', '2', '6', 'False', 'False', 'False', '15', '40', '51', '7', '23', '18'], ['15', '2', '2', '6', 'False', 'False', 'False', '18', '40', '51', '7', '23', '18'], ['15', '2.1', '2.2', '0', 'False', 'False', 'False', '18', '36', '60', '31', '61', '2'], ['15', '2.12', '2.256', '0', 'False', 'False', 'True', '35', '44', '57', '31', '61', '2'], ['15', '2.4', '1.1', '0', 'False', 'True', 'False', '7', '32', '75', '12', '24', '11'], ['15', '2.5', '1', '8', 'True', 'False', 'False', '8', '41', '80', '24', '52', '12'], ['15', '3', '1.5', '7', 'True', 'False', 'False', '5', '22', '75', '10', '26', '8'], ['15', '3', '1.5', '7', 'True', 'False', 'False', '6', '22', '75', '10', '26', '8'], ['16', '1', '1', '7', 'False', 'False', 'True', '21', '43', '56', '30', '60', '3'], ['16', '1', '1.9', '5', 'False', 'False', 'False', '3', '21', '76', '5', '10', '2'], ['16', '1.5', '1.5', '5', 'True', 'False', 'False', '13', '35', '53', '20', '50', '2'], ['16', '1.5', '2', '8', 'False', 'False', 'False', '4', '21', '81', '30', '40', '2'], ['16', '2', '2', '0', 'False', 'False', 'True', '15', '41', '76', '20', '120', '2'], ['16', '2', '2', '7', 'False', 'False', 'False', '10', '35', '78', '13', '26', '2'], ['17', '1', '1.9', '1', 'False', 'False', 'False', '10', '42', '65', '22', '90', '8'], ['17', '1.5', '1.5', '0', 'False', 'False', 'False', '3', '30', '60', '11', '22', '5'], ['17', '1.5', '1.5', 'T1', 'False', 'False', 'False', '12', '21', '78', '20', '40', '2'], ['17', '2', '2', '5', 'False', 'False', 'False', '8', '34', '64', '50', '120', '12'], ['17', '3', '2', '8', 'False', 'False', 'False', '18', '45', '67', '12', '24', '7'], ['18', '1.4', '1.9', '0', 'False', 'False', 'False', '3', '25', '55', '16', '23', '1'], ['18', '1.7', '1', '0', 'False', 'False', 'False', '21', '41', '61', '20', '120', '2'], ['18', '2', '1', '8', 'False', 'False', 'True', '4', '41', '81', '120', '12', '2'], ['18', '2', '1', '8', 'True', 'True', 'False', '5', '41', '80', '24', '52', '12'], ['18', '2', '2', '0', 'True', 'False', 'False', '6', '32', '77', '12', '26', '9'], ['18', '2.5', '1', '8', 'True', 'False', 'False', '3', '11', '65', '55', '180', '16'], ['18', '2.5', '1', '8', 'True', 'False', 'False', '4', '41', '70', '24', '52', '12'], ['18', '2.5', '1', '8', 'True', 'False', 'False', '5', '41', '80', '24', '52', '12'], ['19', '1', '1.1', '0', 'False', 'False', 'False', '12', '42', '61', '20', '40', '12'], ['19', '1.1', '1.5', '2', 'False', 'False', 'False', '8', '35', '73', '20', '40', '11'], ['19', '1.3', '1.8', '0', 'False', 'False', 'False', '18', '35', '61', '7', '23', '18'], ['19', '2.5', '0.9', '8', 'True', 'False', 'False', '5', '40', '81', '24', '52', '11'], ['2', '1', '1', '5', 'False', 'False', 'False', '5', '31', '71', '20', '40', '12'], ['2', '1', '1', '7', 'False', 'False', 'False', '2', '35', '71', '10', '50', '12'], ['2', '1', '1.1', '0', 'False', 'False', 'False', '30', '42', '61', '20', '40', '2'], ['2', '2', '2', '8', 'False', 'False', 'False', '10', '31', '64', '4', '8', '2'], ['2', '2', '2', '8', 'False', 'False', 'False', '28', '37', '66', '16', '97', '2'], ['20', '1', '0.5', '6', 'False', 'False', 'False', '5', '44', '74', '12', '26', '9'], ['20', '1', '1', '0', 'False', 'False', 'False', '4', '41', '71', '12', '50', '2'], ['20', '1', '1', '0', 'False', 'False', 'False', '4', '41', '71', '7', '23', '18'], ['20', '1', '1', '0', 'False', 'False', 'False', '4', '41', '81', '12', '50', '2'], ['20', '1', '1', '5', 'False', 'False', 'False', '3', '31', '71', '10', '120', '12'], ['20', '1', '1', '6', 'False', 'False', 'False', '4', '31', '61', '20', '40', '2'], ['20', '1', '1', '8', 'False', 'False', 'False', '16', '31', '72', '50', '100', '5'], ['20', '1.1', '1.1', 'T1', 'False', 'False', 'False', '21', '41', '61', '20', '40', '2'], ['20', '1.15', '2.46', '1', 'False', 'False', 'False', '4', '48', '54', '12', '46', '2'], ['20', '1.3', '0.4', '8', 'False', 'False', 'False', '4', '30', '70', '33', '66', '3'], ['20', '1.59', '0.77', '2', 'False', 'False', 'False', '6', '38', '81', '54', '56', '10'], ['20', '1.59', '0.77', '2', 'True', 'False', 'False', '42', '38', '50', '54', '56', '10'], ['20', '2', '1', '5', 'False', 'False', 'False', '2', '47', '77', '20', '50', '7'], ['20', '2', '2', '0', 'False', 'False', 'False', '14', '20', '80', '12', '26', '9'], ['20', '2', '2', '0', 'True', 'True', 'True', '14', '20', '80', '12', '26', '9'], ['20', '2', '2', '2', 'False', 'False', 'False', '3', '20', '81', '20', '80', '2'], ['20', '2.2', '2', '6', 'False', 'False', 'False', '11', '33', '71', '50', '100', '4'], ['20', '2.7', '2', '2', 'True', 'False', 'False', '5', '25', '77', '5', '10', '2'], ['20', '2.8', '2.5', '8', 'True', 'False', 'False', '6', '26', '77', '12', '30', '10'], ['21', '1', '0.5', '6', 'False', 'False', 'False', '17', '31', '57', '19', '48', '3'], ['21', '1', '1', '0', 'False', 'False', 'False', '2', '35', '81', '7', '23', '2'], ['21', '1', '1', '0', 'False', 'False', 'False', '3', '31', '71', '10', '60', '2'], ['21', '1', '1', '0', 'False', 'False', 'False', '40', '48', '51', '12', '24', '8'], ['21', '1', '1', '0', 'False', 'False', 'False', '5', '45', '78', '20', '80', '12'], ['21', '1', '1', '1', 'False', 'False', 'False', '12', '27', '69', '20', '120', '12'], ['21', '1', '1', '1', 'False', 'False', 'False', '12', '39', '79', '12', '26', '2'], ['21', '1', '1', '6', 'False', 'False', 'False', '2', '12', '51', '10', '20', '2'], ['21', '1', '1', '6', 'False', 'False', 'False', '25', '32', '77', '12', '26', '2'], ['21', '1', '1', '7', 'False', 'False', 'False', '18', '23', '71', '12', '24', '2'], ['21', '1', '1', '7', 'False', 'False', 'True', '21', '43', '56', '30', '60', '3'], ['21', '1', '1', 'T1', 'True', 'True', 'False', '21', '50', '71', '12', '26', '12'], ['21', '1', '1.1', '0', 'False', 'False', 'False', '30', '42', '61', '20', '40', '2'], ['21', '1.1', '1.1', '5', 'False', 'False', 'False', '4', '41', '80', '50', '100', '220'], ['21', '1.1', '1.5', 'D1', 'False', 'False', 'False', '2', '43', '71', '3', '5', '13'], ['21', '1.2', '0.03', '6', 'False', 'False', 'False', '20', '42', '61', '3', '81', '2'], ['21', '1.2', '0.5', '8', 'False', 'False', 'False', '18', '24', '81', '25', '50', '3'], ['21', '1.3', '2.1', '7', 'False', 'False', 'False', '2', '32', '77', '12', '26', '2'], ['21', '1.5', '1', '2', 'False', 'False', 'False', '8', '49', '71', '20', '40', '8'], ['21', '1.5', '1.8', '7', 'True', 'False', 'False', '6', '31', '71', '7', '23', '18'], ['21', '1.66', '1.74', '5', 'False', 'False', 'False', '2', '33', '55', '41', '130', '44'], ['21', '1.7', '1', '0', 'False', 'False', 'False', '21', '41', '61', '20', '120', '2'], ['21', '1.7', '1', '0', 'False', 'False', 'False', '21', '45', '61', '20', '120', '2'], ['21', '1.7', '1.5', '1', 'False', 'False', 'False', '12', '33', '80', '100', '200', '2'], ['21', '1.8', '1', '5', 'False', 'False', 'False', '5', '16', '78', '6', '91', '9'], ['21', '1.8', '1.9', '0', 'False', 'False', 'False', '40', '49', '59', '50', '100', '18'], ['21', '1.8', '2.1', '5', 'False', 'False', 'False', '3', '12', '61', '50', '70', '5'], ['21', '1.86', '1.94', '6', 'False', 'False', 'False', '5', '4', '81', '41', '120', '30'], ['21', '2', '1', '0', 'False', 'False', 'False', '6', '44', '76', '20', '100', '2'], ['21', '2', '1', '7', 'False', 'False', 'False', '13', '32', '63', '10', '50', '8'], ['21', '2', '1', '7', 'False', 'False', 'False', '5', '22', '71', '5', '20', '2'], ['21', '2', '1.5', '7', 'True', 'False', 'False', '3', '12', '81', '34', '68', '8'], ['21', '2', '2', '0', 'False', 'False', 'False', '34', '12', '71', '500', '100', '16'], ['21', '2', '2', '0', 'False', 'False', 'False', '5', '19', '67', '21', '24', '12'], ['21', '2', '2', '0', 'False', 'True', 'False', '2', '20', '71', '20', '40', '8'], ['21', '2', '2', '5', 'False', 'False', 'False', '10', '25', '78', '12', '81', '12'], ['21', '2', '2', '6', 'False', 'False', 'False', '2', '31', '75', '12', '57', '12'], ['21', '2', '2', '8', 'False', 'False', 'False', '42', '49', '51', '31', '91', '12'], ['21', '2', '2', '8', 'False', 'False', 'False', '5', '27', '55', '31', '91', '11'], ['21', '2', '2', '8', 'False', 'False', 'False', '6', '27', '76', '5', '30', '10'], ['21', '2', '2', '8', 'False', 'True', 'False', '5', '23', '55', '31', '91', '11'], ['21', '2.09', '2.81', '8', 'False', 'False', 'False', '6', '26', '80', '12', '24', '2'], ['21', '2.1', '1.8', '5', 'False', 'False', 'False', '5', '10', '81', '20', '120', '2'], ['21', '2.1', '2', '8', 'True', 'False', 'False', '9', '22', '76', '20', '40', '2'], ['21', '2.1', '2.5', '7', 'False', 'False', 'False', '4', '21', '79', '20', '40', '8'], ['21', '2.4', '1.2', '0', 'True', 'True', 'False', '6', '31', '77', '12', '26', '10'], ['21', '2.4', '1.5', '0', 'True', 'False', 'False', '6', '31', '77', '12', '26', '10'], ['21', '2.5', '1.172', '0', 'True', 'False', 'True', '6', '34', '76', '2', '40', '2'], ['21', '2.5', '1.5', '0', 'True', 'False', 'False', '6', '31', '77', '12', '26', '10'], ['21', '2.6', '2.2', '1', 'False', 'False', 'False', '9', '21', '81', '3', '8', '12'], ['21', '2.7', '2.5', '8', 'True', 'False', 'False', '12', '31', '70', '12', '26', '9'], ['21', '2.71', '2.5', '8', 'True', 'False', 'False', '6', '31', '77', '10', '40', '2'], ['21', '2.8', '2.3', '8', 'False', 'False', 'False', '6', '30', '63', '50', '70', '5'], ['21', '2.9', '1', '7', 'False', 'False', 'False', '2', '31', '80', '20', '40', '2'], ['22', '0.7', '0.6', '8', 'True', 'False', 'False', '19', '44', '59', '22', '44', '8'], ['22', '1', '1', '0', 'False', 'False', 'False', '8', '20', '68', '50', '70', '2'], ['22', '1.1', '1', '1', 'True', 'False', 'False', '9', '27', '74', '20', '40', '12'], ['22', '1.2', '0.9', 'D1', 'False', 'False', 'False', '14', '41', '71', '22', '24', '2'], ['22', '2.2', '2.1', '6', 'False', 'False', 'False', '18', '44', '61', '50', '100', '11'], ['22', '2.3', '2.2', 'D1', 'False', 'False', 'False', '18', '33', '67', '15', '23', '2'], ['23', '1', '1', '7', 'False', 'False', 'False', '33', '40', '56', '12', '26', '2'], ['23', '1.1', '1.1', '2', 'True', 'False', 'False', '11', '40', '73', '31', '60', '2'], ['23', '1.86', '1.94', 'D1', 'False', 'False', 'False', '2', '9', '69', '41', '130', '41'], ['23', '2', '2', '0', 'False', 'False', 'False', '18', '40', '51', '7', '23', '18'], ['23', '2', '2.1', '0', 'False', 'True', 'False', '9', '29', '61', '40', '80', '4'], ['23', '2.1', '1.1', '7', 'False', 'False', 'False', '30', '43', '61', '6', '61', '9'], ['23', '2.78', '1.05', 'D1', 'False', 'False', 'False', '45', '31', '50', '35', '40', '33'], ['24', '1.86', '1.94', '6', 'False', 'False', 'False', '2', '12', '71', '41', '130', '41'], ['24', '1.86', '1.94', '6', 'False', 'False', 'False', '2', '9', '69', '41', '130', '41'], ['24', '1.86', '1.94', '6', 'False', 'False', 'False', '4', '3', '8', '41', '250', '21'], ['24', '2.4', '0.9', '2', 'True', 'False', 'False', '4', '21', '81', '5', '10', '2'], ['24', '2.96', '2.82', '0', 'False', 'False', 'False', '3', '31', '70', '32', '50', '2'], ['24', '3', '3', '1', 'False', 'False', 'False', '9', '33', '63', '20', '50', '8'], ['24', '3.2', '1.99', '6', 'False', 'False', 'False', '36', '45', '58', '33', '28', '23'], ['25', '1', '1', '0', 'False', 'False', 'False', '19', '31', '62', '10', '398', '116'], ['25', '1', '1', '1', 'False', 'False', 'False', '3', '24', '78', '21', '40', '12'], ['25', '2', '1.1', '7', 'False', 'False', 'False', '7', '21', '75', '12', '24', '2'], ['25', '2.4', '1.6', '0', 'False', 'False', 'False', '12', '31', '69', '12', '30', '8'], ['25', '2.4', '1.6', '0', 'False', 'False', 'False', '5', '31', '63', '19', '91', '2'], ['25', '2.4', '1.6', '0', 'True', 'False', 'False', '3', '32', '75', '6', '91', '9'], ['26', '1.6', '2', '6', 'False', 'False', 'False', '21', '29', '58', '11', '97', '2'], ['26', '2.4', '1.57', '0', 'True', 'False', 'False', '6', '32', '77', '12', '26', '9'], ['26', '2.5', '2.2', '0', 'False', 'False', 'False', '4', '35', '71', '20', '100', '2'], ['26', '3.1', '2.06', 'D1', 'False', 'False', 'False', '15', '26', '58', '27', '56', '5'], ['27', '2', '2', '8', 'False', 'False', 'False', '17', '42', '72', '6', '81', '12'], ['28', '1', '1', '0', 'False', 'False', 'False', '32', '41', '65', '8', '51', '2'], ['28', '1.1', '1.3', '8', 'False', 'False', 'False', '5', '41', '80', '24', '52', '12'], ['28', '2.1', '1', '5', 'False', 'False', 'False', '7', '32', '74', '20', '49', '25'], ['29', '1', '1', '7', 'False', 'False', 'False', '4', '31', '71', '7', '23', '18'], ['29', '2', '1', '0', 'False', 'False', 'False', '41', '39', '67', '7', '10', '2'], ['29', '2.18', '2.79', '2', 'False', 'False', 'False', '41', '38', '70', '17', '41', '44'], ['3', '1', '0.5', '5', 'False', 'False', 'False', '2', '41', '61', '25', '50', '7'], ['3', '1', '0.5', '8', 'False', 'False', 'False', '5', '36', '61', '33', '66', '9'], ['3', '1', '1', 'T1', 'False', 'False', 'False', '21', '33', '69', '20', '100', '2'], ['3', '1.3', '0.5', '8', 'False', 'False', 'False', '5', '32', '67', '33', '66', '9'], ['3', '1.7', '0.5', '8', 'False', 'False', 'False', '5', '32', '67', '33', '66', '9'], ['3', '1.7', '1', '5', 'False', 'False', 'False', '3', '21', '71', '20', '40', '2'], ['30', '1', '1', '6', 'False', 'False', 'False', '9', '31', '69', '7', '21', '2'], ['30', '1.8', '1.5', '2', 'False', 'False', 'False', '11', '45', '75', '50', '100', '2'], ['30', '2', '1.3', '0', 'True', 'False', 'False', '4', '45', '78', '20', '80', '2'], ['30', '2', '2', '8', 'False', 'False', 'False', '17', '42', '72', '12', '24', '2'], ['30', '2.5', '2.5', '8', 'False', 'False', 'False', '10', '32', '70', '50', '70', '12'], ['31', '0.7', '0.7', '8', 'False', 'False', 'False', '7', '37', '67', '44', '81', '8'], ['31', '1', '1', '0', 'False', 'False', 'False', '93', '44', '60', '10', '20', '2'], ['31', '1', '1', '0', 'False', 'True', 'False', '21', '42', '51', '20', '120', '12'], ['31', '1', '1', '1', 'False', 'False', 'False', '17', '45', '58', '50', '120', '2'], ['31', '1', '1', '7', 'True', 'False', 'False', '17', '35', '62', '11', '18', '4'], ['31', '1', '1', '8', 'True', 'False', 'False', '15', '2', '55', '5', '140', '12'], ['31', '1.12', '1.2', '0', 'False', 'False', 'False', '9', '31', '81', '6', '81', '2'], ['31', '1.9', '1', '8', 'False', 'False', 'False', '21', '47', '65', '20', '120', '2'], ['31', '1.9', '1', '8', 'False', 'False', 'False', '48', '48', '74', '15', '120', '30'], ['31', '2.1', '2.4', '7', 'False', 'False', 'False', '12', '34', '73', '10', '50', '2'], ['31', '2.3', '2', '0', 'False', 'False', 'False', '21', '32', '68', '22', '120', '3'], ['32', '2', '2.7', '8', 'False', 'False', 'False', '18', '45', '70', '7', '23', '12'], ['33', '1', '1.3', '6', 'False', 'False', 'False', '26', '31', '54', '6', '81', '2'], ['33', '1', '1.5', '1', 'False', 'False', 'False', '11', '45', '75', '10', '40', '12'], ['33', '1.8', '1.5', '2', 'False', 'False', 'False', '11', '45', '75', '2', '40', '2'], ['33', '1.8', '1.5', '2', 'False', 'False', 'False', '11', '45', '75', '2', '40', '41'], ['33', '1.8', '1.5', '2', 'False', 'False', 'False', '11', '45', '75', '50', '100', '2'], ['33', '2', '2', '0', 'False', 'False', 'False', '12', '24', '72', '14', '80', '42'], ['34', '0.52', '0.44', '1', 'False', 'False', 'False', '20', '42', '69', '46', '4', '20'], ['34', '1.8', '1.5', '2', 'False', 'False', 'False', '24', '40', '64', '50', '100', '21'], ['35', '0.93', '1.57', 'D1', 'False', 'False', 'False', '16', '46', '69', '53', '41', '38'], ['35', '1', '1', '2', 'True', 'False', 'False', '11', '45', '72', '20', '40', '8'], ['36', '1', '1', '8', 'False', 'False', 'False', '5', '12', '81', '15', '120', '30'], ['36', '2', '0.3', '7', 'False', 'False', 'False', '18', '41', '65', '20', '40', '2'], ['37', '2.4', '1.57', '0', 'False', 'False', 'False', '6', '32', '77', '20', '40', '12'], ['37', '2.5', '2', '0', 'False', 'False', 'False', '9', '41', '70', '12', '24', '9'], ['37', '3', '2', '6', 'True', 'False', 'False', '15', '30', '61', '40', '80', '14'], ['39', '1', '1', 'T1', 'False', 'False', 'False', '21', '42', '61', '50', '200', '8'], ['39', '2.2', '1', '6', 'False', 'False', 'False', '12', '43', '71', '5', '10', '2'], ['39', '2.719', '2', '8', 'True', 'False', 'False', '5', '41', '80', '24', '52', '12'], ['4', '0.9', '1.5', '7', 'True', 'False', 'False', '13', '29', '77', '3', '13', '2'], ['4', '1.1', '1', '8', 'False', 'False', 'False', '15', '29', '60', '30', '40', '2'], ['4', '1.8', '1.5', '2', 'False', 'False', 'False', '11', '45', '75', '50', '100', '2'], ['4', '1.9', '0.6', '8', 'False', 'False', 'False', '21', '47', '65', '20', '120', '2'], ['4', '2', '1', '0', 'False', 'False', 'False', '4', '41', '71', '20', '80', '2'], ['4', '2', '1', '7', 'False', 'False', 'False', '4', '22', '71', '20', '100', '12'], ['4', '2', '2.1', '7', 'False', 'False', 'False', '10', '31', '71', '20', '100', '12'], ['40', '1.9', '1.6', 'D1', 'False', 'False', 'False', '3', '31', '71', '20', '120', '2'], ['40', '1.99', '2.44', 'D1', 'False', 'False', 'False', '46', '47', '54', '31', '8', '53'], ['40', '2', '2', '0', 'False', 'False', 'False', '9', '21', '81', '24', '12', '220'], ['40', '2', '2', '7', 'False', 'False', 'False', '9', '21', '81', '10', '30', '18'], ['40', '2', '2', '7', 'False', 'False', 'False', '9', '30', '74', '10', '30', '18'], ['40', '3', '2.2', 'T1', 'False', 'False', 'False', '12', '40', '66', '31', '71', '12'], ['41', '1', '1', '0', 'False', 'False', 'False', '9', '33', '70', '12', '24', '9'], ['41', '1', '1', '1', 'False', 'False', 'False', '38', '31', '66', '21', '26', '12'], ['41', '1', '1', '2', 'False', 'False', 'False', '40', '47', '62', '12', '20', '2'], ['41', '1', '1', '8', 'False', 'True', 'False', '43', '39', '58', '12', '31', '12'], ['41', '1.1', '0.92', 'D1', 'False', 'False', 'False', '4', '41', '71', '22', '26', '2'], ['41', '2', '1', '0', 'False', 'False', 'False', '10', '31', '64', '4', '8', '2'], ['41', '2', '2', '0', 'False', 'False', 'False', '10', '31', '64', '4', '8', '2'], ['41', '2.1', '2', '1', 'False', 'False', 'False', '11', '43', '52', '12', '23', '2'], ['41', '3', '2', '8', 'False', 'False', 'False', '16', '43', '57', '4', '12', '12'], ['42', '1', '2', '7', 'False', 'True', 'False', '4', '21', '81', '20', '120', '2'], ['42', '1.6', '2', '6', 'False', 'False', 'False', '21', '29', '58', '10', '20', '12'], ['42', '1.97', '0.33', '2', 'False', 'False', 'False', '46', '35', '68', '35', '13', '52'], ['42', '2', '1', '8', 'False', 'False', 'False', '13', '15', '75', '6', '19', '23'], ['42', '2', '1.6', '5', 'False', 'False', 'False', '9', '34', '61', '20', '30', '8'], ['43', '1', '1', '6', 'False', 'False', 'False', '11', '40', '51', '4', '19', '2'], ['44', '0.9', '1.4', '1', 'False', 'False', 'False', '41', '42', '45', '20', '40', '7'], ['44', '1.3', '1.1', '2', 'False', 'False', 'False', '5', '22', '81', '25', '80', '2'], ['45', '1', '1', '7', 'False', 'False', 'False', '9', '49', '81', '10', '52', '2'], ['45', '3', '1.6', '7', 'True', 'False', 'False', '14', '34', '67', '10', '50', '2'], ['48', '1.2', '3.2', '6', 'False', 'False', 'False', '10', '31', '71', '6', '81', '2'], ['49', '2', '2', '8', 'False', 'False', 'False', '21', '43', '64', '30', '60', '3'], ['5', '0.9', '1.8', '8', 'False', 'False', 'False', '8', '26', '71', '50', '120', '2'], ['5', '1', '0.5', '5', 'False', 'False', 'False', '4', '29', '51', '25', '50', '11'], ['5', '1', '0.5', '7', 'True', 'False', 'False', '2', '31', '72', '5', '20', '12'], ['5', '1.1', '0.1', '8', 'False', 'False', 'False', '5', '32', '67', '33', '66', '9'], ['5', '1.3', '1.8', '0', 'False', 'False', 'False', '18', '35', '61', '7', '23', '18'], ['5', '1.86', '1.94', '6', 'False', 'False', 'False', '2', '7', '65', '41', '130', '41'], ['5', '1.9', '0.5', '7', 'False', 'False', 'False', '5', '16', '78', '12', '26', '9'], ['5', '2', '0.7', '0', 'False', 'False', 'False', '12', '41', '71', '20', '80', '2'], ['5', '2', '2', '7', 'False', 'False', 'False', '9', '37', '70', '12', '24', '9'], ['5', '2.02', '1.75', '7', 'False', 'False', 'False', '12', '31', '81', '58', '31', '8'], ['5', '3', '1', '7', 'False', 'False', 'False', '12', '27', '73', '20', '40', '4'], ['5', '3', '2', '6', 'False', 'False', 'False', '10', '6', '81', '22', '26', '2'], ['5', '3.04', '0.11', '2', 'False', 'False', 'False', '11', '49', '67', '2', '10', '25'], ['5', '3.1', '2.8', '7', 'False', 'False', 'False', '9', '37', '70', '12', '24', '2'], ['5', '3.1', '2.8', '7', 'False', 'False', 'False', '9', '37', '70', '12', '24', '9'], ['50', '1', '1', '0', 'False', 'False', 'False', '18', '21', '51', '7', '23', '12'], ['50', '1', '1', '7', 'False', 'False', 'False', '8', '31', '71', '20', '120', '2'], ['50', '1', '1', '8', 'False', 'False', 'False', '2', '12', '81', '20', '90', '12'], ['50', '1', '1', 'D1', 'True', 'True', 'True', '14', '41', '81', '10', '27', '8'], ['50', '1.1', '1.3', '0', 'True', 'False', 'False', '6', '32', '77', '12', '26', '9'], ['50', '1.1', '1.3', '6', 'False', 'False', 'False', '21', '29', '75', '9', '23', '31'], ['50', '1.86', '1.94', 'T1', 'True', 'False', 'False', '5', '33', '72', '41', '130', '41'], ['50', '2', '1', '0', 'False', 'False', 'False', '10', '31', '64', '4', '8', '2'], ['50', '2', '1', '1', 'False', 'False', 'False', '8', '41', '56', '20', '60', '2'], ['50', '2.1', '1.5', '5', 'False', 'False', 'False', '12', '23', '72', '20', '120', '2'], ['50', '2.2', '2.2', '8', 'True', 'True', 'False', '10', '21', '77', '20', '100', '24'], ['50', '2.3', '1', '1', 'True', 'False', 'False', '6', '39', '71', '14', '38', '8'], ['51', '0.7', '3', '7', 'False', 'False', 'False', '41', '11', '71', '6', '91', '24'], ['51', '1', '1', '7', 'False', 'False', 'False', '4', '21', '71', '18', '44', '21'], ['51', '1', '2', '0', 'False', 'False', 'False', '21', '45', '61', '10', '30', '2'], ['51', '1.1', '0.9', 'D1', 'False', 'False', 'False', '21', '45', '61', '22', '26', '2'], ['51', '1.1', '0.92', 'D1', 'False', 'False', 'True', '9', '43', '71', '22', '26', '2'], ['51', '1.3', '1.3', '2', 'True', 'False', 'False', '6', '27', '76', '5', '30', '10'], ['51', '2', '0.5', '0', 'False', 'False', 'False', '10', '31', '64', '4', '8', '2'], ['51', '2', '1.5', '8', 'False', 'False', 'False', '10', '35', '67', '17', '50', '12'], ['51', '2', '2', '8', 'False', 'False', 'False', '3', '31', '61', '40', '100', '2'], ['51', '2', '2', '8', 'False', 'False', 'False', '5', '31', '79', '12', '120', '2'], ['51', '2', '2', '8', 'True', 'False', 'False', '42', '41', '51', '21', '91', '12'], ['51', '2.1', '2.2', '6', 'False', 'False', 'False', '18', '40', '51', '2', '40', '2'], ['51', '2.1', '2.4', '7', 'True', 'True', 'False', '12', '34', '73', '10', '50', '2'], ['51', '2.2', '2', '7', 'False', 'True', 'False', '19', '33', '67', '34', '62', '12'], ['51', '21', '1', '0', 'False', 'False', 'False', '2', '41', '51', '20', '40', '2'], ['53', '1.1', '0.9', 'D1', 'False', 'False', 'False', '12', '43', '71', '22', '26', '2'], ['53', '1.1', '0.9', 'D1', 'False', 'False', 'False', '14', '41', '71', '22', '24', '2'], ['53', '1.1', '0.92', 'D1', 'False', 'False', 'False', '12', '43', '71', '22', '26', '2'], ['53', '1.1', '0.92', 'D1', 'False', 'False', 'False', '17', '43', '71', '22', '26', '2'], ['55', '0.8', '1', '8', 'False', 'False', 'False', '5', '21', '79', '18', '100', '8'], ['55', '1.1', '1.9', '1', 'False', 'False', 'False', '3', '14', '81', '6', '81', '12'], ['55', '1.4', '1.4', 'T1', 'False', 'False', 'False', '9', '33', '63', '20', '50', '8'], ['55', '1.9', '2.2', '8', 'False', 'False', 'False', '41', '35', '54', '12', '51', '2'], ['55', '2', '1.8', '5', 'False', 'False', 'False', '3', '31', '71', '10', '120', '2'], ['56', '1.3', '0.3', '5', 'False', 'False', 'False', '6', '50', '61', '50', '100', '8'], ['56', '1.8', '1.8', '7', 'False', 'False', 'False', '61', '35', '63', '12', '117', '12'], ['57', '1', '1', '1', 'False', 'False', 'False', '41', '49', '62', '58', '122', '4'], ['6', '1', '1', '2', 'False', 'False', 'False', '5', '31', '50', '5', '20', '2'], ['6', '1', '1', '8', 'False', 'False', 'False', '3', '1', '81', '5', '120', '2'], ['6', '1', '1', 'D1', 'False', 'False', 'False', '3', '22', '72', '20', '40', '4'], ['6', '1', '2', '6', 'False', 'False', 'False', '4', '18', '81', '4', '79', '2'], ['6', '1.1', '1', '8', 'False', 'False', 'False', '5', '42', '61', '4', '20', '4'], ['6', '1.3', '0.5', '8', 'False', 'False', 'False', '5', '32', '67', '33', '66', '9'], ['6', '2', '2', '7', 'False', 'False', 'False', '17', '35', '61', '12', '24', '8'], ['6', '2.2', '1.2', '8', 'False', 'False', 'False', '15', '12', '81', '12', '130', '2'], ['60', '1.6', '0.7', 'T1', 'False', 'False', 'False', '3', '31', '65', '20', '40', '4'], ['60', '2', '2', '1', 'False', 'False', 'False', '48', '35', '58', '30', '100', '18'], ['61', '1.1', '1.6', '0', 'False', 'False', 'False', '11', '23', '66', '3', '91', '2'], ['61', '1.5', '2', 'T1', 'False', 'False', 'False', '3', '31', '61', '20', '40', '2'], ['61', '2.1', '1.8', '5', 'False', 'False', 'False', '12', '23', '72', '20', '120', '2'], ['64', '2.8', '2.5', '8', 'False', 'False', 'False', '21', '48', '64', '12', '55', '2'], ['65', '2.4', '1.57', '0', 'True', 'False', 'False', '6', '21', '77', '12', '26', '9'], ['65', '2.7', '2.8', '7', 'True', 'False', 'False', '5', '41', '79', '24', '52', '12'], ['65', '2.719', '2', '8', 'True', 'False', 'False', '2', '7', '81', '3', '14', '51'], ['65', '2.719', '2', '8', 'True', 'False', 'False', '2', '7', '81', '30', '120', '30'], ['65', '2.719', '2', '8', 'True', 'False', 'False', '5', '41', '78', '24', '52', '12'], ['65', '2.719', '2', '8', 'True', 'False', 'False', '5', '41', '79', '24', '52', '12'], ['65', '2.719', '2', '8', 'True', 'False', 'False', '6', '31', '68', '24', '52', '12'], ['65', '3', '2', '8', 'True', 'False', 'False', '6', '32', '77', '12', '26', '9'], ['65', '3.1', '2', '8', 'True', 'False', 'False', '6', '29', '65', '30', '120', '30'], ['66', '1.86', '1.94', 'T1', 'False', 'False', 'False', '40', '34', '61', '41', '130', '41'], ['67', '2', '2', '7', 'False', 'False', 'False', '18', '40', '51', '7', '23', '18'], ['69', '1', '1', '7', 'False', 'False', 'False', '15', '24', '81', '20', '120', '2'], ['7', '0.9', '0.9', '7', 'False', 'False', 'False', '8', '34', '75', '20', '120', '3'], ['7', '1', '1', '0', 'False', 'False', 'False', '9', '40', '81', '4', '19', '2'], ['7', '1', '1', '2', 'False', 'False', 'False', '3', '37', '70', '12', '24', '9'], ['7', '1', '1', '7', 'False', 'False', 'False', '3', '29', '60', '30', '40', '2'], ['7', '1', '1', '8', 'False', 'False', 'False', '3', '24', '71', '9', '41', '2'], ['7', '1', '1', '8', 'False', 'False', 'False', '6', '41', '71', '5', '20', '2'], ['7', '1', '1.5', '7', 'True', 'False', 'False', '9', '41', '79', '50', '100', '10'], ['7', '1.1', '1.2', '7', 'False', 'False', 'False', '12', '39', '61', '31', '81', '12'], ['7', '1.2', '1.3', '7', 'False', 'False', 'False', '6', '25', '81', '40', '159', '2'], ['7', '1.8', '1.5', '2', 'False', 'False', 'False', '11', '45', '75', '50', '100', '2'], ['7', '1.9', '0.4', '8', 'False', 'False', 'False', '21', '47', '65', '20', '120', '2'], ['7', '1.9', '0.6', '8', 'False', 'False', 'False', '21', '47', '65', '20', '120', '2'], ['7', '1.9', '1.9', '8', 'False', 'False', 'False', '2', '21', '71', '22', '120', '2'], ['7', '2', '1', '8', 'False', 'False', 'False', '3', '31', '81', '20', '120', '2'], ['7', '2', '1.5', '2', 'False', 'False', 'True', '6', '45', '75', '20', '120', '2'], ['7', '2', '2', '0', 'False', 'False', 'False', '4', '41', '71', '20', '80', '2'], ['7', '2', '2', '6', 'False', 'False', 'False', '18', '40', '51', '7', '23', '18'], ['7', '2', '2', '7', 'False', 'False', 'False', '23', '36', '68', '12', '21', '2'], ['7', '2.1', '1.1', '1', 'False', 'False', 'False', '9', '44', '68', '12', '26', '9'], ['7', '2.1', '2', '8', 'False', 'False', 'False', '35', '50', '58', '5', '12', '10'], ['7', '2.4', '1.57', '0', 'False', 'False', 'False', '22', '44', '61', '5', '21', '21'], ['7', '2.4', '1.57', '0', 'False', 'False', 'False', '6', '32', '77', '12', '26', '9'], ['7', '2.5', '1', '8', 'True', 'False', 'False', '5', '41', '80', '24', '52', '12'], ['70', '1', '1', '7', 'False', 'False', 'False', '17', '41', '72', '30', '40', '2'], ['70', '2.2', '2.5', '8', 'False', 'False', 'False', '12', '41', '71', '20', '40', '2'], ['71', '1', '1', 'D1', 'False', 'False', 'False', '46', '46', '69', '12', '61', '10'], ['72', '1', '1', '6', 'True', 'False', 'False', '7', '43', '71', '22', '26', '2'], ['77', '1.86', '1.94', '6', 'False', 'False', 'False', '8', '16', '76', '30', '25', '21'], ['77', '1.86', '2.17', '6', 'False', 'False', 'False', '31', '29', '65', '50', '80', '2'], ['77', '2', '0.5', '7', 'True', 'True', 'True', '5', '12', '81', '6', '81', '12'], ['8', '1', '1', '0', 'False', 'False', 'False', '2', '21', '63', '44', '140', '32'], ['8', '1', '1', '7', 'False', 'False', 'False', '21', '41', '67', '5', '44', '12'], ['8', '1.1', '1.6', '1', 'False', 'False', 'False', '4', '31', '71', '37', '185', '4'], ['8', '1.9', '1.6', '0', 'False', 'False', 'False', '3', '15', '71', '20', '120', '2'], ['8', '2', '2', '2', 'False', 'False', 'False', '7', '40', '66', '4', '19', '3'], ['8', '2.1', '1.9', '2', 'False', 'False', 'False', '3', '30', '50', '15', '50', '4'], ['8', '2.3', '2.9', '0', 'True', 'False', 'False', '6', '28', '77', '12', '26', '9'], ['8', '2.7', '0.5', 'D1', 'False', 'False', 'False', '11', '50', '81', '4', '18', '2'], ['9', '0.8', '0.3', 'T1', 'False', 'False', 'False', '10', '41', '51', '20', '120', '2'], ['9', '1', '0.4', '7', 'False', 'False', 'False', '6', '22', '80', '21', '48', '2'], ['9', '1', '1', '2', 'False', 'False', 'False', '2', '3', '81', '9', '20', '2'], ['9', '1', '1', '7', 'False', 'False', 'False', '2', '12', '81', '20', '90', '3'], ['9', '1', '1', '7', 'False', 'False', 'False', '6', '33', '80', '30', '60', '12'], ['9', '1', '1', '8', 'False', 'False', 'False', '3', '21', '62', '24', '48', '12'], ['9', '1', '1.6', '5', 'False', 'False', 'False', '6', '18', '57', '16', '23', '12'], ['9', '1.4', '1.6', '0', 'False', 'False', 'False', '6', '18', '57', '16', '23', '11'], ['9', '1.9', '2.1', '1', 'False', 'False', 'False', '12', '44', '55', '12', '24', '2'], ['9', '2', '1.1', '7', 'True', 'False', 'False', '5', '28', '76', '13', '42', '12'], ['9', '2', '1.6', '5', 'False', 'False', 'False', '6', '18', '57', '15', '23', '9'], ['9', '2', '2', '7', 'False', 'False', 'False', '18', '21', '69', '7', '23', '12'], ['9', '2', '2.8', '0', 'False', 'False', 'False', '3', '38', '71', '41', '24', '9'], ['9', '2.4', '1.57', '0', 'True', 'False', 'False', '31', '39', '61', '12', '26', '9'], ['9', '2.92', '0.66', '0', 'False', 'False', 'False', '39', '43', '64', '57', '56', '15']]




def backtestingfrommemory(bot, haasomeClient):
  # print(bot)
  baseconfig = haasomeClient.customBotApi.get_custom_bot(bot.guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
  settingsprev = []
  settingsstats = []
  timeinterval = minutestobacktest()
  configroi = []
  startTime = datetime.now()
  print('Downloading backtsting history... Expect results anytime soon')
  for i, v in enumerate(configs):
   configuremh(haasomeClient, bot.guid, configs[i][0], configs[i][1], configs[i][2], configs[i][3], configs[i][4], configs[i][5],configs[i][6], configs[i][7], configs[i][8], configs[i][9], configs[i][10], configs[i][11], configs[i][12])
   configuremhsafety(haasomeClient,bot.guid, 0, 0, 0)
   backtest = haasomeClient.customBotApi.backtest_custom_bot_on_market(bot.accountId, bot.guid, timeinterval, bot.priceMarket.primaryCurrency, bot.priceMarket.secondaryCurrency, bot.priceMarket.contractName)
   backtestr = backtest.result
   roi = backtestr.roi
   prevroi = roi
   
   settings = configs[i][0], configs[i][1], configs[i][2], configs[i][3], configs[i][4], configs[i][5],configs[i][6], configs[i][7], configs[i][8], configs[i][9], configs[i][10], configs[i][11], configs[i][12]
   configroi.append([configs[i][0], configs[i][1], configs[i][2], configs[i][3], configs[i][4], configs[i][5],	configs[i][6], configs[i][7], configs[i][8], configs[i][9], configs[i][10], configs[i][11], configs[i][12], roi])
   settingsprev = settings
   print('ROI:', roi, 'Bot configuration :', configs[i][0], configs[i][1], configs[i][2], configs[i][3], configs[i][4], configs[i][5],configs[i][6], configs[i][7], configs[i][8], configs[i][9], configs[i][10], configs[i][11], configs[i][12], backtest.errorCode, backtest.errorMessage)
  print('time it took: ', datetime.now() - startTime)
  configroiorted = sorted(configroi, key=lambda x: x[13], reverse=False)
  return configroiorted

def makebots(bot, haasomeClient,botType, roilist):
  for i,v in enumerate(roilist):
   print(i, 'ROI: ', v[13])
  botstocreate = int(input('Type number of how any bots yo would like to create?'))
  for bots in range(0,botstocreate):
   i = int(input('Type bot number to create'))
   botname = str(bot.priceMarket.primaryCurrency) + str(' / ') + \
   str(bot.priceMarket.secondaryCurrency) + str(' Roi ') + str(roilist[i][13])
   newbotfrommarket = haasomeClient.customBotApi.new_custom_bot(bot.accountId, botType, botname, bot.priceMarket.primaryCurrency, bot.priceMarket.secondaryCurrency, bot.priceMarket.contractName).result
  #  print('newbotfrommarket guuid', newbotfrommarket.guid)
   guid = newbotfrommarket.guid
   setup_newbotfrommarket = configuremh(haasomeClient, guid,roilist[i][0], roilist[i][1], roilist[i][2], roilist[i][3], roilist[i][4], roilist[i][5], roilist[i][6], roilist[i][7], roilist[i][8], roilist[i][9], roilist[i][10], roilist[i][11], roilist[i][12])
   configuremhsafety(haasomeClient, guid, 0, 0, 0)
   print(botname, 'has been created')

def makebots2(bot, haasomeClient,botType, roilist):
  for i,v in enumerate(roilist):
   print(i, 'ROI: ', v[13])
  botstocreate = int(input('Type number of how any bots yo would like to create?'))
  for bots in range(0,botstocreate):
   i = int(input('Type bot number to create'))
   botname = str(bot.priceMarket.primaryCurrency) + str(' / ') + \
   str(bot.priceMarket.secondaryCurrency) + str(' Roi ') + str(roilist[i][13])
   newbotfrommarket = haasomeClient.customBotApi.new_custom_bot(bot.accountId, botType, botname, bot.priceMarket.primaryCurrency, bot.priceMarket.secondaryCurrency, bot.priceMarket.contractName).result
   setup_newbot = haasomeClient.customBotApi.setup_mad_hatter_bot(botname, newbotfrommarket.guid, newbotfrommarket.accountId,bot.priceMarket.primaryCurrency,bot.priceMarket.secondaryCurrency, bot.priceMarket.contractName, bot.leverage,  bot.customTemplate,  bot.fundsPosition,  bot.currentFeePercentage,  bot.amountType, bot.currentTradeAmount, bot.useTwoSignals, bot.disableAfterStopLoss, bot.interval,bot.includeIncompleteInterval, bot.mappedBuySignal, bot.mappedSellSignal)
  #  print('newbotfrommarket guuid', newbotfrommarket.guid)
   guid = newbotfrommarket.guid
   setup_newbotfrommarket = configuremh(haasomeClient, guid,roilist[i][0], roilist[i][1], roilist[i][2], roilist[i][3], roilist[i][4], roilist[i][5], roilist[i][6], roilist[i][7], roilist[i][8], roilist[i][9], roilist[i][10], roilist[i][11], roilist[i][12])
   configuremhsafety(haasomeClient, guid, 0, 0, 0)
   print(botname, 'has been created')


import expiration

def worker(haasomeClient, bot, timeinterval, i):
  configuremh(haasomeClient, bot.guid, configs[i][0], configs[i][1], configs[i][2], configs[i][3], configs[i][4], configs[i][5],configs[i][6], configs[i][7], configs[i][8], configs[i][9], configs[i][10], configs[i][11], configs[i][12])
  configuremhsafety(haasomeClient,bot.guid, 0, 0, 0)
  backtest = haasomeClient.customBotApi.backtest_custom_bot_on_market(bot.accountId, bot.guid, timeinterval, bot.priceMarket.primaryCurrency, bot.priceMarket.secondaryCurrency, bot.priceMarket.contractName)
  backtestr = backtest.result
  roi = backtestr.roi
  configroi.append([configs[i][0], configs[i][1], configs[i][2], configs[i][3], configs[i][4], configs[i][5],	configs[i][6], configs[i][7], configs[i][8], configs[i][9], configs[i][10], configs[i][11], configs[i][12], roi])
  print('ROI:', roi, 'Bot configuration :', configs[i][0], configs[i][1], configs[i][2], configs[i][3], configs[i][4], configs[i][5],configs[i][6], configs[i][7], configs[i][8], configs[i][9], configs[i][10], configs[i][11], configs[i][12]) #backtest.errorCode, backtest.errorMessage
  
  return configroi

def worker2(target):
  configroi = target
  return configroi


# import bt


def main():
  #expiration date setting:
  # expiration.setexpiration('2019-9-01')

  botType = EnumCustomBotType.MAD_HATTER_BOT
  #configuration information
  ip, secret = configserver.validateserverdata()
  haasomeClient = HaasomeClient(ip, secret)
  bot = botsellector.getallmhbots(haasomeClient)

  btresults =  backtestingfrommemory(bot, haasomeClient)
  #creating bots
  makebots2(bot, haasomeClient,botType, btresults)


main()
