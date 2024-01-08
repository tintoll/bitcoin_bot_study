from volatility import *
import time
import datetime

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