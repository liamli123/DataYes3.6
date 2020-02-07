# -*- coding: utf-8 -*-
import json
import requests
from datetime import date, timedelta


def getalldata(td):

    token = "f5e83593972fd7bd68b6891076decb1b0dc1693f34b891e81a6e5b9ab937fa2e"
    headers = {"Authorization": "Bearer " + token}
    apiurl = 'https://api.wmcloud.com/data/v1//api/market/getMktEqud.json?'
    param = {'beginDate': '', 'endDate': '', 'secID': '', 'ticker': '', 'tradeDate': td, 'isOpen': ''}
    r=requests.get(apiurl, params=param, headers=headers)

    dataresult = json.loads(r.text)

    with open(str(td) + '.json', 'w') as file:
        json.dump(dataresult, file)

    return dataresult

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

    # print (json.dumps(dataresult,indent=2))


def readlocaldata(data):

    r = open(data)
    dataresult = json.loads(r.text)

    return dataresult


if __name__ == '__main__':

    # len(d['data'])=3873
    # d[data][0][secId]
    # print("\nCurrent Date: ", currentdate.strftime('%Y%m%d'))
    # print("52 Weeks before current date: ", ftw.strftime('%Y%m%d'))

    currentdate = (date.today()-timedelta(days=2)).strftime('%Y%m%d')
    ftw = (date.today() - timedelta(weeks=52)).strftime('%Y%m%d')

    d = getalldata(ftw)
    for keys in d:
        print  (keys)
