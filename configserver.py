from __future__ import print_function, unicode_literals
from haasomeapi.HaasomeClient import HaasomeClient
from haasomeapi.enums.EnumErrorCode import EnumErrorCode


import configparser
import os
import re
import sys

import time


import init



def serverdata():

    ip = input('Type Server IP address: ')
    port = input('Type server port number: ')
    secret = input('Type api key: ')

    ipport = 'http://'+ip+':'+port

    config = configparser.ConfigParser()
    config['SERVER DATA'] = {'server_address': ipport, 'secret': secret}
    with open('config.ini', 'w') as configfile:
								config.write(configfile)
    return ipport, secret


				
def validateserverdata():
    ipport = ''
    secret = ''

    config = configparser.ConfigParser()
    config.sections()
    
    try:
        config.read('config.ini')
        logindata = config['SERVER DATA']
        ipport = logindata.get('server_address')
        secret = logindata.get('secret')
        print(ipport, secret)
        haasomeClient = HaasomeClient(ipport, secret)
        if haasomeClient.test_credentials().errorCode != EnumErrorCode.SUCCESS:
            print('\n\n\n\n\n\n\n\n')
            print(haasomeClient.test_credentials().errorMessage)
            print('\nHave you enabled Local API in Haasonline Server Settings? \nIMPORTANT: IP, PORT should have the same data as here, secret must show dots. \nIf there are no dots in Secret, input them and hit SAVE button at the bottom of the page. \n')
            serverdata()
        else: 
            print('\n\n\n\n\n\n\n\n')
            print('Sucessfully connected to HaasOnline!')
            return ipport, secret
    except KeyError:
        serverdata()
    except FileNotFoundError:
        currentfile = Path(str('config.ini'))
        currentfile.touch(exist_ok=True)
        print('Config has been created!')
    
   
        config.read('config.ini')
        logindata = config['SERVER DATA']
        ipport = logindata.get('server_address')
        secret = logindata.get('secret')
    return ipport, secret

def set_bt():
	
    year = input('Write year in 4 digits format: ')
    month = input('write month as 1 to 9, 10 to 12: ')
    day = input('write day as 1-9, 10-31: ')

    config = configparser.ConfigParser()
    config['BT'] = {'year': year, 'month': month,'day': day}
    with open('bt.ini', 'w') as configfile:
								config.write(configfile)
    return year, month, day

def read_bt():
    config = configparser.ConfigParser()
    try:
        config.read('bt.ini')
    except FileNotFoundError:
        currentfile = Path(str('bt.ini'))
        currentfile.touch(exist_ok=True)
        set_bt()
    dd = config['BT']
    year = dd.get('year')
    month = dd.get('month')
    day = dd.get('day')
    return year, month, day
    

def main():
    set_bt()


if __name__ == '__main__':
	main()