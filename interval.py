from datetime import datetime, date
def inticks(year, month, day, interval):
	""" Get backtestin ticks in resolution defined in main bot config
	:param year: int: year number
	:param month: int: month number
	:param day: int: day number
	:param interval
	:returns: 
	:int: numbers of ticks in configured bot time interval from defined dat
	"""
	t1 = date.today()
	t2 = date(year = year, month = month, day = day)
	t3 = t1 - t2
	t4 = int(t3.total_seconds()/60/interval)
	print(t4, 'ticks with', interval, 'minute resolution')
	
	return t4
	
def writetickstoconfig():
	

def main():

	inticks(2019,8,1,5)

if __name__ == '__main__':
	main()

