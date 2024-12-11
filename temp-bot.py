from tradingview_ta import TA_Handler, Interval, Exchange
from binance.client import Client
from binance.enums import *
# client = Client(api_key, api_secret)
import datetime

import pandas as pd
import matplotlib.pyplot as plt

########################################
# CALCULATE DI- & DI+

handler = TA_Handler(
    symbol="BTCUSDT",
    exchange="BINANCE",
    screener="crypto",
    interval=Interval.INTERVAL_1_MINUTE
)
def diPlus():
    analysis = handler.get_analysis()
    return analysis.indicators['ADX+DI']
def diMinus():
    analysis = handler.get_analysis()
    return analysis.indicators['ADX-DI']

########################################
# GLOBALS

STATE = ""
DI_DIFF = 1.05
diPs = []
diMs = []

########################################
# GET MAX QUANTITY

# def get_max_buy():
#     balanceUSDT = client.get_margin_asset(asset='USDT')
#     to_use = float(balanceUSDT['free'])
#     price = float(client.get_margin_price_index(symbol='BTCUSDT'))
#     decide_position_to_use = to_use / price
#     return decide_position_to_use

# def get_max_sell():
#     balanceBTC = client.get_margin_asset(asset='BTC')
#     to_use = float(balanceBTC['free'])
#     price = float(client.get_margin_price_index(symbol='BTCUSDT'))
#     decide_position_to_use = to_use * price
#     return decide_position_to_use

########################################
# OPEN BUY & SELL

def buy():
    print("buy")
    # qty = get_max_buy()
    # order = client.create_margin_order(
    # symbol='BTCUSDT',
    # side=SIDE_BUY,
    # type=ORDER_TYPE_MARKET,
    # quantity=qty,
    # sideEffectType="MARGIN_BUY")

def sell():
    print("sell")
    # qty = get_max_sell()
    # order = client.create_margin_order(
    # symbol='BTCUSDT',
    # side=SIDE_SELL,
    # type=ORDER_TYPE_MARKET,
    # quantity=qty,
    # sideEffectType="MARGIN_BUY")

########################################
# CLOSE OPEN & BUY

def close_buy():
    print("close buy")
    # qty = get_max_sell()
    # order = client.create_margin_order(
    # symbol='BTCUSDT',
    # side=SIDE_SELL,
    # type=ORDER_TYPE_MARKET,
    # quantity=qty,
    # sideEffectType="AUTO_REPAY")

def close_sell():
    print("close sell")
    # qty = get_max_buy()
    # order = client.create_margin_order(
    # symbol='BTCUSDT',
    # side=SIDE_BUY,
    # type=ORDER_TYPE_MARKET,
    # quantity=qty,
    # sideEffectType="AUTO_REPAY")

########################################
# MAIN

while True:
    m = datetime.datetime.now().second
    if(m % 60 == 0):
        print("################")
        M = diMinus()
        P = diPlus()
        diPs.append(P)
        diMs.append(M)
        plt.plot(diPs)
        plt.show()
        print(P)
        print(M)

        # DO SOMETHING
        if(abs(P - M) <= DI_DIFF or (STATE == "buy" and P < M) or (STATE == "sell" and P > M)):
            if(P > M):
                if (STATE != "buy"):
                    print("########### BUY ###########")
                    if(STATE == "sell"):
                        close_sell()
                    STATE = "buy"
                    buy()
            else:
                if (STATE != "sell"):
                    print("########### SELL ###########")
                    if(STATE == "buy"):
                        close_buy()
                    STATE = "sell"
                    sell()
    
