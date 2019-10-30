import pickle
import pandas
import numpy
import init


ip, secret = init.connect()
haasomeClient = HaasomeClient(ip, secret)


class NaseHistoryModule:

	def __init__(self, botobject, btdb, recomendations):
		self.botobject = botobject
		self.btdb = btdb
		self.recomendations = recomendations

class btDb:
	def __init__(self,botobject, bt_record, latestMarkets, similarpairs):
		self.botobject = botobject
		self.bt_record = bt_record
		self.latestMarkets = latestMarkets
		self.optimisations = optimisations
		pass

class basebtevemt:
	def __init__(self, btevent):
		self.btevent = btevent

class btevent:
	def __init__(self, ordebook, botconfigstack, optimisations, profitableperiods):
		self.ordebook = ordebook
		self.botconfigstack = botconfigstack
		self.optimisations = optimisations
		self.profitableperiods

class uniquecombination:
		def __init__(self, bot_type, current_trend, safeties, indicators, insurances, other_params, goodroi_periods):
			self.bot_type = bot_type
			self.safeties = safeties
			self.indicators = indicators
			self.other_params = other_params
			

class optimisation_field:
		def __init__(self, common_good_configs, rules, testedcombinations):
		self.common_good_configs = common_good_configs
		self.rules = rules
		self.testedcombinations = testedcombinations
		self.untestedcombinations = untestedcombinations

class sentimentmonitoring:
	def __init__(self, anomalies_with_sentiment, public_promise, current_state, anomalyDb):
		self.

class sentimenttickdata:
	def __init__(self, coin, current_state, sentimenttickdata, sensitivity):
	self.current_state = current_state
	self.sentimenttickdata = sentimenttickdata
	self.sensitivity = sensitivity 