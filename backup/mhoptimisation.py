
class madHatter:
	
		def __init__(self):
				self


		def findbtperiod():
			interval = setbotbtinterval()
			history = safeHistoryGet(MarketEnum, primarycurrency, secondarycurrency, "", 1, interval*2)
			candles = history.result
			percentagetocheck = int(50)
			print(len(candles))
			timeframeinminutes = int(interval)
			percentagetocheckstep = int(5)

			percentageUpDownFinal = int((int(percentagetocheck)/100 * int(timeframeinminutes)))

			candlesToCheck = []

			highestCandleFromTestRange = None
			lowestCandleFromTestRange = None

			# Get the candles to check
			print("Calculating candles to test for best start time")

			for x in range(int(percentageUpDownFinal)+1):
							if x == 0:
											candlesToCheck.append(candles[timeframeinminutes])
							else:
											candlesToCheck.append(candles[timeframeinminutes-x])
											candlesToCheck.append(candles[timeframeinminutes+x])

			highestCandleFromTestRange = candlesToCheck[0]
			lowestCandleFromTestRange = candlesToCheck[0]

			for candle in candlesToCheck:
							if candle.close > highestCandleFromTestRange.close:
											highestCandleFromTestRange = candle

							if candle.close < lowestCandleFromTestRange.close:
											lowestCandleFromTestRange = candle

			print("Lowest Candle Price Found: " + str(lowestCandleFromTestRange.close))
			print("Highest Candle Price Found: " + str(highestCandleFromTestRange.close))

			stepCandleAmount = int(5/100 * percentageUpDownFinal)

			sortedCandles = sorted(candlesToCheck, key=operator.attrgetter('close'))

			tasks = {}
			botResults = {}
			for x in range (5):

							newBacktestLength = int((datetime.datetime.utcnow() - sortedCandles[stepCandleAmount*x].timeStamp).total_seconds() / 60) 
							task = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountGuid, currentBotGuid, newBacktestLength, primarycurrency, secondarycurrency, contractname).result
							roi = task.roi

							tasks[newBacktestLength] = roi

			while len(botResults) != len(tasks):
							for k, v in tasks.items():
											result = v
											if result != None:
															botResults[k] = result
			print('')
			print("Tested coin pair: " + primarycurrency + "/" + secondarycurrency)
			print("Ran with the following settings")
			print("Percentage To Check: " + str(percentagetocheck))
			print("Percentage To Step " + str(percentagetocheckstep))
			print('')
			bestSettings = list(botResults.values())[0]
			bestLength = list(botResults.keys())[0]

			for k,v in botResults.items():
						if v > bestSettings:
										bestSettings = v
										bestLength = k

						print("Result Length:" + str(k) + " Settings:" + str(v))

			print('')
			print("Smart scalper task finished")
			return "HPRV: " + str(lowestCandleFromTestRange.close) + " LPRV:" + str(highestCandleFromTestRange.close) + " CL:" + str(bestLength) + " BSP:" + str(candles[bestLength].close) + " Settings: " + str(bestSettings)

		def settimeinterval(currentBotGuid, timeinterval):
			timeintervals = [['1 minutes',1],['2 minutes',2],['3 minutes',3],['4 minutes',4],['5 minutes',5],['6 minutes',6],['10 minutes',10],['12 minutes',12],['15 minutes',15],['20 minutes',20],['30 minutes',30],['45 minutes',45],['1 hour',60],['1.5 hours',90],['2 hours',120],['2.5 hours',150],['3 hours',180],['4 hours',240],['6 hours',360],['12 hours',720],['1440 day',1440],['2880 days',2880]]
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(currentBotGuid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			initialinterval = basebotconfig.interval
			pricemarket = basebotconfig.priceMarket
			contractname = pricemarket.contractName
			timeinterval = basebotconfig.interval

			timeintervalnum = ''
			for i,k  in enumerate(timeintervals):
				if k[1] == timeinterval:
					timeintervalnum = i
			selectedinterval = timeintervals[timeintervalnum][0]

			botname, primarycoin, secondarycoin, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, icc, mappedbuysignal, mappedsellsignal, leverage = getbasebotconfig(currentBotGuid)
			configbot = haasomeClient.customBotApi.setup_mad_hatter_bot(accountGuid, currentBotGuid, botname, primarycoin, secondarycoin, customtemplate, contractname, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, timeinterval, icc, mappedbuysignal, mappedsellsignal, float(leverage))
			# print('settimeinterval: ', configurebot.errorCode, configurebot.errorMessage)



		def bttimeintervals(currentBotGuid, accountGuid):
			timeintervals = (['1 minutes',1],['2 minutes',2],['3 minutes',3],['4 minutes',4],['5 minutes',5],['6 minutes',6],['10 minutes',10],['12 minutes',12],['15 minutes',15],['20 minutes',20],['30 minutes',30],['45 minutes',45],['1 hour',60],['1.5 hours',90],['2 hours',120],['2.5 hours',150],['3 hours',180],['4 hours',240],['6 hours',360],['12 hours',720],['1 day',1440],['2 days',2880])
			# print('Available time intervals for current bot are:')
			
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(currentBotGuid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			botname, primary
			coin, secondarycoin, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, icc, mappedbuysignal, mappedsellsignal, leverage = getbasebotconfig(currentBotGuid)
			initialinterval = basebotconfig.interval
			pricemarket = basebotconfig.priceMarket
			contractname = pricemarket.contractName
			timeinterval = basebotconfig.interval
			interval = setbotbtinterval()
			
			btresults = []
			for l in range(0,26):
				print(timeintervals[l][1])
				configbot = haasomeClient.customBotApi.setup_mad_hatter_bot(basebotconfig.accountId, basebotconfig.guid, botname, primarycoin, secondarycoin, customtemplate, contractname, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, timeintervals[l][1], icc, mappedbuysignal, mappedsellsignal, float(leverage))
				print('configurebot', configbot.errorCode, configbot.errorMessage)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId,basebotconfig.guid, interval, primarycoin, secondarycoin, ' ')
				btr = bt.result

		def bbtbbdev(currentBotGuid):
			currentconfig = getmhindicators(currentBotGuid)
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(currentBotGuid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			pricemarket = basebotconfig.priceMarket
			contractname = pricemarket.contractName
			timeinterval = basebotconfig.interval
			botname, primarycoin, secondarycoin, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, icc, mappedbuysignal, mappedsellsignal, leverage = getbasebotconfig(currentBotGuid)
			#configurebot = haasomeClient.customBotApi.setup_mad_hatter_bot(accountGuid, currentBotGuid, botname, primarycoin, secondarycoin, contractname, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, timeinterval, icc, mappedbuysignal, mappedsellsignal, leverage)
			#print('configurebot', configurebot.errorCode, configurebot.errorMessage)
			interval = setbotbtinterval()

			btresults = []
			devuprange = np.arange(0.0,3.0,0.5)
			devdnrange = np.arange(0.0,3.0,0.5)
			i = 0
			for devup in devuprange:
				i += 1
				print(i, 'up: ',devup)
				setdevup = setbbDevUp(currentBotGuid, devup)
				i += 1
				for devdn in devdnrange:
					i += 1
					print(i, 'down: ', devdn)
					setbbDevDown(currentBotGuid, devdn)
					bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountGuid,currentBotGuid,interval, primarycoin, secondarycoin, contractname)
					btr = bt.result
					print(devup, devdn, btr.roi)
					btresults.append([btr.roi,devup, devdn])
			btresultssorted = sorted(btresults, key=lambda x: x[0], reverse=True)
			for i in range(10):
				print(btresultssorted[i][1], btresultssorted[i][2],'ROI ',btresultssorted[i][0])


		def bbtbbl(currentBotGuid):
			currentconfig = getmhindicators(currentBotGuid)
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(currentBotGuid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			pricemarket = basebotconfig.priceMarket
			contractname = pricemarket.contractName
			timeinterval = basebotconfig.interval
			botname, primarycoin, secondarycoin, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, icc, mappedbuysignal, mappedsellsignal, leverage = getbasebotconfig(currentBotGuid)
			#configurebot = haasomeClient.customBotApi.setup_mad_hatter_bot(accountGuid, currentBotGuid, botname, primarycoin, secondarycoin, contractname, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, timeinterval, icc, mappedbuysignal, mappedsellsignal, leverage)
			#print('configurebot', configurebot.errorCode, configurebot.errorMessage)
			btresults = []
			initbbl = currentconfig[0]
			interval = setbotbtinterval()
			for l in range(5,50):
				setbbl = setbbLength(currentBotGuid,l)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountGuid,currentBotGuid,interval, primarycoin, secondarycoin, contractname)
				btr = bt.result
				print('backtest:' , bt.errorCode, bt.errorMessage)
				print(l, btr.roi)
				btresults.append([btr.roi,l])
			btresultssorted = sorted(btresults, key=lambda x: x[0], reverse=True)
			print(btresultssorted[0][1],'gives best roi of: ',btresultssorted[0][0])


			def steptimeinterval(currentBotGuid, accountGuid):
				timeintervals = [['1 minutes',1],['2 minutes',2],['3 minutes',3],['4 minutes',4],['5 minutes',5],['6 minutes',6],['10 minutes',10],['12 minutes',12],['15 minutes',15],['20 minutes',20],['30 minutes',30],['45 minutes',45],['1 hour',60],['1.5 hours',90],['2 hours',120],['2.5 hours',150],['3 hours',180],['4 hours',240],['6 hours',360],['12 hours',720],['1 day',1440],['2 days',2880]]
			# print('Available time intervals for current bot are:')
			if (char == None):
				print('current timeinterval is set to: ', timeinterval)
			basebotconfig = haasomeClient.customBotApi.get_custom_bot(currentBotGuid, EnumCustomBotType.BASE_CUSTOM_BOT).result
			
			timeinterval = basebotconfig.interval
			timeintervalnum = ''
			for i,k  in enumerate(timeintervals):
				if k[1] == timeinterval:
					print(i,k[0],'textline')
					timeintervalnum = i
			selectedinterval = timeintervals[timeintervalnum][1]
			selectedintervaltext = timeintervals[timeintervalnum][0]
			interval = setbotbtinterval()
			
			char = getch()
			if (char =="u"):
				print('increasing value')
				configurebot = settimeinterval(currentBotGuid, selectedinterval)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountGuid,currentBotGuid,interval, pricemarket.primaryCurrency, pricemarket.secondaryCurrency, '')
				btr = bt.result
				timeintervalnum +=1
				selectedinterval = timeintervals[timeintervalnum][1]
				selectedintervaltext = timeintervals[timeintervalnum][0]
				print('backtest:' , bt.errorCode, bt.errorMessage)
				print(btr.roi, selectedintervaltext)
				again = input('type u to increase interval, d to decrease for else\n Your answer: ')
			if (char =="d"):
				configurebot = settimeinterval(currentBotGuid, selectedinterval)
				bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountGuid,currentBotGuid,interval, pricemarket.primaryCurrency, pricemarket.secondaryCurrency, '')
				btr = bt.result
				timeintervalnum -=1
				selectedinterval = timeintervals[timeintervalnum][1]
				selectedintervaltext = timeintervals[timeintervalnum][0]
				print('backtest:' , bt.errorCode, bt.errorMessage)
				print(btr.roi, selectedintervaltext)
				again = input('type u to increase interval, d to decrease')

		def writetimeinterval(currentBotGuid):
				basebotconfig = haasomeClient.customBotApi.get_custom_bot(currentBotGuid, EnumCustomBotType.BASE_CUSTOM_BOT).result
				timeinterval = basebotconfig.interval
				print(timeinterval,' is timeinterval')


		def setstopLoss(currentBotGuid, stopLoss):
				haasomeClient.customBotApi.set_mad_hatter_safety_parameter(
					currentBotGuid, EnumMadHatterSafeties.STOP_LOSS, stopLoss)

		def setbbLength(currentBotGuid ,bbLength):
			setbbl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
					currentBotGuid, EnumMadHatterIndicators.BBANDS, 0, bbLength)
			print('SET BBL: ', setbbl.errorCode, setbbl.errorMessage)

		def setbbDevUp(currentBotGuid,bbDevUp ):
			haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
					currentBotGuid, EnumMadHatterIndicators.BBANDS, 1, bbDevUp)
		def setbbDevDown(currentBotGuid, bbDevDown):
			haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
					currentBotGuid, EnumMadHatterIndicators.BBANDS, 2, bbDevDown)

		def setbbMAType(currentBotGuid, bbMAType):
			haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
					currentBotGuid, EnumMadHatterIndicators.BBANDS, 3, bbMAType)

		def setfcc(currentBotGuid, fcc):
			haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							currentBotGuid, EnumMadHatterIndicators.BBANDS, 5, fcc)

		def setrm(currentBotGuid, rm):
			haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							currentBotGuid, EnumMadHatterIndicators.BBANDS, 6, rm)

		def setmms(currentBotGuid, mms):
			haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							currentBotGuid, EnumMadHatterIndicators.BBANDS, 7, mms)

		def setRSILength(currentBotGuid, RSILength):
			haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
					currentBotGuid, EnumMadHatterIndicators.RSI, 0, RSILength)

		def setRSIBuy(currentBotGuid, RSIBuy):
			haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
					currentBotGuid, EnumMadHatterIndicators.RSI, 1, RSIBuy)

		def setRSSell(currentBotGuid, RSSell):
			haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
					currentBotGuid, EnumMadHatterIndicators.RSI, 2, RSISell)

		def setMACDFast(currentBotGuid, MACDFast):
			haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
					currentBotGuid, EnumMadHatterIndicators.MACD, 0, MACDFast)

		def setMACDSlow(currentBotGuid, MACDSlow):
			haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
					currentBotGuid, EnumMadHatterIndicators.MACD, 1, MACDSlow)
		def setMACDSignal(currentBotGuid, MACDSignal):
			haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
					currentBotGuid, EnumMadHatterIndicators.MACD, 2, MACDSignal)















			# def configuremhsafety(currentBotGuid, sellStep, buyStep, stopLoss):
