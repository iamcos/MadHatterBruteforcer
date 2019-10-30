def indicatorparametersdata(bot, haasomeClient):
    todict = indicatorstodict2(bot)
    for indicator, data in todict.items():
        # if indicator == 'Bollinger Bands':
        for paramname, data1 in todict[indicator].items():
            # if paramname == 'Dev.Down':
            for pramstring, paramvalue in todict[str(indicator)][
                str(paramname)
            ].items():
                print(indicator, paramname, pramstring, paramvalue)
