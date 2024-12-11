from tradingview_ta import TA_Handler, Interval, Exchange
from binance.client import Client

# from binance_f import RequestClient
# from binance_f.constant.test import *
# from binance_f.base.printobject import *
# from binance_f.model.constant import *

from binance.enums import *
client = Client("W7rpTAaiTw9ybnnHGLbxZEBfg83l1njkDuEV2rOrNbTWMzTcz2E98TUfePr9QkG0",
                "ZagqZPhyFeGi5sFJmt1pzulZSXfRV44tup5PprkkXjxqbeGHmBxhLbmVL6pVutWJ")

# client = RequestClient(api_key="W7rpTAaiTw9ybnnHGLbxZEBfg83l1njkDuEV2rOrNbTWMzTcz2E98TUfePr9QkG0",
#                        secret_key="ZagqZPhyFeGi5sFJmt1pzulZSXfRV44tup5PprkkXjxqbeGHmBxhLbmVL6pVutWJ",
#                        url='https://fapi.binance.com')
import datetime

########################################
# CALCULATE DI- & DI+

handler = TA_Handler(
    symbol="BTCUSDTPERP",
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

def khat():
    print("######################################")

########################################
# GET USDT & BTC ASSET INFO



########################################
# GET MAX QUANTITY



########################################
# OPEN BUY & SELL (LONG POSITION)



########################################
# OPEN BUY & SELL (SHORT POSITION)



########################################
# MAIN
print(client.futures_account_balance())
# print(client.futures_account_transfer)
# print(client.futures_ping)
# balance = client.futures_account_balance()
# print(balance)
    