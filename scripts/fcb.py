
bot=haasomeClient.customBotApi.setup_flash_crash_bot(
accountId=bot.accountId,
guid=bot.guid,
name=bot.name,
priceMarket=bot.priceMarket.primaryCurrency,
priceMarket=bot.priceMarket.secondaryCurrency,
currentFeePercentage=bot.currentFeePercentage,
basePrice=bot.basePrice,
priceSpreadType=bot.priceSpreadType,
priceSpread=bot.priceSpread,
percentageBoost=bot.percentageBoost,
minPercentage=bot.minPercentage,
maxPercentage=bot.maxPercentage,
amountType=bot.amountType,
amountSpread=bot.amountSpread,
totalBuyAmount=bot.totalBuyAmount,
totalSellAmount=bot.totalSellAmount,
refillDelay=bot.refillDelay,
safetyEnabled=bot.safetyEnabled,
safetyTriggerLevel=bot.safetyTriggerLevel,
safetyMoveInMarket=bot.safetyMoveInMarket,
safetyMoveOutMarket=bot.safetyMoveOutMarket,
followTheTrend=bot.followTheTrend,
followTheTrendChannelRange=bot.followTheTrendChannelRange,
followTheTrendChannelOffset=bot.followTheTrendChannelOffset,
followTheTrendTimeout=bot.followTheTrendTimeout)