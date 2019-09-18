def indicatorparametersdata(bot, haasomeClient):
		indicators_all = ['Aroon','Aroon Oscillator','AO','BOP','Blind indicator','Bollinger Bands','Bollinger Bands %B','Bollinger Bands %W','Bollinger Bands (Legacy)','Candle Pattern finder','CMO','CRSI','Coppock Curve','DPO','DC','DEMA','Dynamic Buy/Sell','Elliot','EMA','FastRSI','Fibonacci','Fixed Buy/Sell','Fractal','Ichimoku Clouds','KAMA','Keltner Channels','Momentum','MFI','MACD','ROC','RS','RSI','SAR','SMA','SlowRSI','Small Fractal','Stochastic','Stoch-RSI','Stochastic^2','Timed Blind','TD','TRIMA','TRIX','TEMA','UO','WMA','Williams %R']
		
		todict = indicatorstodict2(bot)
		indicators_bot = todict.keys()
		for indicator, data in todict.items():

				if indicator =='Aroon' and indicator in indicators_bot:
					print(indicator)
					# bt = haasomeClient.tradeBotApi.backtest_trade_bot()
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
									print(paramvalue)
				

				elif indicator =='Aroon Oscillator' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
					
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='AO' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='BOP' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='Blind indicator' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='Bollinger Bands' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='Bollinger Bands %B' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='Bollinger Bands %W' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='Bollinger Bands (Legacy)' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='Candle Pattern finder' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='CMO' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='CRSI' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='Coppock Curve' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='DPO' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='DC' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='DEMA' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='Dynamic Buy/Sell' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='Elliot' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='EMA' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='FastRSI' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='Fibonacci' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='Fixed Buy/Sell' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='Fractal' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='Ichimoku Clouds' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='KAMA' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='Keltner Channels' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='Momentum' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='MFI' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='MACD' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='ROC' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='RS' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='RSI' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='SAR' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='SMA' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='SlowRSI' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='Small Fractal' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='Stochastic' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='Stoch-RSI' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='Stochastic^2' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='Timed Blind' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname)
						# for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										# print(paramname, pramstring, paramvalue)
									
				elif indicator =='TD' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='TRIMA' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='TRIX' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='TEMA' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='UO' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='WMA' and indicator in indicators_bot:
					print(indicator)
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)
									
				elif indicator =='Williams %R' and indicator in indicators_bot:
					for paramname, data1 in todict[indicator].items():
						print(paramname,data1)
						for pramstring, paramvalue in todict[str(indicator)][str(paramname)].items():
										 print(pramstring,paramvalue)