class Filament:
    def __init__(self, length) -> None:
        self.dV = 0
        self.length = length

    def set_velocity(self, velocity: float, time: int) -> None:
        self.dV = velocity
        self._calc_length(time)

    def get_length(self, time: int = 0) -> float:
        self._calc_length(time)
        return self.length

    def _calc_length(self, time: int):
        self.length = self.length + self.dV * time


if __name__ == "__main__":
    test = Filament(1)

    assert (test.get_length() - 1) < 1e-4
    
    test.set_velocity(0.1, 4)
    assert (test.get_length() - 1.4) < 1e-4
    
    test.set_velocity(0.2, 2)
    assert (test.get_length() - 1.8) < 1e-4

    test.set_velocity(-0.1, 2)
    assert (test.get_length() - 1.6) < 1e-4    
