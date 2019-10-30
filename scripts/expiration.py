from datetime import datetime, date
import sys

# datet = '2019-8-27'
def setexpiration(expiration):
    ExpirationDate = datetime.strptime(expiration, "%Y-%m-%d").date()
    now = date.today()
    if ExpirationDate >= now:
        print("Expiration date for this script set to", expiration)
        print("Enjoy")
    else:
        sys.exit()
