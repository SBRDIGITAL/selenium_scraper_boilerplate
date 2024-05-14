import time

from selenium.webdriver import Chrome


def open_url(browser: Chrome, url: str) -> None:
    browser.get(url)
    time.sleep(30)