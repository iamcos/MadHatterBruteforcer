## INCOMPLETE DUE TO INABILITY TO CHANGE ANY OF BOT PARAMETERS ##


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

ip, secret = init.connect()

haasomeClient = HaasomeClient(ip, secret)


def setspread(bot):
    haasomeClient = HaasomeClient(ip, secret)

    if bot.priceSpreadType == 0:

        print("bot price spread type is set to Fixed ammount.\n")
        spreadmin = input("Type spread to start from in decimals like 0.05:  ")
        spreadmax = input("Type spread to end with in decimals like 0.55:  ")
        step = input("Type spread step")
        for spread in np.arange(float(spreadmin), float(spreadmax), float(step)):
            # spread = input('Type spread between orders in secondary currency : ')
            cfg = haasomeClient.customBotApi.setup_script_bot()
            print("configuring bot parameters: ", cfg.errorCode, cfg.errorMessage)
            result = cfg.result
            print(result)


def main():
    interval = int(inter.inticks(2019, 8, 26, 5))
    bot = botsellector.getallfcbots(haasomeClient)
    trysetup = setspread(bot)
    # bot = showbotconfig(bot)
    # configure = configurefcbbotparam(bot)
    # bt = btfcb(bot, 0.1, 1.0, 0.1, interval, haasomeClient)


if __name__ == "__main__":
    main()
