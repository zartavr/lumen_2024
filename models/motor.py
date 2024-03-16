class Motor:
    def __init__(self, angular_velocity: float, radius: float) -> None:
        self.omega = angular_velocity
        self.r = radius

    def set_rotation(self, angular_velocity: float) -> None:
        self.omega = angular_velocity

    def set_radius(self, radius: float) -> None:
        self.r = radius
        
    def set_velocity(self, velocity) -> None:
        self.omega = velocity / self.r

    def get_velocity(self) -> float:
        return self.r * self.omega
