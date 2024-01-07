import pyupbit

df = pyupbit.get_ohlcv("KRW-BTC")
df.to_excel('btc.xlsx')
# print(df.tail()) # 마지막 행 5개 가져오기
#
# df["종가하나내린거"] = df["close"].shift(1)
# print(df.head()) # 상위 행 5개 가져오기
#
# print(df)
# # 추가
# df['diff'] = df['high'] - df['low']
# print(df)
#
# # 삭제
# df2 = df.drop('diff', axis=1) # axis=1이여야지 컬럼 삭제, 0이면 행삭제
# print(df2)
# import pandas as pd
#
# data = "2021-01-01"
# index = pd.to_datetime(data)
# print(type(data))
# print(type(index))