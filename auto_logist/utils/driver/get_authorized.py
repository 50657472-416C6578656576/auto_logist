from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


def get_authorized(url: str, login: str, password: str) -> WebDriver:
    driver = webdriver.Chrome()
    driver.get(url)

    login_box = driver.find_element(value='login')
    password_box = driver.find_element(value='password')
    submit_button = driver.find_element(by=By.CLASS_NAME, value='btn-block')

    login_box.send_keys(login)
    password_box.send_keys(password)
    submit_button.click()

    return driver
