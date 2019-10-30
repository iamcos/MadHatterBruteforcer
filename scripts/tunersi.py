class tunersi:
    rsiconfig = []
    basebotconfig = haasomeClient.customBotApi.get_custom_bot(
        guid, EnumCustomBotType.BASE_CUSTOM_BOT
    ).result
    l = basebotconfig.rsi["RsiLength"]
    s = basebotconfig.rsi["RsiOversold"]
    b = basebotconfig.rsi["RsiOverbought"]

    def setl(l):
        for i in enumerate(rsiconfig):
            if i[1] == l and i[2] == s and i[3] == b:
                pass
            else:
                setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                    guid, EnumMadHatterIndicators.RSI, 0, l
                )
                bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                    basebotconfig.accountId,
                    basebotconfig.guid,
                    btinterval,
                    basebotconfig.priceMarket.primaryCurrency,
                    basebotconfig.priceMarket.secondaryCurrency,
                    basebotconfig.priceMarket.contractName,
                )
                btr = bt.result
                print(btr.roi, "RSI: ", l, s, b)
                rsiconfig.append([btr.roi, l, s, b])

    def sets(s):
        for i, x in enumerate(rsiconfig):
            if i[1] == l and i[2] == s and i[3] == b:
                pass
            else:
                setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                    guid, EnumMadHatterIndicators.RSI, 1, s
                )
                bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                    basebotconfig.accountId,
                    basebotconfig.guid,
                    btinterval,
                    basebotconfig.priceMarket.primaryCurrency,
                    basebotconfig.priceMarket.secondaryCurrency,
                    basebotconfig.priceMarket.contractName,
                )
                btr = bt.result
                print(btr.roi, "RSI: ", l, s, b)
                rsiconfig.append([btr.roi, l, s, b])

    def setb(b):
        for i, x in enumerate(rsiconfig):
            if i[1] == l and i[2] == s and i[3] == b:
                pass
            else:
                setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                    guid, EnumMadHatterIndicators.RSI, 2, b
                )
                bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                    basebotconfig.accountId,
                    basebotconfig.guid,
                    btinterval,
                    basebotconfig.priceMarket.primaryCurrency,
                    basebotconfig.priceMarket.secondaryCurrency,
                    basebotconfig.priceMarket.contractName,
                )
                btr = bt.result
                print(btr.roi, "RSI: ", l, s, b)
                rsiconfig.append([btr.roi, l, s, b])
