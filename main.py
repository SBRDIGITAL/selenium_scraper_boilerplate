import time
import traceback

from selenium.webdriver import Chrome

from core.driver import get_driver as gd

from core.scrapping.open_url import open_url



if __name__ == "__main__":
    try:
        url:str = 'https://whatismyipaddress.com/'
        browser:Chrome = gd.get_driver(headless=False)
        open_url(browser=browser, url=url)
    except:
        traceback.print_exc()

    finally:
        try:
            browser.close()
        except:
            traceback.print_exc()
            exit()