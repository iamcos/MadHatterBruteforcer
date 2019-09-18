from haasomeapi.apis.TradeBotApi import TradeBotApi
from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from haasomeapi.HaasomeClient import HaasomeClient
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
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

def showbotconfig(bot):
	bot = bot
	# print(bot.__dict__)
	print(bot.priceSpreadType, bot.priceSpread)
	return bot

def configurefcbbotparam(bot):
	haasomeClient = HaasomeClient(ip, secret)
	cfg = haasomeClient.customBotApi.setup_flash_crash_bot(accountguid=bot.accountId, botguid=bot.guid, botname=bot.name, primarycoin=bot.priceMarket.primaryCurrency, secondarycoin=bot.priceMarket.secondaryCurrency, fee=bot.currentFeePercentage, baseprice=bot.basePrice, priceSpreadType=bot.priceSpreadType, pricespread=bot.priceSpread, percentageboost=bot.percentageBoost, minpercentage=bot.minPercentage,maxpercentage=bot.maxPercentage,amounttype=bot.amountType, amountspread=bot.amountSpread, buyamount=bot.totalBuyAmount, sellamount=bot.totalSellAmount, refilldelay=bot.refillDelay, safetyenabled=bot.safetyEnabled, safetytriggerlevel=bot.safetyTriggerLevel, safetymovein=bot.safetyMoveInMarket, safetymoveout=bot.safetyMoveOutMarket,followthetrend=bot.followTheTrend, followthetrendchannelrange=bot.followTheTrendChannelRange, followthetrendchanneloffset=bot.followTheTrendChannelOffset, followthetrendtimeout=bot.followTheTrendTimeout)
	print('configuring bot parameters: ', cfg.errorCode, cfg.errorMessage)
	return cfg.result


def btfcb(bot, haasomeClient, ticks):	
	bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountId=bot.accountId, guid=bot.guid, ticks=ticks, primaryCurrency=bot.priceMarket.primaryCurrency, secondaryCurrency=bot.priceMarket.secondaryCurrency)
	print(bt.errorMessage, bt.errorCode)
	return bt.result

