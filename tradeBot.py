from haasomeapi.apis.TradeBotApi import TradeBotApi
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import \
    IndicatorOption
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from haasomeapi.HaasomeClient import HaasomeClient

import init

ip, secret = init.connect()

haasomeClient = HaasomeClient(ip, secret)






def getTradeBots(haasomeClient):
	alltradebots = haasomeClient.tradeBotApi.get_all_trade_bots()
	if alltradebots.errorCode != EnumErrorCode.SUCCESS:
		return alltradebots.errorCode, alltradebots.errorMessage
	else: 
		return alltradebots.result

def printTradeBotList(haasomeClient,alltradebots):
	for i, bot in enumerate(alltradebots):
		print(i, bot.name, bot.priceMarket.primaryCurrency+'\\'+bot.priceMarket.secondaryCurrency, len(bot.completedOrders),' orders')
	user_response = input('\nType in bot number to select it: ')
	currentbot = alltradebots[int(user_response)]
	return currentbot

def botconfig(haasomeClient,bot):
		for safety in bot.safeties:
			print(safety)
		for indicator in bot.indicators:
			print(indicator)
		for insurance in bot.insurances:
			print(insurance)


def main():
	alltradebots = getTradeBots(haasomeClient)
	
	print('\n')
	bot = printTradeBotList(haasomeClient,alltradebots)
	print('\n')
	botconfig(haasomeClient,bot)


if __name__ == '__main__':
	main()
