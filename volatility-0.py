import pyupbit

# # 실시간 로직
# df = pyupbit.get_ohlcv('KRW-BTC')
# # 행끝에서 2번째값의 고가를 가져온다.(어제)
# print(df.iloc[-2]['high'])
# print(df.iloc[-2][1]) # 인덱스로도 가져올수 있다.
# print(df.iloc[-2, 1]) # 위와 동일한 값을 가져옴. 이게 실행속도가 더 빠름
# volatility = (df.iloc[-2]['high'] - df.iloc[-2]['low']) * 0.6
# target_price = df.iloc[-1]['open'] + volatility
# print(target_price)

# 함수화
def get_target_price():
    df = pyupbit.get_ohlcv('KRW-BTC')
    volatility = (df.iloc[-2]['high'] - df.iloc[-2]['low']) * 0.6
    target_price = df.iloc[-1]['open'] + volatility
    return target_price

print(get_target_price())