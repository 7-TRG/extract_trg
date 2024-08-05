from extract_trg.extract_trg import req, req2list, list2df, dt2df
import pandas as pd

def test_req():
    code, data = req(dt="20170101", url_param={})
    assert True
    assert code == 200

def test_req2list():
    l = req2list()
    assert l

def test_list2df():
    df = list2df()
    print(df)
    assert isinstance(df, pd.DataFrame) # 반환된 객체가 데이터프레임인지 확인
    assert 'rnum' in df.columns
    assert 'openDt' in df.columns
    assert 'movieNm' in df.columns
    assert 'audiAcc' in df.columns

def test_dt2df():
    df = dt2df()
    assert 'load_dt' in df.columns

