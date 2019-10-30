### BBands tuning and setup ###


def setLength():
    answers = {"selection": None}
    while answers["selection"] != "back":
        action = [
            {
                "type": "list",
                "name": "selection",
                "message": "Chose your next move: ",
                "choices": [
                    "increse",
                    "decrease",
                    "increase 10 steps",
                    "decrease 10 steps",
                    "back",
                ],
            }
        ]

        if answers["selection"] == "increse":
            basebotconfig = haasomeClient.customBotApi.get_custom_bot(
                guid, EnumCustomBotType.BASE_CUSTOM_BOT
            ).result
            currentl = basebotconfig.bBands["Length"]
            currentl += 1
            setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                guid, EnumMadHatterIndicators.BBANDS, 0, currentl
            )
            bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                basebotconfig.accountId,
                basebotconfig.guid,
                btinterval,
                basebotconfig.priceMarket.primaryCurrency,
                basebotconfig.priceMarket.secondaryCurrency,
                basebotconfig.priceMarket.contractName,
            )
            # # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
            btr = bt.result
            print(btr.roi, " ", currentl, "bBands Length")
        elif answers["selection"] == "decrease":
            basebotconfig = haasomeClient.customBotApi.get_custom_bot(
                guid, EnumCustomBotType.BASE_CUSTOM_BOT
            ).result
            currentl = basebotconfig.bBands["Length"]
            currentl -= 1
            setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                guid, EnumMadHatterIndicators.BBANDS, 0, currentl
            )
            bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                basebotconfig.accountId,
                basebotconfig.guid,
                btinterval,
                basebotconfig.priceMarket.primaryCurrency,
                basebotconfig.priceMarket.secondaryCurrency,
                basebotconfig.priceMarket.contractName,
            )
            # # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
            btr = bt.result
            print(btr.roi, " ", currentl, "bBands Length")

        elif answers["selection"] == "increase 10 steps":
            basebotconfig = haasomeClient.customBotApi.get_custom_bot(
                guid, EnumCustomBotType.BASE_CUSTOM_BOT
            ).result
            currentl = basebotconfig.bBands["Length"]
            for x in range(10):
                currentl += 1
                setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                    guid, EnumMadHatterIndicators.BBANDS, 0, currentl
                )
                bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                    basebotconfig.accountId,
                    basebotconfig.guid,
                    btinterval,
                    basebotconfig.priceMarket.primaryCurrency,
                    basebotconfig.priceMarket.secondaryCurrency,
                    basebotconfig.priceMarket.contractName,
                )
                # # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
                btr = bt.result
                print(btr.roi, " ", currentl)

        elif answers["selection"] == "decrease 10 steps":
            basebotconfig = haasomeClient.customBotApi.get_custom_bot(
                guid, EnumCustomBotType.BASE_CUSTOM_BOT
            ).result
            currentl = basebotconfig.bBands["Length"]
            for x in range(10):
                currentl -= 1
                setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                    guid, EnumMadHatterIndicators.BBANDS, 0, currentl
                )
                bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                    basebotconfig.accountId,
                    basebotconfig.guid,
                    btinterval,
                    basebotconfig.priceMarket.primaryCurrency,
                    basebotconfig.priceMarket.secondaryCurrency,
                    basebotconfig.priceMarket.contractName,
                )
                # # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
                btr = bt.result
                print(btr.roi, " ", currentl)
        answers = prompt(action)


