from haasomeapi.apis.MarketDataApi import MarketDataApi
from haasomeapi.dataobjects.accountdata.BaseOrder import BaseOrder
from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot
from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot
from haasomeapi.dataobjects.marketdata.Market import Market
from haasomeapi.dataobjects.util.HaasomeClientResponse import \
				HaasomeClientResponse
from haasomeapi.enums.EnumCurrencyType import EnumCurrencyType
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from haasomeapi.enums.EnumFundPosition import EnumFundPosition
from haasomeapi.enums.EnumMadHatterIndicators import EnumMadHatterIndicators
from haasomeapi.enums.EnumMadHatterSafeties import EnumMadHatterSafeties
from haasomeapi.enums.EnumOrderType import EnumOrderType
from haasomeapi.enums.EnumPriceSource import EnumPriceSource
import init
import botsellector
import interval as iiv
import numpy as np

haasomeClient = init.connect()


def backtest_mh_indicator_ranges(bot):
 ticks = iiv.readinterval(bot.interval)
 results = []
 filename = str(bot.primaryCurrency)+'\\'+str(bot.secondaryCurrency)+' '+str(btinterval)+'.csv'
 with open('filename', 'w', newline='') as csvfile:
	fieldnames = ['resetmiddle', 'allowmidsells', 'matype', 'rsil', 'rsib', 'rsis', 'bbl', 'devup', 'devdn', 'macdfast', 'macdslow', 'macdsign', ]
	csvwriter = csv.DictWriter(csvfile,fieldnames=fieldnames)
	csvwriter.writeheader()
 for signalconsensus in [True, False]:
		bot1= haasomeClient.customBotApi.setup_mad_hatter_bot(bot.name, bot.guid, bot.accountId,
  bot.priceMarket.primaryCurrency, bot.priceMarket.secondaryCurrency, bot.priceMarket.contractName, bot.leverage,  bot.customTemplate, bot.fundsPosition,  bot.currentFeePercentage, bot.amountType, bot.currentTradeAmount, signalconsensus, bot.disableAfterStopLoss, bot.interval, bot.includeIncompleteInterval, bot.mappedBuySignal, bot.mappedSellSignal)
		for resetmiddle in [True,False]:
			bot1= haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
			bot.guid, EnumMadHatterIndicators.BBANDS, 6, resetmiddle)
			for allowmidsells in [True,False]:
				bot1= haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
				bot.guid, EnumMadHatterIndicators.BBANDS, 7, allowmidsells)
				for matype in range(0, 7):
					bot1= haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
					bot.guid, EnumMadHatterIndicators.BBANDS, 3, matype)
					for rsil in range(2, 21,2):
						bot1= haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
						bot.guid, EnumMadHatterIndicators.RSI, 0, rsil)
						for rsib in range(10, 30,2):
							bot1= haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
							bot.guid, EnumMadHatterIndicators.RSI, 1, rsib)
							for rsis in range(60, 80,2):
								bot1= haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid, EnumMadHatterIndicators.RSI, 2, rsis)
								for bbl in range(4, 100):
									bot1= haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
									bot.guid, EnumMadHatterIndicators.BBANDS, 0, bbl)
									for devup in np.arange(0.1,3.2,0.1):
										bot1=haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
									bot.guid, EnumMadHatterIndicators.BBANDS, 1, devup)
										for devdn in np.arange(0.1,3.2,0.1):
											bot1=haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
											bot.guid, EnumMadHatterIndicators.BBANDS, 2, devdn)
											for macdfast in range(10,50,5):
												bot1=haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
												bot.guid, EnumMadHatterIndicators.MACD, 0, macdfast)
												for macdslow in range(macdfast*2,200,5):
													bot1=haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
													bot.guid, EnumMadHatterIndicators.MACD, 1, macdslow)
													for macdsign in range(0,21,2):
														bot1=haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
														bot.guid, EnumMadHatterIndicators.MACD, 2, macdsign)
														bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(bot.accountId, bot.guid,ticks, bot.priceMarket.primaryCurrency, bot.priceMarket.secondaryCurrency, bot.priceMarket.contractName)
														results.append([bt.result.roi,[matype,signalconsensus,resetmiddle,allowmidsells,rsil,rsib,rsis,bbl,devup,devdn,macdfast,macdslow,macdsign]]) #bt.result.completedOrders
														print(bt.errorCode, bt.errorMessage,bt.result.roi,[matype,signalconsensus,resetmiddle,allowmidsells,rsil,rsib,rsis,bbl,devup,devdn,macdfast,macdslow,macdsign])
														with open('filename', 'w', newline='') as csvfile:
															fieldnames = ['ROI','resetmiddle', 'allowmidsells', 'matype', 'rsil', 'rsib', 'rsis', 'bbl', 'devup', 'devdn', 'macdfast', 'macdslow', 'macdsign', ]
															csvwriter = csv.DictWriter(csvfile,fieldnames=fieldnames)
															csvwriter.writerow({'signalconsensus':str(signalconsensus),'resetmiddle': str(resetmiddle), 'allowmidsells': str(allowmidsells), 'matype': str(matype), 'rsil': str(rsil), 'rsib': str(rsib), 'rsis': str(rsis), 'bbl': str(bbl), 'devup': str(devup), 'devdn': str(devdn), 'macdfast': str(macdfast), 'macdslow': str(macdslow), 'macdsign': str(macdsign)})
		
		

def main():

 bot= botsellector.getallmhbots(haasomeClient)
 backtest_mh_indicator_ranges(bot)
if __name__ == '__main__':
	main()
