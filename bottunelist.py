
import haasomeapi.enums.EnumErrorCode as EnumErrorCode
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
from haasomeapi.HaasomeClient import HaasomeClient
# ffrom puinquirer import (Token, ValidationError, Validator, prompt,
                        style_from_dict)
from haasomeapi.enums.EnumMadHatterIndicators import EnumMadHatterIndicators
from haasomeapi.enums.EnumMadHatterSafeties import EnumMadHatterSafeties
import accpairsdata
import botsellector
import connectionstring
import settimeinterval
import getbots
import re

  
haasomeClient = connectionstring.connectionstring()

selectedbots =getbots.getbotlist(haasomeClient)

for bot in selectedbots:
 basebotconfig = haasomeClient.customBotApi.get_custom_bot(bot.guid, EnumCustomBotType.BASE_CUSTOM_BOT).result
 bbLength = basebotconfig.bBands['Length']
 bbDevUp = basebotconfig.bBands['Devup']
 bbDevDown = basebotconfig.bBands['Devdn']
 bbMAType = basebotconfig.bBands['MaType']
 bbDeviation = basebotconfig.bBands['Deviation']
 bbResetMid = basebotconfig.bBands['ResetMid']
 bbMidSells = basebotconfig.bBands['AllowMidSell']
 bbFcc = basebotconfig.bBands['RequireFcc']
 #rsi stuff
 rl = basebotconfig.rsi['RsiLength']
 rs = basebotconfig.rsi['RsiOversold']
 rb = basebotconfig.rsi['RsiOverbought']
 #macd stuff
 mdf = basebotconfig.macd['MacdFast']
 mds = basebotconfig.macd['MacdSlow']
 mdsi = basebotconfig.macd['MacdSign']
 