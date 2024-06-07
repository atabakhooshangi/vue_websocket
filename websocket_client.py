import asyncio
import websockets

clients = set()


async def register(websocket):
    clients.add(websocket)


async def unregister(websocket):
    clients.remove(websocket)


async def broadcast(message):
    if clients:  # asyncio.wait doesn't accept an empty list
        tasks = {asyncio.create_task(client.send(message)) for client in clients}
        await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)


async def handler(websocket, path):
    await register(websocket)
    try:
        async for message in websocket:
            await broadcast(message)
    finally:
        await unregister(websocket)


start_server = websockets.serve(handler, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
