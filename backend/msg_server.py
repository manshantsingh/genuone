import asyncio
import websockets

conns=[]
async def hello(websocket, path):
  conns.append(websocket)
  async for message in websocket:
    for c in conns:
      await c.send(message)

start_server = websockets.serve(hello, '0.0.0.0', 5001)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
