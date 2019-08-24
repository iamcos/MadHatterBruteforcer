
# def writetimeinterval(guid):
#    basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
#    timeinterval = basebotconfig.timeinterval
#    print(timeinterval,' is timeinterval')

# def allcoinshistory():
#    timeintervals = {'1 minutes':1,'2 minutes':2,'3 minutes':3,'4 minutes':4,'5 minutes':5,'6 minutes':6,'10 minutes':10,'12 minutes':12,'15 minutes':15,'20 minutes':20,'30 minutes':30,'45 minutes':45,'1 hour':60,'1.5 hours':90,'2 hours':120,'2.5 hours':150,'3 hours':180,'4 hours':240,'6 hours':360,'12 hours':720,'1 day':1440,'2 days':2880}
#    allpairs = []
#    getpricesources = haasomeClient.marketDataApi.get_enabled_price_sources().result
#    for i,v in enumerate(getpricesources):
#     print(i, v.name)
#    pricesourceobj = getpricesources[2]
#    allmarketpairs = haasomeClient.marketDataApi.get_price_markets(EnumPriceSource.BINANCE).result
#    backtestfor = minutestobacktest()
#    for v in allmarketpairs():
#     history = safeHistoryGet(EnumPriceSource.BINANCE, v.primaryCurrency, v.secondaryCurrency, v.contractName, backtestfor, v[1], k)
#     allpairs.append([i, v.primaryCurrency, v.secondaryCurrency, v.contractName, [v[1],history]])
    
#    print(allpairs)
#    safeHistoryGet(pricesource, primarycoin, secondarycoin, contractname, backtestfor, timeInterval)

# def infinite_bt():
  
#   currentbot = botsellector()
#   # backtestfor = minutestobacktest()
#   guid = currentbot.guid
#   accountId = currentbot.accountId
#   for i in range(0,250):
#     basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result

#     indicators = basebotconfig.timeinterval, basebotconfig.bBands['Length'], basebotconfig.bBands['Devup'],basebotconfig.bBands['Devdn'],basebotconfig.bBands['MaType'],basebotconfig.bBands['Deviation'],basebotconfig.bBands['ResetMid'],basebotconfig.bBands['AllowMidSell'],basebotconfig.bBands['RequireFcc'],basebotconfig.rsi['RsiLength'], basebotconfig.rsi['RsiOversold'], basebotconfig.rsi['RsiOverbought'], basebotconfig.macd['MacdSlow'],basebotconfig.macd['MacdFast'], basebotconfig.macd['MacdSign']
#     bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountId, guid,1440,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
#     btr = bt.result.roi
#     print(btr, 'for 1D', indicators, btr)
  
#     bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountId, guid,1440*5,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
#     btr = bt.result.roi
#     print(btr, 'for 5D', indicators, btr)
  
#     # bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountId, guid,1440*7,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
#     # btr = bt.result.roi
#     # print(btr, 'for 1w', indicators, btr)
  
#     # bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountId, guid,43200,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
#     # btr = bt.result.roi
#     # print(btr, 'for 4W', indicators, btr)

   

# def getbasebotconfig(guid):
#     basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result

#     botname = basebotconfig.name
#     pricemarket = basebotconfig.priceMarket
#     primarycoin = pricemarket.primaryCurrency
#     secondarycoin = pricemarket.secondaryCurrency
#     fee = basebotconfig.currentFeePercentage
#     tradeamount = basebotconfig.currentTradeAmount
#     ammounttype = basebotconfig.amountType
#     coinposition = basebotconfig.coinPosition
#     consensus = basebotconfig.useTwoSignals
#     customtemplate= basebotconfig.customTemplate
#     icc = basebotconfig.includeIncompleteInterval
#     mappedbuysignal = basebotconfig.mappedBuySignal
#     mappedsellsignal = basebotconfig.mappedSellSignal
#     sldisable = basebotconfig.disableAfterStopLoss
#     leverage = basebotconfig.leverage
#     contractname = pricemarket.contractName

#     return botname, pricemarket, primarycoin, secondarycoin, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, icc, mappedbuysignal, mappedsellsignal, leverage, contractname



# def settimeinterval(guid, timeinterval):
  
#   timeintervals = [['1 minutes',1],['2 minutes',2],['3 minutes',3],['4 minutes',4],['5 minutes',5],['6 minutes',6],['10 minutes',10],['12 minutes',12],['15 minutes',15],['20 minutes',20],['30 minutes',30],['45 minutes',45],['1 hour',60],['1.5 hours',90],['2 hours',120],['2.5 hours',150],['3 hours',180],['4 hours',240],['6 hours',360],['12 hours',720],['1440 day',1440],['2880 days',2880]]
#   basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
#   initialinterval = basebotconfig.timeinterval
#   pricemarket = basebotconfig.priceMarket
#   contractname = pricemarket.contractName
#   timeinterval = basebotconfig.timeinterval

#   timeintervalnum = ''
#   for i,k  in enumerate(timeintervals):
#    if k[1] == timeinterval:
#     timeintervalnum = i
#   selectedinterval = timeintervals[timeintervalnum][0]

