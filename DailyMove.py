# -*- coding: utf-8 -*-
import json
import requests
from datetime import date, timedelta
import pandas as pd


def readalldata(td):

    token = "f5e83593972fd7bd68b6891076decb1b0dc1693f34b891e81a6e5b9ab937fa2e"
    headers = {"Authorization": "Bearer " + token}
    apiurl = 'https://api.wmcloud.com/data/v1//api/market/getMktEqud.json?'
    param = {'beginDate': '', 'endDate': '', 'secID': '', 'ticker': '', 'tradeDate': td, 'isOpen': ''}
    r=requests.get(apiurl, params=param, headers=headers)

    dataresult = json.loads(r.text)

    with open(str(td) + '.json', 'w') as file:
        json.dump(dataresult, file)

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

    with open(data, 'r') as myfile:

        d = myfile.read()

    dataresult = json.loads(d)

    return dataresult


def findname(ticker, alldata):
    for i in alldata:
        if i['ticker'] == ticker:
            return i['secShortName']



def findcloseprice(ticker, alldata):
    for i in alldata:
        if i['ticker'] == ticker:
            # print(type(i['closePrice']))
            # print(i['closePrice'])
            return i['closePrice']


def gettickerdata(ticker, alldata): # display all info of a ticker
    for i in alldata:
        if i['ticker'] == ticker:
                for keys in i:
                    print(keys)
                    print(i[keys])

def find52low(d1, d2):
    df = pd.DataFrame(columns=('ticker', 'Name', '52week change'))
    for i in d1:
        try:
            newrow = {'ticker': i['ticker'], 'Name': findname(i['ticker'], d1), '52week change': (i['closePrice']/findcloseprice(i['ticker'], d2)-1)*100} #current price / 52 weeks ago
            df = df.append(newrow, ignore_index=True)
        except:
            pass
    df = df.sort_values(by='52week change', ascending=1)
    return df

        # print(i['closePrice'] / findcloseprice(i['ticker'], d2)


if __name__ == '__main__':

    # len(d['data'])=3873
    # d[data][0][secId]
    # print("\nCurrent Date: ", currentdate.strftime('%Y%m%d'))
    # print("52 Weeks before current date: ", ftw.strftime('%Y%m%d'))

    currentdate = (date.today()-timedelta(days=0)).strftime('%Y%m%d')
    ftw = (date.today() - timedelta(weeks=52)).strftime('%Y%m%d')

    readalldata(currentdate)
    readalldata(ftw)

    d1 = readlocaldata(currentdate + '.json')['data']
    d2 = readlocaldata(ftw + '.json')['data']

    # for item in d['data']:
    #     print(item['closePrice']/findcloseprice(item['ticker'], d['data']))
    #     print(findname(item['ticker'], d['data']))

    print(d1[0]['tradeDate'])
    print(find52low(d1, d2))

