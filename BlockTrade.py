import json
import requests


def blocktrade(tradedate):

    tradedatestring = str(tradedate)

    token = "c7fa8e75250aed46fea546d486a8019cf0ee5a2af08b04d64786c9b04c6eaeac"
    headers = {"Authorization": "Bearer " + token}
    apiurl = 'https://api.wmcloud.com/data/v1//api/market/getMktBlockd.json?'
    param = {'beginDate': '', 'endDate': '', 'secID': '', 'ticker': '', 'assetClass': '', 'tradeDate': tradedatestring}
    r=requests.get(apiurl, params=param, headers=headers)

    dataresult = json.loads(r.text)


    for i in range(len(dataresult['data'])):
       print(json.dumps(dataresult['data'][i], indent=2,ensure_ascii=False))

if __name__ =='__main__':

    blocktrade(20190911)