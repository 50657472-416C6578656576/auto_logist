from dataclasses import dataclass

from auto_logist.utils import get_settings

SETTINGS = get_settings()


@dataclass
class Offer:
    id: str
    kilograms: int
    price: int
    destination: str

    def __post_init__(self):
        self.tons = self.kilograms / 1000
        self._calculate_total_price()
        self.kilometers = ...

    def _calculate_total_price(self):
        self.total_price = self.tons * self.price

    def criterion(self, new_price) -> float:
        return (self.tons * new_price) / self.kilometers

    def update_price(self, new_price) -> bool:
        if self.criterion(new_price) < SETTINGS.MIN_CRITERION:
            return False
        self.price = new_price
        self._calculate_total_price()
        return True
