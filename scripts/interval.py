from datetime import datetime, date
import configserver


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
    t2 = date(year=year, month=month, day=day)
    t3 = t1 - t2
    t4 = int(t3.total_seconds() / 60 / interval)
    # print(t4, 'ticks with', interval, 'minute resolution')

    return t4


def readinterval(bot):
    
    year, month, day = configserver.read_bt()
    ticks = inticks(int(year), int(month), int(day), bot.interval)
    return ticks

def returninterval():
    interval = 1
    return interval


def main():
    pass


if __name__ == "__main__":
    main()
