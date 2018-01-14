import asyncio
import websockets
from subprocess import run
from subprocess import PIPE
from time import sleep
from time import time
import numpy as np
import pandas as pd
from ast import literal_eval
import json

async def hello(websocket, path):
	run(['adb', 'shell', 'am', 'start', '-a', 'android.media.action.STILL_IMAGE_CAMERA'])
	sleep(2)
	columns = ['anger', 'contempt', 'disgust', 'fear', 'happiness', 'neutral', 'sadness', 'surprise']
	data = []
	last_n=[]
	N=1
	while True:
		start = time()
		run(['adb', 'shell' ,'input', 'keyevent', '27'])

		imgName=str(run(['adb', 'shell', 'ls', '/storage/emulated/0/DCIM/Camera/', '-t', '|', 'head', '-1'], stdout=PIPE).stdout)[2:-5]

		run(['adb', 'pull', '/storage/emulated/0/DCIM/Camera/' + imgName])

		out=str(run(['node', 'index.js', imgName], stdout=PIPE).stdout)[2:-3]
		print(out)
		if out == "nothing" or out[0]=='{':
			continue
		arr=[x.split(' ') for x in out.split('\\n')]
		fail=False
		for x in arr:
			if len(x) != 8:
				fail=True
				break
		if fail:
			print("columns mismatch will happen. Will ignore for safety")
			print(arr)

		df=pd.DataFrame(arr, columns=columns, dtype=np.float)
		df['neutral'] = df.neutral*0.5
		sums = df.sum(1)
		df=df.div(sums, axis=0)
		print(df.sum(1))
		d=df.mean() * 100
		data.append(d)
		last_n.append(d)
		if len(last_n) > N:
			last_n.pop(0)

		dic = {
			'last': literal_eval(pd.DataFrame(last_n).mean().to_json()),
			'winning': list(pd.DataFrame(data).mean().sort_values(0, ascending=False).index[0:3]),
			'type': 'emotions_data'
		}
		await websocket.send(json.dumps(dic))
		delta = time() - start
		if delta < 5:
			delta = 5-delta
			print('spared '+str(delta)+' seconds')
			sleep(delta)
		else:
			print('behind by '+str(delta-5)+' seconds')

start_server = websockets.serve(hello, '0.0.0.0', 5000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