def setDevup():
    answers = {"selection": None}
    while answers["selection"] != "back":
        action = [
            {
                "type": "list",
                "name": "selection",
                "message": "Chose your next move: ",
                "choices": [
                    "increse",
                    "decrease",
                    "increase 10 steps",
                    "decrease 10 steps",
                    "back",
                ],
            }
        ]

        if answers["selection"] == "increse":
            basebotconfig = haasomeClient.customBotApi.get_custom_bot(
                guid, EnumCustomBotType.BASE_CUSTOM_BOT
            ).result
            currentl = basebotconfig.bBands["Devup"]
            currentl += 0.1
            setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                guid, EnumMadHatterIndicators.BBANDS, 1, currentl
            )
            bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                basebotconfig.accountId,
                basebotconfig.guid,
                btinterval,
                basebotconfig.priceMarket.primaryCurrency,
                basebotconfig.priceMarket.secondaryCurrency,
                basebotconfig.priceMarket.contractName,
            )
            # # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
            btr = bt.result
            print(btr.roi, " ", currentl)
        elif answers["selection"] == "decrease":
            basebotconfig = haasomeClient.customBotApi.get_custom_bot(
                guid, EnumCustomBotType.BASE_CUSTOM_BOT
            ).result
            currentl = basebotconfig.bBands["Devup"]
            currentl -= 0.1
            setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                guid, EnumMadHatterIndicators.BBANDS, 1, currentl
            )
            bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                basebotconfig.accountId,
                basebotconfig.guid,
                btinterval,
                basebotconfig.priceMarket.primaryCurrency,
                basebotconfig.priceMarket.secondaryCurrency,
                basebotconfig.priceMarket.contractName,
            )
            # # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
            btr = bt.result
            print(btr.roi, " ", currentl)

        elif answers["selection"] == "increase 10 steps":
            basebotconfig = haasomeClient.customBotApi.get_custom_bot(
                guid, EnumCustomBotType.BASE_CUSTOM_BOT
            ).result
            currentl = basebotconfig.bBands["Devup"]
            for x in range(10):
                currentl += 0.1
                setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                    guid, EnumMadHatterIndicators.BBANDS, 1, currentl
                )
                bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                    basebotconfig.accountId,
                    basebotconfig.guid,
                    btinterval,
                    basebotconfig.priceMarket.primaryCurrency,
                    basebotconfig.priceMarket.secondaryCurrency,
                    basebotconfig.priceMarket.contractName,
                )
                # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
                btr = bt.result
                print(btr.roi, " ", currentl)

        elif answers["selection"] == "decrease 10 steps":
            basebotconfig = haasomeClient.customBotApi.get_custom_bot(
                guid, EnumCustomBotType.BASE_CUSTOM_BOT
            ).result
            currentl = basebotconfig.bBands["Devup"]
            for x in range(10):
                currentl -= 0.1
                setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                    guid, EnumMadHatterIndicators.BBANDS, 1, currentl
                )
                bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                    basebotconfig.accountId,
                    basebotconfig.guid,
                    btinterval,
                    basebotconfig.priceMarket.primaryCurrency,
                    basebotconfig.priceMarket.secondaryCurrency,
                    basebotconfig.priceMarket.contractName,
                )
                # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
                btr = bt.result
                print(btr.roi, " ", currentl)
        answers = prompt(action)


def setDevdn():
    answers = {"selection": None}
    while answers["selection"] != "back":
        action = [
            {
                "type": "list",
                "name": "selection",
                "message": "Chose your next move: ",
                "choices": [
                    "increse",
                    "decrease",
                    "increase 10 steps",
                    "decrease 10 steps",
                    "back",
                ],
            }
        ]

        if answers["selection"] == "increse":
            basebotconfig = haasomeClient.customBotApi.get_custom_bot(
                guid, EnumCustomBotType.BASE_CUSTOM_BOT
            ).result
            currentl = basebotconfig.bBands["Devdn"]
            currentl += 0.1
            setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                guid, EnumMadHatterIndicators.BBANDS, 2, currentl
            )
            bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                basebotconfig.accountId,
                basebotconfig.guid,
                btinterval,
                basebotconfig.priceMarket.primaryCurrency,
                basebotconfig.priceMarket.secondaryCurrency,
                basebotconfig.priceMarket.contractName,
            )
            # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
            btr = bt.result
            print(btr.roi, " ", currentl)
        elif answers["selection"] == "decrease":
            basebotconfig = haasomeClient.customBotApi.get_custom_bot(
                guid, EnumCustomBotType.BASE_CUSTOM_BOT
            ).result
            currentl = basebotconfig.bBands["Devdn"]
            currentl -= 0.1
            setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                guid, EnumMadHatterIndicators.BBANDS, 2, currentl
            )
            bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                basebotconfig.accountId,
                basebotconfig.guid,
                btinterval,
                basebotconfig.priceMarket.primaryCurrency,
                basebotconfig.priceMarket.secondaryCurrency,
                basebotconfig.priceMarket.contractName,
            )
            # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
            btr = bt.result
            print(btr.roi, " ", currentl)

        elif answers["selection"] == "increase 10 steps":
            basebotconfig = haasomeClient.customBotApi.get_custom_bot(
                guid, EnumCustomBotType.BASE_CUSTOM_BOT
            ).result
            currentl = basebotconfig.bBands["Devdn"]
            for x in range(10):
                currentl += 0.1
                setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                    guid, EnumMadHatterIndicators.BBANDS, 2, currentl
                )
                bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                    basebotconfig.accountId,
                    basebotconfig.guid,
                    btinterval,
                    basebotconfig.priceMarket.primaryCurrency,
                    basebotconfig.priceMarket.secondaryCurrency,
                    basebotconfig.priceMarket.contractName,
                )
                # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
                btr = bt.result
                print(btr.roi, " ", currentl)

        elif answers["selection"] == "decrease 10 steps":
            basebotconfig = haasomeClient.customBotApi.get_custom_bot(
                guid, EnumCustomBotType.BASE_CUSTOM_BOT
            ).result
            currentl = basebotconfig.bBands["Devdn"]
            for x in range(10):
                currentl -= 0.1
                setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                    guid, EnumMadHatterIndicators.BBANDS, 2, currentl
                )
                bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                    basebotconfig.accountId,
                    basebotconfig.guid,
                    btinterval,
                    basebotconfig.priceMarket.primaryCurrency,
                    basebotconfig.priceMarket.secondaryCurrency,
                    basebotconfig.priceMarket.contractName,
                )
                # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
                btr = bt.result
                print(btr.roi, " ", currentl)
        answers = prompt(action)


