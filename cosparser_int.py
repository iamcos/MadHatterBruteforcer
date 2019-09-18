
import configparser
import sys
import re
import os
from haasomeapi.HaasomeClient import HaasomeClient
from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot
from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot
import haasomeapi.apis.CustomBotApi as customBotApi
import datetime


import regex

from pprint import pprint
# ffrom puinquirer import style_from_dict, Token, prompt
# ffrom puinquirer import Validator, ValidationError


style = style_from_dict({
				Token.QuestionMark: '#E91E63 bold',
				Token.Selected: '#673AB7 bold',
				Token.Instruction: '',  # default
				Token.Answer: '#2196f3 bold',
				Token.Question: '',
})


class PhoneNumberValidator(Validator):
				def validate(self, document):
								ok = regex.match(
												'^([01]{1})?[-.\s]?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})\s?((?:#|ext\.?\s?|x\.?\s?){1}(?:\d+)?)?$', document.text)
								if not ok:
												raise ValidationError(
																message='Please enter a valid phone number',
																cursor_position=len(document.text))  # Move cursor to end


class NumberValidator(Validator):
				def validate(self, document):
								try:
												int(document.text)
								except ValueError:
												raise ValidationError(
																message='Please enter a number',
																cursor_position=len(document.text))  # Move cursor to end


def makeconfigfile():
				config = configparser.ConfigParser()
				config['SERVER DATA'] = {'server_ip': 'EnterIPHere', 'server_port': 8095,
																													'secret': 123}
				with open('config.ini', 'w') as configfile:
								config.write(configfile)


def ipvalidate():
				re.findall('\b(?:[1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-2][0-3])\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-5][0-5])\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-5][0-5])\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-5][0-5])\b', ip)


def writeconfigfile(ip, port, secret):
				config = configparser.ConfigParser()
				config['SERVER DATA'] = {'server_ip': ip,'server_port': port, 'secret': secret}
				config['CONNECTIONSTRING'] = {
								'ip': 'http://'+ip+':'+port, 'secret': secret}
				with open('config.ini', 'w') as configfile:
								config.write(configfile)


def checklogindata():
				data_promt = {
								'type': 'confirm',
								'name': 'serverdata',
								'message': 'Would you like to change server data?',
								'default': True
				}
				answers = prompt(data_promt)
				return answers['serverdata']


def validateData():
				data_response = checklogindata()
				if (data_response == 'ip'):
								print('type new ip here now: ')
								newip = {
												'type': 'input',
												'name': 'newip',
								}
								print('There is a wolf in front of you; a friendly looking dwarf to the right and an impasse to the left.')
								encounter1()
				else:
								print('You cannot go that way. Try again')
								exit_house()


def verifyconfigfile():
				config = configparser.ConfigParser()
				config.sections()
				try:
								config.read('config.ini')
				except FileNotFoundError:
							getserverdata()
				
				# port = serverdata.get('server_port')
				# server = ip + ':' + port
				# secret = serverdata.get('secret')

				# interval = variables.get('interval')

				# if ip == defaultip or ip == " " or ip == "":
				# 				print('Server is not set up. Lets set it up!')
				# 				getserverdata()

				# elif ip != defaultip or ip != " " or ip != "":
				# 	getserverdata()


def connectiondata():
				config = configparser.ConfigParser()
				config.sections()
				config.read('config.ini')
				connectionstring = config['CONNECTIONSTRING']
				# interval = variables.get('interval')
				ip = connectionstring.get('ip')
				secret = connectionstring.get('secret')
				print(ip, secret)
				return ip, secret


def main():
				verifyconfigfile()


def iniciate():
				# makeconfigfile()
				print('Config file config.ini, has just been created. If you havent already done so, go to HTS settings, local api page and maually enter ip, port and secret, hit save below. If you are running this app on the same machine you are running HTS server, then ip can be set to 127.0.0.1 and port to 9000. Secret in this case can be a simple one too because its all done locally')
				print('Type Y and hit return when ready to input server data.')
				getserverdata()


def getserverdata():

				newserverdata = prompt[
								prompt({'type': 'input',
									'name': 'ip',
									'message': 'Type new IP:'
									},
								{'type': 'input',
									'name': 'port',
									'message': 'Type port:'
									},
								{'type': 'input',
									'name': 'secret',
									'message': 'Type secret:'
									}
				]
				print(newserverdata)

				# writeconfigfile(newserverdata['ip'], newserverdata['port'], newserverdata['secret'])
				# print(connectiondata())


def storebotdata():
				allbots = customBotApi.get_all_custom_bots().result
				botsettings = ()
				for botconfig in allbots():
								config = configparser.ConfigParser()
								if botconfig.EnumCustomBotType.MAD_HATTER_BOT:
												currentBotGuid = botconfig.guid
												bbands = botconfig.bBands
												rsi = botconfig.rsi
												macd = botconfig.macd
												macddata = macd.indicatorInterface
												rsidata = rsi.indicatorInterface

												# RSI values
												rsi_length = dict(rsidata[0])
												rsi_buy = dict(rsidata[1])
												rsi_sell = dict(rsidata[2])

												# MACD values
												macd_fast = dict(macddata[0])
												macd_slow = dict(macddata[1])
												macd_signal = dict(macddata[2])

												# BBANDS, RSI, MACD fullconfigs in 1 line:
												bbandsconfig = bbands['Length'], bbands['Devup'], bbands['Devdn'], bbands['MaType'], bbands[
																'Deviation'], bbands['ResetMid'], bbands['AllowMidSell'], bbands['RequireFcc']
												rsiconfig = rsi_length['Value'], rsi_buy['Value'], rsi_sell['Value']
												macdconfig = macd_fast['Value'], macd_slow['Value'], macd_signal['Value']
												botindicatorconfig = bbandsconfig, rsiconfig, macdconfig
												botsettings[botguid] = botindicatorconfig
												config[bot.guid] = {botsettings}
												# Writing it all into a single config file
												# config[botconfig.guid] = {'BOT Configuration': ('bbands': bbandsconfig, 'RSI': rsiconfig, 'MACD': macdconfig, 'primaryCurrency' : botconfig.primaryCurrency, 'secondaryCurrency': botconfig.secondaryCurrency )}
												with open('botsdata.ini', 'w') as configfile:
																config.write(configfile)
																print('Bot Settings file has been created')


def addbotstats():
				config = configparser.ConfigParser()
				config.sections()
				config.read('botsdata.ini')
				try:
								botdata = config['BOT ID']
				except:
								storebotdata()
				if botdata.get['GUID'] == currentBotGuid:
								config[botconfig.guid] = config[botconfig.guid].value.append(
												(int(datetime.datetime.utcnow()), roi))

sd = (getserverdata())