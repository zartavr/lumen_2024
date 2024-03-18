from numpy import sinh, sqrt, cosh
import numpy as np
import scipy.optimize as sp
import matplotlib.pyplot as plt


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
        self.pos_y = y
        self.param_a = self.__get_a(self.pos_x, y)
        self.length = self.__calc_length(self.param_a, self.param_l, self.param_h)
        if self.length_prev != 0:
            self.velocity = self.__calc_velocity(self.length, self.length_prev, self.dt)
        self.length_prev = self.length

    def __get_a(self, x, y) -> float:
        if x == 0:
            return y
        return self.__find_param_a(x, y)

    def __get_param_eq(self):
        return self.pos_y / self.pos_x

    def __catenary_c(self, c):
        param_eq = self.__get_param_eq()
        return c * cosh(1 / c) - param_eq

    def __catenary_a(self, c):
        return c * self.pos_x

    def __find_param_a(self, x, y, debug: bool = False):
        C_BRACKET = [1e-6, 0.834] # ref https://www.desmos.com/calculator/2kehfhnud9
        
        if debug:
            # print(f"a = {self.__catenary_a(res.root)}")
            # print(f"iterations: {res.iterations}")

            c_x = np.linspace(C_BRACKET[0], C_BRACKET[1], 1000)
            c_y = np.array([self.__catenary_c(c) + self.__get_param_eq() for c in c_x])
            param_const = np.array([self.__get_param_eq() for c in c_x])

            plt.figure("a_param")
            plt.plot(c_x, c_y)
            plt.plot(c_x, param_const)
            plt.ylim([0, 10])
            plt.show()

        res = sp.root_scalar(self.__catenary_c, bracket=C_BRACKET, method="brentq")


        return self.__catenary_a(res.root)

    def __calc_length(self, a, l, h):
        return sqrt((2 * a * sinh(l / (2 * a))) ** 2 + h**2)

    def __calc_velocity(self, length, length_prev, dt):
        return (length - length_prev) / dt
