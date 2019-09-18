## Script returns lists of trading pairs with primaryCurrency, secondaryCurrency, contractName, minimumTradeAmount, tradeFee information.
from haasomeapi.enums.EnumPriceSource import EnumPriceSource
from haasomeapi.HaasomeClient import HaasomeClient
# # ffrom puinquirer import (Token, ValidationError, Validator, prompt,
                        style_from_dict)

import botsellector

import settimeinterval
import init
import configparser
import configserver

ip, secret = init.connect()
haasomeClient = HaasomeClient(ip, secret)

def select_account():
    marketsdict = {'BITFINEX' : 1,'BTCE' : 4,'CEXIO' : 5,'OKCOINCOM' : 8,'OKCOINFUTURES' : 9,'BITSTAMP' : 10,'POLONIEX' : 11,'COINBASE' : 12,'BITTREX' : 13,'NOVAEXCHANGE' : 14,'KRAKEN' : 15,'BITMEX' : 17,'SCRIPTEDDRIVER' : 18,'CCEX' : 19,'GEMINI' : 20,'BINANCE' : 21,'HITBTC' : 22,'OKEX' : 23,'HUOBI' : 26,'KUCOIN' : 27,'DERIBIT' : 28}
    marketsdict2 = {'1' : 'BITFINEX', 4 : 'BTCE', 5 : 'CEXIO', 8 : 'OKCOINCOM', 9 : 'OKCOINFUTURES', 10 : 'BITSTAMP', 11 : 'POLONIEX', 12 : 'COINBASE', 13 : 'BITTREX', 14 : 'NOVAEXCHANGE', 15 : 'KRAKEN', 17 : 'BITMEX', 18 : 'SCRIPTEDDRIVER', 19 : 'CCEX', 20 : 'GEMINI', 21 : 'BINANCE', 22 : 'HITBTC', 23 : 'OKEX', 26 : 'HUOBI', 27 : 'KUCOIN', 28 : 'DERIBIT'}

    allaccounts = haasomeClient.accountDataApi.get_enabled_accounts().result
    print(allaccounts)
    guid_enum = []
    guid_name = haasomeClient.marketDataApi.get_enabled_price_sources().result


    for i in guid_name:
        guid_enum.append(marketsdict[str.upper(i)])
        print(marketsdict[str.upper(i)])


    markets = [{
            'type': 'list',
            'name': 'selectedaccount',
            'message': 'Select account',
            'choices': guid_name}]

    market = prompt(markets)
    marketupper = str.upper(market['selectedaccount'])
    selecetdaccountmarkets = []
    allmarkets = haasomeClient.marketDataApi.get_price_markets(marketsdict[marketupper]).result
    


    for v in allmarkets:
        # selecetdaccountmarkets.append([{'name': [v.primaryCurrency, v.secondaryCurrency]}])
        selecetdaccountmarkets.append([v.primaryCurrency, v.secondaryCurrency, v.contractName, v.minimumTradeAmount, v.tradeFee])
        print(v.primaryCurrency, v.secondaryCurrency)
    # print(selecetdaccountmarkets[0])
    return marketupper, selecetdaccountmarkets

one, hey = select_account()
