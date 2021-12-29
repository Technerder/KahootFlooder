import time
import argparse
import threading

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class KahootFlooder:

    def __init__(self):
        self.should_run = False

    def dispatch_bot(self, pin, name):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--use-fake-ui-for-media-stream")
        options.add_argument("--log-level=3")
        options.add_argument("test-type")
        options.add_argument("--js-flags=--expose-gc")
        options.add_argument("--enable-precise-memory-info")
        options.add_argument("--disable-default-apps")

        browser = webdriver.Chrome(options=options)
        wait = WebDriverWait(browser, 10)

        browser.get("https://kahoot.it")
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '#game-input')))
        browser.find_element(by=By.CSS_SELECTOR, value='#game-input').send_keys(pin)
        browser.find_element(by=By.CSS_SELECTOR, value='button[type=submit]').click()
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '#nickname')))
        browser.find_element(by=By.CSS_SELECTOR, value='#nickname').send_keys(u'\u200b'.join(name))
        browser.find_element(by=By.CSS_SELECTOR, value='button[type=submit]').click()

        while self.should_run:
            time.sleep(1)

        browser.close()
        browser.quit()

    def start(self, game_pin, bot_count, base_name):
        self.should_run = True
        for i in range(bot_count):
            threading.Thread(target=self.dispatch_bot, args=(game_pin, f'{base_name}{i}')).start()

    def stop(self):
        self.should_run = False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple script to flood kahoot games')
    parser.add_argument('--pin', type=int, required=True, help='Kahoot game pin')
    parser.add_argument('--count', type=int, required=True, help='Amount of bots')
    parser.add_argument('--prefix', type=str, required=True, help='Prefix for bots (name=prefix{botNumber})')
    args = parser.parse_args()
    flooder = KahootFlooder()
    try:
        print('Starting...')
        flooder.start(args.pin, args.count, args.prefix)
    except KeyboardInterrupt:
        print('Exiting...', end='')
        flooder.stop()
        print('Done!')
    # python kahoot_flooder.py --pin=3803477 --count=5 --prefix="bot_gba"
