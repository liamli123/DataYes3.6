# -*- coding: utf-8 -*-
import json
import requests
from datetime import datetime, timedelta
import pandas as pd
import progressbar as pb
import sys


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


def find52low(td):

    currentdate = datetime.strptime(td, '%Y%m%d').strftime('%Y%m%d')

    ftw = (datetime.strptime(td, '%Y%m%d') - timedelta(weeks=52)).strftime('%Y%m%d')

    readalldata(currentdate)
    readalldata(ftw)

    d1 = readlocaldata(currentdate + '.json')['data']
    d2 = readlocaldata(ftw + '.json')['data']

    df = pd.DataFrame(columns=('ticker', 'Name', '52week change', 'TradeDate Close Price'))
    for i in d1:
        try:
            newrow = {'ticker': i['ticker'], 'Name': findname(i['ticker'], d1),
                      '52week change': (i['closePrice']/findcloseprice(i['ticker'], d2)-1)*100,
                      'TradeDate Close Price': i['closePrice'],
                      '          PE': i['PE']}
            df = df.append(newrow, ignore_index=True)
        except:
            pass
    df = df.sort_values(by='52week change', ascending=1)
    df = df.reset_index(drop=True)
    return df


def backtest(tradedate, testdate):

    currentdate = datetime.strptime(tradedate, '%Y%m%d').strftime('%Y%m%d')

    ftw = (datetime.strptime(tradedate, '%Y%m%d') - timedelta(weeks=52)).strftime('%Y%m%d')

    testdate = datetime.strptime(testdate, '%Y%m%d').strftime('%Y%m%d')

    readalldata(currentdate)
    readalldata(ftw)
    readalldata(testdate)

    d1 = readlocaldata(currentdate + '.json')['data']
    d3 = readlocaldata(testdate + '.json')['data']
    # for item in d['data']:
    #     print(item['closePrice']/findcloseprice(item['ticker'], d['data']))
    #     print(findname(item['ticker'], d['data']))

    df = find52low(currentdate)
    df[testdate + ' Price'] = None
    df[testdate + ' Change'] = None
    allrows = len(df)
    j = 0
    while j < allrows:
        try:
            df.loc[j, testdate+' Price'] = findcloseprice(df.loc[j, 'ticker'], d3)
            df.loc[j, testdate+' Change'] = (df.loc[j, testdate+' Price']/df.loc[j, 'TradeDate Close Price']-1)*100
        except:
            pass
        j = j+1

    print('Trade Date:  ' + d1[0]['tradeDate'])

    df = df.sort_values(by=testdate+' Change', ascending=0)

    with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None,
                           'display.colheader_justify', 'left'):  # more options can be specified also
        print(df)


if __name__ == '__main__':

    # backtest('20170712', '20190813')

    with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None,):
        print(find52low('20200221'))


    # readalldata to load two range of data

    # find52low(finddate) - return dataframe

    # backtest(finddate, test date) - print dataframe

    # print(find52low('20190211'))

    # d = readlocaldata('20200210.json')['data']
    # print(findcloseprice('300304', d))