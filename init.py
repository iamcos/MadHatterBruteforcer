#Haasonline connect script

import configserver
from haasomeapi.HaasomeClient import HaasomeClient
from haasomeapi.enums.EnumErrorCode import EnumErrorCode
def connect():
	ip, secret = configserver.validateserverdata()
	haasomeClient = HaasomeClient(ip, secret)
	# wallets =  haasomeClient.test_credentials().result

	if haasomeClient.test_credentials().errorCode != EnumErrorCode.SUCCESS:
		return haasomeClient.test_credentials().errorCode, haasomeClient.test_credentials().errorMessage
	else: 
		return ip, secret

def main():
	do = connect().test_credentials()

	print('There are ', len(do.result.values()), 'wallets registerd in the system')
	return do.result

if __name__ == '__main__':
	main()