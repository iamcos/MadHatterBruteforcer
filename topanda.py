import pandas as pd
import os

from haasomeapi.apis.ApiBase import ApiBase
from haasomeapi.apis.TradeBotApi import TradeBotApi
from haasomeapi.apis.CustomBotApi import CustomBotApi
from haasomeapi.HaasomeClient import HaasomeClient
import json
from pprint import pprint
import configserver
import init
import interval as iiv
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
ip, secret = init.connect()
haasomeClient = HaasomeClient(ip, secret)
import numpy as np



class BotReader(ApiBase):

	def __init__(self, connectionstring: str, privatekey: str):
			ApiBase.__init__(self, connectionstring, privatekey)

	def _convert_json_bot_to_trade_bot_object(self, jsonstr: str):
					""" Internal function to easily convert json to Tradebot objet
					:param jsonstr: str: Tradebot in a json string

					:returns: :class:`~haasomeapi.dataobjects.tradebot.TradeBot`
					"""

					botinitial = super()._from_json(jsonstr, TradeBot)

					indicators = {}
					safeties = {}
					insurances = {}

					for k, v in botinitial.indicators.items():
									indicatoroptions = []
									indicator = super()._from_json(v, Indicator)
									for indicatoroption in indicator.indicatorInterface:
													indicatoroptions.append(super()._from_json(indicatoroption, IndicatorOption))
									indicator.indicatorInterface = indicatoroptions
									indicators[k] = indicator

					for k, v in botinitial.safeties.items():
									safetyoptions = []
									safety = super()._from_json(v, Safety)
									for safetyoption in safety.safetyInterface:
													safetyoptions.append(super()._from_json(safetyoption, IndicatorOption))
									safety.safetyInterface = safetyoptions
									safeties[k] = safety

					for k, v in botinitial.insurances.items():
									insuranceoptions = []
									insurance = super()._from_json(v, Insurance)
									for insuranceoption in insurance.insuranceInterface:
													insuranceoptions.append(super()._from_json(insuranceoption, IndicatorOption))
									insurance.insuranceInterface = insuranceoptions
									insurances[k] = insurance

					botinitial.indicators = indicators
					botinitial.safeties = safeties
					botinitial.insurances = insurances

					return botinitial
	def _convert_json_bot_to_custom_bot_object(self, jsonstr: str):
						""" Internal function to easily convert json strings to BaseCustomBot objects
						:param jsonstr: str: 

						:returns: :class:`~haasomeapi.dataobjects.custombots.BaseCustomBot`
						"""

						botinitial = super()._from_json(jsonstr, BaseCustomBot)

						orders = []

						for corder in botinitial.completedOrders:
										orders.append(super()._from_json(corder, BaseOrder))

						botinitial.completedOrders = orders

						botinitial.priceMarket = super()._from_json(botinitial.priceMarket, Market)

						return botinitial

	def _convert_json_bot_to_custom_bot_specific(self, bottype: EnumCustomBotType, jsonstr: str):
					""" Internal function to easily convert json strings to specific custom bot objects
					:param bottype: :class:`~haasomeapi.enums.EnumCustomBotType`
					:param jsonstr: str: 
					:returns: any: Returns a Class Instance of bottype specified
					"""

					botinitial = None

					if bottype == EnumCustomBotType.BASE_CUSTOM_BOT:
									botinitial = super()._from_json(jsonstr, BaseCustomBot)
					if bottype == EnumCustomBotType.MARKET_MAKING_BOT:
									botinitial = super()._from_json(jsonstr, MarketMakingBot)
					if bottype == EnumCustomBotType.PING_PONG_BOT:
									botinitial = super()._from_json(jsonstr, BaseCustomBot)
					if bottype == EnumCustomBotType.SCALPER_BOT:
									botinitial = super()._from_json(jsonstr, ScalperBot)
					if bottype == EnumCustomBotType.ORDER_BOT:
									botinitial = super()._from_json(jsonstr, OrderBot)
					if bottype == EnumCustomBotType.FLASH_CRASH_BOT:
									botinitial = super()._from_json(jsonstr, FlashCrashBot)
					if bottype == EnumCustomBotType.INTER_EXCHANGE_ARBITRAGE_BOT:
									botinitial = super()._from_json(jsonstr, InterExchangeArbitrageBot)
					if bottype == EnumCustomBotType.INTELLIBOT_ALICE_BOT:
									botinitial = super()._from_json(jsonstr, BaseCustomBot)
					if bottype == EnumCustomBotType.ZONE_RECOVERY_BOT:
									botinitial = super()._from_json(jsonstr, ZoneRecoveryBot)
					if bottype == EnumCustomBotType.ACCUMULATION_BOT:
									botinitial = super()._from_json(jsonstr, AccumulationBot)
					if bottype == EnumCustomBotType.TREND_LINES_BOT:
									botinitial = super()._from_json(jsonstr, BaseCustomBot)
					if bottype == EnumCustomBotType.MAD_HATTER_BOT:
									botinitial = super()._from_json(jsonstr, MadHatterBot)
					if bottype == EnumCustomBotType.SCRIPT_BOT:
									botinitial = super()._from_json(jsonstr, ScriptBot)
					if bottype == EnumCustomBotType.CRYPTO_INDEX_BOT:
									botinitial = super()._from_json(jsonstr, CryptoIndexBot)
					if bottype == EnumCustomBotType.HAAS_SCRIPT_BOT:
									botinitial = super()._from_json(jsonstr, ScriptBot)
					if bottype == EnumCustomBotType.EMAIL_BOT:
									botinitial = super()._from_json(jsonstr, EmailBot)

					orders = []

					for corder in botinitial.completedOrders:
									orders.append(super()._from_json(corder, BaseOrder))

					botinitial.completedOrders = orders

					botinitial.priceMarket = super()._from_json(botinitial.priceMarket, Market)

					return botinitial

	def read_bot_file(filename):
				with open(filename) as data_file:
							response = json.load(data_file)
							print(data_file)
							return response

	def get_custom_bot(filename):
  
				response = BotReader.read_bot_file(filename)
				botdata = _from_json(response, cls)
				botdata = _convert_json_bot_to_custom_bot_specific(EnumCustomBotType.MAD_HATTER_BOT, response["Result"])
				print(botdata)
					

     #    # try:
					# return self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.BASE_CUSTOM_BOT, response["Result"]))
        # except:
        #     return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
        #                                  response["ErrorMessage"], {})


	def _from_json(data, cls):
					""" Converts a json response to a class object. Can only go 2 nested deep

					:param data: Json data object 
					:parama cls: Class type to convert to

					:returns: any: A instance of the specified class
					"""

					if type(data) is dict:
									annotations: dict = cls.__annotations__ if hasattr(cls, '__annotations__') else None
									if issubclass(cls, List):
													list_type = cls.__args__[0]
													instance: list = list()
													for value in data:
																	instance.append(ApiBase._from_json(value, list_type))
													return instance
									elif issubclass(cls, Dict):
																	key_type = cls.__args__[0]
																	val_type = cls.__args__[1]
																	instance: dict = dict()
																	for key, value in data.items():
																					instance.update({ApiBase._from_json(key, key_type): ApiBase._from_json(value, val_type)})
																	return instance
									else:
													instance: cls = cls()

													for name, value in data.items():

																	if name == "GUID":
																					name = "guid"
																	elif name == "ROI":
																					name = "roi"
																	else:
																					func = lambda s: s[:1].lower() + s[1:] if s else ''
																					name = func(name)
																					field_type = annotations.get(name)

																	if inspect.isclass(field_type) and isinstance(value, (dict, tuple, list, set, frozenset)):
																					setattr(instance, name, ApiBase._from_json(value, field_type))
																	else:
																					setattr(instance, name, value)
													return instance
					return data



def main():

	# hello = BotReader.get_custom_bot('/Users/cosmos/Documents/dockerapp/BotConfigs/sb_9770b7d7-e617-4788-9561-af1b7e263041.XML').result
	# print(hello)

	lsp = np.logspace(0,10,3)
	print(lsp)

main()