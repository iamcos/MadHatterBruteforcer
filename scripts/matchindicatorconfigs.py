import configparser


def indicatorranges(bot):
    indicators = bot.indicators
    for indicator in indicators:
        bot.indicator
    indicator_configs = configparser.ConfigParser()
    indicator_configs.read("indicatorranges.ini")

    indicators = indicator_configs.sections()

    for indicator in indicators:
        options = indicator_configs.options(indicator)
        for parameter in options:
            values = indicator_configs.get(indicator, parameter)
            print(indicator, parameter, values)
