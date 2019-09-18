print_keys(i.bBands.keys())
			print_keys(i.macd.keys())
			print_keys(i.rsi.keys())

		print(i.macd.keys())
		print(i.rsi.keys(),'\n',)
		print(i.bBands['Length'], i.bBands['Devdn'],i.bBands['MaType'], i.bBands['Devup'],i.bBands['RequireFcc'],i.macd['MacdSlow'], i.macd['MacdFast'], i.macd['MacdSign'],  i.rsi['RsiLength'],  i.rsi['RsiOverbought'],  i.rsi['RsiOversold'])