from haasomeapi.enums.EnumFlashSpreadOptions import EnumFlashSpreadOptions
from haasomeapi.HaasomeClient import HaasomeClient
import configserver
import init
import re

def getallcustombots(haasomeClient):
    allbots = haasomeClient.customBotApi.get_all_custom_bots().result
    for i, x in enumerate(allbots):
        print(
            i, x.name, "ROI : ", x.roi
        )  # bottypedict[x.botType] to bring bot type into view
    botnum = input(
        "Type bot number to use from the list above and hit return. \n Your answer: "
    )
    try:
        botnumobj = allbots[int(botnum)]
    except ValueError:
        botnum = input(
            "Wrong symbol. Can only use numbers. Type bot number indecated at the start of the string here: "
        )
    except IndexError:
        botnum = input(
            "Bot number is out of range. Type the number that is present on the list and hit enter: "
        )
    finally:
        botnumobj = allbots[int(botnum)]
    print(botnumobj.name + "is selected!")
    return botnumobj


def return_all_mh_bots(haasomeClient):
    everybot = haasomeClient.customBotApi.get_all_custom_bots().result
    allmhbots = []
    for i, x in enumerate(everybot):
        if x.botType == 15:
            allmhbots.append(x)
    print('there are ', len(allmhbots), 'Mad Hatter Bots in total \n')
    return allmhbots

def get_specific_bot(haasomeClient,botlist):
    
    for i, x in enumerate(botlist):
        print(i, x.name, "ROI : ", x.roi, "with ", len(x.completedOrders), " trades")
    botnum = input(
        "Type bot number to use from the list above and hit return. \n Your answer: "
    )
    try:
        botnumobj = botlist[int(botnum)]
    except ValueError:
        botnum = input(
            "Wrong symbol. Can only use numbers. Type bot number indecated at the start of the string here: "
        )
    except IndexError:
        botnum = input(
            "Bot number is out of range. Type the number that is present on the list and hit enter: "
        )
    finally:
        botnumobj = botlist[int(botnum)]
   
    print("Bot ", botnumobj.name + " is selected!")
    return botnumobj
    
def get_mh_bot(haasomeClient):
    all_mh_bots = return_all_mh_bots(haasomeClient)
    bot = get_specific_bot(haasomeClient,all_mh_bots)
    return bot

def get_trade_bot(haasomeClient,):
    all_trade_bots = return_all_trade_bots(haasomeClient)
    bot = get_specific_bot(haasomeClient,all_trade_bots)
    return bot

def return_all_fcb_bots(haasomeClient):
    everybot = haasomeClient.customBotApi.get_all_custom_bots().result
    allbots = []
    for i, x in enumerate(everybot):
        if x.botType == 6:
            allbots.append(x)
    for i, x in enumerate(allbots):
        print(
            i,
            x.name,
            "ROI : ",
            x.roi,
            "with ",
            len(x.completedOrders),
            " trades and PriceSpreadType: ",
            x.priceSpreadType,
            EnumFlashSpreadOptions(x.priceSpreadType),
        )
    return allbots

def return_all_trade_bots(haasomeClient):
    allbots = haasomeClient.tradeBotApi.get_all_trade_bots().result
    # for i, x in enumerate(allbots):
    #     print(
    #         i,
    #         x.name,
    #         "with ROI : ",
    #         x.roi,
    #         "with ",
    #         len(x.completedOrders),
    #         " trades with indicators ",
    #         len(x.indicators),
    #     )
    return allbots

def getallmhbots(haasomeClient):
    everybot = haasomeClient.customBotApi.get_all_custom_bots().result
    allmhbots = []
    for i, x in enumerate(everybot):
        if x.botType == 15:
            allmhbots.append(x)
    for i, x in enumerate(allmhbots):
        print(i, x.name, "ROI : ", x.roi, "with ", len(x.completedOrders), " trades")
    botnum = input(
        "Type bot number to use from the list above and hit return. \n Your answer: "
    )
    try:
        botnumobj = allmhbots[int(botnum)]
    except ValueError:
        botnum = input(
            "Wrong symbol. Can only use numbers. Type bot number indecated at the start of the string here: "
        )
    except IndexError:
        botnum = input(
            "Bot number is out of range. Type the number that is present on the list and hit enter: "
        )
    finally:
        botnumobj = allmhbots[int(botnum)]
    print("Bot ", botnumobj.name + " is selected!")
    return botnumobj

