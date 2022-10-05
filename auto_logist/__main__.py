from auto_logist.driver import get_authorized
from auto_logist.utils import get_settings

SETTINGS = get_settings()


def go_to_offers(web_driver):
    web_driver.get(f'{SETTINGS.URL}carrier#!/offers/all/new')
    return web_driver


if __name__ == '__main__':
    driver = go_to_offers(get_authorized(SETTINGS.URL, SETTINGS.LOGIN, SETTINGS.PASSWORD))

    # driver.quit()