### RSI PART starts now ###


def setRsiLength():
    answers = {"selection": None}
    while answers["selection"] != "back":
        action = [
            {
                "type": "list",
                "name": "selection",
                "message": "Chose your next move: ",
                "choices": [
                    "increse",
                    "decrease",
                    "increase 10 steps",
                    "decrease 10 steps",
                    "back",
                ],
            }
        ]

        if answers["selection"] == "increse":
            basebotconfig = haasomeClient.customBotApi.get_custom_bot(
                guid, EnumCustomBotType.BASE_CUSTOM_BOT
            ).result
            currentvalue = basebotconfig.rsi["RsiLength"]
            currentvalue += 1
            setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                guid, EnumMadHatterIndicators.RSI, 0, currentvalue
            )
            bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                basebotconfig.accountId,
                basebotconfig.guid,
                btinterval,
                basebotconfig.priceMarket.primaryCurrency,
                basebotconfig.priceMarket.secondaryCurrency,
                basebotconfig.priceMarket.contractName,
            )
            # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
            btr = bt.result
            print(btr.roi, currentvalue)
        elif answers["selection"] == "decrease":
            basebotconfig = haasomeClient.customBotApi.get_custom_bot(
                guid, EnumCustomBotType.BASE_CUSTOM_BOT
            ).result
            currentvalue = basebotconfig.rsi["RsiLength"]
            currentvalue -= 1
            setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                guid, EnumMadHatterIndicators.RSI, 0, currentvalue
            )
            bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                basebotconfig.accountId,
                basebotconfig.guid,
                btinterval,
                basebotconfig.priceMarket.primaryCurrency,
                basebotconfig.priceMarket.secondaryCurrency,
                basebotconfig.priceMarket.contractName,
            )
            # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
            btr = bt.result
            print(btr.roi, currentvalue)

        elif answers["selection"] == "increase 10 steps":
            basebotconfig = haasomeClient.customBotApi.get_custom_bot(
                guid, EnumCustomBotType.BASE_CUSTOM_BOT
            ).result
            currentvalue = basebotconfig.rsi["RsiLength"]
            for x in range(10):
                currentvalue += 1
                setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                    guid, EnumMadHatterIndicators.RSI, 0, currentvalue
                )
                bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                    basebotconfig.accountId,
                    basebotconfig.guid,
                    btinterval,
                    basebotconfig.priceMarket.primaryCurrency,
                    basebotconfig.priceMarket.secondaryCurrency,
                    basebotconfig.priceMarket.contractName,
                )
                # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
                btr = bt.result
                print(btr.roi, currentvalue)

        elif answers["selection"] == "decrease 10 steps":
            basebotconfig = haasomeClient.customBotApi.get_custom_bot(
                guid, EnumCustomBotType.BASE_CUSTOM_BOT
            ).result
            currentvalue = basebotconfig.rsi["RsiLength"]
            for x in range(10):
                currentvalue -= 1
                setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                    guid, EnumMadHatterIndicators.RSI, 0, currentvalue
                )
                bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                    basebotconfig.accountId,
                    basebotconfig.guid,
                    btinterval,
                    basebotconfig.priceMarket.primaryCurrency,
                    basebotconfig.priceMarket.secondaryCurrency,
                    basebotconfig.priceMarket.contractName,
                )
                # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
                btr = bt.result
                print(btr.roi, currentvalue)
        answers = prompt(action)


