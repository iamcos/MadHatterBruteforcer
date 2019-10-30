def create_roi_set():
		roi_set = { '0': 0, '1': 0, '2': 0, '3': 0, '4':0, '5':0}
		return roi_set
	
def update_roi_set(roi_set, roi):

	# def takechangegive(first, second):


	roi_set['5']=roi_set['4']
	roi_set['4']=roi_set['3']	
	roi_set['3']=roi_set['2']
	roi_set['2'] = roi_set['1']
	roi_set['1'] = roi_set['0']
	roi_set['0']= roi
	return roi_set


def getdifference(roi_set):

	diff_set = {'0-1': 0, '1-2': 0, '2-3': 0, '3-4': 0, '4-5':0,}

	diff_set['0-1'] = roi_set['1']-roi_set['0']
	diff_set['1-2'] = roi_set['2']-roi_set['1']
	diff_set['2-3'] = roi_set['3']-roi_set['2']
	diff_set['3-4'] = roi_set['4']-roi_set['3']
	diff_set['4-5'] = roi_set['5']-roi_set['4']

	return diff_set

def decision_maker(diff_set):
	if diff_set['3-4'] == diff_set['2-3'] and  diff_set['2-3'] == diff_set['1-2'] and diff_set['1-2'] == diff_set['2-3']:
		pass

def countsuccess(diff_set):
	succesful = 0
	zero = 0
	negative = 0
	if diff_set['0-1'] > 0:
		sucessful += 1
	if diff_set['0-1'] == 0 and sucessful > 0: #or diff_set['0-1'] == 0.0 
		zero +=1
	if diff_set['0-1'] < 0: 
		negative += 1
	if zero == 2:
		print('ROI zero 3rd time in a row. Need to change something')
		zero == 0
	if succesful == 1:
		print('Roi keeps increasing...')
	if negative == 2:
			switcparameter
	if zero == 4:
		print('Something wrong, RSI Length will be lowered untill we find ROI')
	if RsiOverBought <= 19:
		print('Increasing Rsi Buy')
	if RsiOverSold >= 76:
			print('Lowering Rsi Buy')


def onetwothree(param, value, indicator):

	new_set = create_roi_set()

	initvalue = value

	if indicator == EnumMadHatterIndicators.BBANDS:
	 if param == 0:
			for x in range(3):
				for x in range(3):
					roi = backtest(butnumobj.guid, EnumMadHatterIndicators, param, value)
					update_roi_set(new_set, roi)
			for x in range(3):


def backtest(guid,indicator, param, value, btinterval):
	basebotconfig = haasomeClient.customBotApi.get_custom_bot(guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
	setparam = haasomeClient.customBotApi.set_mad_hatter_indicator_parameter(
					guid, indicator, param, value)
	bt = haasomeClient.customBotApi.backtest_custom_bot_on_market(basebotconfig.accountId, basebotconfig.guid,btinterval,basebotconfig.priceMarket.primaryCurrency, basebotconfig.priceMarket.secondaryCurrency, basebotconfig.priceMarket.contractName)
	btr = bt.results
	roi = btr.roi
	return roi





new_set = create_roi_set()

for x in range(5):
	new_set = update_roi_set(new_set, x)

print(new_set)
diff = getdifference(new_set)


print(diff)