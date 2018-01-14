# import socket
# from time import sleep

# host = '127.0.0.1'
# port = 5000

# mysocket = socket.socket()
# mysocket.bind((host, port))
# mysocket.listen(1)

# conn, addr = mysocket.accept()

# print("Connection from: " + str(addr))

# while True:
# 	data = conn.recv(4096).decode()
# 	if not data:
# 		continue
# 	print ("from connected  user: " + str(data))

# 	data = str(data).upper()
# 	print ("sending: " + str(data))
# 	conn.send(data.encode())
# conn.close()


# # message = input('->')

# # while True:
# # 	mysocket.send(message.encode())


# # mysocket.close()



# import asyncio
# import websockets

# async def echo(websocket, path):
#     async for message in websocket:
#         await websocket.send(message)

# asyncio.get_event_loop().run_until_complete(
#     websockets.serve(echo, 'localhost', 5000))
# asyncio.get_event_loop().run_forever()


import asyncio
import websockets
from time import sleep

async def hello(websocket, path):
    # name = await websocket.recv()
    # print("< {}".format(name))

    greeting = "Hello {}!".format('guri')
    while True:
    	sleep(1)
    	await websocket.send(greeting)
    	print("> {}".format(greeting))

start_server = websockets.serve(hello, 'localhost', 5000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()