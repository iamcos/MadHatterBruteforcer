
def getmhindicators(currentBotGuid):
		basebotconfig = haasomeClient.customBotApi.get_custom_bot(currentBotGuid, EnumCustomBotType.BASE_CUSTOM_BOT).result
		indicators = basebotconfig.bBands['Length'], basebotconfig.bBands['Devup'],basebotconfig.bBands['Devdn'],basebotconfig.bBands['MaType'],basebotconfig.bBands['Deviation'],basebotconfig.bBands['ResetMid'],basebotconfig.bBands['AllowMidSell'],basebotconfig.bBands['RequireFcc'],basebotconfig.bBands['Length'],basebotconfig.rsi['RsiLength'], basebotconfig.rsi['RsiOversold'], basebotconfig.rsi['RsiOverbought'], basebotconfig.macd['MacdSlow'],basebotconfig.macd['MacdFast'], basebotconfig.macd['MacdSign']
		return indicators
		print(indicators)


def getbasebotconfig(currentBotGuid):
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(currentBotGuid, EnumCustomBotType.BASE_CUSTOM_BOT).result

			botname = basebotconfig.name
			pricemarket = basebotconfig.priceMarket
			primarycoin = pricemarket.primaryCurrency
			secondarycoin = pricemarket.secondaryCurrency
			fee = basebotconfig.currentFeePercentage
			tradeamount = basebotconfig.currentTradeAmount
			ammounttype = basebotconfig.amountType
			coinposition = basebotconfig.coinPosition
			consensus = basebotconfig.useTwoSignals
			customtemplate= basebotconfig.customTemplate
			icc = basebotconfig.includeIncompleteInterval
			mappedbuysignal = basebotconfig.mappedBuySignal
			mappedsellsignal = basebotconfig.mappedSellSignal
			sldisable = basebotconfig.disableAfterStopLoss
			leverage = basebotconfig.leverage

			return botname, primarycoin, secondarycoin, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, icc, mappedbuysignal, mappedsellsignal, leverage

def safeHistoryGet(pricesource: EnumPriceSource, primarycoin: str, secondarycoin: str, contractname: str, interval: int, depth: int):
				history = None
				historyResult = False
				failCount = 0

				while historyResult == False:
								history = haasomeClient.marketDataApi.get_history(pricesource, primarycoin, secondarycoin, contractname, interval, depth)
								if len(history.result) > 1:
												historyResult = True
								else:
												failCount = failCount + 1
												time.sleep(1)

								if failCount == 10:
												historyResult = True


				return history