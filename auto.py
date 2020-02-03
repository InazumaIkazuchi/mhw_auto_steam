import keyboard
import time
import sys
import threading

import argparse
parser = argparse.ArgumentParser(description='Automatically press space key')
args = parser.parse_args()

RUNNING = True
	
# press space every 10 seconds, to deal with the cut-scenes
def timer_runner():
	global RUNNING
	while RUNNING:
		time.sleep(10)
		keyboard.release('space')
		keyboard.press('space')
	
# used for termination
def stop_running(args):
	global RUNNING
	RUNNING = False
	keyboard.release('space')
	
timer = threading.Thread(target=timer_runner)

print('='*20)
print('\n请在5秒以内切到游戏内蒸汽机画面……按Q结束\n')
print('Please switch to your game window in 5 seconds...Press \'Q\' to end\n')
print('五秒内で蒸気機関管理所に行ってください。「Q」を押してこのプログラムを止める事ができます。')

keyboard.on_press_key('q', stop_running)
# wait 5 seconds before starting, give the user some time to switch the game window
time.sleep(5)

if RUNNING:
	timer.start()
	keyboard.press('space')
	# block until 'Q' is pressed
	keyboard.wait('q')
	timer.join()
