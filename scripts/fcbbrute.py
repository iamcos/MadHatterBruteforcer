from haasomeapi.apis.TradeBotApi import TradeBotApi
from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from haasomeapi.HaasomeClient import HaasomeClient

# from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
from haasomeapi.enums.EnumFlashSpreadOptions import EnumFlashSpreadOptions
import interval as inter
import init
import haasomeapi.enums.EnumIndicator as EnumIndicator
import botsellector
import numpy as np
import interval as iiv

ticks = iiv.readinterval()
import configserver
from haasomeapi.HaasomeClient import HaasomeClient
from decimal import Decimal

ip, secret = configserver.validateserverdata()
haasomeClient = HaasomeClient(ip, secret)


def setspread(bot):
    ip, secret = configserver.validateserverdata()
    haasomeClient = HaasomeClient(ip, secret)

    print(bot.priceSpreadType)
    type = EnumFlashSpreadOptions.FIXED_AMOUNT
    ip, secret = init.connect()

    if bot.priceSpreadType == 1:
        print("bot spread type and selected are ")
        print("bot price spread type is set to Fixed ammount.\n")
        spreadmin = (
            0.1
        )  # float(input('Type spread to start from in decimals like 0.05:  '))
        spreadmax = (
            1.0
        )  # float(input('Type spread to end with in decimals like 0.55:  '))
        step = 0.05  # float(input('Type spread step'))
        for spread in np.arange(Decimal(spreadmin), Decimal(spreadmax), Decimal(step)):
            cfg = haasomeClient.customBotApi.setup_flash_crash_bot(
                bot.accountId,
                bot.guid,
                bot.name,
                bot.priceMarket.primaryCurrency,
                bot.priceMarket.secondaryCurrency,
                bot.currentFeePercentage,
                bot.basePrice,
                1,
                bot.priceSpread,
                bot.percentageBoost,
                bot.minPercentage,
                bot.maxPercentage,
                bot.amountType,
                bot.amountSpread,
                bot.totalBuyAmount,
                bot.totalSellAmount,
                bot.refillDelay,
                bot.safetyEnabled,
                bot.safetyTriggerLevel,
                bot.safetyMoveInMarket,
                bot.safetyMoveOutMarket,
                bot.followTheTrend,
                bot.followTheTrendChannelRange,
                bot.followTheTrendChannelOffset,
                bot.followTheTrendTimeout,
            )
            bt = btfcb(bot, haasomeClient, ticks)
            print(bt.roi)
            print("configuring bot parameters: ", cfg.errorCode, cfg.errorMessage)
            result = cfg.result
            print(result)
        return cfg.result
    if bot.priceSpreadType == 1:  # Percentage
        print("bot price spread type is set to Fixed ammount.\n")
        spreadmin = (
            0.1
        )  # float(input('Type spread to start fbm in decimals like 0.05:  '))
        spreadmax = (
            1.5
        )  # float(input('Type spread to end with in decimals like 0.55:  '))
        step = 0.05  # float(input('Type spread step'))
        for spread in np.arange(Decimal(spreadmin), Decimal(spreadmax), Decimal(step)):
            # spread = input('Type spread between orders in secondary currency : ')
            cfg = haasomeClient.customBotApi.setup_flash_crash_bot(
                accountguid=bot.accountId,
                botguid=bot.guid,
                botname=bot.name,
                primarycoin=bot.priceMarket.primaryCurrency,
                secondarycoin=bot.priceMarket.secondaryCurrency,
                fee=bot.currentFeePercentage,
                baseprice=bot.basePrice,
                priceSpreadType=1,
                pricespread=spread,
                percentageboost=bot.percentageBoost,
                minpercentage=bot.minPercentage,
                maxpercentage=bot.maxPercentage,
                amounttype=bot.amountType,
                amountspread=bot.amountSpread,
                buyamount=bot.totalBuyAmount,
                sellamount=bot.totalSellAmount,
                refilldelay=bot.refillDelay,
                safetyenabled=bot.safetyEnabled,
                safetytriggerlevel=bot.safetyTriggerLevel,
                safetymovein=bot.safetyMoveInMarket,
                safetymoveout=bot.safetyMoveOutMarket,
                followthetrend=bot.followTheTrend,
                followthetrendchannelrange=bot.followTheTrendChannelRange,
                followthetrendchanneloffset=bot.followTheTrendChannelOffset,
                followthetrendtimeout=bot.followTheTrendTimeout,
            )
            bt = btfcb(bot, haasomeClient, ticks)
            print(bt.roi)
            print("configuring bot parameters: ", cfg.errorCode, cfg.errorMessage)
        return cfg.result

    if bot.priceSpreadType == 2:  # percentage with boost
        # print('bot price spread type is set to Fixed ammount.\n')
        # spread = float(input('type Spread'))
        for boost in np.arange(0.2, 1.2, 0.1):
            boosty = Decimal(boost)
            # spread = input('Type spread between orders in secondary currency : ')
            cfg = haasomeClient.customBotApi.setup_flash_crash_bot(
                bot.accountId,
                bot.guid,
                bot.name,
                bot.priceMarket.primaryCurrency,
                bot.priceMarket.secondaryCurrency,
                bot.currentFeePercentage,
                bot.basePrice,
                3,
                bot.priceSpread,
                bot.percentageBoost,
                bot.minPercentage,
                bot.maxPercentage,
                bot.amountType,
                bot.amountSpread,
                bot.totalBuyAmount,
                bot.totalSellAmount,
                bot.refillDelay,
                bot.safetyEnabled,
                bot.safetyTriggerLevel,
                bot.safetyMoveInMarket,
                bot.safetyMoveOutMarket,
                bot.followTheTrend,
                bot.followTheTrendChannelRange,
                bot.followTheTrendChannelOffset,
                bot.followTheTrendTimeout,
            )
            bt = btfcb(bot, haasomeClient, ticks)
            print(bt.roi)
            print("configuring bot parameters: ", cfg.errorCode, cfg.errorMessage)
        return cfg.result

    if bot.priceSpreadType == 3:  # exp
        print("bot price spread type is set to Fixed ammount.\n")
        spreadmin = (
            0.5
        )  # float(input('Type spread to start from in decimals like 0.05:  '))
        spreadmax = (
            1.0
        )  # float(input('Type spread to end with in decimals like 0.55:  '))
        step = 0.1  # float(input('Type spread step'))
        boost = 0.01
        multiplyer = 0.1
        for spread in np.arange(float(spreadmin), float(spreadmax), float(step)):
            cfg = haasomeClient.customBotApi.setup_flash_crash_bot(
                accountguid=bot.accountId,
                botguid=bot.guid,
                botname=bot.name,
                primarycoin=bot.priceMarket.primaryCurrency,
                secondarycoin=bot.priceMarket.secondaryCurrency,
                fee=bot.currentFeePercentage,
                baseprice=bot.basePrice,
                priceSpreadType=3,
                pricespread=spread,
                percentageboost=multiplyer,
                minpercentage=bot.minPercentage,
                maxpercentage=bot.maxPercentage,
                amounttype=bot.amountType,
                amountspread=bot.amountSpread,
                buyamount=bot.totalBuyAmount,
                sellamount=bot.totalSellAmount,
                refilldelay=bot.refillDelay,
                safetyenabled=bot.safetyEnabled,
                safetytriggerlevel=bot.safetyTriggerLevel,
                safetymovein=bot.safetyMoveInMarket,
                safetymoveout=bot.safetyMoveOutMarket,
                followthetrend=bot.followTheTrend,
                followthetrendchannelrange=bot.followTheTrendChannelRange,
                followthetrendchanneloffset=bot.followTheTrendChannelOffset,
                followthetrendtimeout=bot.followTheTrendTimeout,
            )
            bt = btfcb(cfg.result, haasomeClient, ticks)
            print(bt.roi)
            print("configuring bot parameters: ", cfg.errorCode, cfg.errorMessage)
        return cfg.result
    if bot.priceSpreadType == 0:  # exp
        print("bot price spread type is set to Fixed ammount.\n")
        spreadmin = (
            0.5
        )  # float(input('Type spread to start from in decimals like 0.05:  '))
        spreadmax = (
            1.0
        )  # float(input('Type spread to end with in decimals like 0.55:  '))
        step = 0.1  # float(input('Type spread step'))
        boost = 0.01
        multiplyer = 0.1
        for spread in np.arange(float(spreadmin), float(spreadmax), float(step)):
            cfg = haasomeClient.customBotApi.setup_flash_crash_bot(
                accountguid=bot.accountId,
                botguid=bot.guid,
                botname=bot.name,
                primarycoin=bot.priceMarket.primaryCurrency,
                secondarycoin=bot.priceMarket.secondaryCurrency,
                fee=bot.currentFeePercentage,
                baseprice=bot.basePrice,
                priceSpreadType=0,
                pricespread=spread,
                percentageboost=bot.percentageBoost,
                minpercentage=bot.minPercentage,
                maxpercentage=bot.maxPercentage,
                amounttype=bot.amountType,
                amountspread=bot.amountSpread,
                buyamount=bot.totalBuyAmount,
                sellamount=bot.totalSellAmount,
                refilldelay=bot.refillDelay,
                safetyenabled=bot.safetyEnabled,
                safetytriggerlevel=bot.safetyTriggerLevel,
                safetymovein=bot.safetyMoveInMarket,
                safetymoveout=bot.safetyMoveOutMarket,
                followthetrend=bot.followTheTrend,
                followthetrendchannelrange=bot.followTheTrendChannelRange,
                followthetrendchanneloffset=bot.followTheTrendChannelOffset,
                followthetrendtimeout=bot.followTheTrendTimeout,
            )
            bt = btfcb(bot, haasomeClient, ticks)
            print("BT result: ", bt.roi)
            print("configuring bot parameters: ", cfg.errorCode, cfg.errorMessage)


def btfcb(bot, haasomeClient, ticks):
    bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
        bot.accountId,
        bot.guid,
        ticks,
        bot.priceMarket.primaryCurrency,
        bot.priceMarket.secondaryCurrency,
        bot.priceMarket.contractName,
    )
    print(bt.errorMessage, bt.errorCode)
    return bt.result


def main():
    interval = int(inter.inticks(2019, 8, 26, 5))
    bot = botsellector.getallfcbots(haasomeClient)
    trysetup = setspread(bot)
    # bot = showbotconfig(bot)
    # configure = configurefcbbotparam(bot)
    # bt = btfcb(bot, 0.1, 1.0, 0.1, interval, haasomeClient)


if __name__ == "__main__":
    main()
