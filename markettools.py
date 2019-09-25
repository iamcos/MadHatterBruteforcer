
from haasomeapi.HaasomeClient import HaasomeClient
import botsellector
import configparser_cos
import configserver
import json
import savehistory
from 		haasomeapi.dataobjects.accountdata.BaseOrder import BaseOrder
from datetime import datetime


import plotly.express as px
import pandas as pd




from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
ip, secret = configserver.validateserverdata()
haasomeClient = HaasomeClient(ip, secret)
class GlobalCover:
	def __init__(self, market, configs, indicators,)
	allmarkets = haasomeClient.marketDataApi.get_all_price_markets()

class ContiniousBacktesting():
	pass

def backtesting_visualization(bot):
	if len(bot.completedOrders) > 0:
		start_time = bot.completedOrders[0]['addedTime']
		today = datetime.date.today()
		requiredhistorylength = (today-start_time)
		
		marketdata = savehistory.market_history(bot.priceMarket, requiredhistorylength, bot.interval)
		pdmarketdata = pd.
		marketdata = px.data.marketdata()
		fig = px.box(marketdata, y="addedTime")
		fig.show()

	backtesting_visualization()