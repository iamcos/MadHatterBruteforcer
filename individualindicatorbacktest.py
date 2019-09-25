from haasomeapi.HaasomeClient import HaasomeClient
import botsellector
import configparser_cos
import configserver
import json
import savehistory
from 		haasomeapi.dataobjects.accountdata.BaseOrder import BaseOrder
from datetime import datetime


import plotly.express as px
import pandas as pd
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
ip, secret = configserver.validateserverdata()
haasomeClient = HaasomeClient(ip, secret)

