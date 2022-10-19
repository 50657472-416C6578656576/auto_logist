from time import sleep

from selenium.common import StaleElementReferenceException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.wait import WebDriverWait

from auto_logist.driver import open_new_tab, close_current_tab
from auto_logist.utils.get_digits import get_value

YANDEX_CONFIG = {
    'URL': 'https://yandex.ru/maps/routes/',
    'FROM_XPATH': '//input[@placeholder="Откуда"]',
    'TO_XPATH': '//input[@placeholder="Куда"]',
    'KILOMETERS_BLOCK_CLASS': 'auto-route-snippet-view__route-subtitle',
    'START': 'Москва',
}


def open_new_map(driver: WebDriver) -> None:
    open_new_tab(driver)
    driver.get(YANDEX_CONFIG['URL'])
    print('opened')
    sleep(3)


def send_to_input(wait: WebDriverWait, web_driver: WebDriver, find_by: By, what_to_find: str, value_to_send: str):
    wait.until(lambda driver: driver.find_element(find_by, what_to_find))
    while True:
        try:
            form = web_driver.find_element(find_by, what_to_find)
            form.send_keys(value_to_send)
            break
        except StaleElementReferenceException:
            continue


def distance(web_driver: WebDriver, start: str = YANDEX_CONFIG['START'], finish: str = 'Москва') -> float | None:
    wait = ui.WebDriverWait(web_driver, 10)
    open_new_tab(web_driver)
    web_driver.get(YANDEX_CONFIG['URL'])

    send_to_input(wait, web_driver, By.XPATH, YANDEX_CONFIG['FROM_XPATH'], f'{start}\ue007')
    send_to_input(wait, web_driver, By.XPATH, YANDEX_CONFIG['TO_XPATH'], f'{finish}\ue007')

    kilometers = wait.until(lambda driver: driver.find_element(By.CLASS_NAME, YANDEX_CONFIG['KILOMETERS_BLOCK_CLASS']))
    value = get_value(kilometers.text)

    close_current_tab(web_driver)
    return value
