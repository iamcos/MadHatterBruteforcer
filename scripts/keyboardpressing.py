while True:
  try:  # used try so that if user pressed other than the given key error will not be shown
     if keyboard.is_pressed('q'):
        initialparam = getmhindicators(currentBotGuid)[0]
        print('Bbands length selected', initialparam)
        indicator = [EnumMadHatterIndicators.BBANDS, 0, 'Bbands L']

       elif keyboard.is_pressed('0'):
        print('Zero pressed. quitting')
        break

       elifif keyboard.is_pressed('w'):
        print('bbands deviation rought bruteforce initiated')
        bbtbbdev(currentBotGuid)
       elifif keyboard.is_pressed('e'):
        print('bbands deviation precise stepping bruteforcer algorithm iniciated')
        bbtbbdevprecise(currentBotGuid)

       elifif keyboard.is_pressed('a'):
        initialparam = getmhindicators(currentBotGuid)[8]
        indicator = [EnumMadHatterIndicators.RSI, 0,'RSI L']
        print('RSI l selected', initialparam)
       elifif keyboard.is_pressed('s'):
        currentconfig = getmhindicators(currentBotGuid)
        initialparam = getmhindicators(currentBotGuid)[9]
        print('RSI Buy selected', initialparam)
        indicator = [EnumMadHatterIndicators.RSI, 1,'RSI Buy']

       elifif keyboard.is_pressed('d'):
          initialparam = getmhindicators(currentBotGuid)[10]
          print('RSI Sell value: ', initialparam)
          indicator = [EnumMadHatterIndicators.RSI, 2, 'RSI Sell']
       elifif keyboard.is_pressed('z'):
          initialparam = getmhindicators(currentBotGuid)[11]
          print('MACD Fast selected', initialparam)
          indicator = [EnumMadHatterIndicators.MACD, 0,'MACD Fast']
       elifif keyboard.is_pressed('x'):
        initialparam = getmhindicators(currentBotGuid)[12]
        print('MACD Slow selected', initialparam)
        indicator = [EnumMadHatterIndicators.MACD, 1, 'MACD Slow']
       elifif keyboard.is_pressed('c'):
          initialparam = getmhindicators(currentBotGuid)[13]
          print('MACD Signal selected', initialparam)
          indicator = 	[EnumMadHatterIndicators.MACD, 2, 'MACD signal']
      	elif keyboard.is_pressed('u'):
          btresults = []
          botorderhistory =[]
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
              for i,v in enumerate(completedorders):
                try:
                 botorderhistory.append([bt.result.completedOrders[1].unixAddedTime, bt.result.completedOrders[1].amountFilled,bt.result.completedOrders[1].profits])
                 print(botorderhistory)
                except IndexError:
                  print('index error! means no order took place.')

              
              # order = [completedorders.amount, completedorders.ammountFilled, completedorders.addedTime, completedorders.orderStatus]
             
              # print('backtest:' , bt.errorCode, bt.errorMessage)
              print(initialparam, indicator[2], btr.roi)
              btresults.append([btr.roi,initialparam])

							elif keyboard.is_pressed('i'):
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
								elif keyboard.is_pressed('j'):
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

					elif keyboard.is_pressed('k'):
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