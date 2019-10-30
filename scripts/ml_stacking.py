import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like # may be necessary in some versions of pandas
import pandas_datareader.data as web


def get_symbols(symbols,data_source, begin_date=None,end_date=None):
    out = pd.DataFrame()
    for symbol in symbols:
        df = web.DataReader(symbol, data_source,begin_date, end_date)\
        [['AdjOpen','AdjHigh','AdjLow','AdjClose','AdjVolume']].reset_index()
        df.columns = ['date','open','high','low','close','volume'] #my convention: always lowercase
        df['symbol'] = symbol # add a new column which contains the symbol so we can keep multiple symbols in the same dataframe
        df = df.set_index(['date','symbol'])
        out = pd.concat([out,df],axis=0) #stacks on top of previously collected data
    return out.sort_index()
        
prices = get_symbols(['AAPL','CSCO'],data_source='quandl',\
                     begin_date='2015-01-01',end_date='2017-01-01')

features = pd.DataFrame(index=prices.index)
features['volume_change_ratio'] = prices.groupby(level='symbol').volume\
.diff(1) / prices.groupby(level='symbol').shift(1).volume
features['momentum_5_day'] = prices.groupby(level='symbol').close\
.pct_change(5) 

features['intraday_chg'] = (prices.groupby(level='symbol').close\
                            .shift(0) - prices.groupby(level='symbol').open\
                            .shift(0))/prices.groupby(level='symbol').open.shift(0)

features['day_of_week'] = features.index.get_level_values('date').weekday

features['day_of_month'] = features.index.get_level_values('date').day

features.dropna(inplace=True)
print(features.tail(10))