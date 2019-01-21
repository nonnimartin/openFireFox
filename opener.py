import webbrowser as wb
import os
import subprocess
import time

def openFireFox():
	p = subprocess.Popen(["firefox", "http://www.google.com"])
	return p

def main():
	#open firefox tab
	firefox = openFireFox()
	#time.sleep(10)
	#firefox.kill()


if __name__ == '__main__':
    main()