from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

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


def get_rows(driver: WebDriver) -> list[WebElement]:
    rows = driver.find_elements(By.TAG_NAME, 'tr')
    return rows


def handle_table(driver: WebDriver) -> None:
    for row in get_rows(driver):
        if (parsed := parse_row(row)) and (offer := Offer.from_dict(parsed)):
            print(offer)
