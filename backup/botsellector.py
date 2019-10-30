def botsellector():
	allbots = haasomeClient.customBotApi.get_all_custom_bots().result
	for i, x in enumerate(allbots):
			print(i, x.name)
	botnum = input(
			'Type bot number to use from the list above and hit return. \n Your answer: ')
	botnumobj = allbots[int(botnum)]
	print(botnumobj.name +'is selected!')
	return botnumobj