import websockets
import csv as csv
import asyncio
import json
import schedule
from validator import parseAndValidate

url = "wss://stream.binance.com:9443/ws/"

streams = [
    "ethbtc@miniTicker","bnbbtc@miniTicker","wavesbtc@miniTicker","bchabcbtc@miniTicker",
    "bchsvbtc@miniTicker","xrpbtc@miniTicker","tusdbtc@miniTicker","eosbtc@miniTicker",
    "trxbtc@miniTicker","ltcbtc@miniTicker","xlmbtc@miniTicker","bcptbtc@miniTicker",
    "adabtc@miniTicker","zilbtc@miniTicker","xmrbtc@miniTicker","stratbtc@miniTicker",
    "zecbtc@miniTicker","qkcbtc@miniTicker","neobtc@miniTicker","dashbtc@miniTicker","zrxbtc@miniTicker"
]

async def handler(websocket):
    while True:
        message = await websocket.recv()
        
        parseAndValidate(message)

        sendMessage()

async def main():
    async with websockets.connect(url + '/'.join(streams)) as ws:
        await handler(ws)
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())