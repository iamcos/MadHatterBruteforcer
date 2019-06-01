import decimal as Decimal
import numpy as np
btresults = []
devuprange = np.arange(0.0,3.0,0.5)
devdnrange = np.arange(0.0,3.0,0.5)
print(therange)
i = 0
for devup in devuprange:
	i += 1
	print(i, 'up: ',dev)
	setdevup = setbbDevUp(currentbotGuid, dev)
	i += 1
	for devdn in devdnrange:
		i += 1
		print(i, 'down: ', dev)
		setbbDevDown(currentBotGuid, dev)
		bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(accountGuid,currentBotGuid,interval, primarycoin, secondarycoin, contractname)
		btr = bt.result
		btresults.append([btr.roi,devup, devdn])
	btresultssorted = sorted(btresults, key=lambda x: x[0], reverse=True)
	print(btresultssorted[0][1],'gives best roi of: ',btresultssorted[0][0])