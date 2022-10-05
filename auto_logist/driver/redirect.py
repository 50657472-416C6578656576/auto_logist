from selenium.webdriver.remote.webdriver import WebDriver

from auto_logist.utils import get_settings

SETTINGS = get_settings()


def go_to_offers(web_driver: WebDriver) -> WebDriver:
    web_driver.get(f'{SETTINGS.TARGET_HOST}{SETTINGS.OFFER_URL_PATH}')
    return web_driver
