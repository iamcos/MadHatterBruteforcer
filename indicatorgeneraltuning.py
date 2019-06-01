def indicatorfinetune(currentBotGuid, indicator):

	setstopLoss(currentBotGuid, stopLoss):
	haasomeClient.customBotApi.set_mad_hatter_safety_parameter(
		currentBotGuid, EnumMadHatterSafeties.STOP_LOSS, stopLoss)

	setbbLength(currentBotGuid ,bbLength):
	setbbl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
		currentBotGuid, EnumMadHatterIndicators.BBANDS, 0, bbLength)
	print('SET BBL: ', setbbl.errorCode, setbbl.errorMessage)

	setbbDevUp(currentBotGuid,bbDevUp):
	haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
		currentBotGuid, EnumMadHatterIndicators.BBANDS, 1, bbDevUp)
	setbbDevDown(currentBotGuid, bbDevDown):
	haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
		currentBotGuid, EnumMadHatterIndicators.BBANDS, 2, bbDevDown)

	setbbMAType(currentBotGuid, bbMAType):
	haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
		currentBotGuid, EnumMadHatterIndicators.BBANDS, 3, bbMAType)

	setfcc(currentBotGuid, fcc):
	haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				currentBotGuid, EnumMadHatterIndicators.BBANDS, 5, fcc)

	setrm(currentBotGuid, rm):
	haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				currentBotGuid, EnumMadHatterIndicators.BBANDS, 6, rm)

	setmms(currentBotGuid, mms):
	haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				currentBotGuid, EnumMadHatterIndicators.BBANDS, 7, mms)

	setRSILength(currentBotGuid, RSILength):
	haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
		currentBotGuid, EnumMadHatterIndicators.RSI, 0, RSILength)

	setRSIBuy(currentBotGuid, RSIBuy):
	haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
		currentBotGuid, EnumMadHatterIndicators.RSI, 1, RSIBuy)

	setRSSell(currentBotGuid, RSSell):
	haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
		currentBotGuid, EnumMadHatterIndicators.RSI, 2, RSISell)

	setMACDFast(currentBotGuid, MACDFast):
	haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
		currentBotGuid, EnumMadHatterIndicators.MACD, 0, MACDFast)

	setMACDSlow(currentBotGuid, MACDSlow):
	haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
		currentBotGuid, EnumMadHatterIndicators.MACD, 1, MACDSlow)
	setMACDSignal(currentBotGuid, MACDSignal):
	haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
		currentBotGuid, EnumMadHatterIndicators.MACD, 2, MACDSignal)
	 direction = 'u':
		stoploop = 'no'
		currentconfig = getmhindicators(currentBotGuid)
		basebotconfig = haasomeClient.customBotApi.get_custom_bot(currentBotGuid, EnumCustomBotType.BASE_CUSTOM_BOT).result
		pricemarket = basebotconfig.priceMarket
		contractname = pricemarket.contractName
		timeinterval = basebotconfig.interval
		botname, primarycoin, secondarycoin, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, icc, mappedbuysignal, mappedsellsignal, leverage = getbasebotconfig(currentBotGuid)
		#configurebot = haasomeClient.customBotApi.setup_mad_hatter_bot(accountGuid, currentBotGuid, botname, primarycoin, secondarycoin, contractname, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, timeinterval, icc, mappedbuysignal, mappedsellsignal, leverage)
		#print('configurebot', configurebot.errorCode, configurebot.errorMessage)
		btresults = []
		initialparam = currentconfig[inconfigplace]
		newparam =  initialparam
		backtestfor = minutestobacktest()
		if stoploop != None:
			if direction = 'u':
				for v in range(0,3):
					newparam  +=1
					indicator(newparam)
					bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountGuid,currentBotGuid,backtestfor, primarycoin, secondarycoin, contractname)
					btr = bt.result
					print('backtest:' , bt.errorCode, bt.errorMessage)
					print(newparam, indicator, btr.roi)
					btresults.append([btr.roi,newparam])
					newparam =  initialparam
			if direction = 'd':
				for v in range(0,3):
						newparam  -= 1
						indicator(newparam)
						bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountGuid,currentBotGuid,backtestfor, primarycoin, secondarycoin, contractname)
						btr = bt.result
						print('backtest:' , bt.errorCode, bt.errorMessage)
						print(newparam, indicator, btr.roi)
						btresults.append([btr.roi,newparam])
		
			btresultssorted = sorted(btresults, key=lambda x: x[0], reverse=True)
			print(btresultssorted[0][1],'gives best roi of: ',btresultssorted[0][0])
			indicator(currentBotGuid,btresultssorted[0][1])	

				print(btresultssorted[0][1],'Has been Set ')