def setRsiOversold():
    answers = {"selection": None}
    while answers["selection"] != "back":
        basebotconfig = haasomeClient.customBotApi.get_custom_bot(
            guid, EnumCustomBotType.BASE_CUSTOM_BOT
        ).result
        currentvalue = basebotconfig.rsi["RsiOversold"]
        action = [
            {
                "type": "list",
                "name": "selection",
                "message": "Chose your next move: ",
                "choices": [
                    "increse",
                    "decrease",
                    "increase 10 steps",
                    "decrease 10 steps",
                    "back",
                ],
            }
        ]
        if answers["selection"] == "increse":

            currentvalue += 1
            setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                guid, EnumMadHatterIndicators.RSI, 1, currentvalue
            )
            bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                basebotconfig.accountId,
                basebotconfig.guid,
                btinterval,
                basebotconfig.priceMarket.primaryCurrency,
                basebotconfig.priceMarket.secondaryCurrency,
                basebotconfig.priceMarket.contractName,
            )
            # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
            btr = bt.result
            print(btr.roi, currentvalue)
        elif answers["selection"] == "decrease":
            # basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
            # currentvalue = basebotconfig.rsi['RsiOversold']
            currentvalue -= 1
            setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                guid, EnumMadHatterIndicators.RSI, 1, currentvalue
            )
            bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                basebotconfig.accountId,
                basebotconfig.guid,
                btinterval,
                basebotconfig.priceMarket.primaryCurrency,
                basebotconfig.priceMarket.secondaryCurrency,
                basebotconfig.priceMarket.contractName,
            )
            # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
            btr = bt.result
            print(btr.roi, currentvalue)

        elif answers["selection"] == "increase 10 steps":
            # basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
            # currentvalue = basebotconfig.rsi['RsiOversold']
            for x in range(10):
                currentvalue += 1
                setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                    guid, EnumMadHatterIndicators.RSI, 1, currentvalue
                )
                bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                    basebotconfig.accountId,
                    basebotconfig.guid,
                    btinterval,
                    basebotconfig.priceMarket.primaryCurrency,
                    basebotconfig.priceMarket.secondaryCurrency,
                    basebotconfig.priceMarket.contractName,
                )
                # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
                btr = bt.result
                print(btr.roi, currentvalue)

        elif answers["selection"] == "decrease 10 steps":
            # basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
            # currentvalue = basebotconfig.rsi['RsiOversold']
            for x in range(10):
                currentvalue -= 1
                setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                    guid, EnumMadHatterIndicators.RSI, 1, currentvalue
                )
                bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                    basebotconfig.accountId,
                    basebotconfig.guid,
                    btinterval,
                    basebotconfig.priceMarket.primaryCurrency,
                    basebotconfig.priceMarket.secondaryCurrency,
                    basebotconfig.priceMarket.contractName,
                )
                # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
                btr = bt.result
                print(btr.roi, currentvalue)
        answers = prompt(action)


