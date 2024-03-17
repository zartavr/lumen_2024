from numpy import sinh, sqrt


class Controller:
    def __init__(self, d_support_length, d_support_height, x_pos=0) -> None:
        # ref docs/attachments/image.png
        self.param_l = d_support_length
        self.param_h = d_support_height
        self.pos_x = x_pos
        
        self.length = 0
        self.param_a = 0

        self.length_prev = 0
        self.dt = 1  # sec

        self.velocity = 0

    def get_velocity(self):
        return self.velocity
    
    def get_length(self):
        return self.velocity
    
    def get_param_a(self):
        return self.velocity

    def update(self, y):
        self.param_a = self.__get_a(self.pos_x, y)
        self.length = self.__calc_length(self.param_a, self.param_l, self.param_h)
        if self.length_prev != 0:
            self.velocity = self.__calc_velocity(self.length, self.length_prev, self.dt)
        self.length_prev = self.length

    def __get_a(self, x, y) -> float:
        if x == 0:
            return y
        return self.__calc_param_a(x, y)

    def __calc_param_a(self, x, y):
        print("Not implemented")
        return 0

    def __calc_length(self, a, l, h):
        return sqrt((2 * a * sinh(l / (2 * a))) ** 2 + h ** 2)

    def __calc_velocity(self, length, length_prev, dt):
        return (length - length_prev) / dt
