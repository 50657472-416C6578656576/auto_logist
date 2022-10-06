from time import sleep

from auto_logist.driver import get_authorized, go_to_offers, get_driver
from auto_logist.parser import handle_table
from auto_logist.utils import get_settings

SETTINGS = get_settings()


def main():
    driver = go_to_offers(get_authorized(SETTINGS.TARGET_HOST, SETTINGS.LOGIN, SETTINGS.PASSWORD))
    sleep(3)    # TODO: переделать на Wait For
    handle_table(driver)


def test():
    driver = get_driver()
    driver.get('file:///C:/Users/Petr/Yandex/auto-logist/html-pages/Logist%20Pro%20-.html#!/')
    handle_table(driver)


if __name__ == '__main__':
    test()
    # driver.quit()
