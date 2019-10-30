
def indicatorfinetune(currentBotGuid):
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
		char = getch()
		print('qwe - bbandsa, asd - rsi, zxc - macd. u - increasesetting up in range, d - down in range')
		print('Keyboard shortcunts: \n for selecting Bollinger bands\n w:bbl e:bbup ')
		if (char == "q"):
			indicator = 	[EnumMadHatterIndicators.BBANDS, 0]
			print('SET selected: ', setbbl.errorCode, setbbl.errorMessage)

		elif (char == "w"):
			print('bbands devup selected')
			indicator = 	[EnumMadHatterIndicators.BBANDS, 1]

		elif (char == "e"):
			print('bbands devdn selected')
			indicator = [EnumMadHatterIndicators.BBANDS, 2]

		elif (char == "a"):
			print('RSI l selected')
			indicator = [EnumMadHatterIndicators.RSI, 0]

		elif (char == "s"):
				print('RSI Buy selected')
				indicator = [EnumMadHatterIndicators.RSI, 1]

		elif (char == "s"):
				print('RSI Sell selected')
				indicator = [EnumMadHatterIndicators.RSI, 2]
		elif (char == "z"):
				print('MACD Fast selected')
				indicator = [EnumMadHatterIndicators.MACD, 0]
		elif (char == "x"):
			print('MACD Slow selected')
			indicator = [EnumMadHatterIndicators.MACD, 1]
		elif (char == "c"):
				print('MACD Signal selected')
				indicator = 	[EnumMadHatterIndicators.MACD, 2]
		elif (char == 2424832) or char == 'u':
			btresults = []
			for v in range(0,3):
						newparam =  initialparam
						newparam  +=1
						haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				currentBotGuid, indicator,newparam)
						bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountGuid,currentBotGuid,backtestfor, primarycoin, secondarycoin, contractname)
						btr = bt.result
						print('backtest:' , bt.errorCode, bt.errorMessage)
						print(newparam, indicator, btr.roi)
						btresults.append([btr.roi,newparam])
						btresultssorted = sorted(btresults, key=lambda x: x[0], reverse=True)
						print(btresultssorted[0][1],'gives best roi of: ',btresultssorted[0][0])
						indicator(currentBotGuid,btresultssorted[0][1])	
						haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				currentBotGuid, indicator,tresultssorted[0][1])
		elif (char == 2621440) or char == 'd':
				btresults = []
				newparam =  initialparam
				for v in range(0,3):
							newparam  -= 1
							haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				currentBotGuid, indicator,newparam)
							bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountGuid,currentBotGuid,backtestfor, primarycoin, secondarycoin, contractname)
							btr = bt.result
							print('backtest:' , bt.errorCode, bt.errorMessage)
							print(newparam, indicator, btr.roi)
							btresults.append([btr.roi,newparam])
							btresultssorted = sorted(btresults, key=lambda x: x[0], reverse=True)
							print(btresultssorted[0][1],'gives best roi of: ',btresultssorted[0][0])

							haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				currentBotGuid, indicator,tresultssorted[0][1])
			


def tuneRsiLength():
	btroilist = []
	basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
	currentvalue = basebotconfig.rsi['RsiLength']
		for x in range(3):
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.RSI, 0	, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
			btroilist.append(btr.roi, currentvalue)
			currentvalue +=1
		for x in range(3):
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(guid, EnumMadHatterIndicators.RSI, 0	, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
			btroilist.append(btr.roi, currentvalue)
			currentvalue -=1
		btroilistsorted = sorted(btroilist, key=lambda x: x[0], reverse=True)
		setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				guid, EnumMadHatterIndicators.RSI, 0	, btroilistsorted[0][1])


def tuneRsiOversold():
		btroilist = []
		basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
		currentvalue = basebotconfig.rsi['RsiOversold']
		for x in range(3):
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.RSI, 1, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
			btroilist.append(btr.roi, currentvalue)
			currentvalue +=1
		for x in range(3):
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.RSI, 1, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
			btroilist.append(btr.roi, currentvalue)
			currentvalue -=1
		btroilistsorted = sorted(btroilist, key=lambda x: x[0], reverse=True)
		setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				guid, EnumMadHatterIndicators.RSI, 1	, btroilistsorted[0][1])




def tuneRsiOverbought():
			btroilist = []
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.rsi['RsiOverbought']
			for x in range(3):
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.RSI, 2, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi, currentvalue)
				btroilist.append(btr.roi, currentvalue)
				currentvalue +=1
				for x in range(3):
					setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
								guid, EnumMadHatterIndicators.RSI, 2, currentvalue)
					bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
					print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
					btr = bt.result
					print(btr.roi, currentvalue)
					btroilist.append(btr.roi, currentvalue)
					currentvalue -=1
			btroilistsorted = sorted(btroilist, key=lambda x: x[0], reverse=True)
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				guid, EnumMadHatterIndicators.RSI, 2	, btroilistsorted[0][1])


