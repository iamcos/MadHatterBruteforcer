from haasomeapi.enums.EnumFlashSpreadOptions import EnumFlashSpreadOptions
from haasomeapi.HaasomeClient import HaasomeClient
import configserver
ip, secret = configserver.validateserverdata()
haasomeClient = HaasomeClient(ip, secret)
def getallcustombots(haasomeClient):
  allbots = haasomeClient.customBotApi.get_all_custom_bots().result
  for i, x in enumerate(allbots):
        print(i, x.name, 'ROI : ',x.roi) #bottypedict[x.botType] to bring bot type into view
  botnum = input(
    'Type bot number to use from the list above and hit return. \n Your answer: ')
  try:
    botnumobj = allbots[int(botnum)]
  except ValueError:
     botnum = input(
    'Wrong symbol. Can only use numbers. Type bot number indecated at the start of the string here: ')
  except IndexError: 
    botnum = input(
    'Bot number is out of range. Type the number that is present on the list and hit enter: ')
  finally:
    botnumobj = allbots[int(botnum)]
  print(botnumobj.name +'is selected!')
  return botnumobj

def getallmhbots(haasomeClient):
    everybot = haasomeClient.customBotApi.get_all_custom_bots().result
    allmhbots = []
    for i, x in enumerate(everybot):
        if x.botType == 15:
          allmhbots.append(x)
    for i, x in enumerate(allmhbots): 
      print(i, x.name, 'ROI : ',x.roi,'with ', len(x.completedOrders),' trades')
    botnum = input(
  'Type bot number to use from the list above and hit return. \n Your answer: ')
    try:
      botnumobj = allmhbots[int(botnum)]
    except ValueError:
      botnum = input(
      'Wrong symbol. Can only use numbers. Type bot number indecated at the start of the string here: ')
    except IndexError: 
      botnum = input(
      'Bot number is out of range. Type the number that is present on the list and hit enter: ')
    finally:
      botnumobj = allmhbots[int(botnum)]
    print('Bot ', botnumobj.name + ' is selected!')
    return botnumobj

def getallfcbots(haasomeClient):
    everybot = haasomeClient.customBotApi.get_all_custom_bots().result
    allbots = []
    for i, x in enumerate(everybot):
        if x.botType == 6:
          allbots.append(x)
    for i, x in enumerate(allbots): 
      print(i, x.name, 'ROI : ',x.roi,'with ', len(x.completedOrders),' trades and PriceSpreadType: ', x.priceSpreadType, EnumFlashSpreadOptions(x.priceSpreadType))
    botnum = input(
  'Type bot number to use from the list above and hit return. \n Your answer: ')
    try:
      botnumobj = allbots[int(botnum)]
    except ValueError:
      botnum = input(
      'Wrong symbol. Can only use numbers. Type bot number indecated at the start of the string here: ')
    except IndexError: 
      botnum = input(
      'Bot number is out of range. Type the number that is present on the list and hit enter: ')
    finally:
      botnumobj = allbots[int(botnum)]
    print('Bot ', botnumobj.name + ' is selected!')
    return botnumobj

def getalltradebots(haasomeClient):
    everybot = haasomeClient.tradeBotApi.get_all_trade_bots().result
    for i, x in enumerate(everybot): 
      print(i, x.name, 'with ROI : ',x.roi,'with ', len(x.completedOrders),' trades with indicators ', len(x.indicators), )
    botnum = input(
  'Type bot number to use from the list above and hit return. \n Your answer: ')
    try:
      botnumobj = everybot[int(botnum)]
    except ValueError:
      botnum = input(
      'Wrong symbol. Can only use numbers. Type bot number indecated at the start of the string here: ')
    except IndexError: 
      botnum = input(
      'Bot number is out of range. Type the number that is present on the list and hit enter: ')
    finally:
      botnumobj = everybot[int(botnum)]
    print('Bot ', botnumobj.name + ' is selected!')
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
  if len(everybot) ==0:
    print('\nThere are no Custom Bots and No Tradebots.')
  else:
    for i, x in enumerate(everybot): 
      print(i, x.name)
    botnum = input(
  'Type bot number to use from the list above and hit return. \n Your answer: ')
    try:
      botnumobj = everybot[int(botnum)]
    except ValueError:
      botnum = input(
      'Wrong symbol. Can only use numbers. Type bot number indecated at the start of the string here: ')
    except IndexError: 
      botnum = input(
      'Bot number is out of range. Type the number that is present on the list and hit enter: ')
    finally:
      botnumobj = everybot[int(botnum)]
    print('Bot ', botnumobj.name + ' is selected!')
    return botnumobj

def main():
  bot = getallbots(haasomeClient)

if __name__ == '__main__':
  main()
