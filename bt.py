def do(bot, haasomeClient):
  print(bot)
  baseconfig = haasomeClient.customBotApi.get_custom_bot(bot.guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
  settingsprev = []
  settingsstats = []
  timeinterval = minutestobacktest()
  configroi = []
  startTime = datetime.now()
  print('Downloading backtsting history... Expect results anytime soon')
  for i, v in enumerate(configs):
   configuremh(haasomeClient, bot.guid, configs[i][0], configs[i][1], configs[i][2], configs[i][3], configs[i][4], configs[i][5],configs[i][6], configs[i][7], configs[i][8], configs[i][9], configs[i][10], configs[i][11], configs[i][12])
   configuremhsafety(haasomeClient,bot.guid, 0, 0, 0)
   backtest = haasomeClient.customBotApi.backtest_custom_bot_on_market(bot.accountId, bot.guid, timeinterval, bot.priceMarket.primaryCurrency, bot.priceMarket.secondaryCurrency, bot.priceMarket.contractName)
   backtestr = backtest.result
   roi = backtestr.roi
   prevroi = roi
   
   settings = configs[i][0], configs[i][1], configs[i][2], configs[i][3], configs[i][4], configs[i][5],configs[i][6], configs[i][7], configs[i][8], configs[i][9], configs[i][10], configs[i][11], configs[i][12]
   configroi.append([configs[i][0], configs[i][1], configs[i][2], configs[i][3], configs[i][4], configs[i][5],	configs[i][6], configs[i][7], configs[i][8], configs[i][9], configs[i][10], configs[i][11], configs[i][12], roi])
   settingsprev = settings
   print('ROI:', roi, 'Bot configuration :', configs[i][0], configs[i][1], configs[i][2], configs[i][3], configs[i][4], configs[i][5],configs[i][6], configs[i][7], configs[i][8], configs[i][9], configs[i][10], configs[i][11], configs[i][12], backtest.errorCode, backtest.errorMessage)
  print('time it took: ', datetime.now() - startTime)
  configroiorted = sorted(configroi, key=lambda x: x[13], reverse=False)
return configroiorted