# -*- coding: utf-8 -*-
import json
import requests
from datetime import date, timedelta


def getalldata(td):

    token = "75c383a6bba684f08359093d22146952c2ff1ee6f1369fb3f6f21c021bfe7674"
    headers = {"Authorization": "Bearer " + token}
    apiurl = 'https://api.wmcloud.com/data/v1//api/market/getMktEqud.json?'
    param = {'beginDate': '', 'endDate': '', 'secID': '', 'ticker': '', 'tradeDate': td, 'isOpen': ''}
    r=requests.get(apiurl, params=param, headers=headers)
    with open(str(td) + '.json', 'w') as file:
        json.dump(r, file)

    dataresult = json.loads(r.text)

    #the returned is a dictionary
    #key
    #retCode
    #retMsg
    #data
        #data is a list[0-9999]

            #list[0] is a dictionary

                    # secID
                    # ticker
                    # secShortName
                    # exchangeCD
                    # tradeDate
                    # preClosePrice
                    # actPreClosePrice
                    # openPrice
                    # highestPrice
                    # lowestPrice
                    # closePrice
                    # turnoverVol
                    # turnoverValue
                    # dealAmount
                    # turnoverRate
                    # accumAdjFactor
                    # negMarketValue
                    # marketValue
                    # chgPct
                    # PE
                    # PE1
                    # PB
                    # isOpen
                    # vwap

    return dataresult

    # print (json.dumps(dataresult,indent=2))


def readlocaldata(data):

    r = open(data)
    dataresult = json.loads(r.text)

    return dataresult


if __name__ == "__main__":

    # len(d['data'])=3873

    # d[data][0][secId]
    # print("\nCurrent Date: ", currentdate.strftime('%Y%m%d'))
    # print("52 Weeks before current date: ", ftw.strftime('%Y%m%d'))

    currentdate = date.today()-timedelta(days=1)
    ftw= (date.today() - timedelta(weeks=52))
    d = getalldata(currentdate)

    for keys in d:
        print(keys)
