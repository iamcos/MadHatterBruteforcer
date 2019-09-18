from haasomeapi.HaasomeClient import HaasomeClient
# # ffrom puinquirer import style_from_dict, Token, prompt
# # ffrom puinquirer import Validator, ValidationError
import connectionstring
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
haasomeClient = connectionstring.connectionstring()
def makeaccountsmenu():
	results ={}
	activatedaccounts = haasomeClient.accountDataApi.get_enabled_accounts().result
	options = []

	for k, v in activatedaccounts.items():
		options.append({'Market:': k, 'value': v})
		# print(k, v)
	print(options)
	questions =[{'type': 'list','name': 'selectedpair','message': 'Select pair for backtesting by using your up and down keys',
			'choices': options}]
	# print(questions)
	return questions	


answers = prompt(makeaccountsmenu())


		# wallet = haasomeClient.accountDataApi.get_wallet(key)
		# results[key] = wallet.result
		# print(key,value)
		#	print(wallet)

		# print(activatedaccounts)
	# help(activatedaccounts)