#   botname, primarycoin, secondarycoin, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, icc, mappedbuysignal, mappedsellsignal, leverage, contractname = getbasebotconfig(guid)
#   configbot = haasomeClient.customBotApi.setup_mad_hatter_bot(accountId, guid, botname, primarycoin, secondarycoin, customtemplate, contractname, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, timeinterval, icc, mappedbuysignal, mappedsellsignal, float(leverage))
#   # print('settimeinterval: ', configurebot.errorCode, configurebot.errorMessage)



# def bttimeintervals(guid, accountId):
#   backtestfor = minutestobacktest()
#   # timeintervals = [['1 minutes',1],['2 minutes',2],['3 minutes',3],['4 minutes',4],['5 minutes',5],['6 minutes',6],['10 minutes',10],['12 minutes',12],['15 minutes',15],['20 minutes',20],['30 minutes',30],['45 minutes',45],['1 hour',60],['1.5 hours',90],['2 hours',120],['2.5 hours',150],['3 hours',180],['4 hours',240],['6 hours',360],['12 hours',720],['1 day',1440],['2 days',2880]]
#   timeintervals = {'1 minutes':1,'2 minutes':2,'3 minutes':3,'4 minutes':4,'5 minutes':5,'6 minutes':6,'10 minutes':10,'12 minutes':12,'15 minutes':15,'20 minutes':20,'30 minutes':30,'45 minutes':45,'1 hour':60,'1.5 hours':90,'2 hours':120,'2.5 hours':150,'3 hours':180,'4 hours':240,'6 hours':360,'12 hours':720,'1 day':1440,'2 days':2880}
#   print(timeintervals)
#   print(timeintervals['30 minutes'])
#   basebotconfig, indicators, basebotdict, missingmarketdata = getmhconfig(guid)
#   btresults = {}
#   newbotfrommarket = haasomeClient.customBotApi.new_custom_bot_from_market(accountId, botType, 'new bot', basebotconfig.priceMarket)
#   pricemarkeT = basebotconfig.priceMarket
#   # help(pricemarkeT)
#   # print('Yoo!!!', pricemarkeT.__dict__)
#   print
#   for k, v in enumerate(timeintervals):
#    intervall = timeintervals.values
#    print(intervall)
#    botresult = newbotfrommarket.result
#    print(newbotfrommarket)
#    BotGuid = botresult.guid
#    configbot = haasomeClient.customBotApi.setup_mad_hatter_bot(basebotdict['accountId'], basebotdict['botGuid'],  basebotdict['botname'], missingmarketdata['primarycoin'],missingmarketdata['secondarycoin'], basebotdict['customtemplate'], '', basebotdict['coinposition'], missingmarketdata['fee'], basebotdict['ammounttype'], basebotdict['tradeamount'], basebotdict['consensus'], basebotdict['sldisable'],intervall, basebotdict['icc'], basebotdict['mappedbuysignal'], basebotdict['mappedsellsignal'], basebotdict['leverage'])
#    print('configurebot', configbot.errorCode, configbot.errorMessage)
#    bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotdict['accountId'], basebotdict['botGuid'],backtestfor, missingmarketdata['primarycoin'], missingmarketdata['secondarycoin'], 'BTC/USDT').result
   
#    btresults.update({'ROI':bt.roi, 'timeinterval': timeintervals[v],'pricemarket': basebotconfig.priceMarket,'primarycoin': pricemarket.primaryCurrency,'secondarycoin': pricemarket.secondaryCurrency,'fee': basebotconfig.currentFeePercentage,'tradeamount': basebotconfig.currentTradeAmount,'ammounttype': basebotconfig.amountType,'coinposition': basebotconfig.coinPosition,'consensus': basebotconfig.useTwoSignals,'customtemplate': basebotconfig.customTemplate,'icc': basebotconfig.includeIncompleteInterval,'mappedbuysignal': basebotconfig.mappedBuySignal,'mappedsellsignal': basebotconfig.mappedSellSignal,'sldisable': basebotconfig.disableAfterStopLoss,'leverage': basebotconfig.leverage, 'contractname': '', 'leverage': basebotconfig.leverage})
#    print(btresults)
  
  
# def bbtbbdev(guid):
#   basebotconfig, indicators, basebotdict, missingmarketdata = getmhconfig(guid)
#   btresults = []
#   devuprange = np.arange(0.7,3.0,0.5)
#   devdnrange = np.arange(0.7,3.0,0.5)
#   i = 0
#   for devup in devuprange:
#    i += 1
#    print(i, 'up: ',devup)
#    setdevup = setbbDevUp(guid, devup)
#    i += 1
#    for devdn in devdnrange:
#     i += 1
#     print(i, 'down: ', devdn)
#     setbbDevDown(guid, devdn)
#     bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotdict['accountId'], basebotdict['botGuid'],backtestfor,missingmarketdata['primarycoin'],missingmarketdata['secondarycoin'], contractname)
#     btr = bt.resul
#     print(devup, devdn, btr.roi)
#     btresults.append([btr.roi,devup, devdn])
#   btresultssorted = sorted(btresults, key=lambda x: x[0], reverse=True)
#   for i in range(10):
#    print(btresultssorted[i][1], btresultssorted[i][2],'ROI ',btresultssorted[i][0])
#   setdevup = setbbDevUp(guid, btresultssorted[i][1])
#   setbbDevDown(guid, btresultssorted[i][2])
#   print('deviations set to the top result')

