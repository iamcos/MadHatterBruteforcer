def tune_indicator(therange,direction,indicator):
	basebotconfig = haasomeClient.customBotApi.get_custom_bot(basebotconfig.guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
	if indicator == EnumMadHatterIndicators.RSI and parameter == 0:
		currentvalue = basebotconfig.rsi['RsiLength']
	if indicator == EnumMadHatterIndicators.RSI and parameter == 1:
		currentvalue = basebotconfig.rsi['RsiOversold']
	if indicator == EnumMadHatterIndicators.RSI and parameter == 2:
		currentvalue = basebotconfig.rsi['RsiOverbought']
	if indicator == EnumMadHatterIndicators.BBANDS and parameter == 0:
		currentvalue = basebotconfig.bBands['Length']
	if indicator == EnumMadHatterIndicators.BBANDS and parameter == 1:
		currentvalue = basebotconfig.bBands['Devup']
	if indicator == EnumMadHatterIndicators.BBANDS and parameter == 2:
		currentvalue = basebotconfig.bBands['Devdn']
	# if indicator == bBands and parameter == 3:
	# 	currentvalue = basebotconfig.bBands['Reserved']
	# if indicator == bBands and parameter == 4:
	# 	currentvalue = basebotconfig.bBands['Reserved']
	if indicator == EnumMadHatterIndicators.MACD and parameter == 0:
			currentvalue = basebotconfig.macd['MacdFast']
	if indicator == EnumMadHatterIndicators.MACD and parameter == 1:
		currentvalue = basebotconfig.macd['MacdSlow']
	if indicator == EnumMadHatterIndicators.MACD and parameter == 2:
		currentvalue = basebotconfig.macd['MacdSign']

	setnewvalue = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						basebotconfig.guid, indicator, parameter, currentvalue)

def bt():
	results = []
	bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
	btr = bt.result
	print(btr.roi, indicator, parameter, currentvalue)
	results.append([btr.roi, indicator, parameter, currentvalue])
	return results

	
currentvalue = currentvalue+(1*direction)



if indicator == EnumMadHatterIndicators.RSI: 
		basebotconfig = haasomeClient.customBotApi.get_custom_bot(basebotconfig.guid, EnumCustomBotType.BASE_CUSTOM_BOT).result

		parameter = 0
		currentvalue = basebotconfig.rsi['RsiLength']
		initval = currentvalue
		for x in range(therange):
			setnewvalue = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						basebotconfig.guid, indicator, parameter, currentvalue+1)
			
		parameter = 1
		currentvalue1 = basebotconfig.rsi['RsiOversold']
		initval1 = currentvalue1
		for x in range(3):
			setnewvalue = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						basebotconfig.guid, indicator, parameter, currentvalue1+1)

		currentvalue = initval
		for x in range(therange):
			setnewvalue = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						basebotconfig.guid, indicator, parameter, currentvalue+(1*-1))
			parameter = 1
			currentvalue = basebotconfig.rsi['RsiOversold']
			setnewvalue = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							basebotconfig.guid, indicator, parameter, currentvalue+(0.1*direction))
			parameter = 2
			currentvalue = basebotconfig.rsi['RsiOverbought']
			setnewvalue = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						basebotconfig.guid, indicator, parameter, currentvalue+(0.1*direction))

	
if indicator == EnumMadHatterIndicators.RSI and parameter == 1:
	currentvalue = basebotconfig.rsi['RsiOversold']
if indicator == EnumMadHatterIndicators.RSI and parameter == 2: