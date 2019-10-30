import time
import config
import logging
import datetime
import operator

from config import huey
from config import hueyLocal

from haasomeworker.util.HaasManager import HaasManager

from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from haasomeapi.enums.EnumPriceSource import EnumPriceSource
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType

from haasomeworker.util.Util import Util

def safeHistoryGet(pricesource: EnumPriceSource, primarycoin: str, secondarycoin: str, contractname: str, interval: int, depth: int):
    history = None
    historyResult = False
    failCount = 0

    while historyResult == False:
        history = HaasManager.haasomeClient.marketDataApi.get_history(pricesource, primarycoin, secondarycoin, contractname, interval, depth)
        if len(history.result) > 1:
            historyResult = True
        else:
            failCount = failCount + 1
            time.sleep(1)

        if failCount == 10:
            historyResult = True


    return history

@huey.task()
def smart_scalper_bot_task(taskname: str, accountguid: str, primarycurrency: str, secondarycurrency: str, 
    timeframeinminutes: int, fee: float, starttargetprecentage: float, endtargetprecentage: float, steptargetprecentage: float, 
    startsafetythreshold: float, endsafetythreshold: float, stepsafetythreshold: float,
    percentagetocheck: float, percentagetocheckstep: float):

    logging.info("Started smart scalper task " + taskname)

    HaasManager.init_haas_manager(config.SERVER_CONFIG["ipport"], config.SERVER_CONFIG["secret"])

    accountInfo = HaasManager.haasomeClient.accountDataApi.get_account_details(config.SERVER_CONFIG["accountGuid"]).result
    
    history = safeHistoryGet(EnumPriceSource(accountInfo.connectedPriceSource), primarycurrency, secondarycurrency, "", 1, timeframeinminutes*2)

    candles = history.result

    percentageUpDownFinal = int(percentagetocheck/100 * timeframeinminutes)

    candlesToCheck = []

    highestCandleFromTestRange = None
    lowestCandleFromTestRange = None

    # Get the candles to check
    logging.info("Calculating candles to test for best start time")

    for x in range(int(percentageUpDownFinal)+1):
        if x == 0:
            candlesToCheck.append(candles[timeframeinminutes])
        else:
            candlesToCheck.append(candles[timeframeinminutes-x])
            candlesToCheck.append(candles[timeframeinminutes+x])

    highestCandleFromTestRange = candlesToCheck[0]
    lowestCandleFromTestRange = candlesToCheck[0]

    for candle in candlesToCheck:
        if candle.close > highestCandleFromTestRange.close:
            highestCandleFromTestRange = candle

        if candle.close < lowestCandleFromTestRange.close:
            lowestCandleFromTestRange = candle

    logging.info("Lowest Candle Price Found: " + str(lowestCandleFromTestRange.close))
    logging.info("Highest Candle Price Found: " + str(highestCandleFromTestRange.close))

    stepCandleAmount = int(5/100 * percentageUpDownFinal)

    sortedCandles = sorted(candlesToCheck, key=operator.attrgetter('close'))

    tasks = {}
    botResults = {}

    for x in range (5):

        newBacktestLength = int((datetime.datetime.utcnow() - sortedCandles[stepCandleAmount*x].timeStamp).total_seconds() / 60)
        
        task = backtest_scalper_full_bot_task("TSmrtScalper-"+str(x), config.SERVER_CONFIG["accountGuid"], primarycurrency, secondarycurrency, 
            newBacktestLength, fee, starttargetprecentage, endtargetprecentage, steptargetprecentage, 
            startsafetythreshold, endsafetythreshold, stepsafetythreshold, False)

        tasks[newBacktestLength] = task

    while len(botResults) != len(tasks):
        for k, v in tasks.items():
            result = v.get()
            if result != None:
                botResults[k] = result
    print('')
    print("Tested coin pair: " + primarycurrency + "/" + secondarycurrency)
    print("Ran with the following settings")
    print("Percentage To Check: " + str(percentagetocheck))
    print("Percentage To Step " + str(percentagetocheckstep))
    print('')

    bestSettings = list(botResults.values())[0]
    bestLength = list(botResults.keys())[0]
    
    for k,v in botResults.items():
        if v['ROI'] > bestSettings['ROI']:
            bestSettings = v
            bestLength = k

        print("Result Length:" + str(k) + " Settings:" + str(v))

    print('')
    logging.info("Smart scalper task finished")
    return "HPRV: " + str(lowestCandleFromTestRange.close) + " LPRV:" + str(highestCandleFromTestRange.close) + " CL:" + str(bestLength) + " BSP:" + str(candles[bestLength].close) + " Settings: " + str(bestSettings)

