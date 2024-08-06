import requests
import os
import json
import pandas as pd

def req(dt="20170101", url_param={}):
    key = os.getenv("MOVIE_API_KEY")
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    url = f"{base_url}?key={key}&targetDt={dt}"
    for k, v in url_param.items():
        url = url + f"&{k}={v}"
    
    r = requests.get(url)
    code = r.status_code
    data = r.json()

    return code, data

def req2list(dt="20170101", url_param={}):
    _, data = req(dt, url_param)
    l = data['boxOfficeResult']['dailyBoxOfficeList']
    return l

def list2df(dt="20170101", url_param={}):
    l = req2list(dt, url_param)
    # list를 dataFrame으로 
    df = pd.DataFrame(l)
    return df

# df 저장 + 파티셔닝 날짜넣기?
def dt2df(dt="20170101", url_param={}):
    df = list2df(dt, url_param)
    df['load_dt'] = dt
    return df

