from __future__ import print_function, unicode_literals

import configparser
import os
import re
import sys

import regex
from PyInquirer import (Token, ValidationError, Validator, print_json, prompt,
                        style_from_dict)


class ipvalidator(Validator):
    def validate(self, document):
            ok = regex.match('^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$', document.text)
            if not ok:
                raise ValidationError(message='Please enter valid IP. Example: 129.0.0.1', cursor_position=len(document.text))  # Move cursor to end
class portvalidator(Validator):
    def validate(self, document):
            ok = regex.match('^([1-9][0-9]{0,3}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])(-([1-9][0-9]{0,3}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5]))?$', document.text)
            if not ok:
                raise ValidationError(message='Please enter valid PORT. Example: 8095', cursor_position=len(document.text))  # Move cursor to end

def newserverdata():

    questions = [
        {
            'type': 'input',
            'name': 'ip',
            'message': 'Type server IP here:',
            'validate': ipvalidator,

        }, 
        {
            'type': 'input',
            'name': 'port',
            'message': 'Type server PORT here:',
            'validate': portvalidator,

        },
        {
            'type': 'input',
            'name': 'secret',
            'message': 'Type server Secret or API Key here:',

        }
    ]


    serverdata = prompt(questions)
    ip = serverdata['ip']+':'+serverdata['port']
    secret = serverdata['secret']
    print(serverdata['ip'],serverdata['port'], serverdata['secret'])
    config = configparser.ConfigParser()
    config['SERVER DATA'] = {'server_ip': serverdata['ip'],'server_port': serverdata['port'], 'secret': serverdata['secret']}
    config['CONNECTIONSTRING'] = {'ip': 'http://'+serverdata['ip']+':'+serverdata['port'], 'secret': serverdata['secret']}
    with open('config.ini', 'w') as configfile:
								config.write(configfile)
    return ip, secret



				
def validateserverdata():
    user_response = None
    config = configparser.ConfigParser()
    config.sections()
    try:
        config.read('config.ini')
        connectionstring = config['CONNECTIONSTRING']
        ip = connectionstring.get('ip')
        secret = connectionstring.get('secret')
    except KeyError:
        newserverdata()
        config.read('config.ini')
        connectionstring = config['CONNECTIONSTRING']
        ip = connectionstring.get('ip')
        secret = connectionstring.get('secret')
        user_response = input('Is server data correct?')
    if user_response == 'n':
        newserverdata()
    else:
        pass    
    return ip, secret
