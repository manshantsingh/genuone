import asyncio
import websockets

async def hello(websocket, path):
  async for message in websocket:
    await websocket.send(message)

start_server = websockets.serve(hello, '0.0.0.0', 5001)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