def setspread(bot):
	haasomeClient = HaasomeClient(ip, secret)

	if bot.priceSpreadType == 1:
		print('bot price spread type is set to Fixed ammount.\n')
		spread = input('Type spread between orders in secondary currency : ')
		cfg = haasomeClient.customBotApi.setup_flash_crash_bot(accountguid=bot.accountId, botguid=bot.guid, botname=bot.name, primarycoin=bot.priceMarket.primaryCurrency, secondarycoin=bot.priceMarket.secondaryCurrency, fee=bot.currentFeePercentage, baseprice=bot.basePrice, priceSpreadType=bot.priceSpreadType, pricespread=bot.priceSpread, percentageboost=bot.percentageBoost, minpercentage=bot.minPercentage,maxpercentage=bot.maxPercentage,amounttype=bot.amountType, amountspread=bot.amountSpread, buyamount=bot.totalBuyAmount, sellamount=bot.totalSellAmount, refilldelay=bot.refillDelay, safetyenabled=bot.safetyEnabled, safetytriggerlevel=bot.safetyTriggerLevel, safetymovein=bot.safetyMoveInMarket, safetymoveout=bot.safetyMoveOutMarket,followthetrend=bot.followTheTrend, followthetrendchannelrange=bot.followTheTrendChannelRange, followthetrendchanneloffset=bot.followTheTrendChannelOffset, followthetrendtimeout=bot.followTheTrendTimeout)
		print('configuring bot parameters: ', cfg.errorCode, cfg.errorMessage)
		return cfg.result
	if bot.priceSpreadType == 0:
		print('bot price spread type is set to percentage.\n')
		spread = input('Type spread in decimal as 0.1: ')
		cfg = haasomeClient.customBotApi.setup_flash_crash_bot(accountguid=bot.accountId, botguid=bot.guid, botname=bot.name, primarycoin=bot.priceMarket.primaryCurrency, secondarycoin=bot.priceMarket.secondaryCurrency, fee=bot.currentFeePercentage, baseprice=bot.basePrice, priceSpreadType=, pricespread=spread, percentageboost=bot.percentageBoost, minpercentage=bot.minPercentage,maxpercentage=bot.maxPercentage,amounttype=bot.amountType, amountspread=bot.amountSpread, buyamount=bot.totalBuyAmount, sellamount=bot.totalSellAmount, refilldelay=bot.refillDelay, safetyenabled=bot.safetyEnabled, safetytriggerlevel=bot.safetyTriggerLevel, safetymovein=bot.safetyMoveInMarket, safetymoveout=bot.safetyMoveOutMarket,followthetrend=bot.followTheTrend, followthetrendchannelrange=bot.followTheTrendChannelRange, followthetrendchanneloffset=bot.followTheTrendChannelOffset, followthetrendtimeout=bot.followTheTrendTimeout)
		print('configuring bot parameters: ', cfg.errorCode, cfg.errorMessage)
		return cfg.result
	if bot.priceSpreadType == 2:
		print('bot price spread type is set to percentage with boost.\n')
		spread = input('Type spread in decimal as 0.1: ')
		boost = input('Type boost percentage in decimal as 1.01: ')
		cfg = haasomeClient.customBotApi.setup_flash_crash_bot(accountguid=bot.accountId, botguid=bot.guid, botname=bot.name, primarycoin=bot.priceMarket.primaryCurrency, secondarycoin=bot.priceMarket.secondaryCurrency, fee=bot.currentFeePercentage, baseprice=bot.basePrice, priceSpreadType=bot.priceSpreadType, pricespread=spread, percentageboost=boost, minpercentage=bot.minPercentage,maxpercentage=bot.maxPercentage,amounttype=bot.amountType, amountspread=bot.amountSpread, buyamount=bot.totalBuyAmount, sellamount=bot.totalSellAmount, refilldelay=bot.refillDelay, safetyenabled=bot.safetyEnabled, safetytriggerlevel=bot.safetyTriggerLevel, safetymovein=bot.safetyMoveInMarket, safetymoveout=bot.safetyMoveOutMarket,followthetrend=bot.followTheTrend, followthetrendchannelrange=bot.followTheTrendChannelRange, followthetrendchanneloffset=bot.followTheTrendChannelOffset, followthetrendtimeout=bot.followTheTrendTimeout)
		print('configuring bot parameters: ', cfg.errorCode, cfg.errorMessage)
		return cfg.result
	if bot.priceSpreadType == 3:
		print('bot price spread type is set to exponential.\n')
		boost = input('Type multiplyer in decimal as 0.1: ')
		minp = input('Type minimum percentage in decimal as 0.2: ')
		maxp = input('Type maximum percentage in decimal as 20.01: ')
		cfg = haasomeClient.customBotApi.setup_flash_crash_bot(accountguid=bot.accountId, botguid=bot.guid, botname=bot.name, primarycoin=bot.priceMarket.primaryCurrency, secondarycoin=bot.priceMarket.secondaryCurrency, fee=bot.currentFeePercentage, baseprice=bot.basePrice, priceSpreadType=bot.priceSpreadType, pricespread=spread, percentageboost=boost, minpercentage=minp,maxpercentage=maxp,amounttype=bot.amountType, amountspread=bot.amountSpread, buyamount=bot.totalBuyAmount, sellamount=bot.totalSellAmount, refilldelay=bot.refillDelay, safetyenabled=bot.safetyEnabled, safetytriggerlevel=bot.safetyTriggerLevel, safetymovein=bot.safetyMoveInMarket, safetymoveout=bot.safetyMoveOutMarket,followthetrend=bot.followTheTrend, followthetrendchannelrange=bot.followTheTrendChannelRange, followthetrendchanneloffset=bot.followTheTrendChannelOffset, followthetrendtimeout=bot.followTheTrendTimeout)
		print('configuring bot parameters: ', cfg.errorCode, cfg.errorMessage)
		return cfg.result
	




def main():
	interval = int(inter.inticks(2019,8,26, 5))
	bot = botsellector.getallfcbots(haasomeClient)
	trysetup = setspread(bot)
	# bot = showbotconfig(bot)
	# configure = configurefcbbotparam(bot)
	# bt = btfcb(bot, 0.1, 1.0, 0.1, interval, haasomeClient)

if __name__ == '__main__':
	main()