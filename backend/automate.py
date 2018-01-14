from subprocess import run
from subprocess import PIPE
from os import system
from time import sleep

system('adb shell am start -a android.media.action.STILL_IMAGE_CAMERA')
sleep(2)
while True:
	system('adb shell input keyevent 27')

	sleep(1)
	imgName=str(run(['adb', 'shell', 'ls', '/storage/emulated/0/DCIM/Camera/', '-t', '|', 'head', '-1'], stdout=PIPE).stdout)[2:-5]

	sleep(1)
	system('adb pull /storage/emulated/0/DCIM/Camera/' + imgName)

	sleep(1)
	out=str(run(['node', 'index.js', imgName], stdout=PIPE).stdout)