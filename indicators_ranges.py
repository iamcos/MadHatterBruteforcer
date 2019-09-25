def backtest_indicator(bot):
			indicators = get_indicator_interfaces(bot)
			results = []
			if gettradebot.indicators[guid].indicatorTypeShortName == 'Aroon':
				 for xxx in np.arange(2, 12, 2):
						change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(gettradebot.guid, guid, 2, xxx)
						bt = haasomeClient.tradeBotApi.backtest_trade_bot(gettradebot.guid, ticks)
						printerrors(bt, 'bt')
						printerrors(change, 'change')
						print(bt.result.roi)
						for x in np.arange(10, 50, 10):
							change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(gettradebot.guid, guid, 0, x)
							bt = haasomeClient.tradeBotApi.backtest_trade_bot(gettradebot.guid, ticks)
							printerrors(bt, 'bt')
							printerrors(change, 'change')
							print(bt.result.roi)
							for xx in np.arange(20, 100, 10):
								change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(gettradebot.guid, guid, 1, xx)
								bt = haasomeClient.tradeBotApi.backtest_trade_bot(gettradebot.guid, ticks)
								printerrors(bt, 'bt')
								printerrors(change, 'change')
								print(bt.result.roi)	
								results.append([bt.result.roi, x, xx, xxx])
			elif gettradebot.indicators[guid].indicatorTypeShortName == 'CRSI': #missing ROC
				 for l in np.arange(2, 40, 2):
						change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(gettradebot.guid, guid, 0, l)
						bt = haasomeClient.tradeBotApi.backtest_trade_bot(gettradebot.guid, ticks)
						printerrors(bt, 'bt')
						printerrors(change, 'change')
						print(bt.result.roi)
						for b in np.arange(10, 40, 2):
							change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(gettradebot.guid, guid, 3, b)
							bt = haasomeClient.tradeBotApi.backtest_trade_bot(gettradebot.guid, ticks)
							printerrors(bt, 'bt')
							printerrors(change, 'change')
							print(bt.result.roi)
							for s in np.arange(65, 81, 2):
								change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(gettradebot.guid, guid, 4, s)
								bt = haasomeClient.tradeBotApi.backtest_trade_bot(gettradebot.guid, ticks)
								printerrors(bt, 'bt')
								printerrors(change, 'change')
								print(bt.result.roi)	
								for lud in np.arange(2, 5, 1):
										change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(gettradebot.guid, guid, 1, lud)
										bt = haasomeClient.tradeBotApi.backtest_trade_bot(gettradebot.guid, ticks)
										printerrors(bt, 'bt')
										printerrors(change, 'change')
										print(bt.result.roi)	
										results.append([bt.result.roi, l, lud, b, s])
			elif gettradebot.indicators[guid].indicatorTypeShortName == None:
				pass
				return bot
			else: 
				pass
