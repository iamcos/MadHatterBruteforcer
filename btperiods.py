
from haasomeapi.HaasomeClient import HaasomeClient
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError
import connectionstring
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
haasomeClient = connectionstring.connectionstring()
import settimeinterval
import csv
from haasomeapi.HaasomeClient import HaasomeClient
import haasomeapi.enums.EnumErrorCode as EnumErrorCode
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError
import connectionstring
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
haasomeClient = connectionstring.connectionstring()
import botsellector
import time
from pathlib import Path
import os.path


# using unix time to define `3 periods to backtest against to make 3 trend strategies
# Strategies will be backtested from time to time to tetermine which one is to use.