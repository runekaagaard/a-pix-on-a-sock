import asyncio
import datetime
from random import randint
import websockets

H = 15
W = 15

SOCKS = [[None] * H for x in range(W)]
COLORS = ["#" + x * 6 for x in "01234567890abcdef"]
I = 0


async def connect(websocket, path):
    global I
    I += 1
    while True:
        x = int(path.split("/")[1])
        y = int(path.split("/")[-1])
        SOCKS[x][y] = websocket
        await asyncio.sleep(1010101010101010)


async def animate():
    async def paint(x, y, color):
        sock = SOCKS[x][y]
        if sock is None:
            return
        await sock.send(color)

    while True:
        if I < H * W:
            await asyncio.sleep(0.1)
        for x in range(H):
            for y in range(W):
                await paint(x, y, COLORS[randint(0, 15)])
        await asyncio.sleep(0.05)


event_loop = asyncio.get_event_loop()

event_loop.create_task(animate())
event_loop.run_until_complete(
    websockets.serve(connect, 'localhost', 5678))

event_loop.run_forever()
