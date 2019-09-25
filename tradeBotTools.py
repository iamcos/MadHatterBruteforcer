def del_duplicate_indicators(bot):
	indicators = []
	types = []
	copies = []
	short_names = []

	for guid in bot.indicators:
		short_names.append(bot.indicators[guid].indicatorTypeShortName)
		types.append([bot.indicators[guid].indicatorType])
		indicators.append([bot.indicators[guid].indicatorType, guid])
	for i, v in enumerate(types):
			# print(i[0])
			if types.count(v) > 1:
						copies.append(indicators[i])
						
	# del sorted(copies)[::2]
	
	copies = sorted(copies)[::2]
	if len(copies) > 0:
		for i in copies:
			d= 	haasomeClient.tradeBotApi.remove_indicator(bot.guid, i[1])
			print('deleted ',bot.indicators[i[1]].indicatorTypeShortName, d.errorCode, d.errorMessage)
	else: 
		print('Current bot has no duplicating indicators')

def show_missing_indicators(bot):
	short_names = []
	for guid in bot.indicators:
		short_names.append(bot.indicators[guid].indicatorTypeFullName)
	li_diff =set(short_names) ^ set(all_indicators_names.all_indicators_names)
	print('Indicators not in bot:')
	for i in li_diff:
		print(i)