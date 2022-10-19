from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
import selenium.webdriver.support.ui as ui
import selenium.common.exceptions as exceptions
from selenium.webdriver.support.wait import WebDriverWait

from auto_logist.models import Offer


def parse_row(row: WebElement) -> dict[str, list[str]]:
    elements = row.find_elements(By.TAG_NAME, 'td')
    parsed = dict()
    for element in elements:
        if not (element_class := element.get_attribute('class')):
            key, *value = element.text.strip().split('\n')
            parsed[key] = value
        elif element_class == 'buttons':
            ...
    return parsed


def get_rows(driver: WebDriver, wait: WebDriverWait) -> list[WebElement]:
    try:
        rows = wait.until(lambda web_driver: web_driver.find_elements(By.TAG_NAME, 'tr'))
    except exceptions.TimeoutException:
        return []
    return rows


def handle_table(driver: WebDriver) -> None:
    wait = ui.WebDriverWait(driver, 10)
    wait.until(lambda web_driver: web_driver.find_elements(By.TAG_NAME, 'thead'))
    for row in get_rows(driver, wait):
        if (parsed := parse_row(row)) and (offer := Offer.from_dict(parsed)):
            offer.update_kilometers(driver)
            print(offer)
