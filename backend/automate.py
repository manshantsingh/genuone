import asyncio
import websockets
from subprocess import run
from subprocess import PIPE
from time import sleep
import numpy as np
import pandas as pd

async def hello(websocket, path):
	run(['adb', 'shell', 'am', 'start', '-a', 'android.media.action.STILL_IMAGE_CAMERA'])
	sleep(2)
	columns = ['anger', 'contempt', 'disgust', 'fear', 'happiness', 'neutral', 'sadness', 'surprise']
	data = []
	last_n=[]
	N=5
	while True:
		sleep(1)
		run(['adb', 'shell' ,'input', 'keyevent', '27'])

		sleep(1)
		imgName=str(run(['adb', 'shell', 'ls', '/storage/emulated/0/DCIM/Camera/', '-t', '|', 'head', '-1'], stdout=PIPE).stdout)[2:-5]

		sleep(1)
		run(['adb', 'pull', '/storage/emulated/0/DCIM/Camera/' + imgName])

		sleep(1)
		out=str(run(['node', 'index.js', imgName], stdout=PIPE).stdout)[2:-3]
		print(out)
		if out == "nothing":
			continue
		arr=[x.split(' ') for x in out.split('\\n')]
		d=pd.DataFrame(arr, columns=columns, dtype=np.float).mean()
		data.append(d)
		last_n.append(d)
		if len(last_n) > N:
			last_n.pop(0)
		await websocket.send(pd.DataFrame(last_n).mean().to_json())

start_server = websockets.serve(hello, 'localhost', 5000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

	