# def bbtbbdevprecise(guid):
#   currentconfig = getmhindicators(guid)
#   currentdevup = currentconfig[1]
#   currentdevdn = currentconfig[2]
#   basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
#   pricemarket = basebotconfig.priceMarket
#   contractname = pricemarket.contractName
#   timeinterval = basebotconfig.timeinterval
#   botname, primarycoin, secondarycoin, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, icc, mappedbuysignal, mappedsellsignal, leverage, contractname = getbasebotconfig(guid)
#   #configurebot = haasomeClient.customBotApi.setup_mad_hatter_bot(accountId, guid, botname, primarycoin, secondarycoin, contractname, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, timeinterval, icc, mappedbuysignal, mappedsellsignal, leverage)
#   #print('configurebot', configurebot.errorCode, configurebot.errorMessage)
#   backtestfor = minutestobacktest()
#   btresults = [] 
#   stepup = 0.1
#   startup = currentdevup-(stepup*3)
#   endup = currentdevup+(stepup*3)
#   devuprange = np.around(np.arange(startup,endup,stepup), 2)
  
#   stepdn = 0.1
#   startdn = currentdevup-(stepdn*3)
#   enddn = currentdevup+(stepdn*3)
#   devdnrange = np.arange(startdn,enddn,stepdn)
#   devdnrange = np.around(devdnrange, 2)
#   for devup in devuprange:
  
#    setbbDevUp(guid, devup)
#    for devdn in devdnrange:
#     print('up: ',devup, 'down: ', devdn)
#     setbbDevDown(guid, devdn)
#     bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountId,guid,backtestfor, primarycoin, secondarycoin, contractname)
#     btr = bt.result
#     print(btr.roi, devup, devdn)
#     btresults.append([btr.roi,devup,devdn])
#   btresultssorted = sorted(btresults, key=lambda x: x[0], reverse=True)
#   for i in range(10):
#    print(btresultssorted[i][1], btresultssorted[i][2],'ROI ',btresultssorted[i][0])
#   setdevup = setbbDevUp(guid, btresultssorted[i][1])
#   setbbDevDown(guid, btresultssorted[i][2])
  # print('deviations set to the top result')


# def bbtrsil(guid):
#   currentconfig = getmhindicators(guid)
#   basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
#   pricemarket = basebotconfig.priceMarket
#   contractname = pricemarket.contractName
#   timeinterval = basebotconfig.timeinterval
#   botname, primarycoin, secondarycoin, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, icc, mappedbuysignal, mappedsellsignal, leverage, contractname = getbasebotconfig(guid)
#   #configurebot = haasomeClient.customBotApi.setup_mad_hatter_bot(accountId, guid, botname, primarycoin, secondarycoin, contractname, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, timeinterval, icc, mappedbuysignal, mappedsellsignal, leverage)
#   #print('configurebot', configurebot.errorCode, configurebot.errorMessage)
#   btresults = []
#   initrsil = currentconfig[8]
#   backtestfor = minutestobacktest()
#   for l in range(2,21):
#    setrsil = setRSILength(guid,l)
#    bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountId,guid,backtestfor, primarycoin, secondarycoin, contractname)
#    btr = bt.result
#    print('backtest:' , bt.errorCode, bt.errorMessage)
#    print(l, btr.roi)
#    btresults.append([btr.roi,l])
#   btresultssorted = sorted(btresults, key=lambda x: x[0], reverse=True)
#   print(btresultssorted[0][1],'gives best roi of: ',btresultssorted[0][0])

# # def bbtrsifinetune(guid):
#    currentconfig = getmhindicators(guid)
#    basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
#    pricemarket = basebotconfig.priceMarket
#    contractname = pricemarket.contractName
#    timeinterval = basebotconfig.timeinterval
#    botname, primarycoin, secondarycoin, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, icc, mappedbuysignal, mappedsellsignal, leverage, contractname = getbasebotconfig(guid)
#    #configurebot = haasomeClient.customBotApi.setup_mad_hatter_bot(accountId, guid, botname, primarycoin, secondarycoin, contractname, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, timeinterval, icc, mappedbuysignal, mappedsellsignal, leverage)
#    #print('configurebot', configurebot.errorCode, configurebot.errorMessage)
#    btresults = []
#    initrsil = currentconfig[8]
#    newrsil =  initrsil
#    backtestfor = minutestobacktest()
#    for l in range(0,3):
#     newrsil  += 1
#     setRSILength(guid,newrsil)
#     bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountId,guid,backtestfor, primarycoin, secondarycoin, contractname)
#     btr = bt.result
#     print('backtest:' , bt.errorCode, bt.errorMessage)
#     print(newrsil, btr.roi)
#     btresults.append([btr.roi,newrsil])
#    newrsil =  initrsil
#    for l in range(0,3):
#     newrsil  -= 1
#     setRSILength(guid,newrsil)
#     bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountId,guid,backtestfor, primarycoin, secondarycoin, contractname)
#     btr = bt.result
#     print('backtest:' , bt.errorCode, bt.errorMessage)
#     print(newrsil, btr.roi)
#     btresults.append([btr.roi,newrsil])
#    btresultssorted = sorted(btresults, key=lambda x: x[0], reverse=True)
#    print(btresultssorted[0][1],'gives best roi of: ',btresultssorted[0][0])