def setRsiOverbought():
    answers = {"selection": None}
    while answers["selection"] != "back":
        basebotconfig = haasomeClient.customBotApi.get_custom_bot(
            guid, EnumCustomBotType.BASE_CUSTOM_BOT
        ).result
        currentvalue = basebotconfig.rsi["RsiOverbought"]
        action = [
            {
                "type": "list",
                "name": "selection",
                "message": "Chose your next move: ",
                "choices": [
                    "increse",
                    "decrease",
                    "increase 10 steps",
                    "decrease 10 steps",
                    "back",
                ],
            }
        ]
        if answers["selection"] == "increse":
            currentvalue += 1
            setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                guid, EnumMadHatterIndicators.RSI, 2, currentvalue
            )
            bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                basebotconfig.accountId,
                basebotconfig.guid,
                btinterval,
                basebotconfig.priceMarket.primaryCurrency,
                basebotconfig.priceMarket.secondaryCurrency,
                basebotconfig.priceMarket.contractName,
            )
            # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
            btr = bt.result
            print(btr.roi, currentvalue)
        elif answers["selection"] == "decrease":
            # basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
            # currentvalue = basebotconfig.rsi['RsiOverbought']
            currentvalue -= 1
            setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                guid, EnumMadHatterIndicators.RSI, 2, currentvalue
            )
            bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                basebotconfig.accountId,
                basebotconfig.guid,
                btinterval,
                basebotconfig.priceMarket.primaryCurrency,
                basebotconfig.priceMarket.secondaryCurrency,
                basebotconfig.priceMarket.contractName,
            )
            # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
            btr = bt.result
            print(btr.roi, currentvalue)

        elif answers["selection"] == "increase 10 steps":
            # basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
            # currentvalue = basebotconfig.rsi['RsiOverbought']
            for x in range(10):
                currentvalue += 1
                setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                    guid, EnumMadHatterIndicators.RSI, 2, currentvalue
                )
                bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                    basebotconfig.accountId,
                    basebotconfig.guid,
                    btinterval,
                    basebotconfig.priceMarket.primaryCurrency,
                    basebotconfig.priceMarket.secondaryCurrency,
                    basebotconfig.priceMarket.contractName,
                )
                # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
                btr = bt.result
                print(btr.roi, currentvalue)

        elif answers["selection"] == "decrease 10 steps":
            # basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
            # currentvalue = basebotconfig.rsi['RsiOverbought']
            for x in range(10):
                currentvalue -= 1
                setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                    guid, EnumMadHatterIndicators.RSI, 2, currentvalue
                )
                bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                    basebotconfig.accountId,
                    basebotconfig.guid,
                    btinterval,
                    basebotconfig.priceMarket.primaryCurrency,
                    basebotconfig.priceMarket.secondaryCurrency,
                    basebotconfig.priceMarket.contractName,
                )
                # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
                btr = bt.result
                print(btr.roi, currentvalue)
        answers = prompt(action)


### MACD Configuration strings ###


def setMacdFast():
    answers = {"selection": None}
    while answers["selection"] != "back":
        action = [
            {
                "type": "list",
                "name": "selection",
                "message": "Chose your next move: ",
                "choices": [
                    "increse",
                    "decrease",
                    "increase 10 steps",
                    "decrease 10 steps",
                    "back",
                ],
            }
        ]

        if answers["selection"] == "increse":
            basebotconfig = haasomeClient.customBotApi.get_custom_bot(
                guid, EnumCustomBotType.BASE_CUSTOM_BOT
            ).result
            currentvalue = basebotconfig.macd["MacdFast"]
            currentvalue += 1
            setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                guid, EnumMadHatterIndicators.MACD, 0, currentvalue
            )
            bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                basebotconfig.accountId,
                basebotconfig.guid,
                btinterval,
                basebotconfig.priceMarket.primaryCurrency,
                basebotconfig.priceMarket.secondaryCurrency,
                basebotconfig.priceMarket.contractName,
            )
            # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
            btr = bt.result
            print(btr.roi, " ", currentvalue)
        elif answers["selection"] == "decrease":
            basebotconfig = haasomeClient.customBotApi.get_custom_bot(
                guid, EnumCustomBotType.BASE_CUSTOM_BOT
            ).result
            currentvalue = basebotconfig.macd["MacdFast"]
            currentvalue -= 1
            setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                guid, EnumMadHatterIndicators.MACD, 0, currentvalue
            )
            bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                basebotconfig.accountId,
                basebotconfig.guid,
                btinterval,
                basebotconfig.priceMarket.primaryCurrency,
                basebotconfig.priceMarket.secondaryCurrency,
                basebotconfig.priceMarket.contractName,
            )
            # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
            btr = bt.result
            print(btr.roi, " ", currentvalue)

        elif answers["selection"] == "increase 10 steps":
            basebotconfig = haasomeClient.customBotApi.get_custom_bot(
                guid, EnumCustomBotType.BASE_CUSTOM_BOT
            ).result
            currentvalue = basebotconfig.macd["MacdFast"]
            for x in range(10):
                currentvalue += 1
                setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                    guid, EnumMadHatterIndicators.MACD, 0, currentvalue
                )
                bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                    basebotconfig.accountId,
                    basebotconfig.guid,
                    btinterval,
                    basebotconfig.priceMarket.primaryCurrency,
                    basebotconfig.priceMarket.secondaryCurrency,
                    basebotconfig.priceMarket.contractName,
                )
                # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
                btr = bt.result
                print(btr.roi, " ", currentvalue)

        elif answers["selection"] == "decrease 10 steps":
            basebotconfig = haasomeClient.customBotApi.get_custom_bot(
                guid, EnumCustomBotType.BASE_CUSTOM_BOT
            ).result
            currentvalue = basebotconfig.macd["MacdFast"]
            for x in range(10):
                currentvalue -= 1
                setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                    guid, EnumMadHatterIndicators.MACD, 0, currentvalue
                )
                bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                    basebotconfig.accountId,
                    basebotconfig.guid,
                    btinterval,
                    basebotconfig.priceMarket.primaryCurrency,
                    basebotconfig.priceMarket.secondaryCurrency,
                    basebotconfig.priceMarket.contractName,
                )
                # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
                btr = bt.result
                print(btr.roi, " ", currentvalue)
        answers = prompt(action)


