#!/usr/bin/env python3

import krakenex
import time
import datetime
import decimal
import calendar
import http

class Order:
    def __init__(self, kApi, txid):
        self._kApi = kApi
        self._txid = txid
        self._status = ''
        self._volume = 0.0
        self._volume_exec = 0.0
        self._type = ''
        self._description = ''
        self.update()
    
    def update(self):
        try:
            self._ret = self._kApi.query_private('QueryOrders',
                                            {'txid': self._txid})
        except (http.client.HTTPException) as e:
            print(e.args[0])
            time.sleep(1)
            self.update()

        if (self._ret['error'] != []):
            print(str(self._ret['error']))
        else:
            self._status = self._ret['result'][self._txid]['status']
            self._description = self._ret['result'][self._txid]['descr']['order']
            self._volume = decimal.Decimal(self._ret['result'][self._txid]['vol'])
            self._volume_exec = decimal.Decimal(self._ret['result'][self._txid]['vol_exec'])

    def getStatus(self):
        return self._status

    def getTxid(self):
        return self._txid 

    def getVolume(self):
        return self._volume

    def getVolumeExec(self):
        return self._volume_exec

    def getVolumeOpen(self):
        return self._volume - self._volume_exec

    def print(self):
        if (self._ret['error'] != []):
            print(str(datetime.datetime.now()) + ' ' + str(self._txid) + ' - ' + str(self._ret['error']))
        else:
            print(str(datetime.datetime.now()) + ' ' + str(self._txid) + ' - ' + str(self._description) + ' status: ' + self._status)

    def isClosed(self):
        if self._status == 'closed':
            return True
        else:
            return False

    def isOpen(self):
        if self._status == 'open':
            return True
        else:
            return False

