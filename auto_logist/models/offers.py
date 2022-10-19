from dataclasses import dataclass

from selenium.webdriver.chrome.webdriver import WebDriver

from auto_logist.utils import get_settings
from auto_logist.utils.maps.yandex import distance

SETTINGS = get_settings()


def get_destination(str_list: list[str]) -> str:
    return ' '.join(str_list)


def get_price(str_list: list[str]) -> int:
    before = str_list.index('Лучшая цена')
    target, ptr = str_list[before + 1], 0
    while ptr + 1 < len(target) and target[ptr].isdigit():
        ptr += 1
    result = int(target[:ptr])
    return result


def get_weight(str_list: list[str]) -> tuple[int, bool]:
    ptr, string = 0, ''.join(str_list).upper()
    if 'НАВАЛ' in string:
        return 0, False
    while ptr + 1 < len(string) and string[ptr].isdigit():
        ptr += 1
    result = int(string[:ptr])
    return result, True


@dataclass
class Offer:
    id: str
    kilograms: int
    price: int
    destination: str

    @staticmethod
    def from_dict(some_dict: dict):
        kilograms, acceptable = get_weight(some_dict['Груз'])
        if not acceptable:
            return None
        offer_id = some_dict['Номер'][0]
        price = get_price(some_dict['Цена'])
        destination = get_destination(some_dict['Выгрузка'])
        return Offer(
            offer_id,
            kilograms,
            price,
            destination,
        )

    def __post_init__(self):
        self.tons = self.kilograms / 1000
        self.__calculate_total_price()
        self.kilometers = None

    def get_kilometers(self):
        return self.kilometers

    def update_kilometers(self, driver: WebDriver):
        self.kilometers = distance(driver, finish=self.destination)
        return self.kilometers

    def __calculate_total_price(self):
        self.total_price = self.tons * self.price

    def criterion(self, new_price) -> float:
        return (self.tons * new_price) / self.get_kilometers()

    def update_price(self, new_price) -> bool:
        if self.criterion(new_price) < SETTINGS.MIN_CRITERION:
            return False
        self.price = new_price
        self.__calculate_total_price()
        return True

    def __repr__(self):
        return f'<{self.id}, total={self.total_price}RUB, km={self.kilometers}>'