# def bbtbbl(guid):
#   currentconfig = getmhindicators(guid)
#   basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
#   pricemarket = basebotconfig.priceMarket
#   contractname = pricemarket.contractName
#   timeinterval = basebotconfig.timeinterval
#   botname, primarycoin, secondarycoin, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, icc, mappedbuysignal, mappedsellsignal, leverage, contractname = getbasebotconfig(guid)
#   #configurebot = haasomeClient.customBotApi.setup_mad_hatter_bot(accountId, guid, botname, primarycoin, secondarycoin, contractname, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, timeinterval, icc, mappedbuysignal, mappedsellsignal, leverage)
#   #print('configurebot', configurebot.errorCode, configurebot.errorMessage)
#   btresults = []
#   initbbl = currentconfig[0]
#   backtestfor = minutestobacktest()
#   for l in range(5,50):
#    setbbl = setbbLength(guid,l)
#    bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountId,guid,backtestfor, primarycoin, secondarycoin, contractname)
#    btr = bt.result
#    print('backtest:' , bt.errorCode, bt.errorMessage)
#    print(l, btr.roi)
#    btresults.append([btr.roi,l])
#   btresultssorted = sorted(btresults, key=lambda x: x[0], reverse=True)
#   print(btresultssorted[0][1],'gives best roi of: ',btresultssorted[0][0])
  


# def steptimeinterval(guid, accountId):
#   # timeintervals = [['1 minutes',1],['2 minutes',2],['3 minutes',3],['4 minutes',4],['5 minutes',5],['6 minutes',6],['10 minutes',10],['12 minutes',12],['15 minutes',15],['20 minutes',20],['30 minutes',30],['45 minutes',45],['1 hour',60],['1.5 hours',90],['2 hours',120],['2.5 hours',150],['3 hours',180],['4 hours',240],['6 hours',360],['12 hours',720],['1 day',1440],['2 days',2880]]
 
#   # print('Available time intervals for current bot are:')
#   if (char == None):
#    print('current timeinterval is set to: ', timeinterval)
#   basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
  
#   timeinterval = basebotconfig.timeinterval
#   timeintervalnum = ''
#   for i,k  in enumerate(timeintervals):
#    if k[1] == timeinterval:
#     print(i,k[0],'textline')
#     timeintervalnum = i
#   selectedinterval = timeintervals[timeintervalnum][1]
#   selectedintervaltext = timeintervals[timeintervalnum][0]
#   backtestfor = minutestobacktest()
# def sharemhbot(guid):
#   getbasebotconfig(guid)
  


# def safeHistoryGet(pricesource: EnumPriceSource, primarycoin: str, secondarycoin: str, contractname: str,backtestfor: int, depth: int):
#       history = None
#       historyResult = False
#       failCount = 0

#       while historyResult == False:
#            history = haasomeClient.marketDataApi.get_history(pricesource, primarycoin, secondarycoin, contractname,backtestfor, depth)
#            if len(history.result) > 1:
#                 historyResult = True
#            else:
#                 failCount = failCount + 1
#                 time.sleep(5)

#            if failCount == 10:
                # historyResult = True


      # return history

# def getmhindicators(guid):
#    basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
#    indicators = basebotconfig.bBands['Length'], basebotconfig.bBands['Devup'],basebotconfig.bBands['Devdn'],basebotconfig.bBands['MaType'],basebotconfig.bBands['Deviation'],basebotconfig.bBands['ResetMid'],basebotconfig.bBands['AllowMidSell'],basebotconfig.bBands['RequireFcc'],basebotconfig.rsi['RsiLength'], basebotconfig.rsi['RsiOversold'], basebotconfig.rsi['RsiOverbought'], basebotconfig.macd['MacdSlow'],basebotconfig.macd['MacdFast'], basebotconfig.macd['MacdSign']
#    print(indicators)
#    return indicators
# botnumobj = botsellector()
# pricemarket = botnumobj.priceMarket
# accountId = botnumobj.accountId
# guid = botnumobj.guid
# currentBotname = botnumobj.name
# MarketEnum = pricemarket.priceSource
# primarycurrency = pricemarket.primaryCurrency
# secondarycurrency = pricemarket.secondaryCurrency
# contractname = pricemarket.contractName
# try:
#   leverage = botnumobj.Leverage
# except:
#   leverage = Decimal(0.0)


