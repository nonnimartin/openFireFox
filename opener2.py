import subprocess
import sys
import time
import json
import random
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

def openFireFoxWebDriver(target):
    capa = DesiredCapabilities.FIREFOX
    capa["pageLoadStrategy"] = "none"
    driver = webdriver.Firefox(desired_capabilities=capa)
    driver.get(target)
    return driver

def getHtmlElement(driver, element, target):

    #create and populate list to randomly select add to click
    ad_elems_list = list()

    #sleep to allow page to load MAY NOT BE NEEDED NOW
    time.sleep(15)
    all_iframes = driver.find_elements_by_tag_name("iframe")

    # get all iframes and search for adds
    for this_iframe in all_iframes:
        try:
            id_attr = this_iframe.get_attribute("id")
            print(id_attr)
            if str(id_attr).startswith("google_ads_iframe_"):
                ad_elems_list.append(this_iframe)
                #this click is working but handle differently
                #this_iframe.click()
        except:
            #handle exceptions
            pass

    # get random number within range of ad elements list
    elems_list_length = len(ad_elems_list)
    print('length of list = ' + str(elems_list_length))
    rand_num          = random.randint(0, elems_list_length - 1)
    return ad_elems_list[rand_num]

def openFireFox(target):
    p = subprocess.Popen(["firefox", target])
    return p

def getTarget():
    with open('config.json') as f:
        data = json.load(f)
    f.close()
    return data['target']

def getSelector():
    with open('config.json') as f:
        data = json.load(f)
    f.close()
    return data['selector']

def getElType():
    with open('config.json') as f:
        data = json.load(f)
    f.close()
    return data['elType']

def getAttr():
    with open('config.json') as f:
        data = json.load(f)
    f.close()
    return data['attr']

def getMinutes():
    with open('config.json') as f:
        data = json.load(f)
    f.close()
    return int(data['min'])

def getRandomNumber(top):
    for x in range(top):
        return random.randint(1,top)

def getBsObject(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def getHtml(target):
    r = requests.get(target)
    return r.content

border   = "======================================================="
target   = getTarget()
selector = getSelector()
elType   = getElType()
attr     = getAttr()

def main():

    #minutes = getMinutes()

    html    = getHtml(target)
    soup    = getBsObject(html)
    hrefs   = soup.find_all(elType)

    newsLinks   = list()

    for link in hrefs:
        if link.has_attr(attr):
            thisLink = str(link[attr])
            if thisLink.startswith(selector):
                newsLinks.append(thisLink)

    linksLen  = len(newsLinks)

    while True:

        randomNum = getRandomNumber(linksLen - 1)
        page = target + newsLinks[randomNum]

        #open firefox tab
        thisDriver = openFireFoxWebDriver(page)

        thisElem = getHtmlElement(thisDriver, 'video', target)

        #click selected ad
        thisElem.click()

        #thisDriver.quit()


if __name__ == '__main__':
    main()