def tuneDevdn():
	btroilist = []
	basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
	currentvalue = basebotconfig.rsi['Devdn']
	initvalue = currentvalue
	for x in range(5):
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.BBANDS, 2	, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
			btroilist.append([btr.roi, currentvalue])
			currentvalue +=0.1
	currentvalue = initvalue-0.1
	for x in range(5):
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(guid, EnumMadHatterIndicators.BBANDS, 2	, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
			btroilist.append([btr.roi, currentvalue])
			currentvalue -=0.1
	btroilistsorted = sorted(btroilist, key=lambda x: x[0], reverse=True)
	setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				guid, EnumMadHatterIndicators.BBANDS, 2	, btroilistsorted[0][1])
	print(btroilistsorted[0][1])


def tuneDevup():
		btroilist = []
		basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
		currentvalue = basebotconfig.bBands['Devup']
		initvalue = currentvalue
		for x in range(5):
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.BBANDS, 1, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
			btroilist.append([btr.roi, currentvalue])
			currentvalue +=0.1
		currentvalue = initvalue-0.1
		for x in range(5):
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.BBANDS, 1, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
			btroilist.append([btr.roi, currentvalue])
			currentvalue -=0.1
		btroilistsorted = sorted(btroilist, key=lambda x: x[0], reverse=True)
		setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				guid, EnumMadHatterIndicators.BBANDS, 1	, btroilistsorted[0][1])




def tuneLength():
			btroilist = []
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.bBands['Length']
			initvalue = currentvalue
			for x in range(5):
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.BBANDS, 0, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi, currentvalue)
				btroilist.append([btr.roi, currentvalue])
				currentvalue +=1
			currentvalue = initvalue-1
			for x in range(5):
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.BBANDS, 0 currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi, currentvalue)
				btroilist.append([btr.roi, currentvalue])
				currentvalue -=1
			btroilistsorted = sorted(btroilist, key=lambda x: x[0], reverse=True)
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				guid, EnumMadHatterIndicators.BBANDS, 0	, btroilistsorted[0][1])





def tuneMacdSlow():
	btroilist = []
	basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
	currentvalue = basebotconfig.macd['MacdSlow']
	initvalue = currentvalue
	for x in range(5):
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.MACD, 1	, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
			btroilist.append([btr.roi, currentvalue])
			currentvalue +=1
	currentvalue = initvalue-1
	for x in range(5):
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(guid, EnumMadHatterIndicators.MACD,1	, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
			btroilist.append([btr.roi, currentvalue])
			currentvalue -=1
	btroilistsorted = sorted(btroilist, key=lambda x: x[0], reverse=True)
	setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				guid, EnumMadHatterIndicators.MACD,1	, btroilistsorted[0][1])
	print(btroilistsorted[0][1])


def tuneMacdFast():
		btroilist = []
		basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
		currentvalue = basebotconfig.MACD['MacdFast']
		initvalue = currentvalue
		for x in range(5):
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.MACD, 0, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
			btroilist.append([btr.roi, currentvalue])
			currentvalue +=1
		currentvalue = initvalue-1
		for x in range(5):
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						guid, EnumMadHatterIndicators.MACD, 0, currentvalue)
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
			print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
			btr = bt.result
			print(btr.roi, currentvalue)
			btroilist.append([btr.roi, currentvalue])
			currentvalue -=1
		btroilistsorted = sorted(btroilist, key=lambda x: x[0], reverse=True)
		setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				guid, EnumMadHatterIndicators.MACD, 0	, btroilistsorted[0][1])




def tuneMacdSignal():
			btroilist = []
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			currentvalue = basebotconfig.macd['MacdSignal']
			initvalue = currentvalue
			for x in range(5):
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.MACD, 2, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi, currentvalue)
				btroilist.append([btr.roi, currentvalue])
				currentvalue +=1
			currentvalue = initvalue-1
			for x in range(5):
				setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							guid, EnumMadHatterIndicators.MACD, 2, currentvalue)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
				print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
				btr = bt.result
				print(btr.roi, currentvalue)
				btroilist.append([btr.roi, currentvalue])
				currentvalue -=1
			btroilistsorted = sorted(btroilist, key=lambda x: x[0], reverse=True)
			setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				guid, EnumMadHatterIndicators.MACD, 2	, btroilistsorted[0][1])