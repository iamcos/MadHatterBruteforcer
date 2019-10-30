import pandas as pd
import numpy as np
from botdatabase import BotDB
import plotly.graph_objects as go
import datetime
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

def csv_to_data_array():
	nhlDF = pd.read_csv('allbots2.csv')
	# nhlDF.reset_index( inplace=True)
	nhlDF.set_index(['primarycoin','secondarycoin','interval','rsil', 'rsib', 'rsis', 'bbl', 'devup', 'devdn'], inplace=True)
	nhlDF.sort_index(inplace=True)

	# print(nhlDF.index)
	print(nhlDF.head(20))
	print(nhlDF.tail(20))



def market_and_trade_data_combination(marketdata_csv,botobject_db):
	marketdata = pd.read_csv(marketdata_csv)
	marketdata['timeStamp'] = pd.to_datetime(marketdata['timeStamp'])
	botlist = BotDB.load_botlist(botobject_db)

	orderbook2 =pd.DataFrame(columns = ['bot_guid', 'orderbook', 'timeStamp', 'price', 'type'])
	orderbook = pd.DataFrame()
	for bot in botlist:
			orderlist = [(x.pair, x.orderType, x.price, x.amountFilled	, x.unixAddedTime) for x in bot.completedOrders]
	
	df = pd.DataFrame(orderlist)
	df.melt(df)

	df['timeStamp'] = pd.to_datetime(df['timeStamp'],unit='s')
	marketdata2 = pd.merge(marketdata, df, how = 'left', on = 'timeStamp')
	return marketdata2


def candlesticks_with_trades(market_and_trades_DataFrame):
	plt.figure()
	market_and_trades_DataFrame.plot(kind='line', x = 'timeStamp', y = [ 'price', 'currentBuyValue']) 
	fig = go.Figure(data=[go.Candlestick(x=market_and_trades_DataFrame['timeStamp'],
		open=market_and_trades_DataFrame['open'],
		high=market_and_trades_DataFrame['highValue'],
		low=market_and_trades_DataFrame['lowValue'],
		close=market_and_trades_DataFrame['close'])])
	fig.add_trace(go.Scatter(x=market_and_trades_DataFrame['timeStamp'],y=market_and_trades_DataFrame['price'], mode = 'markers', name='markers',marker_color='rgba(152, 0, 0, .8)'))

	fig.show()

def main():

	d = market_and_trade_data_combination('EOS\BTC 10080.csv','EOS\BTC 10080.db')
	# print(d)
if __name__ == '__main__':
		main()

