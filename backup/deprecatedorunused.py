def getmhbotconfig(currentBotGuid):
	botconfig = haasomeClient.customBotApi.get_custom_bot(currentBotGuid, EnumCustomBotType.MAD_HATTER_BOT).result
	basebotconfig = haasomeClient.customBotApi.get_custom_bot(currentBotGuid, EnumCustomBotType.BASE_CUSTOM_BOT).result
	#help(botconfig)
	print('\n',botconfig.__dict__,'\n')
	# print('\n',botconfig.__annotations__,'\n')
	rsi = botconfig.rsi
	rsidata = rsi.indicatorInterface
	rsi_length = dict(rsidata[0])
	rsi_buy = dict(rsidata[1])
	rsi_sell = dict(rsidata[2])
	rsiconfig = rsi_length['Value'], rsi_buy['Value'], rsi_sell['Value']
	bbands = botconfig.bBands
	bbandsconfig = bbands['Length'], bbands['Devup'],bbands['Devdn'],bbands['MaType'],bbands['Deviation'],bbands['ResetMid'],bbands['AllowMidSell'],bbands['RequireFcc'],bbands['Length']
	macd = botconfig.macd
	macddata = macd.indicatorInterface
	macd_fast = dict(macddata[0])
	macd_slow = dict(macddata[1])
	macd_signal = dict(macddata[2])
	includeincompleteinterval = botconfig.includeIncompleteInterval
	usetwosignals = botconfig.useTwoSignals
	contractname = ''#botconfig.ContractName
	coinposition = ''#botconfig.CoinPosition
	mappedlongsignal = ''#botconfig.MappedLongSignal
	mappedshortsignal = ''#botconfig.MappedShortSignal
	isorderstoplossactive = botconfig.isOrderStopLossActive
	isextensionorderactive = botconfig.isExtensionOrderActive
	currenttradeammount = botconfig.currentTradeAmount
	lastbuyprice = botconfig.lastBuyPrice
	lastsellprice = botconfig.lastSellPrice
	accountGuid = botconfig.accountId
	currentBotGuid = botconfig.accountId
	botname = botconfig.name
	leverage = botconfig.leverage
	botlogbook = ''#botconfig.botlogbook

rval
	macdconfig = macd_fast['Value'], macd_slow['Value'], macd_signal['Value']
	
	bbandsrsimacd = bbands['Length'], bbands['Devup'],bbands['Devdn'],bbands['MaType'],bbands['Deviation'],bbands['ResetMid'],bbands['AllowMidSell'],bbands['RequireFcc'],bbands['Length'],rsi_length['Value'], rsi_buy['Value'], rsi_sell['Value'], macd_fast['Value'], macd_slow['Value'], macd_signal['Value']
	
	customtemplate = botconfig.customTemplate
	print(bbandsconfig, rsiconfig, macdconfig, '\n', bbandsrsimacd, '\n', customtemplate, '\n', leverage, botname, currentBotGuid, accountGuid,lastsellprice,lastbuyprice,currenttradeammount,isextensionorderactive, isorderstoplossactive, mappedshortsignal, mappedlongsignal, coinposition, usetwosignals, includeincompleteinterval, coinposition)
	return  bbandsconfig, rsiconfig, macdconfig



def findstoploss():
		interval = setinterval()
		sl = np.arange(1, 10, 0.5)
		slroi = list()
		roi = list()
		initialroi = list()
		setsafety = configuremhsafety(currentBotGuid,0, 0, 0)
		bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
				accountGuid, currentBotGuid, interval, primarycurrency, secondarycurrency, contractname)
		print(bt.errorCode, bt.errorMessage, bt.result)
		backtest = bt.result
		initialroi = backtest.roi
		print('initial Roi is:', initialroi)
		print('Stoploss range for testing: sl')
		for x in sl:
			setsafety = configuremhsafety(currentBotGuid, 0, 0, x)
		
			bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
			accountGuid, currentBotGuid, interval, primarycurrency, secondarycurrency, contractname)
			print(bt.errorCode, bt.errorMessage, bt.result)
			roi = backtest.roi
			print(x, roi)
			slroi.append([x, roi])
		sortedroi = (sorted(slroi, key=lambda x: x[1], reverse=True))
		print('Best ROI result in first iteration is:',
					sortedroi[0][1], 'with stoploss:', sortedroi[0][0])
		currentsl = sortedroi[0][0]
		for i in np.arange(0,20,1):
			currentsl = Decimal(currentsl) - Decimal(0.1)
			setsafety = configuremhsafety(currentBotGuid, 0, 0, currentsl)
			backtest = haasomeClient.customBotApi.backtest_custom_bot_on_market(
						accountGuid, currentBotGuid, interval, primarycurrency, secondarycurrency, contractname).result
			roi = backtest.roi
			slroi.append([currentsl, roi])
			print(currentsl, roi)
		currentsl = sortedroi[0][0]
		for i in np.arange(0,20,1):
			currentsl = Decimal(currentsl) + Decimal(0.1)
			setsafety = configuremhsafety(currentBotGuid, 0, 0, currentsl)
			backtest = haasomeClient.customBotApi.backtest_custom_bot_on_market(
						accountGuid, currentBotGuid, interval, primarycurrency, secondarycurrency, contractname).result
			roi = backtest.roi
			slroi.append([currentsl, roi])
			print(currentsl, roi)