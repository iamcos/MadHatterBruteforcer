from __future__ import print_function

import csv
import datetime
import time
from pathlib import Path

import dash
import haasomeapi.enums.EnumErrorCode as EnumErrorCode
import ipywidgets as widgets
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly as py
import plotly.graph_objects as go
import spicy as special
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
from haasomeapi.enums.EnumOrderType import EnumOrderType
from haasomeapi.enums.EnumPriceSource import EnumPriceSource
from haasomeapi.HaasomeClient import HaasomeClient
from ipywidgets import fixed, interact, interact_manual, interactive

import botsellector
import init
import interval as iiv
import rotator

matplotlib.style.use('ggplot')



# py.offline.init_notebook_mode(connected = True)
haasomeClient = init.connect()


def get_specific_market():
	markets = {}
	all_price_sources = haasomeClient.marketDataApi.get_enabled_price_sources().result
	primarycurrency = []
	secondarycurrency = []
	pairs = []
	for i,market in enumerate(all_price_sources):
		# markets[market] = haasomeClient.marketDataApi.get_price_markets(21).result
		markets[market] = haasomeClient.marketDataApi.get_price_markets(EnumPriceSource[market.upper()]).result
		print(i, market)
	user_input = int(input('Type market number to select'))
	market = all_price_sources[user_input]
	for market in markets[market]:
		if market.secondaryCurrency not in secondarycurrency:
			secondarycurrency.append(market.secondaryCurrency)
		if market.primaryCurrency not in primarycurrency:
			primarycurrency.append(market.primaryCurrency)
		if market.secondaryCurrency and market.primaryCurrency not in pairs:
			pairs.append([market.secondaryCurrency, market.primaryCurrency, market.contractName])
	print(pairs)

class MarketData:

	def get_market_data(bot):
		ticks = iiv.readinterval()
		market_history_request = haasomeClient.marketDataApi.get_history(
			bot.priceMarket.priceSource,
			bot.priceMarket.primaryCurrency,
			bot.priceMarket.secondaryCurrency,
			bot.priceMarket.contractName,
			bot.interval,
			ticks)
		print('downloading history for ', bot.priceMarket.primaryCurrency, bot.priceMarket.secondaryCurrency)
		print(market_history_request.errorCode.value)
		if market_history_request.errorCode.value == 100:
			market_history = market_history_request.result
			if len(market_history_request.result) != 0:
				print(len(market_history_request.result), 'ticks of market history retrieved')
				return market_history
			else:
				print('But', len(market_history_request.result), 'means nothing was recieved' )
		else:
			print('things did not go as planned. aborting')

	
	def to_df(market_history):
		
		# market_data = [(None,x.unixTimeStamp,x.open,x.highValue, x.lowValue,x.close,x.volume,x.currentBuyValue,x.currentSellValue) for x in market_history]
		market_data = [{'timeStamp':x.timeStamp,'unixTimeStamp':pd.to_datetime(x.unixTimeStamp,unit='s'),'open':x.open,'highValue':x.highValue, 'lowValue':x.lowValue,'close':x.close,'volume':x.volume,'currentBuyValue':x.currentBuyValue,'currentSellValue':x.currentSellValue} for x in market_history]
		# print(market_data)
		# market_history_dataframe = pd.DataFrame(market_data, index= ('timeStamp','unixTimeStamp','open','highValue', 'lowValue','close','volume','currentBuyValue','currentSellValue'))
		df = pd.DataFrame(market_data)
		return df

	def df_to_csv(df, bot):
		ticks = iiv.readinterval()
		filename = (
			str(bot.priceMarket.primaryCurrency)
			+ "\\"
			+ str(bot.priceMarket.secondaryCurrency)
			+ " "
			+ str(ticks)
			+ ".csv")
		df.to_csv(filename)
		print('Market History Sucessfuly Saved to CSV')

class BotScripts:

		def orders_to_df(bot):

		#turns completed orders to dataframe. If bot has no orders then returns
			if len(bot.completedOrders) > 0:
				completedOrders = [{'pair': (x.pair.primaryCurrency, x.pair.secondaryCurrency), 'orderId':x.orderId,'orderStatus':x.orderStatus, 'orderType':x.orderType, 'price': x.price,'amount':x.amount,'amountFilled':x.amountFilled,'unixTimeStamp':pd.to_datetime(x.unixAddtoredTime,unit='s')} for x in bot.completedOrders]
				orders_df = pd.DataFrame(completedOrders)

			else:
				completedOrders = [{'pair': None, 'orderId': None,'orderStatus':None, 'orderType':None, 'price': None,'amount':None,'amountFilled':None,'unixTimeStamp':datetime.today}for x in range(1)]
				orders_df = pd.DataFrame(completedOrders)
			return orders_df

		def backtest_bots(bot):
			results, bot_object_list  = rotator.backtestingfrommemory(bot, haasomeClient)
			return bot_object_list


	def combine_orders_with_history(df, orders_df):
	#does what it says - combines into a single dataframe orders and history for future use. 
		history_with_orders = pd.merge(df,orders_df,how = 'left', on = 'unixTimeStamp')
			# history_with_orders['unixTimeStamp'] = pd.to_datetime(history_with_orders['unixTimeStamp'])

		return history_with_orders

		def calculate_profit_lables(orders_df):
			print(orders_df)
			for index, row in orders_df.iterrows():
			
					if orders_df.loc[index,'orderType'] == 0:
						if orders_df.loc[index, 'price'] != 0:
							orders_df.loc[index,'profit'] = orders_df.loc[index, 'price'] + orders_df.loc[str(int(index) - 1), 'price']
					else:
						orders_df.loc[index,'profit'] = orders_df.loc[index, 'price'] - orders_df.loc[str(int(index) - 1), 'price']
			print(orders_df)
			return orders_df