def gets_pecific_mh_bot_list(haasomeClient):
    everybot = haasomeClient.customBotApi.get_all_custom_bots().result
    allmhbots = []
    for i, x in enumerate(everybot):
        if x.botType == 15:
            if x.name.startswith('Tune'):
                allmhbots.append(x)
    print('There are ', len(allmhbots), 'in qeue with each having top 3 best results recreated as bots.')
    return allmhbots

def getallfcbots(haasomeClient):
    everybot = haasomeClient.customBotApi.get_all_custom_bots().result
    allbots = []
    for i, x in enumerate(everybot):
        if x.botType == 6:
            allbots.append(x)
    for i, x in enumerate(allbots):
        print(
            i,
            x.name,
            "ROI : ",
            x.roi,
            "with ",
            len(x.completedOrders),
            " trades and PriceSpreadType: ",
            x.priceSpreadType,
            EnumFlashSpreadOptions(x.priceSpreadType),
        )
    botnum = input(
        "Type bot number to use from the list above and hit return. \n Your answer: "
    )
    try:
        botnumobj = allbots[int(botnum)]
    except ValueError:
        botnum = input(
            "Wrong symbol. Can only use numbers. Type bot number indecated at the start of the string here: "
        )
    except IndexError:
        botnum = input(
            "Bot number is out of range. Type the number that is present on the list and hit enter: "
        )
    finally:
        botnumobj = allbots[int(botnum)]
    print("Bot ", botnumobj.name + " is selected!")
    return botnumobj


def getalltradebots(haasomeClient):
    everybot = haasomeClient.tradeBotApi.get_all_trade_bots().result
    for i, x in enumerate(everybot):
        print(
            i,
            x.name,
            "with ROI : ",
            x.roi,
            "with ",
            len(x.completedOrders),
            " trades with indicators ",
            len(x.indicators),
        )
    botnum = input(
        "Type bot number to use from the list above and hit return. \n Your answer: "
    )
    try:
        botnumobj = everybot[int(botnum)]
    except ValueError:
        botnum = input(
            "Wrong symbol. Can only use numbers. Type bot number indecated at the start of the string here: "
        )
    except IndexError:
        botnum = input(
            "Bot number is out of range. Type the number that is present on the list and hit enter: "
        )
    finally:
        botnumobj = everybot[int(botnum)]
    print("Bot ", botnumobj.name + " is selected!")
    return botnumobj


def botlist(haasomeClient):
    allbots = haasomeClient.customBotApi.get_all_custom_bots().result
    return allbots


def getallbots(haasomeClient):
    everybot = []
    custombots = haasomeClient.customBotApi.get_all_custom_bots().result
    for x in custombots:
        everybot.append(x)
    tradebots = haasomeClient.tradeBotApi.get_all_trade_bots().result
    for x in tradebots:
        everybot.append(x)
    if len(everybot) == 0:
        print("\nThere are no Custom Bots and No Tradebots.")
    else:
        for i, x in enumerate(everybot):
            print(i, x.name)
        botnum = input(
            "Type bot number to use from the list above and hit return. \n Your answer: "
        )
        try:
            botnumobj = everybot[int(botnum)]
        except ValueError:
            botnum = input(
                "Wrong symbol. Can only use numbers. Type bot number indecated at the start of the string here: "
            )
        except IndexError:
            botnum = input(
                "Bot number is out of range. Type the number that is present on the list and hit enter: "
            )
        finally:
            botnumobj = everybot[int(botnum)]
        print("Bot ", botnumobj.name + " is selected!")
        return botnumobj


def main():
    haasomeClient = init.connect()
    bot = gets_pecific_mh_bot_list(haasomeClient)


if __name__ == "__main__":
    main()
