from tradingview_ta import TA_Handler, Interval, Exchange
from binance.client import Client
from binance.enums import *
client = Client("W7rpTAaiTw9ybnnHGLbxZEBfg83l1njkDuEV2rOrNbTWMzTcz2E98TUfePr9QkG0",
                "ZagqZPhyFeGi5sFJmt1pzulZSXfRV44tup5PprkkXjxqbeGHmBxhLbmVL6pVutWJ")
import datetime, math
import time
########################################
# CALCULATE DI- & DI+

handler = TA_Handler(
    symbol="BTCUSDT",
    exchange="BINANCE",
    screener="crypto",
    interval=Interval.INTERVAL_15_MINUTES
)
def diPlus():
    analysis = handler.get_analysis()
    return analysis.indicators['ADX+DI']
def diMinus():
    analysis = handler.get_analysis()
    return analysis.indicators['ADX-DI']

########################################
# GLOBALS

STATE = "none"
DI_DIFF = 3
TMP_STATE = "buy"

def khat():
    print("######################################")

########################################
# GET USDT & BTC ASSET INFO

# LONG QTY
def availableUSDT():
    usdt = client.get_max_margin_loan(asset='USDT')
    return (float(usdt['amount']) * 1.5) * 0.995

# SHORT QTY
def availableBTC():
    btc = client.get_max_margin_loan(asset='BTC')
    return (float(btc['amount']))

# def availableUSDT():
#     User = client.get_margin_account()
#     Assets = User['userAssets']
    # for i in Assets:
    #     if(i['asset'] == "USDT"):
    #         balanceUSDT = i
#     to_use = float(balanceUSDT['free'])
#     # to_use = round(to_use, 5)
#     return to_use

# def availableBTC():
#     User = client.get_margin_account()
#     Assets = User['userAssets']
#     for i in Assets:
#         if(i['asset'] == "BTC"):
#             balanceBTC = i
#     to_use = float(balanceBTC['free'])
#     return to_use

########################################
# GET MAX QUANTITY

def convertUsdtBtc(usdt):
    price = float(client.get_margin_price_index(symbol='BTCUSDT').get('price'))
    decide_position_to_use = usdt / price
    return decide_position_to_use

# def get_max_sell():
#     to_use = availableBTC()
#     price = float(client.get_margin_price_index(symbol='BTCUSDT').get('price'))
#     decide_position_to_use = to_use * price
#     return decide_position_to_use

########################################
# OPEN BUY & SELL

def longMargin():
    usdt = availableUSDT()
    qty = convertUsdtBtc(usdt)
    qty *= 10**6
    qty = math.ceil(qty)
    qty /= 10**6
    print("QTYYYYY")
    print(qty)
    while True:
        flag = False
        try:
            order = client.create_margin_order(
                symbol='BTCUSDT',
                side=SIDE_BUY,
                type=ORDER_TYPE_MARKET,
                quantity=qty,
                sideEffectType="MARGIN_BUY"
            )
            flag = True
        except Exception as e:
            pass
        if flag is False:
            time.sleep(0.2)
            print("failure")
        else: 
            print('succeed')
            break
    ex = order['executedQty']
    khat()
    print("Buy")
    print("Quantity : " + ex)
    return float(ex)

def shortMargin():
    qty = availableBTC()
    qty *= 10**6
    qty = math.ceil(qty)
    qty /= 10**6
    print(qty)
    order = client.create_margin_order(
    symbol='BTCUSDT',
    side=SIDE_SELL,
    type=ORDER_TYPE_MARKET,
    quantity=qty,
    sideEffectType="MARGIN_BUY")
    ex = order['executedQty']
    khat()
    print("Buy")
    print("Quantity : " + ex)
    return float(ex)

########################################
# CLOSE BUY & SELL

def closeLong(qty):
    order = client.create_margin_order(
        symbol='BTCUSDT',
        side=SIDE_SELL,
        type=ORDER_TYPE_MARKET,
        quantity=qty,
        sideEffectType="AUTO_REPAY"
    )
    ex = order['executedQty']
    khat()
    print("Close Long")
    print("Quantity : " + ex)

def closeShort(qty):
    order = client.create_margin_order(
        symbol='BTCUSDT',
        side=SIDE_BUY,
        type=ORDER_TYPE_MARKET,
        quantity=qty,
        sideEffectType="AUTO_REPAY"
    )
    ex = order['executedQty']
    khat()
    print("Close Short")
    print("Quantity : " + ex)

########################################
# BUY & SELL FUNCTIONS

def buy():
    khat()
    STATE = "buy"
    print(">>>>>>>>>>> BUY <<<<<<<<<<<")
    tmp = longMargin()
    khat()
    return tmp

def sell():
    khat()
    STATE = "sell"
    print(">>>>>>>>>>> SELL <<<<<<<<<<<")
    tmp = shortMargin()
    khat()
    return tmp

########################################
# MAIN
print(availableUSDT())
print(availableBTC())

longPos = 0.0
shortPos = 0.0

while True:
    a = int(input())
    if(a == 1):
        longPos = buy()
        print("LONG POS" + str(longPos))
    elif(a == 2):
        closeLong(longPos)
    elif(a == 3):
        shortPos = sell()
    else:
        closeShort(shortPos)

M = diMinus()
P = diPlus()
if(M > P):
    TMP_STATE = "sell"

# while True:
#     a = int(input())
#     if a == 1:
#         buy()
#     elif a == 2:

    # m = datetime.datetime.now().minute
    # if(m % 15 == 0):
    #     khat()
    #     M = diMinus()
    #     P = diPlus()
    #     if(M > P):
    #         TMP_STATE = "sell"
    #     print(" STATE : " + str(STATE))
    #     print(" + : " + str(P))
    #     print(" - : " + str(M))
    #     khat()

    #     # ALGORITHM
        
    #     # STATE : NONE

    #     if(STATE == "none"):
    #         if(TMP_STATE == "sell"):
    #             if(P - M >= DI_DIFF):
    #                 buy()
        
    #     # STATE : BUY

    #     elif(STATE == "buy"):
    #         if(M - P >= DI_DIFF):
    #             sell()

    #     # STATE : SELL

    #     elif(STATE == "sell"):
    #         if(P - M >= DI_DIFF):
    #             buy()
    