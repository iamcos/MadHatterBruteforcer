def indicatorsintobots(haasomeClient, bot, interval):
	ticks = btinterval.readinterval()
	newbots = []
	createdbots = []
	
	for guid in bot.indicators: 
		newbotname = bot.name+' '+bot.indicators[guid].indicatorTypeShortName+' temp'
		newbot = haasomeClient.tradeBotApi.clone_trade_bot(bot.accountId, bot.guid, newbotname, bot.priceMarket.primaryCurrency, bot.priceMarket.secondaryCurrency, bot.priceMarket.contractName, bot.leverage, False, False, False, True, True).result
		cloeindicator = haasomeClient.tradeBotApi.clone_indicator(bot.guid, guid, newbot.guid).result
	
		gettradebot = haasomeClient.tradeBotApi.get_trade_bot(newbot.guid).result
		for guid in gettradebot.indicators:
			for i, options in enumerate(gettradebot.indicators[str(guid)].indicatorInterface):

				for i in range(2, 20, 1):
					change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(gettradebot.guid, guid, i, options.value)
					printerrors(change,'change')
					bt = haasomeClient.tradeBotApi.backtest_trade_bot(gettradebot.guid, ticks)
					printerrors(bt,'bt')
					btr = bt.result.roi
					print(btr)



					def botconfig(haasomeClient,bot):
		safeties = []
	indicators = []
	insurances = []

		# Printing Safeties data
	print('\n',len(bot.safeties),' Safeties')
	for guid in bot.safeties:
		print(bot.safeties[guid].safetyName)
		safeties.append([guid, bot.safeties[guid].safetyName])
	#printing Safeties interface data
		for interface in bot.safeties[guid].safetyInterface:
			for i in range(start, stop, step):
			
					print(interface.title, interface.value, interface.options)
	
		
		for interface in bot.indicators[guid].indicatorInterface:
				print(interface.__dict__)
				# print(interface.fieldType)
				print(interface.title, interface.value , interface.options)


		indicators.append([guid, bot.indicators[guid].indicatorName])
		# print(EnumIndicator.EnumIndicator(bot.indicators[guid].indicatorType))
			# Printing indicator interface data
		for interface in bot.indicators[guid].indicatorInterface:
				print(interface.__dict__)
				# print(interface.fieldType)
				print(interface.title) #interface.value , interface.options
	print('\n')
