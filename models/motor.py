class Motor:
    def __init__(self, angular_velocity: float, radius: float) -> None:
        self.omega = angular_velocity
        self.r = radius

    def set_rotation(self, angular_velocity: float) -> None:
        self.omega = angular_velocity

    def set_radius(self, radius: float) -> None:
        self.r = radius

    def get_velocity(self) -> float:
        return self.set_radius * self.omega
