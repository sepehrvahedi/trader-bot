import websocket, json, pprint, talib, numpy

SOCKET = "wss://stream.binance.com:9443/ws/btcusdt@kline_1m"
DI_PERIOD = 14
DI_DIFF = 1.05
TRADE_SYMBOL = 'BTCUSDT'

count = 0

closes = []
highs = []
lows = []
position = "BUY"

def on_open(ws):
    print('opened connection')

def on_close(ws):
    print('closed connection')

def on_message(ws, message):
    global closes, highs, lows, position

    # print('received message')
    json_message = json.loads(message)
    # pprint.pprint(json_message)

    candle = json_message['k']

    is_candle_closed = candle['x']
    close = candle['c']
    low = candle['l']
    

    if is_candle_closed:
        print('candle closed at {}'.format(close ))
        closes.append(float(close))
        highs.append(float(high))
        lows.append(float(low))
        print("closes")
        print(closes)
        print("highs")
        print(highs)
        print("lows")
        print(lows)

        if len(closes) >= DI_PERIOD:
            print("YESS")
            np_closes = numpy.array(closes)
            # print(np_closes)
            np_highs = numpy.array(highs)
            np_lows = numpy.array(lows)

            diP = talib.PLUS_DI(np_highs, np_lows, np_closes, DI_PERIOD)
            diM = talib.MINUS_DI(np_highs, np_lows, np_closes, DI_PERIOD)

            print("all DI's calculated so far")
            print(diP)
            print("=========")
            print(diM)

            lastP = diP[-1]
            lastM = diM[-1]

            print("the current plus DI = {}".format(lastP))
            print("the current minus DI = {}".format(lastM))

            if(abs(lastM - lastP) > DI_DIFF):
                if lastM < lastP and position != "BUY":
                    print("======================BUY BUY BUY======================")
                    position = "BUY"
                    #buy here

                elif position != "SELL":
                    print("======================SELL SELL SELL======================")
                    position = "SELL"
            #         #sell here

ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()