import json
import requests


def blocktrade(tradedate):

    tradedatestring = str(tradedate)

    token = "75c383a6bba684f08359093d22146952c2ff1ee6f1369fb3f6f21c021bfe7674"
    headers = {"Authorization": "Bearer " + token}
    apiurl = 'https://api.wmcloud.com/data/v1//api/market/getMktBlockd.json?'
    param = {'beginDate': '', 'endDate': '', 'secID': '', 'ticker': '', 'assetClass': '', 'tradeDate': tradedatestring}
    r=requests.get(apiurl, params=param, headers=headers)

    dataresult = json.loads(r.text)


    for i in range(len(dataresult['data'])):
       print(json.dumps(dataresult['data'][i], indent=2,ensure_ascii=False))

if __name__ =='__main__':

    blocktrade(20190911)