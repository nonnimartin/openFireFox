import webbrowser as wb
import os
import subprocess
import time
import json
import random
from bs4 import BeautifulSoup
import requests

border = "======================================================="

def openFireFox(target):
	p = subprocess.Popen(["firefox", target])
	return p

def getTarget():
	with open('config.json') as f:
		data = json.load(f)
	return data['target']

def getMinutes():
	with open('config.json') as f:
		data = json.load(f)
	return int(data['min'])

def getRandomNumber(top):
	for x in range(10):
		return random.randint(1,top)

def getBsObject(html):
	soup = BeautifulSoup(html, 'html.parser')
	return soup

def getHtml(target):
	r = requests.get(target)
	return r.content

def main():

	target  = getTarget()
	minutes = getMinutes()
	seconds = minutes * 100

	html    = getHtml(target)
	soup    = getBsObject(html)
	hrefs soup.find_all('a')

	
	# while True:
		
	# 	#open firefox tab
	# 	firefox = openFireFox(target)
	# 	print border
	# 	print "Opening Firefox for " + str(minutes) + " minutes"
	# 	print " "
	# 	time.sleep(seconds)
	# 	firefox.kill()
	# 	print "Killed Firefox"
	# 	print " "
	# 	print border


if __name__ == '__main__':
    main()