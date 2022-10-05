from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


def get_table_rows(driver: WebDriver) -> list:
    rows = driver.find_elements(By.TAG_NAME, 'tr')
    for row in rows:
        print(row.text[:20])

    return rows