def setMacdSlow():
    answers = {"selection": None}
    while answers["selection"] != "back":
        action = [
            {
                "type": "list",
                "name": "selection",
                "message": "Chose your next move: ",
                "choices": [
                    "increse",
                    "decrease",
                    "increase 10 steps",
                    "decrease 10 steps",
                    "back",
                ],
            }
        ]

        if answers["selection"] == "increse":
            basebotconfig = haasomeClient.customBotApi.get_custom_bot(
                guid, EnumCustomBotType.BASE_CUSTOM_BOT
            ).result
            currentvalue = basebotconfig.macd["MacdSlow"]
            currentvalue += 1
            setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                guid, EnumMadHatterIndicators.MACD, 1, currentvalue
            )
            bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                basebotconfig.accountId,
                basebotconfig.guid,
                btinterval,
                basebotconfig.priceMarket.primaryCurrency,
                basebotconfig.priceMarket.secondaryCurrency,
                basebotconfig.priceMarket.contractName,
            )
            # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
            btr = bt.result
            print(btr.roi, " ", currentvalue)
        elif answers["selection"] == "decrease":
            basebotconfig = haasomeClient.customBotApi.get_custom_bot(
                guid, EnumCustomBotType.BASE_CUSTOM_BOT
            ).result
            currentvalue = basebotconfig.macd["MacdSlow"]
            currentvalue -= 1
            setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                guid, EnumMadHatterIndicators.MACD, 1, currentvalue
            )
            bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                basebotconfig.accountId,
                basebotconfig.guid,
                btinterval,
                basebotconfig.priceMarket.primaryCurrency,
                basebotconfig.priceMarket.secondaryCurrency,
                basebotconfig.priceMarket.contractName,
            )
            # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
            btr = bt.result
            print(btr.roi, " ", currentvalue)

        elif answers["selection"] == "increase 10 steps":
            basebotconfig = haasomeClient.customBotApi.get_custom_bot(
                guid, EnumCustomBotType.BASE_CUSTOM_BOT
            ).result
            currentvalue = basebotconfig.macd["MacdSlow"]
            for x in range(10):
                currentvalue += 1
                setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                    guid, EnumMadHatterIndicators.MACD, 1, currentvalue
                )
                bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                    basebotconfig.accountId,
                    basebotconfig.guid,
                    btinterval,
                    basebotconfig.priceMarket.primaryCurrency,
                    basebotconfig.priceMarket.secondaryCurrency,
                    basebotconfig.priceMarket.contractName,
                )
                # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
                btr = bt.result
                print(btr.roi, " ", currentvalue)

        elif answers["selection"] == "decrease 10 steps":
            basebotconfig = haasomeClient.customBotApi.get_custom_bot(
                guid, EnumCustomBotType.BASE_CUSTOM_BOT
            ).result
            currentvalue = basebotconfig.macd["MacdSlow"]
            for x in range(10):
                currentvalue -= 1
                setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                    guid, EnumMadHatterIndicators.MACD, 1, currentvalue
                )
                bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                    basebotconfig.accountId,
                    basebotconfig.guid,
                    btinterval,
                    basebotconfig.priceMarket.primaryCurrency,
                    basebotconfig.priceMarket.secondaryCurrency,
                    basebotconfig.priceMarket.contractName,
                )
                # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
                btr = bt.result
                print(btr.roi, " ", currentvalue)
        answers = prompt(action)


