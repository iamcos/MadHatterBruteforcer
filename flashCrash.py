from haasomeapi.apis.TradeBotApi import TradeBotApi
from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from haasomeapi.HaasomeClient import HaasomeClient
import interval as inter
import init
import haasomeapi.enums.EnumIndicator as EnumIndicator
import botsellector
import numpy as np

ip, secret = init.connect()

haasomeClient = HaasomeClient(ip, secret)

def getFCBotOrderList(bot):
	orders = []
	for i in bot.slots:
		orders.append(bot.slots[i])
	return orders

def configFCBot(bot, haasomeClient):
	bot = haasomeClient.customBotApi.setup_flash_crash_bot(bot.accountId, bot.guid, bot.name, bot.priceMarket.primaryCurrency, bot.priceMarket.secondaryCurrency, bot.currentFeePercentage, bot.basePrice, bot.priceSpreadType, bot.priceSpread, bot.percentageBoost, bot.minPercentage,bot.maxPercentage,bot.amountType, bot.amountSpread, bot.totalBuyAmount, bot.totalSellAmount, bot.refillDelay, bot.safetyEnabled, bot.safetyTriggerLevel, bot.safetyMoveInMarket, bot.safetyMoveOutMarket,bot.followTheTrend, bot.followTheTrendChannelRange, bot.followTheTrendChannelOffset, bot.followTheTrendTimeout)
	print(bot.errorCode, bot.errorMessage)

def btspreadranga(bot, start, stop, step, interval,haasomeClient):
	for spread in np.arange(start, stop, step):
		bot = haasomeClient.customBotApi.setup_flash_crash_bot(bot.accountId, bot.guid, bot.name, bot.priceMarket.primaryCurrency, bot.priceMarket.secondaryCurrency, bot.currentFeePercentage, bot.basePrice, bot.priceSpreadType, spread, bot.percentageBoost, bot.minPercentage,bot.maxPercentage,bot.amountType, bot.amountSpread, bot.totalBuyAmount, bot.totalSellAmount, bot.refillDelay, bot.safetyEnabled, bot.safetyTriggerLevel, bot.safetyMoveInMarket, bot.safetyMoveOutMarket,bot.followTheTrend, bot.followTheTrendChannelRange, bot.followTheTrendChannelOffset, bot.followTheTrendTimeout)
		bot = bot.result
		bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(bot.accountId, bot.guid, interval, bot.priceMarket.primaryCurrency, bot.priceMarket.secondaryCurrency,'')
		print(bt.result.roi)
		
		# bt = haasomeClient.customBotApi.backtest_custom_bot(bot.guid,interval)
		
		print(bt.errorCode, bt.errorMessage)

	

def main():
	interval = int(inter.inticks(2019,8,26, 5))
	bot = botsellector.getallfcbots(haasomeClient)

	bt = btspreadranga(bot, 0.1, 1.0, 0.1, interval, haasomeClient)

if __name__ == '__main__':
	main()