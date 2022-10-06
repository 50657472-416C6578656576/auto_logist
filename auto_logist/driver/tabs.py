from selenium.webdriver.remote.webdriver import WebDriver


def open_new_tab(driver: WebDriver, url: str = '') -> None:
    driver.execute_script(f'window.open("{url}");')
    driver.switch_to.window(driver.window_handles[-1])


def close_current_tab(driver: WebDriver) -> None:
    driver.execute_script("window.close();")
    driver.switch_to.window(driver.window_handles[-1])
