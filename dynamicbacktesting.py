from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()



while True:
					char = getch()
					if (char == 'q'):
							initialparam = getmhindicators(currentBotGuid)[0]
							print('Bbands length selected', initialparam)
							indicator = [EnumMadHatterIndicators.BBANDS, 0, 'Bbands L']

					elif (char == '0'):
							print('Zero pressed. quitting')
							break

					elif (char == "w"):
							print('bbands deviation rought bruteforce initiated')
							bbtbbdev(currentBotGuid, backtestfor)
					elif (char == "e"):
							print('bbands deviation precise stepping bruteforcer algorithm iniciated')
							bbtbbdevprecise(currentBotGuid, backtestfor)

					elif (char == "a"):
							initialparam = getmhindicators(currentBotGuid)[8]
							indicator = [EnumMadHatterIndicators.RSI, 0,'RSI L']
							print('RSI l selected', initialparam)
					elif (char == "s"):
							currentconfig = getmhindicators(currentBotGuid)
							initialparam = getmhindicators(currentBotGuid)[9]
							print('RSI Buy selected', initialparam)
							indicator = [EnumMadHatterIndicators.RSI, 1,'RSI Buy']

					elif (char == "d"):
									initialparam = getmhindicators(currentBotGuid)[10]
									print('RSI Sell value: ', initialparam)
									indicator = [EnumMadHatterIndicators.RSI, 2, 'RSI Sell']
					elif (char == "z"):
									initialparam = getmhindicators(currentBotGuid)[11]
									print('MACD Fast selected', initialparam)
									indicator = [EnumMadHatterIndicators.MACD, 0,'MACD Fast']
					elif (char == "x"):
							initialparam = getmhindicators(currentBotGuid)[12]
							print('MACD Slow selected', initialparam)
							indicator = [EnumMadHatterIndicators.MACD, 1, 'MACD Slow']
					elif (char == "c"):
									initialparam = getmhindicators(currentBotGuid)[13]
									print('MACD Signal selected', initialparam)
									indicator = 	[EnumMadHatterIndicators.MACD, 2, 'MACD signal']
					elif (char == 66) or char == 'u':
									btresults = []
									botorderhistory  =()
									start = 0
									stop = 4
									step = 1
									for v in np.arange(start,stop,step):
													initialparam  +=1
													haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
											currentBotGuid, indicator[0],indicator[1],initialparam)
													bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountGuid,currentBotGuid,backtestfor, primarycoin, secondarycoin, contractname)
													btr = bt.result
													completedorders = btr.completedOrders
													for i,v in completedorders:
															# pair = order.pair
															# orderId = order.orderIdaddedTime
															# orderStatus 	= order.orderStatus
															# orderType 	= order.orderType
															# fundMovement 	= order.fundMovement
															# price 	= order.price
															# amount 	= order.amount
															# amountFilled 	= order.amountFilled
															# addedTime 	= order.addedTime
															# unixAddedTime 	= order.unixAddedTime
															# inti 	= order.int
															try:
																botorderhistory.append([bt.result.completedOrders[1].unixAddedTime, bt.result.completedOrders[1].amountFilled,bt.result.completedOrders[1].profits])
																print(botorderhistory)
															except IndexError:
																	print('index error! means no order took place.')

													
													# order = [completedorders.amount, completedorders.ammountFilled, completedorders.addedTime, completedorders.orderStatus]
												
													# print('backtest:' , bt.errorCode, bt.errorMessage)
													print(initialparam, indicator[2], btr.roi)
													btresults.append([btr.roi,initialparam])

					elif (char == 66) or char == 'i':
									btresults = []
									start = 0
									stop = 1
									step = 1
									for v in np.arange(start,stop,step):
													initialparam  +=1
													haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
											currentBotGuid, indicator[0],indicator[1],initialparam)
													bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountGuid,currentBotGuid,backtestfor, primarycoin, secondarycoin, contractname)
													btr = bt.result
													completedorders = btr.completedOrders
													# print('backtest:' , bt.errorCode, bt.errorMessage)
													print(initialparam, indicator[2], btr.roi)
													btresults.append([btr.roi,initialparam])
									# btresultssorted = sorted(btresults, key=lambda x: x[0], reverse=True)
									# print(btresultssorted[0][1],'gives best roi of: ',btresultssorted[0][0])
									# haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
									# 			currentBotGuid, indicator[0], indicator[1],btresultssorted[0][1])
					elif (char == 67) or char == 'j':
													btresults = []
													start = 0
													stop = 4
													step = 1
													initialparam =  initialparam
													for v in np.arange(start, stop, step):
																			initialparam  -= 1
																			haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
																			currentBotGuid, indicator[0],indicator[1],initialparam)
																			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountGuid,currentBotGuid,backtestfor, primarycoin, secondarycoin, contractname)
																			btr = bt.result
																			# print('backtest:' , bt.errorCode, bt.errorMessage)
																			print(initialparam, indicator[2], btr.roi)
																			btresults.append([btr.roi,initialparam])

					elif (char == 67) or char == 'k':
													btresults = []
													start = 0
													stop = 1
													step = 1
													initialparam =  initialparam
													for v in np.arange(start, stop, step):
																			initialparam  -= 1
																			haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
																			currentBotGuid, indicator[0],indicator[1],initialparam)
																			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountGuid,currentBotGuid,backtestfor, primarycoin, secondarycoin, contractname)
																			btr = bt.result
																			# print('backtest:' , bt.errorCode, bt.errorMessage)
																			print(initialparam, indicator[2], btr.roi)
																			btresults.append([btr.roi,initialparam])