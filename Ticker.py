#!/usr/bin/env python3

import krakenex
import decimal
import http
import time

class Ticker:
    def __init__(self, kApi, pair, JSONdata=None):
        self._kApi = kApi
        self._pair = pair
        
        if (JSONdata):
            self._currentPrice = decimal.Decimal(JSONdata['result'][self._pair]['c'][0])
            self._bid = decimal.Decimal(JSONdata['result'][self._pair]['b'][0])
            self._ask = decimal.Decimal(JSONdata['result'][self._pair]['a'][0])
        else:
            self.update()

    def __str__(self):
        return self._pair + ': price: ' + str(self._currentPrice) + ' bid: '+ str(self._bid) + ' ask: ' + str(self._bid)

    def update(self):
        try:
            self._ret = self._kApi.query_public('Ticker', {'pair': self._pair})
        except (http.client.HTTPException) as e:
            print(e.args[0])
            time.sleep(1)
            self.update()

        self._currentPrice = decimal.Decimal(self._ret['result'][self._pair]['c'][0])
        self._bid = decimal.Decimal(self._ret['result'][self._pair]['b'][0])
        self._ask = decimal.Decimal(self._ret['result'][self._pair]['a'][0])

    def getCurrentPrice(self):
        return self._currentPrice

    def getBid(self):
        return self._bid

    def getAsk(self):
        return self._ask

    def getPair(self):
        return self._pair

    def printData(self):
        print(self._pair + ': price: ' + str(self._currentPrice) + ' bid: '+ str(self._bid) + ' ask: ' + str(self._bid))