# 	sellStep == 0
# 	buyStep == 0
# 	sellStep = haasomeClient.customBotApi.set_mad_hatter_safety_parameter(
# 			currentBotGuid, EnumMadHatterSafeties.PRICE_CHANGE_TO_SELL, sellStep)
# 	buyStep = haasomeClient.customBotApi.set_mad_hatter_safety_parameter(
# 			currentBotGuid, EnumMadHatterSafeties.PRICE_CHANGE_TO_BUY, buyStep)
# 	stopLoss = haasomeClient.customBotApi.set_mad_hatter_safety_parameter(
# 			currentBotGuid, EnumMadHatterSafeties.STOP_LOSS, stopLoss)

# def configuremh(currentBotGuid, bbLength, bbDevUp, bbDevDown, bbMAType, fcc, rm, mms, RSILength, RSIBuy, RSISell, MACDSlow, MACDFast, MACDSignal):
	
# 				bbLength = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
# 						currentBotGuid, EnumMadHatterIndicators.BBANDS, 0, bbLength)

# 				bbDevUp = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
# 						currentBotGuid, EnumMadHatterIndicators.BBANDS, 1, bbDevUp)

# 				bbDevDown = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
# 						currentBotGuid, EnumMadHatterIndicators.BBANDS, 2, bbDevDown)

