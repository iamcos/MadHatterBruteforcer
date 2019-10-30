import re


def getbotlist(haasomeClient):
    templatebots = []
    allbots = haasomeClient.customBotApi.get_all_custom_bots().result
    # print(allbots)
    for bot in allbots:
        if bot.name.startswith("Tune") == True:
            templatebots.append(bot)

    return templatebots