@huey.task()
def backtest_scalper_bot_task(taskname: str, accountguid: str, primarycurrency: str, secondarycurrency: str, 
    timeframeinminutes: int, fee: float, targetprecentage: float, safetythreshold: float):

    logging.info("Started backtest scalper " + taskname)
    HaasManager.init_haas_manager(config.SERVER_CONFIG["ipport"], config.SERVER_CONFIG["secret"])
    
    accountInfo = HaasManager.haasomeClient.accountDataApi.get_account_details(config.SERVER_CONFIG["accountGuid"]).result

    # Create Template Bot
    logging.info("Creating bot template " + taskname+"-Task-Template")
    templateResult = HaasManager.haasomeClient.customBotApi.new_custom_bot(config.SERVER_CONFIG["accountGuid"], EnumCustomBotType.SCALPER_BOT, taskname+"-Task-Template", primarycurrency, secondarycurrency, "")
    templateBot = templateResult.result

    history = safeHistoryGet(EnumPriceSource(accountInfo.connectedPriceSource), primarycurrency, secondarycurrency, "", 1, timeframeinminutes*2)

    # Setup Scalper Bot
    scalperSetupResult = HaasManager.haasomeClient.customBotApi.setup_scalper_bot(config.SERVER_CONFIG["accountGuid"], templateBot.guid, templateBot.name, 
        primarycurrency, secondarycurrency, "LOCKEDLIMITORDERGUID", "", 0.0, 1000.0, secondarycurrency, fee, targetprecentage, safetythreshold)

    # Backtest Bot
    logging.info("Backtesting bot on market "+primarycurrency+"/"+secondarycurrency)

    backTestResult = HaasManager.haasomeClient.customBotApi.backtest_custom_bot_on_market(config.SERVER_CONFIG["accountGuid"], templateBot.guid, timeframeinminutes, primarycurrency, secondarycurrency, "")

    # Delete Template Bot
    logging.info("Deleting bot template " + taskname+"-Task-Template")
    removeTemplate = HaasManager.haasomeClient.customBotApi.remove_custom_bot(templateBot.guid)
    logging.info("Backtest task finished " + taskname)

    return "TP:"+ str(round(targetprecentage,2)) + " ST:" + str(round(safetythreshold,2)) + " ROI:"+ str(backTestResult.result.roi)

@hueyLocal.task()
def backtest_scalper_full_bot_task(taskname: str, accountguid: str, primarycurrency: str, secondarycurrency: str, 
    timeframeinminutes: int, fee: float, starttargetprecentage: float, endtargetprecentage: float, steptargetprecentage: float,
    startsafetythreshold: float, endsafetythreshold: float, stepsafetythreshold: float, displayTextUpdate: bool = True):

    logging.info("Started backtest scalper " + taskname)
    HaasManager.init_haas_manager(config.SERVER_CONFIG["ipport"], config.SERVER_CONFIG["secret"])
    
    accountInfo = HaasManager.haasomeClient.accountDataApi.get_account_details(config.SERVER_CONFIG["accountGuid"]).result

    # Create Template Bot
    logging.info("Creating bot template " + taskname+"-Task-Template")
    templateResult = HaasManager.haasomeClient.customBotApi.new_custom_bot(config.SERVER_CONFIG["accountGuid"], EnumCustomBotType.SCALPER_BOT, taskname+"-Task-Template", primarycurrency, secondarycurrency, "")
    templateBot = templateResult.result

    history = safeHistoryGet(EnumPriceSource(accountInfo.connectedPriceSource), primarycurrency, secondarycurrency, "", 1, timeframeinminutes*2)

    highestBotRoi = None
    winningTargetPercentage = 0
    winningSafteyThreshold = 0

    for x in Util.frange(starttargetprecentage, endtargetprecentage, steptargetprecentage):
        for y in Util.frange(startsafetythreshold, endsafetythreshold, stepsafetythreshold):

            # Setup Scalper Bot
            scalperSetupResult = HaasManager.haasomeClient.customBotApi.setup_scalper_bot(config.SERVER_CONFIG["accountGuid"], templateBot.guid, templateBot.name, 
                primarycurrency, secondarycurrency, "LOCKEDLIMITORDERGUID", "", 0.0, 1000.0, secondarycurrency, fee, x, y)

            # Backtest Bot

            if displayTextUpdate:
                logging.info("Backtesting bot on market "+primarycurrency+"/"+secondarycurrency + " TP:" + str(x) + " ST:" + str(y))

            backTestResult = HaasManager.haasomeClient.customBotApi.backtest_custom_bot_on_market(config.SERVER_CONFIG["accountGuid"], templateBot.guid, 
                timeframeinminutes, primarycurrency, secondarycurrency, "")

            backTestBot = backTestResult.result

            if backTestResult.errorCode == EnumErrorCode.SUCCESS:
                if highestBotRoi == None:
                    highestBotRoi = backTestBot
                    winningTargetPercentage = x
                    winningSafteyThreshold = y

                else:
                    if backTestBot.roi > highestBotRoi.roi :
                        highestBotRoi = backTestBot
                        winningTargetPercentage = x
                        winningSafteyThreshold = y

    # Delete Template Bot
    logging.info("Deleting bot template " + taskname+"-Task-Template")
    removeTemplate = HaasManager.haasomeClient.customBotApi.remove_custom_bot(templateBot.guid)
    logging.info("Backtest task finished " + taskname)

    return {"TP":round(winningTargetPercentage,2), "ST":round(winningSafteyThreshold,2), "ROI":highestBotRoi.roi}

