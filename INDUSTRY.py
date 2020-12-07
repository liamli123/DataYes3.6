# -*- coding: utf-8 -*-
import json
import requests
from datetime import datetime, timedelta
import pandas as pd
import numpy as np


def industry():


    token = "7729e4b39cf01d67214d0273b4ac59f8890bb4cfbd2ae4fe150143dd02aa8ef8"
    headers = {"Authorization": "Bearer " + token}
    apiurl = 'https://api.wmcloud.com/data/v1//api/equity/getEquIndustry.json?'
    param = {'secID': '', 'ticker': '', 'industryVersionCD': '', 'industry': '', 'industryID1': '', 'industryID2': '', 'industryID3': '', 'intoDate': '', 'intoDate': '', 'equTypeID': '', 'industryID': '',}
    r = requests.get(apiurl, params=param, headers=headers)
    dataresult = json.loads(r.text)
    return dataresult

if __name__ =='__main__':

    df=pd.DataFrame(industry()['data'])
    df.to_csv(r'E:\Python\DataYes3.6\industry.csv',index = False, header=True)