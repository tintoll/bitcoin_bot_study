import pyupbit

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