# def indicatorfinetune(guid):
# 		currentconfig = getmhindicators(guid)
# 		# print(currentconfig)
# 		pricemarket = basebotconfig.priceMarket
# 		timeinterval = basebotconfig.timeinterval
# 		botname, primarycoin, secondarycoin, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, icc, mappedbuysignal, mappedsellsignal, leverage, contractname = getbasebotconfig(guid)
# 		#configurebot = haasomeClient.customBotApi.setup_mad_hatter_bot(accountId, guid, botname, primarycoin, secondarycoin, contractname, customtemplate, coinposition, fee, ammounttype, tradeamount, consensus, sldisable, timeinterval, icc, mappedbuysignal, mappedsellsignal, leverage)
# 		#print('configurebot', configurebot.errorCode, configurebot.errorMessage)
# 		# def getch():
# 		# 	fd = sys.stdin.fileno()
# 		# 	old_settings = termios.tcgetattr(fd)
# 		# 	try:
# 		# 					tty.setraw(sys.stdin.fileno())
# 		# 					ch = sys.stdin.read(1)

# 		# 	finally:
# 		# 					termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
# 		# 	return ch

# 		# 	button_delay = 0.2

# 		# 	fd = sys.stdin.fileno()
# 		# 	fl = fcntl.fcntl(fd, fcntl.F_GETFL)
# 		# 	fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)


# 		btresults = []
# 		bestroi = []
		
		
# 		backtestfor = minutestobacktest()
# 		print('Tap Q to select bbands length, A,S,D are for 3 rsi parameters. Z, X, C select MACD preferences. \n U does 3 backtests up, J - 3 bt down. I one bt up, K one bt down')
# 		while True:
# 				char = getch()
# 				if (char == 'q'):
# 					print('Bbands length selected')
# 					indicator = 	[EnumMadHatterIndicators.BBANDS, 0, 'Bbands L']
# 					initialparam = currentconfig[0]

# 				elif (char == '0'):
# 					print('Zero pressed. quitting')
# 					break

# 				elif (char == "w"):
# 					print('bbands deviation rought bruteforce initiated')
# 					bbtbbdev(guid, backtestfor)

# 				# elif (char == "e"):
# 				# 	print('bbands devdn selected')
# 				# 	indicator = [EnumMadHatterIndicators.BBANDS, 2]
# 				# 	initialparam = currentconfig[2]
# 				# 	start = 0.1
# 				# 	stop = 0.3
# 				# 	step = 0.1

# 				elif (char == "a"):
# 					print('RSI l selected')
# 					indicator = [EnumMadHatterIndicators.RSI, 0, 'RSI L']
# 					initialparam = currentconfig[8]


				
# 				elif (char == "2"):
# 					print('Step set to 2')
# 					step -=2
				


# 				elif (char == "d"):
# 						print('RSI Buy selected')
# 						currentconfig = getmhindicators(guid)
# 						indicator = [EnumMadHatterIndicators.RSI, 1,'RSI Buy']
# 						initialparam = currentconfig[9]

# 				elif (char == "s"):
# 						print('RSI Sell selected')
# 						indicator = [EnumMadHatterIndicators.RSI, 2, 'RSI Sell']
# 						initialparam = currentconfig[10]
# 				elif (char == "z"):
# 						print('MACD Fast selected')
# 						indicator = [EnumMadHatterIndicators.MACD, 0,'MACD Fast']
# 						initialparam = currentconfig[11]
# 				elif (char == "x"):
# 					print('MACD Slow selected')
# 					indicator = [EnumMadHatterIndicators.MACD, 1, 'MACD Slow']
# 					initialparam = currentconfig[12]
				
# 				elif (char == "c"):
# 						print('MACD Signal selected')
# 						indicator = 	[EnumMadHatterIndicators.MACD, 2, 'MACD signal']
# 						initialparam = currentconfig[13]
			
# 				elif (char == 66) or char == 'u':
# 						btresults = []
# 						start = 0
# 						stop = 4
# 						step = 1
# 						for v in np.arange(start,stop,step):
							
# 								initialparam  +=1
# 								haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
# 							guid, indicator[0],indicator[1],initialparam)
# 								bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountId,guid,backtestfor, primarycoin, secondarycoin, contractname)
# 								btr = bt.result
# 								# print('backtest:' , bt.errorCode, bt.errorMessage)
# 								print(initialparam, indicator[2], btr.roi)
# 								btresults.append([btr.roi,initialparam])

# 				elif (char == 66) or char == 'i':
# 						btresults = []
# 						start = 0
# 						stop = 1
# 						step = 1
# 						for v in np.arange(start,stop,step):
							
# 								initialparam  +=1
# 								haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
# 							guid, indicator[0],indicator[1],initialparam)
# 								bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountId,guid,backtestfor, primarycoin, secondarycoin, contractname)
# 								btr = bt.result
# 								# print('backtest:' , bt.errorCode, bt.errorMessage)
# 								print(initialparam, indicator[2], btr.roi)
# 								btresults.append([btr.roi,initialparam])
# 						# btresultssorted = sorted(btresults, key=lambda x: x[0], reverse=True)
# 						# print(btresultssorted[0][1],'gives best roi of: ',btresultssorted[0][0])
# 						# haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
# 						# 			guid, indicator[0], indicator[1],btresultssorted[0][1])
# 				elif (char == 67) or char == 'j':
# 								btresults = []
# 								start = 0
# 								stop = 4
# 								step = 1
# 								initialparam =  initialparam
# 								for v in np.arange(start, stop, step):
# 											initialparam  -= 1
# 											haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
# 											guid, indicator[0],indicator[1],initialparam)
# 											bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountId,guid,backtestfor, primarycoin, secondarycoin, contractname)
# 											btr = bt.result
# 											# print('backtest:' , bt.errorCode, bt.errorMessage)
# 											print(initialparam, indicator[2], btr.roi)
# 											btresults.append([btr.roi,initialparam])

