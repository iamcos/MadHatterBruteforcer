def recreate_stored_bots(bot, configs, haasomeClient):
	current_bot = haasomeClient.customBotApi.clone_custom_bot_simple(bot.accountId, bot.guid, 'temp: '+bot.name).result
	results = []


	setup_bot = haasomeClient.customBotApi.setup_mad_hatter_bot(
		botName = current_bot.name,
		botGuid=current_bot.guid,
		accountGuid=current_bot.accountId,
		primaryCoin=current_bot.priceMarket.primaryCurrency,
		secondaryCoin=current_bot.priceMarket.secondaryCurrency,
		contractName=bb.priceMarket.contractName,
		leverage=current_bot.leverage,
		templateGuid=bb.customTemplate,
		position=bb.coinPosition,
		fee=current_bot.currentFeePercentage,
		tradeAmountType=current_bot.amountType,
		tradeAmount=current_bot.currentTradeAmount,
		useconsensus=bb.useTwoSignals,
		disableAfterStopLoss=bb.disableAfterStopLoss,
		interval=bb.interval,
		includeIncompleteInterval=bb.includeIncompleteInterval,
		mappedBuySignal=bb.mappedBuySignal,
		mappedSellSignal=bb.mappedSellSignal,
	)
	 for bb in (configs):
		if current_bot.bBands["Length"] != bb.bBands["Length"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid,
				EnumMadHatterIndicators.BBANDS,
				0,
				bb.bBands["Length"],
			)
			try:
			  print(do.errorCode, do.errorMessage, 'Length')
			except :
			  pass
		if current_bot.bBands["Devup"] != bb.bBands["Devup"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid, EnumMadHatterIndicators.BBANDS, 1, bb.bBands["Devup"]
			)
			try:
			  print(do.errorCode, do.errorMessage, 'Devup')
			except :
			  pass
		if current_bot.bBands["Devdn"] != bb.bBands["Devdn"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid, EnumMadHatterIndicators.BBANDS, 2, bb.bBands["Devdn"]
			)
			try:
			  print(do.errorCode, do.errorMessage, 'Devdn')
			except :
			  pass
		if current_bot.bBands["MaType"] != bb.bBands["MaType"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid,
				EnumMadHatterIndicators.BBANDS,
				3,
				bb.bBands["MaType"],
			)
			try:
			  print(do.errorCode, do.errorMessage, 'MaType')
			except :
			  pass
		if current_bot.bBands["AllowMidSell"] != bb.bBands["AllowMidSell"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid,
				EnumMadHatterIndicators.BBANDS,
				5,
				bb.bBands["AllowMidSell"],
			)
			try:
			  print(do.errorCode, do.errorMessage, 'AllowMidSell')
			except :
			  pass
		if current_bot.bBands["RequireFcc"] != bb.bBands["RequireFcc"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid,
				EnumMadHatterIndicators.BBANDS,
				6,
				bb.bBands["RequireFcc"],
			)
			try:
			  print(do.errorCode, do.errorMessage, 'RequireFcc')
			except :
			  pass
		if current_bot.rsi["RsiLength"] != bb.rsi["RsiLength"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid, EnumMadHatterIndicators.RSI, 0, bb.rsi["RsiLength"]
			)
			try:
			  print(do.errorCode, do.errorMessage, 'RsiLength')
			except :
			  pass
		if current_bot.rsi["RsiOverbought"] != bb.rsi["RsiOverbought"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid,
				EnumMadHatterIndicators.RSI,
				1,
				bb.rsi["RsiOverbought"],
			)
			try:
			  print(do.errorCode, do.errorMessage, 'RsiOverbought')
			except :
			  pass
		if current_bot.rsi["RsiOversold"] != bb.rsi["RsiOversold"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid, EnumMadHatterIndicators.RSI, 2, bb.rsi["RsiOversold"]
			)
			try:
			  print(do.errorCode, do.errorMessage, 'RsiOversold')
			except :
			  pass
		if current_bot.macd["MacdFast"] != bb.macd["MacdFast"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid, EnumMadHatterIndicators.MACD, 0, bb.macd["MacdFast"]
			)
			try:
			  print(do.errorCode, do.errorMessage, 'MacdFast')
			except :
			  pass
		if current_bot.macd["MacdSlow"] != bb.macd["MacdSlow"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid, EnumMadHatterIndicators.MACD, 1, bb.macd["MacdSlow"]
			)
			try:
			  print(do.errorCode, do.errorMessage, 'MacdSlow')
			except :
			  pass

		if current_bot.macd["MacdSign"] != bb.macd["MacdSign"]:
			do = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				current_bot.guid, EnumMadHatterIndicators.MACD, 2, bb.macd["MacdSign"]
			)
			try:
			  print(do.errorCode, do.errorMessage, 'MacdSign')
			except :
			  pass

		ticks = iiv.readinterval(current_bot)
		bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
			current_bot.accountId,
			current_bot.guid,
			int(ticks),
			current_bot.priceMarket.primaryCurrency,
			current_bot.priceMarket.secondaryCurrency,
			current_bot.priceMarket.contractName,
		)
		try:
			print("bt", bt.errorCode, bt.errorMessage)
			btr = bt.result
			roi = btr.roi

			print(roi)
			results.append(btr)
		except:
			pass
		

		
		delete = haasomeClient.customBotApi.remove_custom_bot(current_bot.guid)
	


	return results