class Plot:

	def plot_bot_trades(history_with_orders):
		plt.figure()
		history_with_orders.plot(kind='line', x = 'unixTimeStamp', y = [ 'price', 'currentBuyValue']) 
		fig = go.Figure(data=[go.Candlestick(x=history_with_orders['unixTimeStamp'],
			open=history_with_orders['open'],
			high=history_with_orders['highValue'],
			low=history_with_orders['lowValue'],
			close=history_with_orders['close'])])
		fig.add_trace(go.Scatter(x=history_with_orders['unixTimeStamp'],y=history_with_orders['price'], mode = 'markers', name='markers',marker_color='rgba(0, 152, 26, 1.8)'))
		# fig.add_trace(go.Scatter (mode = 'markers', x=history_with_orders['unixTimeStamp'],y=history_with_orders['price'], marker = dict(color = 'LightSkyBlue', size=120)))

		fig.show()

def plot_bot_trades2(history_with_orders):
	plt.figure()
	history_with_orders.plot(kind = 'line', x = 'unixTimeStamp', y = [ 'currentBuyValue'])
	fig = go.figure(data=[go.Candlestick(x=history_with_orders['unixTimeStamp'],
		open=history_with_orders['open'],
		high=history_with_orders['highValue'],
		low=history_with_orders['lowValue'],
		close=history_with_orders['close'],
		title = 'Trade History',
		updatemenus=[dict(
				type="buttons",
				buttons=[dict(label="Play",
						method="animate",
						args=[None])])])]),

	fig.add_trace(go.Scatter(x=history_with_orders['unixTimeStamp'],y=history_with_orders['price'], mode = 'markers', marker = dict(size=20, color='LightSkyBlue'), name = 'trades'))

	def plot_bots(botlist):
		#incomplete i think
		market_history = MarketData.get_market_data(botlist[0])
		mh_df = MarketData.to_df(market_history)
		plt.figure()
		mh_df.plot(kind='line', x = 'unixTimeStamp', y = ['currentBuyValue'])
		fig = go.Figure(data=[go.Candlestick(x=mh_df['unixTimeStamp'],
			open=mh_df['open'],
			high=mh_df['highValue'],
			low=mh_df['lowValue'],
			close=mh_df['close'])])
		for bot in botlist:
			if len(bot.completedOrders)>0:
				orders_df = MarketData.BotScripts.orders_to_df(bot)
				fig.add_trace(go.Scatter(x = orders_df['unixTimeStamp'], y = orders_df['price'], mode = 'markers', marker = dict(size=20), name = str(bot.roi)+' ROI '+str(bot.guid)))

		fig.show()


def bot_to_plot(bot):
	#Gets market history, turns it into data frame, then does the same for bot orders and plots it on a graph
	market_history = MarketData.get_market_data(bot)
	mh_df = MarketData.to_df(market_history)
	orders = MarketData.BotScripts.orders_to_df(bot)
	orders_ticks = combine_orders_with_history(mh_df, orders)
	# Plot.plot_bot_trades(orders_ticks)
	plot_bot_trades2(orders_ticks)

def make_frames(botlist):
	#Frames are used to animate a graph with different data
	market_history = MarketData.get_market_data(botlist[0])
	mh_df = MarketData.to_df(market_history)
	frames = []
	for bot in botlist:
		orders = MarketData.BotScripts.orders_to_df(bot)
		frames.append(go.Frame(data=[go.Scatter(x = mh_df['unixTimeStamp'], y = orders['price'], name= bot.guid)]))
	frames.append(go.Layout(title_text="End Title"))
	# print(frames)
	return frames, mh_df


def botlist_orderbook_combine_with_market_ticks(botlist):
	market_history = MarketData.get_market_data(botlist[0])
	histories_with_orders = []
	mh_df = MarketData.to_df(market_history)
	for bot in botlist:
		orders = MarketData.BotScripts.orders_to_df(bot)
		orders_ticks = combine_orders_with_history(mh_df, orders)
		histories_with_orders.append([bot.roi,bot.guid,orders_ticks])
	return histories_with_orders



def main5():
	bot = botsellector.getallmhbots(haasomeClient)
	orders_df = MarketData.BotScripts.orders_to_df(bot)
	orders_df_with_profit = calculate_profit_lables(orders_df)


def main4():
	bot = botsellector.getallmhbots(haasomeClient)
	(haasomeClient)
	botobjects = backtest_bots(bot)
	Plot.plot_bots(botobjects)

def main3():
	bot = botsellector.getallmhbots(haasomeClient)
	(haasomeClient)
	bot_to_plot(bot)

def main2():
	bot = botsellector.getallmhbots(haasomeClient)
	(haasomeClient)
	botobjects = backtest_bots(bot)
	orders_on_market_history = MarketData.botlist_orderbook_combine_with_market_ticks(botobjects)
	Plot.plot_bots(orders_on_market_history)

	#
	#  print(mh_df)
def main6():
	# bot = botsellector.getallbots(haasomeClient)
	ticks = iiv.readinterval()
	# save_single_market_history(bot, ticks)
	get_specific_market()

def main():
	pass


if __name__ == "__main__":
	main4()

	