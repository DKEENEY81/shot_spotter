#!/usr/local/bin/python3

from requests import get
import pandas as pd
import json

url = "https://opendata.arcgis.com/datasets/89bfd2aed9a142249225a638448a5276_29.geojson"
response = get(url)

#print(response.headers['content-type'])

##retrieves json formatted data via API
def get_info():
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

data = get_info()

##convert to dataframe and flatten dict of dicts
dk = pd.DataFrame.from_dict(data)
dk2 = dk['features'].apply(pd.Series)
dk3 = dk2['properties'].apply(pd.Series)

##coerce existing column to date/time, create separate columns for 
dk3['DATETIME'] = pd.to_datetime(dk3['DATETIME'])
dk3['YEAR'] = pd.DatetimeIndex(dk3['DATETIME']).year
dk3['MONTH'] = pd.DatetimeIndex(dk3['DATETIME']).month
dk3['DAY'] = pd.DatetimeIndex(dk3['DATETIME']).day
dk3['DOW'] = dk3['DATETIME'].dt.day_name()

print(dk3.head())









