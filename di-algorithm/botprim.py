from tradingview_ta import TA_Handler, Interval, Exchange
import time


handler = TA_Handler(
    symbol="BTCUSDT",
    exchange="BINANCE",
    screener="crypto",
    interval=Interval.INTERVAL_15_MINUTES
)
def dip():
    analysis = handler.get_analysis()
    return analysis.indicators['ADX+DI']
def diM():
    analysis = handler.get_analysis()
    return analysis.indicators['ADX-DI']

# while True:
#     print('candle')