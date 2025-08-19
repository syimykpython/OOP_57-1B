class Distance:
    _units_to_meters = {
        "cm": 0.01,
        "m": 1,
        "km": 1000
    }

    def __init__(self, value: float , unit: str = 'm'):
        if unit not in self._units_to_meters:
            raise ValueError(f"Не поддерживается {unit}")
        self.value = value
        self.unit = unit

    def __str__(self):
        return  f'{self.value} {self.unit}'

    def to_metters(self):
        return self.value * self._units_to_meters[self.unit]

    @staticmethod
    def convert(value_in_metters, unit):
        return  value_in_metters / Distance._units_to_meters[unit]

    def __add__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        total_metters = self.to_metters() + other.to_metters()
        return Distance(self.convert(total_metters, self.unit), self.unit)


    def __sub__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        total_metters = self.to_metters() - other.to_metters()
        if total_metters < 0:
            raise ValueError('результат не может быть отрицательным')
        return Distance(self.convert(total_metters, self.unit), self.unit)


    def __eq__(self, other):
        return self.to_metters() == other.to_metters()

    def __lt__(self, other):
        return self.to_metters() < other.to_metters()

    def __le__(self, other):
        return self.to_metters() <= other.to_metters()

    def __gt__(self, other):
        return self.to_metters() > other.to_metters()

    def __ge__(self, other):
        return self.to_metters() >= other.to_metters()

