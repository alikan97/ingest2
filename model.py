import json

class BinanceTickerStream:
    def __init__(self, e, t, s, c, o, h, l, tbv, tqv) -> None:
        self.timestamp = t
        self.symbol = s
        self.close = c
        self.open = o
        self.high = h
        self.low = l