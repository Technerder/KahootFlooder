from time import sleep
from threading import Thread
from selenium import webdriver

numberOfBots = 1
baseName = 'Bot'
gamePin = ''

delayBeforeLeaving = 20
delayBetweenActions = 2.5

def createBot(pin, name):
    
    browser = webdriver.PhantomJS()
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
