import pyupbit
from pandas import DataFrame

# df = pyupbit.get_ohlcv("KRW-BTC")
# k = 0.5
# 변동폭 = (df['high']-df['low']) * k
# df['변동폭'] = 변동폭
# df['목표가'] = df['open'] + df['변동폭'].shift(1)
#
# cond = df['high'] >= df['목표가']
# 매수 = df.loc[cond, '목표가']
# 매도 = df.loc[cond, 'close']
#
# df['매수'] = 매수
# df['매도'] = 매도
# 수익률 = 매도/매수
# df['수익률'] = 수익률
#
#
# print(수익률.cumprod())



def 변동성돌파전략(ticker, k):
    df = pyupbit.get_ohlcv(ticker)

    변동폭 = (df['high'] - df['low']) * k
    목표 = df['open'] + 변동폭.shift(1)

    조건 = df['high'] >= 목표
    매수 = 목표[조건]
    매도 = df.loc[조건, 'close']

    수익률 = 매도 / 매수
    return 수익률.cumprod().iloc[-1]


data = []
for k in range(1, 11):
    수익률 = 변동성돌파전략("KRW-BTC", k/10)
    data.append([ k/10, 수익률 ])

df = DataFrame(data)
df.columns = ["k", "수익률"]
print(df.head())

df.sort_values('수익률')