import websockets
import csv as csv
import asyncio
from parse import parseAndValidate
from kinesis import KinesisClient
import schedule
from logger import send_log, Log_Level

streamUrl = "wss://stream.binance.com:9443/ws/"

client = KinesisClient('crypto_streams')

subscribedSymbols = [
    "ethbtc@miniTicker","bnbbtc@miniTicker","xrpbtc@miniTicker","eosbtc@miniTicker",
    "trxbtc@miniTicker","ltcbtc@miniTicker","xlmbtc@miniTicker","adabtc@miniTicker",
    "zecbtc@miniTicker","neobtc@miniTicker","maticbtc@miniTicker","algobtc@miniTicker"
]

async def ingest(websocket):
    if client is None:
        send_log(Log_Level.ERROR, "Error: Client Unavailable")
        
    schedule.every(30).seconds.do(client.send)

    while True:
        schedule.run_pending()
        message = await websocket.recv()
        
        parsedData = parseAndValidate(message)
        client.put(parsedData)

async def run():
    listenerUrl = streamUrl + '/'.join(subscribedSymbols)
    async with websockets.connect(listenerUrl) as ws:
        await ingest(ws)
        await asyncio.Future()
