import configparser
import sys
import re
import os
from haasomeapi.HaasomeClient import HaasomeClient
from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot
from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot
import haasomeapi.apis.CustomBotApi as customBotApi
import datetime


#Commands to store local api login data and modify it in case of inability to connect to haas is here

def makeconfigfile():
    config = configparser.ConfigParser()
    config["SERVER DATA"] = {
        "server_ip": "EnterIPHere",
        "server_port": 8095,
        "secret": 123,
    }
    with open("config.ini", "w") as configfile:
        config.write(configfile)



def writeconfigfile(ip, port, secret):
    #Write config data to config file
    config = configparser.ConfigParser()
    config["SERVER DATA"] = {"server_ip": ip, "server_port": port, "secret": secret}
    config["CONNECTIONSTRING"] = {"ip": "http://" + ip + ":" + port, "secret": secret}
    with open("config.ini", "w") as configfile:
        config.write(configfile)


def verifyconfigfile():
    #asks to readd data to a config file in case of failure to connect to haas
    config = configparser.ConfigParser()
    config.sections()
    try:
        config.read("config.ini")
    except FileNotFoundError:
        makeconfigfile()
    defaultip = "EnterIPHere"
    try:
        serverdata = config["SERVER DATA"]
    except KeyError:
        iniciate()
    ip = serverdata.get("server_ip")
    port = serverdata.get("server_port")
    server = ip + ":" + portsel
    secret = serverdata.get("secret")

    # interval = variables.get('interval')

    if ip == defaultip or ip == " " or ip == "":
        print("Server is not set up. Lets set it up!")
        getserverdata()

    elif ip != defaultip or ip != " " or ip != "":

        print(
            "Mad-Hatter Bot Rotator script by Cosmos \n Two things thing to do first! \n\n Firstly configure Local API. This is done Haasonline Settings at the bottom left menu. \nThere you need to manually input all 3 fields: ip, port and third one Key. Key is the secret. \nIf you are planing to run Rotator on the same machine as Haasonline, then ip can be set to 127.0.0.1. \nMy port preference is 8095. \nYou must type each field even though there may already be something in it written as example. \nFor Secret or Key you should only use numbers and letters and avoid special characters.\n Once done hit safe. Once interface refresh go back there and check if all the fields you just editet are not empty, but contain ip, port and password.Select or create new Mad Hatter bot and configure market, time interval, trade ammount and hit safe. \n\n Once done, do a few backtests for different time intervals by hand using the BT remote that can be found at the top right corner, first icon from left. \n\n\n Current Server data is:\n IP: ",
            ip,
            "PORT: ",
            port,
            "SECRET",
            secret,
            "\n\n Type Y if correct, N if you want to change server data now now.\n Your response: ",
        )
        user_resp = sys.stdin.read(1)
        if user_resp == "Y" or user_resp == "y":
            print("Server is set up!")
        elif user_resp == "N" or user_resp == "n":
            getserverdata()


def connectiondata():
    #older way of returning local api connection string
    config = configparser.ConfigParser()
    config.sections()
    config.read("config.ini")
    connectionstring = config["CONNECTIONSTRING"]
    # interval = variables.get('interval')
    ip = connectionstring.get("ip")
    secret = connectionstring.get("secret")
    print(ip, secret)
    return ip, secret


def main():
    verifyconfigfile()


def iniciate():
    # makeconfigfile()
    #iniciates createion and population of the config file
    print(
        "Config file config.ini, has just been created. If you havent already done so, go to HTS settings, local api page and maually enter ip, port and secret, hit save below. If you are running this app on the same machine you are running HTS server, then ip can be set to 127.0.0.1 and port to 9000. Secret in this case can be a simple one too because its all done locally"
    )
    print("Type Y and hit return when ready to input server data.")
    getserverdata()

def intervals():
    #contains time intervals dictionary for backtesting periods in minutes. Not used.
      intervals = {
        "1H": 60,
        "2H": 120,
        "3H": 180,
        "4H": 240,
        "5H": 300,
        "6H": 360,
        "7H": 420,
        "8H": 480,
        "9H": 540,
        "10H": 600,
        "11H": 660,
        "12H": 720,
        "13H": 780,
        "14H": 840,
        "15H": 900,
        "16H": 960,
        "17H": 1020,
        "18H": 1080,
        "19H": 1140,
        "20H": 1200,
        "21H": 1260,
        "22H": 1320,
        "23H": 1380,
        "24H": 1440,
        "1D": 1440,
        "2D": 2880,
        "3D": 4320,
        "4D": 5760,
        "5D": 7200,
        "6D": 8640,
        "7D": 10080,
        "8D": 11520,
        "9D": 12960,
        "10D": 14400,
        "11D": 15840,
        "12D": 17280,
        "13D": 18720,
        "14D": 20160,
        "15D": 21600,
        "16D": 23040,
        "17D": 24480,
        "18D": 25920,
        "19D": 27360,
        "20D": 28800,
        "21D": 30240,
        "22D": 31680,
        "23D": 33120,
        "24D": 34560,
        "25D": 36000,
        "26D": 37440,
        "27D": 38880,
        "28D": 40320,
        "29D": 41760,
        "30D": 43200,
    }

def getserverdata():
    #get haasomeapi ip, port and secret for further storage.
  
    ip = input("Write server ip here (example 127.0.0.1):")
    print(ip, " stored in config as ip")
    port = input("Write server port here (example 8095):")
    print(port, " stored as port number")
    secret = input("WWrite server secret here (example fkass): ")
    print(secret, " stored as secret")

    writeconfigfile(ip, port, secret)
