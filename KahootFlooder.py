from time import sleep
from threading import Thread
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

numberOfBots = 25
baseName = 'Bot'
gamePin = '635746'

delayBeforeLeaving = 20
delayBetweenActions = 2.5

def createBot(pin, name):

    options = Options()
    options.add_argument("--headless")
    options.add_argument("test-type")
    options.add_argument("--js-flags=--expose-gc")
    options.add_argument("--enable-precise-memory-info")
    options.add_argument("--disable-default-apps");
    
    browser = webdriver.Chrome(chrome_options = options)
    browser.get("http://kahoot.it")
    
    sleep(delayBetweenActions)
    
    browser.find_element_by_css_selector('#inputSession').send_keys(pin)
    browser.find_element_by_css_selector('.btn-greyscale').click()
    
    sleep(delayBetweenActions)
    
    browser.find_element_by_css_selector('#username').send_keys((u'\u200b').join(name))
    browser.find_element_by_css_selector('.btn-greyscale').click()

    sleep(delayBeforeLeaving)

    browser.close()
    
for i in range(numberOfBots): 
    
    Thread(target = lambda : createBot(gamePin, baseName + str(i))).start()
