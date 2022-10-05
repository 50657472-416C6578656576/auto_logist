from auto_logist.driver import get_authorized, go_to_offers
from auto_logist.utils import get_settings

SETTINGS = get_settings()


if __name__ == '__main__':
    driver = go_to_offers(get_authorized(SETTINGS.TARGET_HOST, SETTINGS.LOGIN, SETTINGS.PASSWORD))

    # driver.quit()
