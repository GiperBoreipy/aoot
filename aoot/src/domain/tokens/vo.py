from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Ticker:
    value: str

    @property
    def instrument_id(self) -> str:
        return self.value + "-USDT"
