
if bot.indicators[guid].indicatorType == 32:
				interface = []
				prevbtr = []
				for value in np.arange(3, 30, 1):
					change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(bot.guid, guid, 0, value)
					# print(change.errorCode, change.errorMessage)
					bt = haasomeClient.tradeBotApi.backtest_trade_bot(bot.guid, interval)
					btr = bt.result.roi
					print(btr, value)
					
					
					if btr == prevbtr:
						pass	
					else:
						interface.append([btr, value])
				
				
				int2 = sorted(interface, key=lambda x: x[0], reverse=False)
				print(interface)
				change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(bot.guid, guid, 0, int2[-1][1])
				
				for value in np.arange(2, 40, 1):
					change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(bot.guid, guid, 1, value)
					# print(change.errorCode, change.errorMessage)
					bt = haasomeClient.tradeBotApi.backtest_trade_bot(bot.guid, interval)
					btr = bt.result.roi
					print(btr, value)
					interface.append([btr, value])
				
				int2 = sorted(interface, key=lambda x: x[0], reverse=False)
				print(interface)
				change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(bot.guid, guid, 1, int2[-1][1])
				for value in np.arange(60, 80, 1):
					change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(bot.guid, guid, 2, value)
						# print(change.errorCode, change.errorMessage)
					bt = haasomeClient.tradeBotApi.backtest_trade_bot(bot.guid, interval)
					btr = bt.result.roi
					print(btr, value)
					interface.append([btr, value])
				int2 = sorted(interface, key=lambda x: x[0], reverse=False)
				print(interface)
				change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(bot.guid, guid, 2, int2[-1][1])

			

def backtesting(start, stop, step, bot,guid,field, interval, haasomeClient):
	interface = []
	prevbtr = []
	for value in np.arange(start, stop, step):
			change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(bot.guid, guid, field, value)
			# print(change.errorCode, change.errorMessage)
			bt = haasomeClient.tradeBotApi.backtest_trade_bot(bot.guid, interval)
			btr = bt.result.roi
			print(btr, value)
			if btr == prevbtr:
				pass	
			else:
				interface.append([btr, value])					
	int2 = sorted(interface, key=lambda x: x[0], reverse=False)
	# print(interface)
	change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(bot.guid, guid, 0, int2[-1][1])
	return 

	for interface in bot.indicators[guid].indicatorInterface:
		if interface.fieldType == 1:
			if interface.title == 'Length':
					backtesting(5, 50, interface.step, bot, guid, interface, interval, haasomeClient)
			if interface.title == 'RSI Length':
					backtesting(5, 50, interface.step, bot, guid, interface, interval, haasomeClient)
			if interface.title == 'Buy Level':
						backtesting(10, 50, interface.step, bot, guid, interface, interval, haasomeClient)
			if interface.title == 'Sell Level':
						backtesting(50, 90, interface.step, bot, guid, interface, interval, haasomeClient)
			if interface.title == 'Short length':
						backtesting(2, 50, interface.step, bot, guid, interface, interval, haasomeClient)
			if interface.title == 'Middle length':
						backtesting(2, 50, interface.step, bot, guid, interface, interval, haasomeClient)
			if interface.title == 'Long length':
						backtesting(50, 100, interface.step, bot, guid, interface, interval, haasomeClient)
			if interface.title == 'Swing':
						backtesting(0, 0, interface.step, bot, guid, interface, interval, haasomeClient)
			if interface.title == 'Fast K':
						backtesting(2, 20, interface.step, bot, guid, interface, interval, haasomeClient)
			if interface.title == 'Fast D':
						backtesting(2, 20, interface.step, bot, guid, interface, interval, haasomeClient)
			if interface.title == 'Dev.Up':
							backtesting(0, 3, interface.step, bot, guid, interface, interval, haasomeClient)
			if interface.title == 'Dev.Down':
						backtesting(0, 3, interface.step, bot, guid, interface, interval, haasomeClient)





if bot.indicators[guid].indicatorType == 3:
	pass
if bot.indicators[guid].indicatorType == 4:
	#BOP
	for interface in bot.indicators[guid].indicatorInterface:
		if interface.name = 'length':
				backtesting(5, 50, 2, bot, guid, interface, interval, haasomeClient)
