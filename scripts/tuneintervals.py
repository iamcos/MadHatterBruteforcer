def tune_timeinterval():

    basebotconfig = haasomeClient.customBotApi.get_custom_bot(
        guid, EnumCustomBotType.MAD_HATTER_BOT
    ).result
    marketdata = []
    marketobject = haasomeClient.marketDataApi.get_price_markets(
        basebotconfig.priceMarket.priceSource
    )
    marketobjectr = marketobject.result
    for i, v in enumerate(marketobjectr):
        if (
            marketobjectr[i].primaryCurrency
            == basebotconfig.priceMarket.primaryCurrency
            and marketobjectr[i].secondaryCurrency
            == basebotconfig.priceMarket.secondaryCurrency
        ):
            marketdata = marketobjectr[i]

    intervals = {
        "0 minutes": 0,
        "1 minutes": 1,
        "2 minutes": 2,
        "3 minutes": 3,
        "4 minutes": 4,
        "5 minutes": 5,
        "6 minutes": 6,
        "10 minutes": 10,
        "12 minutes": 12,
        "15 minutes": 15,
        "20 minutes": 20,
        "30 minutes": 30,
        "45 minutes": 45,
        "1 hour": 60,
        "1.5 hours": 90,
        "2 hours": 120,
        "2.5 hours": 150,
        "3 hours": 180,
        "4 hours": 240,
        "6 hours": 360,
        "12 hours": 720,
        "1 day": 1440,
        "2 days": 2880,
    }
    intervalindex = []
    intervalkeys = list(intervals.keys())
    intervalvalues = list(intervals.values())
    paramroi = []
    for n, i in enumerate(intervalvalues):
        if i == basebotconfig.interval:
            intervalindex = n
            print("Current bot interval: ", intervalindex, " Minutes")
        initinterval = intervalindex

        while intervalindex >= 0 and intervalindex <= 12:
            configuremadhatter = haasomeClient.customBotApi.setup_mad_hatter_bot(
                basebotconfig.name,
                basebotconfig.guid,
                basebotconfig.accountId,
                basebotconfig.priceMarket.primaryCurrency,
                basebotconfig.priceMarket.secondaryCurrency,
                marketdata.contractName,
                basebotconfig.leverage,
                basebotconfig.customTemplate,
                basebotconfig.coinPosition,
                marketdata.tradeFee,
                basebotconfig.amountType,
                basebotconfig.currentTradeAmount,
                basebotconfig.useTwoSignals,
                basebotconfig.disableAfterStopLoss,
                intervalvalues[intervalindex],
                basebotconfig.includeIncompleteInterval,
                basebotconfig.mappedBuySignal,
                basebotconfig.mappedSellSignal,
            )
            print(configuremadhatter.result.interval, "minutes")
            bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                basebotconfig.accountId,
                basebotconfig.guid,
                btinterval,
                basebotconfig.priceMarket.primaryCurrency,
                basebotconfig.priceMarket.secondaryCurrency,
                marketdata.contractName,
            )
            print("backrtested mad hatter", bt.errorCode, bt.errorMessage)
            btr = bt.result
            print(btr.roi)
            paramroi.append([btr.roi, intervalvalues[intervalindex]])
            intervalindex += 1
        while initinterval > 0 and initinterval <= 12:
            configuremadhatter = haasomeClient.customBotApi.setup_mad_hatter_bot(
                basebotconfig.name,
                basebotconfig.guid,
                basebotconfig.accountId,
                basebotconfig.priceMarket.primaryCurrency,
                basebotconfig.priceMarket.secondaryCurrency,
                marketdata.contractName,
                basebotconfig.leverage,
                basebotconfig.customTemplate,
                basebotconfig.coinPosition,
                marketdata.tradeFee,
                basebotconfig.amountType,
                basebotconfig.currentTradeAmount,
                basebotconfig.useTwoSignals,
                basebotconfig.disableAfterStopLoss,
                intervalvalues[initinterval],
                basebotconfig.includeIncompleteInterval,
                basebotconfig.mappedBuySignal,
                basebotconfig.mappedSellSignal,
            )
            print(configuremadhatter.result.interval, "minutes")
            bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                basebotconfig.accountId,
                basebotconfig.guid,
                btinterval,
                basebotconfig.priceMarket.primaryCurrency,
                basebotconfig.priceMarket.secondaryCurrency,
                marketdata.contractName,
            )
            print("backrtested mad hatter", bt.errorCode, bt.errorMessage)
            btr = bt.result
            print(btr.roi)
            paramroi.append([btr.roi, intervalvalues[initinterval]])
            initinterval -= 1

        paramroisorted = sorted(paramroi, key=lambda x: x[0], reverse=True)
        configuremadhatter = haasomeClient.customBotApi.setup_mad_hatter_bot(
            basebotconfig.name,
            basebotconfig.guid,
            basebotconfig.accountId,
            basebotconfig.priceMarket.primaryCurrency,
            basebotconfig.priceMarket.secondaryCurrency,
            marketdata.contractName,
            basebotconfig.leverage,
            basebotconfig.customTemplate,
            basebotconfig.coinPosition,
            marketdata.tradeFee,
            basebotconfig.amountType,
            basebotconfig.currentTradeAmount,
            basebotconfig.useTwoSignals,
            basebotconfig.disableAfterStopLoss,
            intervalvalues[paramroisorted[0]],
            basebotconfig.includeIncompleteInterval,
            basebotconfig.mappedBuySignal,
            basebotconfig.mappedSellSignal,
        )
        print("best time interval has been set")