# 				bbMAType = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
# 						currentBotGuid, EnumMadHatterIndicators.BBANDS, 3, bbMAType)

# 				RSILength = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
# 						currentBotGuid, EnumMadHatterIndicators.RSI, 0, RSILength)

# 				RSIBuy = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
# 						currentBotGuid, EnumMadHatterIndicators.RSI, 1, RSIBuy)

# 				RSSell = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
# 						currentBotGuid, EnumMadHatterIndicators.RSI, 2, RSISell)

# 				MACDFast = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
# 						currentBotGuid, EnumMadHatterIndicators.MACD, 0, MACDFast)

# 				MACDSlow = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
# 						currentBotGuid, EnumMadHatterIndicators.MACD, 1, MACDSlow)
# 				MACDSignal = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
# 						currentBotGuid, EnumMadHatterIndicators.MACD, 2, MACDSignal)

# 				fcc = fcc
# 				if fcc == 1:
# 						fcc = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
# 								currentBotGuid, EnumMadHatterIndicators.BBANDS, 5, True)
# 				elif fcc == 0:
# 						fcc = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
# 								currentBotGuid, EnumMadHatterIndicators.BBANDS, 5, false)
# 				else:
# 						fcc = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
# 								currentBotGuid, EnumMadHatterIndicators.BBANDS, 5, fcc)

# 				rm = rm
# 				if rm == 1:
# 						rm = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
# 								currentBotGuid, EnumMadHatterIndicators.BBANDS, 6, True)
# 				elif rm == 0:
# 						rm = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
# 								currentBotGuid, EnumMadHatterIndicators.BBANDS, 6, False)
# 				else:
# 						rm = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
# 								currentBotGuid, EnumMadHatterIndicators.BBANDS, 6, rm)

# 				mms = mms
# 				if mms == 1:
# 						mms = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
# 								currentBotGuid, EnumMadHatterIndicators.BBANDS, 7, True)
# 				elif mms == 0:
# 						mms = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
# 								currentBotGuid, EnumMadHatterIndicators.BBANDS, 7, false)
# 				else:
# 						mms = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
# 								currentBotGuid, EnumMadHatterIndicators.BBANDS, 7, mms)
# 				return currentBotGuid
