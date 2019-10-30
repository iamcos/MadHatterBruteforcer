from haasomeapi.HaasomeClient import HaasomeClient

# ffrom puinquirer import style_from_dict, Token, prompt
# ffrom puinquirer import Validator, ValidationError
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
import prompt
import tuner
import settimeinterval
import botsellector
import savehistory
import init
haasomeClient = init.connect()
import botsellector
import interval as iiv

def selectparametertochange(bot.guid):
    basebotconfig = haasomeClient.customBotApi.get_custom_bot(
        bot.guid, EnumCustomBotType.BASE_CUSTOM_BOT
    ).result
    questions = [
        {
            "type": "list",
            "name": "selectedparameter",
            "message": "Select parameter to change by using keys up and down then hit return",
            "choices": [
                {
                    "name": "Bot time interval: "
                    + str(basebotconfig.interval)
                    + " minutes",
                    "value": "interval",
                },
                {
                    "name": "bBands MaType: " + str(basebotconfig.bBands["MaType"]),
                    "value": "MaType",
                },
                {"name": "Change BT range", "value": "therange"},
                {
                    "name": "bBands Length: " + str(basebotconfig.bBands["Length"]),
                    "value": "Length",
                },
                {
                    "name": "bBands Dev Up: " + str(basebotconfig.bBands["Devup"]),
                    "value": "Devup",
                },
                {
                    "name": "bBands Dev Down: " + str(basebotconfig.bBands["Devdn"]),
                    "value": "Devdn",
                },
                {
                    "name": "Rsi Length: " + str(basebotconfig.rsi["RsiLength"]),
                    "value": "RsiLength",
                },
                {
                    "name": "Rsi Buy: " + str(basebotconfig.rsi["RsiOversold"]),
                    "value": "RsiOversold",
                },
                {
                    "name": "Rsi Sell: " + str(basebotconfig.rsi["RsiOverbought"]),
                    "value": "RsiOverbought",
                },
                {
                    "name": "MACD Fast: " + str(basebotconfig.macd["MacdFast"]),
                    "value": "MacdFast",
                },
                {
                    "name": "MACD Slow: " + str(basebotconfig.macd["MacdSlow"]),
                    "value": "MacdSlow",
                },
                {
                    "name": "MACD Signal: " + str(basebotconfig.macd["MacdSign"]),
                    "value": "MacdSign",
                },
                {"name": "All Coins:", "value": "allcoins"},
                {"name": "Changing time interval: ", "value": "setTimeInterval"},
                {"name": "Full autotuning", "value": "fullauto"},
                {"name": "Select Another Bot", "value": "selectanotherbot"},
                {"name": "exit", "value": "exit"},
            ],
        }
    ]
    return questions


def startconfiguring(therange, bot, btinterval):
    while True:
        answers = prompt(selectparametertochange(bot.guid))
        if answers["selectedparameter"] == "interval":
            answers = prompt(savehistory.makepairmenu(bot.guid))
            print(answers)
            history = savehistory.dlhistory(answers, btinterval, 1)
            # history = savehistory.dlhistory(answers, btinterval)
        if answers["selectedparameter"] == "MaType":
            pass
        if answers["selectedparameter"] == "Length":
            tuner.tuneLength(therange, bot.guid, btinterval)
        if answers["selectedparameter"] == "Devup":
            tuner.tuneDevup(therange, bot.guid, btinterval)
        if answers["selectedparameter"] == "Devdn":
            tuner.tuneDevdn(therange, bot.guid, btinterval)
        if answers["selectedparameter"] == "RsiLength":
            tuner.tuneRsiLength(therange, bot.guid, btinterval)
        if answers["selectedparameter"] == "RsiOversold":
            tuner.tuneRsiOversold(therange, bot.guid, btinterval)
        if answers["selectedparameter"] == "RsiOverbought":
            tuner.tuneRsiOverbought(therange, bot.guid, btinterval)
        if answers["selectedparameter"] == "MacdFast":
            tuner.tuneMacdFast(therange, bot.guid, btinterval)
        if answers["selectedparameter"] == "MacdSlow":
            tuner.tuneMacdSlow(therange, bot.guid, btinterval)
        if answers["selectedparameter"] == "MacdSign":
            tuner.tuneMacdSignal(therange, bot.guid, btinterval)
        if answers["selectedparameter"] == "allcoins":
            pass
            # tuner.results = probeallmarkets()
        if answers["selectedparameter"] == "setTimeInterval":
            btinterval = settimeinterval()
        if answers["selectedparameter"] == "fullauto":
            pass
        if answers["selectedparameter"] == "selectanotherbot":
            botnumobj = botsellector.getallcustombots(haasomeClient)
            bot.guid = botnumobj.bot.guid

        if answers["selectedparameter"] == "therange":
            therange = settherange()
        if answers["selectedparameter"] == "exit":
            break

    return answers
