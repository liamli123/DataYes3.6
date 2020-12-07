# -*- coding: utf-8 -*-
import json
import requests
from datetime import datetime, timedelta
import pandas as pd
import numpy as np


def blocktrade(tradedate):


    token = "7729e4b39cf01d67214d0273b4ac59f8890bb4cfbd2ae4fe150143dd02aa8ef8"
    headers = {"Authorization": "Bearer " + token}
    apiurl = 'https://api.wmcloud.com/data/v1//api/market/getMktBlockd.json?'
    param = {'beginDate': '', 'endDate': '', 'secID': '', 'ticker': '', 'assetClass': '', 'tradeDate': tradedate}
    r = requests.get(apiurl, params=param, headers=headers)

    dataresult = json.loads(r.text)
    return dataresult

if __name__ =='__main__':

    tradedate='20201204'
    df = pd.DataFrame(blocktrade(tradedate)['data'])

    desired_width = 320
    pd.set_option('display.width', desired_width)
    np.set_printoptions(linewidth=desired_width)
    df.to_csv(r'E:\Python\DataYes3.6\block' + tradedate + '.csv',index = False, header=True)