from selenium import webdriver
from auto_logist.utils import get_settings

driver = webdriver.Chrome()


def auth():
    settings = get_settings()
    driver.get(settings.URL)

    login_box = driver.find_element(value='login')
    password_box = driver.find_element(value='password')
    submit_button = driver.find_element(by='class name', value='btn-block')

    login_box.send_keys(settings.LOGIN)
    password_box.send_keys(settings.PASSWORD)
    submit_button.click()


if __name__ == '__main__':
    auth()
