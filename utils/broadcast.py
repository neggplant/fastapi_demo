"""
广播消息
https://juejin.cn/s/python%20websocket%20server%20broadcast
"""
import asyncio
import websockets


async def broadcast(websocket, path):
    while True:
        message = await websocket.recv()
        await asyncio.wait([ws.send(message) for ws in clients])


async def handler(websocket, path):
    clients.add(websocket)
    try:
        await broadcast(websocket, path)
    finally:
        clients.remove(websocket)


clients = set()

start_server = websockets.serve(handler, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
