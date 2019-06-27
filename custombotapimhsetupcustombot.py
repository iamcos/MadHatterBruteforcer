def setup_mad_hatter_bot2(self, botName: str, botGuid: str, accountGuid: str, primaryCoin: str, secondaryCoin: str, contractName: str, leverage: str, templateGuid: str, position: str, fee: float, tradeAmountType:  EnumBotTradeAmount, tradeAmount: float, useconsensus:bool, disableAfterStopLoss: bool,
                             interval: int, includeIncompleteInterval: bool, mappedBuySignal: EnumFundPosition, mappedSellSignal: EnumFundPosition):
        """ Modify Mad Hatter bot

        :param botGuid: str: Custom bot guid
        :param botName: str: Name for the new custom bot
        :param accountGuid: str: Account guid
        :param primaryCoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondaryCoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param contractName: str: Contract name (Optional)
        :param tradeAmountType: :class:`~haasomeapi.enums.EnumBotTradeAmount` Trade amount type
        :param tradeamount: float: Trade amount to use
        :param leverage: float: Leverage percentage to use (Optional)
        :param fee: float: Fee percentage to be used in calculations
        :param templateGuid: str: templateguid
        :param position: str: Position bot should start in EX. For BNB/BTC if you have no BNB set to BTC
        :param useconsensus: bool: Enable Consensus Mode
        :param disableAfterStopLoss: bool: Disable bot after stop loss
        :param interval: int: Price Ticker Minute Interval. Ex. 1,2,3,,5,15,30, etc
        :param includeIncompleteInterval: bool: Allow a incomplete price ticker

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.MadHatterBot`: Mad Hatter bot object
        """

        response = super()._execute_request("/SetupMadHatterBot",  {"botGuid": botGuid,
                                                                    "botName": botName,
                                                                    "accountGuid": accountGuid,
                                                                    "primaryCoin": primaryCoin,
                                                                    "secondaryCoin": secondaryCoin,
                                                                    "contractName": contractName,
                                                                    "tradeAmountType": str(EnumBotTradeAmount(tradeAmountType).value),
                                                                    "tradeAmount": float(str(tradeAmount).replace(',', '.')),
                                                                    "leverage": float(str(leverage).replace(',', '.')),
                                                                    "fee": float(str(fee).replace(',', '.')),
                                                                    "templateGuid": templateGuid,
                                                                    "position": position,
                                                                    "useTwoSignals": str(useconsensus).lower(),
                                                                    "disableAfterStopLoss": str(disableAfterStopLoss).lower(),
                                                                    "interval": interval,
                                                                    "includeIncompleteInterval": str(includeIncompleteInterval).lower(),
                                                                    "mappedBuySignal": str(EnumFundPosition(mappedBuySignal).value),
                                                                    "mappedSellSignal": str(EnumFundPosition(mappedSellSignal).value
                                                                    )
                                                                   })
        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.MAD_HATTER_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})