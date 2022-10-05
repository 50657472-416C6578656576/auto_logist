from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from auto_logist.utils import get_settings


def get_driver():
    chrome_driver_path = get_settings().DRIVER_PATH
    print(chrome_driver_path)
    driver = webdriver.Chrome(chrome_driver_path)
    return driver


def get_authorized(url: str, login: str, password: str) -> WebDriver:
    driver = get_driver()
    driver.get(url)

    login_box = driver.find_element(value='login')
    password_box = driver.find_element(value='password')
    submit_button = driver.find_element(by=By.CLASS_NAME, value='btn-block')

    login_box.send_keys(login)
    password_box.send_keys(password)
    submit_button.click()

    return driver
