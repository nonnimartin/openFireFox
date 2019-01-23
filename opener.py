import webbrowser as wb
import os
import subprocess
import time
import json

def openFireFox(target):
	p = subprocess.Popen(["firefox", target])
	return p

def getTarget():
	with open('config.json') as f:
		data = json.load(f)
	return data['target']

def main():
	target = getTarget()
	#open firefox tab
	firefox = openFireFox(target)
	#time.sleep(10)
	#firefox.kill()


if __name__ == '__main__':
    main()