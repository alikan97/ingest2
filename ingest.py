import websockets
import csv as csv
import asyncio
from parse import parseAndValidate
from kinesis import KinesisClient

url = "wss://stream.binance.com:9443/ws/"
client = KinesisClient('Stream')

subscribedSymbols = [
    "ethbtc@miniTicker","bnbbtc@miniTicker","wavesbtc@miniTicker","bchabcbtc@miniTicker",
    "bchsvbtc@miniTicker","xrpbtc@miniTicker","tusdbtc@miniTicker","eosbtc@miniTicker",
    "trxbtc@miniTicker","ltcbtc@miniTicker","xlmbtc@miniTicker","bcptbtc@miniTicker",
    "adabtc@miniTicker","zilbtc@miniTicker","xmrbtc@miniTicker","stratbtc@miniTicker",
    "zecbtc@miniTicker","qkcbtc@miniTicker","neobtc@miniTicker","dashbtc@miniTicker","zrxbtc@miniTicker"
]

async def ingest(websocket):
    while True:
        message = await websocket.recv()
        
        parsedData = parseAndValidate(message)

        client.put(parsedData, 'KEY')

async def run():
    listenerUrl = url + '/'.join(subscribedSymbols)

    async with websockets.connect(listenerUrl) as ws:
        await ingest(ws)
        await asyncio.Future()
