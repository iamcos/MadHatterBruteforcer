from haasomeapi.apis.TradeBotApi import TradeBotApi
from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from haasomeapi.HaasomeClient import HaasomeClient
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
import interval as inter
import init
import haasomeapi.enums.EnumIndicator as EnumIndicator
import botsellector
from haasomeapi.enums.EnumFlashSpreadOptions import EnumFlashSpreadOptions
import numpy as np
import interval as iiv

def getFCBotOrderList(bot):
	#Returns Flash-Crash Bot current open orders list
	orders = []
	for i in bot.slots:
		orders.append(bot.slots[i])
	return orders

def showbotconfig(bot):
	bot = bot
	# print(bot.__dict__)
	print(bot.priceSpreadType, bot.priceSpread)
	return bot

def configfcb(bot):
	#Configure brute-forcing parameters for Flash-Crash Bot based on its current mode.
	bot = bot
	haasomeClient = init.connect()
	#Fixed Ammount configuration
	if bot.priceSpreadType == 1:
		print('bot price spread type is set to Fixed ammount.\n')
		pricespread_min = float(input('Type spread min between orders in secondary currency : '))
		pricespread_max = float(input('Type spread max between orders in secondary currency : '))
		pricespread_step = float(input('Type spread step between max and min spread in secondary currency : '))
		

	#Percentage configuration
	elif bot.priceSpreadType == 0:
		print('bot price spread type is set to percentage.\n')
		pricespread = input('Type spread in decimal as 0.1: ')
	#Exponential configuration
	elif bot.priceSpreadType == 3:
		print('bot price spread type is set to exponential.\n')
		percentageboost = input('Type multiplyer in decimal as 0.1: ')
		minpercentage = input('Type minimum percentage in decimal as 0.2: ')
		maxpercentage = input('Type maximum percentage in decimal as 20.01: ')
	else:
		print('current FCB spread type is unsupported')

	def cfg(accountguid=bot.accountId, botguid=bot.guid, botname=bot.name, primarycoin=bot.priceMarket.primaryCurrency, secondarycoin=bot.priceMarket.secondaryCurrency, fee=bot.currentFeePercentage, baseprice=bot.basePrice, priceSpreadType=bot.priceSpreadType, pricespread=bot.priceSpread, percentageboost=bot.percentageBoost, minpercentage=bot.minPercentage,maxpercentage=bot.maxPercentage,amounttype=bot.amountType, amountspread=bot.amountSpread, buyamount=bot.totalBuyAmount, sellamount=bot.totalSellAmount, refilldelay=bot.refillDelay, safetyenabled=bot.safetyEnabled, safetytriggerlevel=bot.safetyTriggerLevel, safetymovein=bot.safetyMoveInMarket, safetymoveout=bot.safetyMoveOutMarket,followthetrend=bot.followTheTrend, followthetrendchannelrange=bot.followTheTrendChannelRange, followthetrendchanneloffset=bot.followTheTrendChannelOffset, followthetrendtimeout=bot.followTheTrendTimeout
):
		cfg = haasomeClient.customBotApi.setup_flash_crash_bot(accountguid=bot.accountId, botguid=bot.guid, botname=bot.name, primarycoin=bot.priceMarket.primaryCurrency, secondarycoin=bot.priceMarket.secondaryCurrency, fee=bot.currentFeePercentage, baseprice=bot.basePrice, priceSpreadType=EnumFlashSpreadOptions(bot.priceSpreadType), pricespread=bot.priceSpread, percentageboost=bot.percentageBoost, minpercentage=bot.minPercentage,maxpercentage=bot.maxPercentage,amounttype=bot.amountType, amountspread=bot.amountSpread, buyamount=bot.totalBuyAmount, sellamount=bot.totalSellAmount, refilldelay=bot.refillDelay, safetyenabled=bot.safetyEnabled, safetytriggerlevel=bot.safetyTriggerLevel, safetymovein=bot.safetyMoveInMarket, safetymoveout=bot.safetyMoveOutMarket,followthetrend=bot.followTheTrend, followthetrendchannelrange=bot.followTheTrendChannelRange, followthetrendchanneloffset=bot.followTheTrendChannelOffset, followthetrendtimeout=bot.followTheTrendTimeout)
		print('configuring bot parameters: ', cfg.errorCode, cfg.errorMessage)
		ticks = iiv.readinterval()
		bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(bot.accountId,bot.guid,ticks,bot.priceMarket.primaryCurrency,bot.priceMarket.secondaryCurrency,bot.priceMarket.contractName)
		print('backtesting bot parameters: ', bt.errorCode, bt.errorMessage)
		print(bt.result.roi, pricespread)
		return cfg.result


	for pricespread in np.arange(pricespread_min,pricespread_max, pricespread_step):
			bot = cfg(pricespread = round(pricespread,2))


def main():
	haasomeClient = init.connect()
	bot = botsellector.getallfcbots(haasomeClient)
	trysetup = configfcb(bot)
	# bot = showbotconfig(bot)
	# configure = configurefcbbotparam(bot)
	# bt = btfcb(bot, 0.1, 1.0, 0.1, interval, haasomeClient)

if __name__ == '__main__':
	main()