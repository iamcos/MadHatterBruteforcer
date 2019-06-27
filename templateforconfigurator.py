def setRsiLength():
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
			currentvalue = basebotconfig.rsi['Length']
			currentvalue +=1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.RSI, 0	, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
		elif answers['selection'] == 'decrease':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.rsi['Length']
			currentvalue -=1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.RSI, 0, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)

		elif answers['selection'] == 'increase 10 steps':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.rsi['Length']
			for x in range(10):
				currentvalue +=1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.RSI, 0, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi, currentvalue)

		elif answers['selection'] == 'decrease 10 steps':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.rsi['Length']
			for x in range(10):
				currentvalue -=1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.RSI, 0, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi, currentvalue)
		answers = prompt(action)

def setRsiBuy():
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
			currentvalue = basebotconfig.rsi['RsiOverbought']
			currentvalue +=1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.RSI, 1, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
		elif answers['selection'] == 'decrease':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.rsi['RsiOverbought']
			currentvalue -=1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.RSI, 1, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)

		elif answers['selection'] == 'increase 10 steps':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.rsi['RsiOverbought']
			for x in range(10):
				currentvalue +=1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.RSI, 1, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi, currentvalue)

		elif answers['selection'] == 'decrease 10 steps':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.rsi['RsiOverbought']
			for x in range(10):
				currentvalue -=1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.RSI, 1, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi, currentvalue)
		answers = prompt(action)


	def setRsiBuy():
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
			currentvalue = basebotconfig.rsi['RsiOverbought']
			currentvalue +=1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.RSI, 1, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
		elif answers['selection'] == 'decrease':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.rsi['RsiOverbought']
			currentvalue -=1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.RSI, 1, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)

		elif answers['selection'] == 'increase 10 steps':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.rsi['RsiOverbought']
			for x in range(10):
				currentvalue +=1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.RSI, 1, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi, currentvalue)

		elif answers['selection'] == 'decrease 10 steps':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.rsi['RsiOverbought']
			for x in range(10):
				currentvalue -=1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.RSI, 1, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi, currentvalue)
		answers = prompt(action)


	def setRsiSell():
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
			currentvalue = basebotconfig.rsi['RsiOversold']
			currentvalue +=1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.RSI, 1, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
		elif answers['selection'] == 'decrease':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.rsi['RsiOversold']
			currentvalue -=1
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.RSI, 2, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)

		elif answers['selection'] == 'increase 10 steps':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.rsi['RsiOversold']
			for x in range(10):
				currentvalue +=1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.RSI, 2, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi, currentvalue)

		elif answers['selection'] == 'decrease 10 steps':
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.rsi['RsiOversold']
			for x in range(10):
				currentvalue -=1
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.RSI, 2, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,10000,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi, currentvalue)
		answers = prompt(action)
### Helper classes ###