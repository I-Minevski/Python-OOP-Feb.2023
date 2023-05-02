class Vehicle():
    DEFAULT_FUEL_CONSUMPTION: [float, int] = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption: float = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers) -> None:
        consumed_fuel = self.fuel_consumption * kilometers
        if self.fuel >= consumed_fuel:
            self.fuel -= consumed_fuel

