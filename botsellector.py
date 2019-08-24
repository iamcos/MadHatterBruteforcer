
def botsellector(haasomeClient):
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