# 				elif (char == 67) or char == 'k':
# 								btresults = []
# 								start = 0
# 								stop = 1
# 								step = 1
# 								initialparam =  initialparam
# 								for v in np.arange(start, stop, step):
# 											initialparam  -= 1
# 											haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
# 											guid, indicator[0],indicator[1],initialparam)
# 											bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountId,guid,backtestfor, primarycoin, secondarycoin, contractname)
# 											btr = bt.result
# 											# print('backtest:' , bt.errorCode, bt.errorMessage)
# 											print(initialparam, indicator[2], btr.roi)
# 											btresults.append([btr.roi,initialparam])
# 								# p0btresultssorted = sorted(btresults, key=lambda x: x[0], reverse=True)
# 								# print(btresultssorted[0][1],'gives best roi of: ',btresultssorted[0][0])
# 								# haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
# 								# guid, indicator[0], indicator[1],btresultssorted[0][1])	

# def savehistoricaldataatofile():
#    backtestfor = minutestobacktest()
#    timeinterval = input('type time interval number')
#    history = haasomeClient.marketDataApi.get_history(MarketEnum, primarycurrency, secondarycurrency, contractname, timeinterval,backtestfor).result
#    print(history)
#    with open('history.csv', 'w', newline='') as csvfile:
#       fieldnames = ['timeStamp','unixTimeStamp','open','highValue','lowValue','close','volume','currentBuyValue','currentSellValue']
#       csvwriter = csv.DictWriter(csvfile,fieldnames=fieldnames)
#       csvwriter.writeheader()
#       for i, v in enumerate(history):
#        csvwriter.writerow({'timeStamp': str(v.timeStamp),'unixTimeStamp': str(v.unixTimeStamp), 'open': float(v.open), 'highValue':  float(v.highValue), 'lowValue': float(v.lowValue),'close' : float(v.close),'volume': float(v.volume),'currentBuyValue': str(v.currentBuyValue),'currentSellValue': float(v.currentSellValue)})

# bottypedict = {1:'MARKET_MAKING_BOT',2:'PING_PONG_BOT',3:'SCALPER_BOT',4:'ORDER_BOT',6:'FLASH_CRASH_BOT',8:'INTER_EXCHANGE_ARBITRAGE_BOT',9:'INTELLIBOT_ALICE_BOT',12:'ZONE_RECOVERY_BOT',13:'ACCUMULATION_BOT',14:'TREND_LINES_BOT',15:'MAD_HATTER_BOT',16:'SCRIPT_BOT',17:'CRYPTO_INDEX_BOT',18:'HAAS_SCRIPT_BOT',19:'EMAIL_BOT',20:'ADVANCED_INDEX_BOT',1000:'BASE_CUSTOM_BOT'}

# def botsellector():
#   everybot = haasomeClient.customBotApi.get_all_custom_bots().result
#   allmhbots = []
#   for i, x in enumerate(everybot):
#       if x.botType == 15:
#         allmhbots.append(x)
 
#   for i, x in enumerate(allmhbots): 
#     print(i, x.name, 'ROI : ',x.roi, len(x.completedOrders),' trades') 
#   botnum = input(
#     'Type bot number to use from the list above and hit return. \n Your answer: ')
#   try:
#     botnumobj = allmhbots[int(botnum)]
#   except ValueError:
#      botnum = input(
#     'Wrong symbol. Can only use numbers. Type bot number indecated at the start of the string here: ')
#   except IndexError: 
#     botnum = input(
#     'Bot number is out of range. Type the number that is present on the list and hit enter: ')
#   finally:
#     botnumobj = allmhbots[int(botnum)]
#   print('Bot ', botnumobj.name +' is selected!')
#   return botnumobj

# def bottimeinterval():
#   timeintervals = {'1 minutes':1,'2 minutes':2,'3 minutes':3,'4 minutes':4,'5 minutes':5,'6 minutes':6,'10 minutes':10,'12 minutes':12,'15 minutes':15,'20 minutes':20,'30 minutes':30,'45 minutes':45,'1 hour':60,'1.5 hours':90,'2 hours':120,'2.5 hours':150,'3 hours':180,'4 hours':240,'6 hours':360,'12 hours':720,'1 day':1440,'2 days':2880}
#   print('Available time intervals for current bot are:')
#   timeintext = list(timeintervals.keys())

