def setMacdFast():
	answers = {'selection': None}
	while answers['selection'] != 'back':
		action = [
						{
							'type':'list',
							'name':'selection',
							'message': 'Chose your next move: ',
							'choices': ['increse', 'decrease', 'increase 10 steps','decrease 10 steps', 'back']}]
					
		if answers['selection'] == 'increse':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.macd['MacdFast']
			currentvalue +=1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.MACD, 0, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi,' ', currentvalue)
		elif answers['selection'] == 'decrease':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.macd['MacdFast']
			currentvalue -=1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.MACD, 0, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi,' ', currentvalue)

		elif answers['selection'] == 'increase 10 steps':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.macd['MacdFast']
			for x in range(10):
				currentvalue +=1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.MACD, 0, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi,' ', currentvalue)

		elif answers['selection'] == 'decrease 10 steps':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.macd['MacdFast']
			for x in range(10):
				currentvalue -=1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.MACD, 0, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi,' ', currentvalue)
		answers = prompt(action)


def setMacdSlow():
	answers = {'selection': None}
	while answers['selection'] != 'back':
		action = [
						{
							'type':'list',
							'name':'selection',
							'message': 'Chose your next move: ',
							'choices': ['increse', 'decrease', 'increase 10 steps','decrease 10 steps', 'back']}]
					
		if answers['selection'] == 'increse':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.macd['MacdSlow']
			currentvalue +=1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.MACD, 1, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi,' ', currentvalue)
		elif answers['selection'] == 'decrease':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.macd['MacdSlow']
			currentvalue -=1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.MACD, 1, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi,' ', currentvalue)

		elif answers['selection'] == 'increase 10 steps':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.macd['MacdSlow']
			for x in range(10):
				currentvalue +=1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.MACD, 1, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi,' ', currentvalue)

		elif answers['selection'] == 'decrease 10 steps':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.macd['MacdSlow']
			for x in range(10):
				currentvalue -=1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.MACD, 1, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi,' ', currentvalue)
		answers = prompt(action)


		def setMacdSignal():
	answers = {'selection': None}
	while answers['selection'] != 'back':
		action = [
						{
							'type':'list',
							'name':'selection',
							'message': 'Chose your next move: ',
							'choices': ['increse', 'decrease', 'increase 10 steps','decrease 10 steps', 'back']}]
					
		if answers['selection'] == 'increse':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.macd['MacdSignal']
			currentvalue +=1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.MACD, 2, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi,' ', currentvalue)
		elif answers['selection'] == 'decrease':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.macd['MacdSignal']
			currentvalue -=1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.MACD, 2, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi,' ', currentvalue)

		elif answers['selection'] == 'increase 10 steps':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.macd['MacdSignal']
			for x in range(10):
				currentvalue +=1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.MACD, 2, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi,' ', currentvalue)

		elif answers['selection'] == 'decrease 10 steps':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.macd['MacdSignal']
			for x in range(10):
				currentvalue -=1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.MACD, 2, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi,' ', currentvalue)
		answers = prompt(action)