import json
from model import BinanceTickerStream

def parseAndValidate(data:list) -> BinanceTickerStream:
    # Load data into JSON format
    data = json.loads(data)

    # Construct new data obj (DF, LIst...)
    parsedData = BinanceTickerStream(e = data['e'],
                                     t = data['E'],
                                     s = data['s'],
                                     c = data['c'],
                                     o = data['o'],
                                     h = data['h'],
                                     l = data['l'],
                                     tbv = data['v'],
                                     tqv = data['q'])
    print("symbol is " + data['s'])
    return parsedData.__dict__