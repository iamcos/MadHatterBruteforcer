def forindicators():

	ranges = [['Aroon', 0, 0, 10, 30, 2],\
 ['Aroon Oscillator', 0, 0, 10, 30, 2],\
 ['AO', 0, 0,5, 20, 2],\
 ['AO', 1, 1,20, 40, 2],\
 ['AO', 2, 2,-2, -0.5, 2],\
 ['AO', 3, 3,0.5, 2, 2],\
 ['BOP', 0, 0,2, 20, 2],\
 ['BOP', 1, 1,-2, -0.5, 2],\
 ['BOP', 2, 2,0.5, 2, 2],\
 ['Bollinger Bands', 0, 0,4, 50, 2],\
 ['Bollinger Bands', 1, 1,0.3, 2.1, 0.2],\
 ['Bollinger Bands', 2, 2,0.3, 2.1, 0.2],\
 ['Bollinger Bands %B', 0, 0,4, 50, 2],\
 ['Bollinger Bands %B', 1, 1,0.3, 2.1, 0.2],\
 ['Bollinger Bands %B', 2, 2,0.3, 2.1, 0.2],\
 ['Bollinger Bands %W', 0, 0,4, 50, 2],\
 ['Bollinger Bands %W', 1, 1,0.3, 2.1, 0.2],\
 ['Bollinger Bands %W', 2, 2,0.3, 2.1, 0.2],\
 ['Bollinger Bands %W', 3, 3,0.001, 0.1, 0.01],\
 ['Bollinger Bands %W', 4, 4,0.002, 0.2, 0.01],\
 ['Bollinger Bands (Legacy', 0, 0,4, 50, 2],\
 ['Bollinger Bands (Legacy)', 1, 1,0.3, 2.1, 0.2],\
 ['Bollinger Bands (Legacy)' , 2, 2,0.3, 2.1, 0.2],\
 ['Candle Pattern finder',0, 'SimpleUpCandle', 'SimpleDownCandle', 'SimpleDoubleUpCandle', 'SimpleDoubleDownCandle', 'TwoCrows', 'ThreeBlackCrows', 'ThreeInsideUp', 'ThreeInsideDown', 'ThreeLineStrikeBullish', 'ThreeLineStrikeBearish', 'ThreeOutsideUp', 'ThreeOutsideDown', 'ThreeStarsInSouth', 'ThreeStarsInNorth', 'ThreeWhiteSoldiers', 'AdvanceBlock', 'BeltHoldBullish', 'BeltHoldBearish', 'BreakawayBullish', 'BreakawayBearish', 'ClosingMarubozu', 'ConcealBabysWall', 'CounterAttackBullish', 'CounterAttackBearish', 'Doji', 'DojiStar', 'DragonflyDoji', 'EngulfingBullish', 'EngulfingBearish', 'GapSideSideWhite', 'GravestoneDoji', 'Hammer', 'HangingMan', 'HaramiBullish', 'HaramiBearish', 'HaramiCrossBullish', 'HaramiCrossBearish', 'HighWave', 'HikkakeBullish', 'HikkakeBearish', 'HomingPigeon', 'Identical3Crows', 'InNeck', 'InvertedHammer', 'KickingBearish', 'KickingBullish', 'LadderBottom', 'LongLeggedDoji', 'LongLine', 'MarubozuBullish', 'MarubozuBearish', 'MatchingLow', 'OnNeck', 'Piercing', 'RickshawMan', 'RiseFall3Methods', 'SeperatingLines', 'ShootingStar', 'ShortLine', 'SpinningTop', 'StalledPattern', 'StickSandwhichUp', 'StickSandwhichDown', 'TasukiGap', 'Thrusting', 'Tristar'],\
	['CMO', 0, 0,2, 40, 2],\
 ['CMO', 1, 1,-10.0, -2.0, 2.0],\
 ['CMO', 2, 2,10.0, 2.0 , 2.0],\
 ['CRSI', 0, 0,2, 20, 2],\
 ['CRSI', 1, 2, 10, 2],\
 ['CRSI', 2, 80, 100, 2],\
 ['CRSI', 3, 10, 30, 2],\
 ['CRSI', 4, 70, 90, 2],\
 ['Coppock Curve', 0, 0,6, 21, 4],\
 ['Coppock Curve', 1, 14, 40, 4],\
 ['Coppock Curve', 2, 2, 20, 4],\
 ['Coppock Curve', 3, -0,1, -0.2, -0.02],\
 ['Coppock Curve', 4, 0,1, 0.2, 0.02],\
 ['DPO', 0, 0,8, 16, 2],\
 ['DPO', 1, 19, 36, 2],\
 ['DPO', 2, -0,1, -0.2, -0.02],\
 ['DPO', 3, 0,1, 0.2, 0.02],\
 ['DC', 0, 0,2, 100, 2],\
 ['DEMA', 0, 0,4, 21, 2],\
 ['DEMA', 1, 8, 42, 2],\
 ['DEMA', 2, 0, 0, 0],\
 ['Dynamic Buy/Sell', 0, 0,20, 240, 10],\
 ['Elliot', 0, 0,5, 80, 5],\
 ['EMA', 0, 0,4, 21, 2],\
 ['EMA', 1, 8, 42, 2],\
 ['EMA', 2, 0, 0, 0],\
 ['FastRSI', 0, 0,6, 30, 2],\
 ['FastRSI', 1, 2, 10, 1],\
 ['FastRSI', 2, 10, 45 , 2],\
 ['FastRSI', 3, 59, 81, 2],\
 ['Fibonacci', 0, 0,5, 40, 2],\
 ['Fixed Buy/Sell', 0, 0,0.0, 2.5, 2],\
 ['Fixed Buy/Sell', 1, 0.0, 2.5, 2],\
 ['Ichimoku Clouds', 0, 0,6, 30, 2],\
 ['Ichimoku Clouds', 1, 12, 40, 2],\
 ['Ichimoku Clouds', 2, 40, 80, 2],\
 ['Ichimoku Clouds', 3, 26, 50, 2],\
 ['Ichimoku Clouds', 4, 'CloudTwist', 'CloudBreakOut'],\
 ['KAMA', 0, 0,2, 20, 2],\
 ['KAMA', 1, 20, 40, 2],\
 ['Keltner Channels', 0, 0,2, 3, 0.1],\
 ['Keltner Channels', 1, 2,0, 1, 0.1],\
 ['Keltner Channels', 2, 2, 3, 0.1],\
 ['Momentum', 0, 0,2, 20, 2],\
 ['MFI', 0, 0,2, 20, 2],\
 ['MFI', 1, 10, 45 , 2],\
 ['MFI', 2, 59, 81, 2],\
 ['MACD', 0, 0,2, 20, 2],\
 ['MACD', 1, 4, 40, 2],\
 ['MACD', 2, 2, 12, 2],\
 ['MACD', 3, 'MACD-Signal Cross', 'MACD-Zero Cross', 'Signal-Zero Cross'],\
 ['ROC (Alt)', 0, 10, 0, 50, 2],\
 ['ROC (Alt)', 1, 10, 40, 2],\
 ['ROC (Alt)', 2, 60, 80, 2],\
 ['ROC', 0, 0,10, 40, 2],\
 ['ROC', 1, -0.2,-0.05, 0.02],\
 ['ROC', 2, 0.1, 0.3, 0.02],\
 ['RS', 0, 0,10, 40, 2],\
 ['RSI', 0, 0,2, 21, 2],\
 ['RSI', 1, 10, 40, 2],\
 ['RSI', 2, 60, 81, 2],\
 ['SAR', 0, 0,0.02, 0.2, 0.02],\
 ['SAR', 1, 0.1, 0.2, 2],\
 ['SMA', 0, 0,2, 40, 2],\
 ['SMA', 1, 4, 80, 2],\
 ['SMA', 2, 0.0, 0.01, 0.001],\
 ['SlowRSI', 0, 0,2, 40, 2],\
 ['SlowRSI', 1, 2, 12, 2],\
 ['SlowRSI', 2, 10, 40, 2],\
 ['SlowRSI', 3, 60, 81, 2],\
 ['Stochastic', 0, 0,2, 40, 2],\
 ['Stochastic', 1, 10, 40, 2],\
 ['Stochastic', 2, 60, 81, 2],\
 ['Stoch-RSI', 0, 0,2, 40, 2],\
 ['Stoch-RSI', 1, 3, 10, 2],\
 ['Stoch-RSI', 2, 2, 8, 2],\
 ['Stoch-RSI', 3, 10, 40, 2],\
 ['Stoch-RSI', 4, 60, 81, 2],\
 ['Stoch-RSI', 5, 'Threshold Cross', 'Lines Cross'],\
 ['Stochastic^2', 0, 0,2, 20, 2],\
 ['Stochastic^2', 1, 10, 40, 2],\
 ['Stochastic^2', 2, 60, 81, 2],\
 ['Timed Blind', 0, 0,10, 200, 2],\
 ['TD', 0, 0,2, 15, 2],\
 ['TD', 1, 4, 20, 2],\
 ['TD', 2, False],\
 ['TD', 3, 3, 18, 2],\
 ['TD', 4, 3, 20, 2],\
 ['TD', 5, False],\
 ['TRIMA', 0, 0,2, 20, 2],\
 ['TRIMA', 1, 4, 40, 2],\
 ['TRIX', 0, 0,2, 20, 2],\
 ['TEMA', 0, 0,2, 20, 2],\
 ['TEMA', 1, 2, 40, 2],\
 ['TEMA', 2, 0.0, 0.1, 0.01],\
 ['UO', 0, 0,2, 10, 2],\
 ['UO', 1, 5, 20, 2],\
 ['UO', 2, 10, 30, 2],\
 ['WMA', 0, 0,2, 10, 2],\
 ['WMA', 1, 2, 30, 2],\
 ['WMA', 2, 0.0, 0.1, 0.01],\
 ['Williams %R', 0, 0,2, 21, 2],\
 ['Williams %R', 1, -30, -20, 2],\
 ['Williams %R', 2, -70, -90, 2]]
	return ranges