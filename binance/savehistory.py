
from haasomeapi.HaasomeClient import HaasomeClient
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError
import connectionstring
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
haasomeClient = connectionstring.connectionstring()
import settimeinterval
import csv
from haasomeapi.HaasomeClient import HaasomeClient
import haasomeapi.enums.EnumErrorCode as EnumErrorCode
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError
import connectionstring
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
haasomeClient = connectionstring.connectionstring()
import botsellector
import time
from pathlib import Path
import os.path
import interval as iiv 

# btinterval = input('type the number of candles  you wish to recive from history servers')


def allmarketshistory(bot):
	ticks = iiv.readinterval(1)
	basebotconfig = haasomeClient.customBotApi.get_custom_bot(bot, EnumCustomBotType.MAD_HATTER_BOT).result
	pricemarket = basebotconfig.priceMarket
	pricemarkets = haasomeClient.marketDataApi.get_price_markets(pricemarket.priceSource).result
	historydata = []
	interval = 1
	marketobject = haasomeClient.marketDataApi.get_price_markets(basebotconfig.priceMarket.priceSource)
	marketobjectr = marketobject.result
	while True:
				for v in(marketobjectr):
					
					filename = str(v.primaryCurrency)+'\\'+str(v.secondaryCurrency)+' '+str(btinterval)+'.csv'
					historystat = haasomeClient.marketDataApi.get_history(v.priceSource, v.primaryCurrency, v.secondaryCurrency, v.contractName,interval,btinterval)
					marketstats = str(historystat.errorCode)
					print(marketstats)


					if marketstats == 'EnumErrorCode.SUCCESS':
							marketticks = historystat.result
							if len(historystat.result) != 0:
								currentfile = Path(str(filename))
								currentfile.touch(exist_ok=True)
								print(filename, 'created!')
								with open(filename, 'w', newline='') as csvfile:
									fieldnames = ['timeStamp','unixTimeStamp','open','highValue','lowValue','close','volume','currentBuyValue','currentSellValue']
									csvwriter = csv.DictWriter(csvfile,fieldnames=fieldnames)
									csvwriter.writeheader()
									for v in(marketticks):
										csvwriter.writerow({'timeStamp': str(v.timeStamp),'unixTimeStamp': str(v.unixTimeStamp), 'open': float(v.open), 'highValue':  float(v.highValue), 'lowValue': float(v.lowValue),'close' : float(v.close),'volume': float(v.volume),'currentBuyValue': str(v.currentBuyValue),'currentSellValue': float(v.currentSellValue)})
							else:
								historystat = haasomeClient.marketDataApi.get_history(v.priceSource, v.primaryCurrency, v.secondaryCurrency, v.contractName,interval,btinterval)
								marketstats = str(historystat.errorCode)
					elif marketstats == 'EnumErrorCode.PRICE_MARKET_IS_SYNCING':
								time.sleep(2)
								historystat = haasomeClient.marketDataApi.get_history(v.priceSource, v.primaryCurrency, v.secondaryCurrency, v.contractName,interval,btinterval)
								time.sleep(2)
								marketstats = str(historystat.errorCode)
								print(marketstats)
								if len(historystat.result) != 0:
									currentfile = Path(str(filename))
									currentfile.touch(exist_ok=True)
									print(filename, 'created!')
									with open(filename, 'w', newline='') as csvfile:
										fieldnames = ['timeStamp','unixTimeStamp','open','highValue','lowValue','close','volume','currentBuyValue','currentSellValue']
										csvwriter = csv.DictWriter(csvfile,fieldnames=fieldnames)
										csvwriter.writeheader()
										for v in(marketticks):
											csvwriter.writerow({'timeStamp': str(v.timeStamp),'unixTimeStamp': str(v.unixTimeStamp), 'open': float(v.open), 'highValue':  float(v.highValue), 'lowValue': float(v.lowValue),'close' : float(v.close),'volume': float(v.volume),'currentBuyValue': str(v.currentBuyValue),'currentSellValue': float(v.currentSellValue)})



# all_oof_it = allmarketshistory(bot, 3400)