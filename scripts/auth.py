import hmac
import hashlib
import collections
from typing import Dict


    @staticmethod
    def generate_signature(parameters: Dict[str, str], privatekey: str):
        parameter_string = ""

        parameters = collections.OrderedDict(sorted(parameters.items()))

        for key, value in parameters.items():
            parameter_string += "&" + str(key) + "=" + str(value)

        parameter_string = parameter_string.replace("&", "", 1)

        key = bytes(privatekey, 'UTF-8')
        message = bytes(parameter_string, 'UTF-8')

        digester = hmac.new(key, message, hashlib.sha256)
        signature = digester.digest()
        signature = signature.hex().replace("-", "").upper()


http://127.0.0.1:8050/SetupFlashCrashBot?botName=RenamedLocalApi&botGuid=6927d0ac-ee3d-4c6b-ac9c-150e3da136c0&accountGuid=43b1c5f8-31d4-45c0-9163-81b1443146b4&primaryCoin=ETH&secondaryCoin=BTC&fee=0&basePrice=100&priceSpreadType=FixedAmount&priceSpread=5&percentageBoost=10&minPercentage=1&maxPercentage=5&amountType=Base&amountSpread=10&sellAmount=0&buyAmount=100&refillDelay=10&fttEnabled=True&fttOffset=10&fttRange=1&fttTimeout=100&safetyTriggerLevel=15&safetyEnabled=True&safetyMoveInOut=True
