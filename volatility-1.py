import pyupbit
import time
import datetime

def get_target_price():
    df = pyupbit.get_ohlcv('KRW-BTC')
    volatility = (df.iloc[-2]['high'] - df.iloc[-2]['low']) * 0.6
    target_price = df.iloc[-1]['open'] + volatility
    return target_price

def buy_crypto_current(upbit, price):
    krw = upbit.get_balance('KRW')
    unit = 10000 / price
    print(krw, unit)
    # 현재가에 10만원어치 수량을 지정가 주문을 넣어라
    return upbit.buy_limit_order("KRW-BTC", price, unit)

def sell_crypto_currency(upbit):
    unit = upbit.get_balance("KRW-BTC")
    # 시장가 매도
    return upbit.sell_market_order("KRW-BTC", unit)

with open('real.txt', 'r') as f:
    access = f.readline().strip()
    secret = f.readline().strip()

upbit = pyupbit.Upbit(access, secret)
target_price = get_target_price()

hold_flag = False # 매수했다면 True 아니면 False

while True:

    now = datetime.datetime.now() # 현재시간
    mid = datetime.datetime(now.year, now.month, now.day, 9,0,0) # upbit 하루 단위인 9시
    delta = datetime.timedelta(seconds=10) # 시간 간격이 필요해서 10초를 구해옴.

    if mid <= now <= mid + delta:
        if hold_flag == True:
            ret = sell_crypto_currency(upbit)
            print("매도", ret)
        target_price = get_target_price()
        hold_flag = False
    else:
        price = pyupbit.get_current_price('KRW-BTC')
        if target_price <= price and hold_flag == False:
            ret = buy_crypto_current(upbit, price)
            print("매수", ret)
            hold_flag = True
    print(now, target_price, price)
    time.sleep(1)

