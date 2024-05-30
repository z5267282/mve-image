import asyncio
import websockets
import sys


async def send_message(movie_name):
    uri = "ws://localhost:6000"
    async with websockets.connect(uri) as websocket:
        await websocket.send(movie_name)

movie_name = sys.argv[1]
asyncio.run(send_message(movie_name))
