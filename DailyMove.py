# -*- coding: utf-8 -*-
import json
import requests


def getalldata():

    token = "c7fa8e75250aed46fea546d486a8019cf0ee5a2af08b04d64786c9b04c6eaeac"
    headers = {"Authorization": "Bearer " + token}
    apiurl = 'https://api.wmcloud.com/data/v1//api/market/getMktEqud.json?'
    param = {'beginDate': '', 'endDate': '', 'secID': '', 'ticker': '', 'tradeDate': '20190917','isOpen': ''}
    r=requests.get(apiurl, params=param, headers=headers)

    dataresult = json.loads(r.text)

    print (json.dumps(dataresult,indent=2))

if __name__ =='__main__':

    getalldata()