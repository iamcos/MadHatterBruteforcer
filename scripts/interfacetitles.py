interfacetitles = [
    "Acceleration",
    "Atr Length",
    "Buy level",
    "Buy level",
    "Buy level",
    "Buy level",
    "Buy price",
    "Buy price",
    "Buy threshold",
    "Buy threshold",
    "Buy threshold",
    "Buy threshold",
    "Buy threshold",
    "Buy/Sell Trigger",
    "ChikouSpan",
    "Dev.Down",
    "Dev.Up",
    "Fast D",
    "Fast K",
    "Kijun-Sen",
    "Length-1",
    "Length-2",
    "Length",
    "Length",
    "Length",
    "Length",
    "Long length",
    "Long Length",
    "Long length",
    "Long",
    "Lookback For Buy",
    "Lookback For Sell",
    "Lookback",
    "Lookback",
    "MaximumStep",
    "Middle Length",
    "Minutes before adjust",
    "Minutes before signal change",
    "Multiplier",
    "Number Of Candles For Buy",
    "Number Of Candles For Sell",
    "Pattern",
    "ROC-1",
    "ROC-2",
    "ROC",
    "ROC",
    "RSI Length",
    "Sell level",
    "Sell level",
    "Sell level",
    "Sell level",
    "Sell price",
    "Sell threshold",
    "Sell threshold",
    "Sell threshold",
    "Sell threshold",
    "Sell threshold",
    "Senkou Span B",
    "Short length",
    "Short length",
    "Short Length",
    "Short",
    "Signal Length",
    "Signal Length",
    "Signal length",
    "Signal When Buy Sequence Broke",
    "Signal When Sell Sequence Broke",
    "Sma Length",
    "Swing",
    "Tenkan-Sen",
    "Trigger method",
    "Trigger method",
    "U/D Length",
    "WMALength",
]

for i in interfacetitles:
    print("for x in range(len(key)):")
    print(" if key2 ==" + "'" + str(i) + "'" + ":")
    print("  start =value2*0.8 ")
    print("  stop =value2*1.2 ")
    print("  step =value2*0.1 ")
    print("  for x in np.arange(start,stop,step):")
    print(
        "   change = haasomeClient.tradeBotApi.edit_bot_indicator_settings(gettradebot.guid, guid, 0, x)"
    )
    print(
        "   bt = haasomeClient.tradeBotApi.backtest_trade_bot(gettradebot.guid, ticks)"
    )
    print("   printerrors(bt)")
    print("   printerrors(change)")
    print("   print(bt.result.roi)")
    print("   results.append([bt.result.roi, x])")