#   for i, k in enumerate(timeintext):
#    print(i, k)
#   userinput = input('type interval number to select it: ')
#   selected = timeintext[int(userinput)]
#   selectedintervalinminutes = timeintervals[selected]
#   print(selected, 'set as time interval')
#   return selectedintervalinminutes
# def getrawbot():
#   currentbot = botsellector()
#   # backtestfor = minutestobacktest()
#   guid = currentbot.guid
#   one, two  = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT)
#   print(one, two)
  



# def getmhconfig(guid):
#    basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
#    indicators = {}
#    basebotdict = {}
#    missingmarketdata = {}
#    currentpricesource = []
#    pricemarket = basebotconfig.priceMarket
#    pricemarkets = haasomeClient.marketDataApi.get_price_markets(pricemarket.priceSource).result
#   #  print(basebotconfig.__dict__)
#    for i, v in enumerate(pricemarkets):
#     if v.primaryCurrency == pricemarket.primaryCurrency and v.secondaryCurrency == pricemarket.secondaryCurrency:
#       # missingmarketdata.update({'mintradeammount':v.minimumTradeAmount, 'fee':v.tradeFee, 'pricesource': v.priceSource,'primarycoin': v.primaryCurrency,'secondarycoin': v.secondaryCurrency, 'contractname': v.contractName, 'displayname': v.displayName})
#       missingmarketdata.update({'mintradeammount':v.minimumTradeAmount, 'fee':v.tradeFee, 'pricesource': v.priceSource,'primarycoin': v.primaryCurrency,'secondarycoin': v.secondaryCurrency, 'contractname': v.contractName, 'displayname': v.displayName, 'shortname': v.shortName})
#       print(missingmarketdata, '\n\n\n')
#    print(missingmarketdata)
#    indicators.update({'timeinterval': basebotconfig.interval, 'bbl':basebotconfig.bBands['Length'], 'bbdevup':basebotconfig.bBands['Devup'],'bbdevdn':basebotconfig.bBands['Devdn'],'matype': basebotconfig.bBands['MaType'],'Deviation':basebotconfig.bBands['Deviation'],'rm':basebotconfig.bBands['ResetMid'],'ams': basebotconfig.bBands['AllowMidSell'],'fcc':basebotconfig.bBands['RequireFcc'],'rsil':basebotconfig.rsi['RsiLength'], 'rsisell':basebotconfig.rsi['RsiOversold'], 'rsibuy': basebotconfig.rsi['RsiOverbought'], 'macdslow':basebotconfig.macd['MacdSlow'],'macdfast': basebotconfig.macd['MacdFast'], 'macdsign':basebotconfig.macd['MacdSign']})
#    print(indicators)
#    basebotdict.update({'accountId': basebotconfig.accountId,'botGuid':basebotconfig.guid, 'botname': basebotconfig.name,'tradeamount': basebotconfig.currentTradeAmount,'ammounttype': basebotconfig.amountType,'coinposition': basebotconfig.coinPosition,'consensus': basebotconfig.useTwoSignals,'customtemplate': basebotconfig.customTemplate,'icc': basebotconfig.includeIncompleteInterval,'mappedbuysignal': basebotconfig.mappedBuySignal,'mappedsellsignal': basebotconfig.mappedSellSignal,'sldisable': basebotconfig.disableAfterStopLoss,'leverage': basebotconfig.leverage, 'contractname': missingmarketdata['contractname']}) #'minimumtradeammount': pricemarket.minimumTradeAmount
#    print(basebotdict)
   
#    return basebotconfig, indicators, basebotdict, missingmarketdata


# def findbtperiod():
#   backtestfor = minutestobacktest()
#   history = safeHistoryGet(MarketEnum, primarycurrency, secondarycurrency, "", 1,backtestfor*2)
#   candles = history.result
#   percentagetocheck = int(50)
#   print(len(candles))
#   timeframeinminutes = int(interval)
#   percentagetocheckstep = int(5)

#   percentageUpDownFinal = int((int(percentagetocheck)/100 * int(timeframeinminutes)))

#   candlesToCheck = []

#   highestCandleFromTestRange = None
#   lowestCandleFromTestRange = None

#   # Get the candles to check
#   print("Calculating candles to test for best start time")

#   for x in range(int(percentageUpDownFinal)+1):
#        if x == 0:
#             candlesToCheck.append(candles[timeframeinminutes])
#        else:
#             candlesToCheck.append(candles[timeframeinminutes-x])
#             candlesToCheck.append(candles[timeframeinminutes+x])

#   highestCandleFromTestRange = candlesToCheck[0]
#   lowestCandleFromTestRange = candlesToCheck[0]

#   for candle in candlesToCheck:
#        if candle.close > highestCandleFromTestRange.close:
#             highestCandleFromTestRange = candle

#        if candle.close < lowestCandleFromTestRange.close:
#             lowestCandleFromTestRange = candle

#   print("Lowest Candle Price Found: " + str(lowestCandleFromTestRange.close))
#   print("Highest Candle Price Found: " + str(highestCandleFromTestRange.close))

#   stepCandleAmount = int(5/100 * percentageUpDownFinal)

#   sortedCandles = sorted(candlesToCheck, key=operator.attrgetter('close'))