def setMacdSign():
    answers = {"selection": None}
    while answers["selection"] != "back":
        action = [
            {
                "type": "list",
                "name": "selection",
                "message": "Chose your next move: ",
                "choices": [
                    "increse",
                    "decrease",
                    "increase 10 steps",
                    "decrease 10 steps",
                    "back",
                ],
            }
        ]

        if answers["selection"] == "increse":
            basebotconfig = haasomeClient.customBotApi.get_custom_bot(
                guid, EnumCustomBotType.BASE_CUSTOM_BOT
            ).result
            currentvalue = basebotconfig.macd["MacdSign"]
            currentvalue += 1
            setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                guid, EnumMadHatterIndicators.MACD, 2, currentvalue
            )
            bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                basebotconfig.accountId,
                basebotconfig.guid,
                btinterval,
                basebotconfig.priceMarket.primaryCurrency,
                basebotconfig.priceMarket.secondaryCurrency,
                basebotconfig.priceMarket.contractName,
            )
            # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
            btr = bt.result
            print(btr.roi, " ", currentvalue)
        elif answers["selection"] == "decrease":
            basebotconfig = haasomeClient.customBotApi.get_custom_bot(
                guid, EnumCustomBotType.BASE_CUSTOM_BOT
            ).result
            currentvalue = basebotconfig.macd["MacdSign"]
            currentvalue -= 1
            setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                guid, EnumMadHatterIndicators.MACD, 2, currentvalue
            )
            bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                basebotconfig.accountId,
                basebotconfig.guid,
                btinterval,
                basebotconfig.priceMarket.primaryCurrency,
                basebotconfig.priceMarket.secondaryCurrency,
                basebotconfig.priceMarket.contractName,
            )
            # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
            btr = bt.result
            print(btr.roi, " ", currentvalue)

        elif answers["selection"] == "increase 10 steps":
            basebotconfig = haasomeClient.customBotApi.get_custom_bot(
                guid, EnumCustomBotType.BASE_CUSTOM_BOT
            ).result
            currentvalue = basebotconfig.macd["MacdSign"]
            for x in range(10):
                currentvalue += 1
                setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                    guid, EnumMadHatterIndicators.MACD, 2, currentvalue
                )
                bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                    basebotconfig.accountId,
                    basebotconfig.guid,
                    btinterval,
                    basebotconfig.priceMarket.primaryCurrency,
                    basebotconfig.priceMarket.secondaryCurrency,
                    basebotconfig.priceMarket.contractName,
                )
                # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
                btr = bt.result
                print(btr.roi, " ", currentvalue)

        elif answers["selection"] == "decrease 10 steps":
            basebotconfig = haasomeClient.customBotApi.get_custom_bot(
                guid, EnumCustomBotType.BASE_CUSTOM_BOT
            ).result
            currentvalue = basebotconfig.macd["MacdSign"]
            for x in range(10):
                currentvalue -= 1
                setl = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
                    guid, EnumMadHatterIndicators.MACD, 2, currentvalue
                )
                bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(
                    basebotconfig.accountId,
                    basebotconfig.guid,
                    btinterval,
                    basebotconfig.priceMarket.primaryCurrency,
                    basebotconfig.priceMarket.secondaryCurrency,
                    basebotconfig.priceMarket.contractName,
                )
                # print('backrtested mad hatter',bt.errorCode, bt.errorMessage)
                btr = bt.result
                print(btr.roi, " ", currentvalue)
        answers = prompt(action)
