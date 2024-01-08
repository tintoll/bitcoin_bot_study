import pyupbit

df = pyupbit.get_ohlcv("KRW-BTC")
k = 0.5
변동폭 = (df['high']-df['low']) * k
df['변동폭'] = 변동폭
df['목표가'] = df['open'] + df['변동폭'].shift(1)

df['매수'] = df['목표가'] if df['high'] >= df['목표가'] else 0


if df['high'] >= df['목표가']:
    매수 = df['목표가']
    매도 = df['close']
    수익률 = 매수 / 매도
else:
    매수 = 0
    매도 = 0
    수익률 = 0

df['매수'] = 매수
df['매도'] = 매도
df['수익률'] = 수익률


print(df)