#   tasks = {}
#   botResults = {}
#   for x in range (5):

#        newBacktestLength = int((datetime.datetime.utcnow() - sortedCandles[stepCandleAmount*x].timeStamp).total_seconds() / 60) 
#        task = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountId, guid, newBacktestLength, primarycurrency, secondarycurrency, contractname).result
#        roi = task.roi

#        tasks[newBacktestLength] = roi

#   while len(botResults) != len(tasks):
#        for k, v in tasks.items():
#             result = v
#             if result != None:
#                   botResults[k] = result
#   print('')
#   print("Tested coin pair: " + primarycurrency + "/" + secondarycurrency)
#   print("Ran with the following settings")
#   print("Percentage To Check: " + str(percentagetocheck))
#   print("Percentage To Step " + str(percentagetocheckstep))
#   print('')
#   bestSettings = list(botResults.values())[0]
#   bestLength = list(botResults.keys())[0]

#   for k,v in botResults.items():
#       if v > bestSettings:
#            bestSettings = v
#            bestLength = k

#       print("Result Length:" + str(k) + " Settings:" + str(v))

#   print('')
#   print("Smart scalper task finished")
#   return "HPRV: " + str(lowestCandleFromTestRange.close) + " LPRV:" + str(highestCandleFromTestRange.close) + " CL:" + str(bestLength) + " BSP:" + str(candles[bestLength].close) + " Settings: " + str(bestSettings)

 # user_resp2 = input(
  #  'What would you like to do with selected bot? \n\n 1. Backtest config on different time intervals? )(does not work in most cases, waiting for api wrapper to be updated).\n 2. Quick bruteforce bollingerbaands length. \n 3.Test Bbands devUP and devDOWN combinations. \n 4. Do your crazy coding shit\n 5. Enable interactive backtesting mode: 1 buttno changes bot parameter and gives you instant ROI. \n 6 rawbotdata \n 0. Backtest multiple settings')
  #   #\n4. Interactive time interval backtesting \n 5. Test bot for every time interval \n \n Your answer: 
  # if user_resp2 == '0':
   

  # if user_resp2 == '1':
  #  bttimeintervals(guid, accountId)
  #  # getmhconfig(guid)
  # elif user_resp2 == '2':
  #   bbtrsifinetune(guid)	
  #  # allcoinshistory()
  # elif user_resp2 == '3':
  #  bbtbbdev(guid)
   
  # #  bttimeintervals(guid, accountId)
  # elif user_resp2 == '4':
  #  infinite_bt()
  #  # bttimeintervals(guid, accountId)
  # elif user_resp2 == '5':
  #  indicatorfinetune(guid)
  #  # bttimeintervals(guid, accountId)
  # elif user_resp2 == '6':
  #  getrawbot()
  # elif user_resp2 == '7':
  #  pass
  # elif user_resp2 == '8':
  #  bttimeintervals(guid, accountId)
  # elif user_resp2 == '9':
  #  pass

# def btbblrange():

# def setstopLoss(guid, stopLoss):
#   haasomeClient.customBotApi.set_mad_hatter_safety_parameter(
#     guid, EnumMadHatterSafeties.STOP_LOSS, stopLoss)

# def setbbLength(guid ,bbLength):

#   setbbl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
#     guid, EnumMadHatterIndicators.BBANDS, 0, bbLength)
#   print('SET BBL: ', setbbl.errorCode, setbbl.errorMessage)

# def setbbDevUp(guid,bbDevUp ):
#   haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
#     guid, EnumMadHatterIndicators.BBANDS, 1, bbDevUp)
# def setbbDevDown(guid, bbDevDown):
#   haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
#     guid, EnumMadHatterIndicators.BBANDS, 2, bbDevDown)

# def setbbMAType(guid, bbMAType):
#   haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
#     guid, EnumMadHatterIndicators.BBANDS, 3, bbMAType)

# def setfcc(guid, fcc):
#   haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
#        guid, EnumMadHatterIndicators.BBANDS, 5, fcc)

# def setrm(guid, rm):
#   haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
#        guid, EnumMadHatterIndicators.BBANDS, 6, rm)

# def setmms(guid, mms):
#   haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
#        guid, EnumMadHatterIndicators.BBANDS, 7, mms)

# def setRSILength(guid, RSILength):
#   haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
#     guid, EnumMadHatterIndicators.RSI, 0, RSILength)

# def setRSIBuy(guid, RSIBuy):
#   haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
#     guid, EnumMadHatterIndicators.RSI, 1, RSIBuy)

# def setRSSell(guid, RSSell):
#   haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
#     guid, EnumMadHatterIndicators.RSI, 2, RSISell)

# def setMACDFast(guid, MACDFast):
#   haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
#     guid, EnumMadHatterIndicators.MACD, 0, MACDFast)

# def setMACDSlow(guid, MACDSlow):
#   haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
#     guid, EnumMadHatterIndicators.MACD, 1, MACDSlow)
# def setMACDSignal(guid, MACDSignal):
#   haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
#     guid, EnumMadHatterIndicators.MACD, 2, MACDSignal)