@huey.task()
def backtest_pingpong_bot_task(taskname: str, accountguid: str, primarycurrency: str, secondarycurrency: str, 
    timeframeinminutes: int, fee: float):

    logging.info("Started ping pong task " + taskname)

    HaasManager.init_haas_manager(config.SERVER_CONFIG["ipport"], config.SERVER_CONFIG["secret"])
    
    accountInfo = HaasManager.haasomeClient.accountDataApi.get_account_details(config.SERVER_CONFIG["accountGuid"]).result

    # Create Template Bot
    logging.info("Creating bot template " + taskname+"-Task-Template")
    templateResult = HaasManager.haasomeClient.customBotApi.new_custom_bot(config.SERVER_CONFIG["accountGuid"], EnumCustomBotType.PING_PONG_BOT, taskname+"-Task-Template", primarycurrency, secondarycurrency, "")
    templateBot = templateResult.result

    history = safeHistoryGet(EnumPriceSource(accountInfo.connectedPriceSource), primarycurrency, secondarycurrency, "", 1, timeframeinminutes*2)

    # Setup ping pong Bot
    scalperSetupResult = HaasManager.haasomeClient.customBotApi.setup_ping_pong_bot(config.SERVER_CONFIG["accountGuid"], templateBot.guid, templateBot.name, 
        primarycurrency, secondarycurrency, "", 0.0, 1000.0, secondarycurrency, fee)

    # Backtest Bot
    logging.info("Backtesting bot on market "+primarycurrency+"/"+secondarycurrency)

    backTestResult = HaasManager.haasomeClient.customBotApi.backtest_custom_bot_on_market(config.SERVER_CONFIG["accountGuid"], templateBot.guid, timeframeinminutes, primarycurrency, secondarycurrency, "")

    # Delete Template Bot
    logging.info("Deleting bot template " + taskname+"-Task-Template")
    removeTemplate = HaasManager.haasomeClient.customBotApi.remove_custom_bot(templateBot.guid)
    logging.info("Backtest task finished " + taskname)

    return "ROI: "+ str(backTestResult.result.roi)

@huey.task()
def backtest_pingpong_full_bot_task(taskname: str, accountguid: str, basecurrency: str, timeframeinminutes: int, fee: float):

    results = []
    marketsToRun = []

    logging.info("Started ping pong full " + taskname)

    HaasManager.init_haas_manager(config.SERVER_CONFIG["ipport"], config.SERVER_CONFIG["secret"])
    
    accountInfo = HaasManager.haasomeClient.accountDataApi.get_account_details(config.SERVER_CONFIG["accountGuid"]).result

    markets = HaasManager.haasomeClient.marketDataApi.get_price_markets(EnumPriceSource(accountInfo.connectedPriceSource)).result

    for market in markets:
        if market.secondaryCurrency == basecurrency:
            marketsToRun.append(market)

    logging.info("Creating bot template " + taskname+"-Task-Template")

    templateResult = HaasManager.haasomeClient.customBotApi.new_custom_bot(config.SERVER_CONFIG["accountGuid"], EnumCustomBotType.PING_PONG_BOT, 
        taskname+"-Task-Template", markets[0].primaryCurrency, markets[0].secondaryCurrency, "")

    templateBot = templateResult.result

    for market in marketsToRun:

        history = safeHistoryGet(EnumPriceSource(accountInfo.connectedPriceSource), market.primaryCurrency, market.secondaryCurrency, "", 1, timeframeinminutes*2)

        # Setup ping pong Bot
        scalperSetupResult = HaasManager.haasomeClient.customBotApi.setup_ping_pong_bot(config.SERVER_CONFIG["accountGuid"], templateBot.guid, templateBot.name, 
            market.primaryCurrency, market.secondaryCurrency, "", 0.0, 1000.0, market.secondaryCurrency, fee)

        # Backtest Bot
        backTestResult = HaasManager.haasomeClient.customBotApi.backtest_custom_bot_on_market(config.SERVER_CONFIG["accountGuid"], templateBot.guid, 
            timeframeinminutes, market.primaryCurrency, market.secondaryCurrency, "")

        if backTestResult.result:
            results.append([market.primaryCurrency+"/"+market.secondaryCurrency, backTestResult.result.roi])
            logging.info("Backtesting bot on market "+market.primaryCurrency+"/"+market.secondaryCurrency+": " + str(backTestResult.result.roi))


    # Delete Template Bot
    logging.info("Deleting bot template " + taskname+"-Task-Template")
    removeTemplate = HaasManager.haasomeClient.customBotApi.remove_custom_bot(templateBot.guid)
    logging.info("Backtest task finished " + taskname)

    return results