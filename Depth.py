#!/usr/bin/env python3

import krakenex
import decimal
import http

class Depth:
    def __init__(self, kApi, pair):
        self._kApi = kApi
        self._pair = pair
        self.update()

    def update(self):
        try:
            self._ret = self._kApi.query_public('Depth', {'pair': self._pair})
        except (http.client.HTTPException) as e:
            print(e.args[0])

    def getAskPrice(self, count):
        return(decimal.Decimal(self._ret['result'][self._pair]['asks'][count][0]))

    def getAskVolume(self, count):
        return(decimal.Decimal(self._ret['result'][self._pair]['asks'][count][1]))

    def getBidPrice(self, count):
        return(decimal.Decimal(self._ret['result'][self._pair]['bids'][count][0]))

    def getBidVolume(self, count):
        return(decimal.Decimal(self._ret['result'][self._pair]['bids'][count][1]))


    def pritnData(self):
        print(str(self._ret))