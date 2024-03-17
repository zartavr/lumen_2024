from numpy import cosh, sinh, sqrt
import scipy.optimize as sp
import numpy as np
import matplotlib.pyplot as plt


class Catenary:
    def __init__(self, d_support_length, d_support_height, length) -> None:
        # ref docs/attachments/image.png
        self.param_l = d_support_length
        self.param_h = d_support_height
        self.length = length
        self.param_a = 0
        self.B_BRACKET = [1e-6, 1 / self.param_l]

    def set_catenary_length(self, length):
        self.length = length

    def set_param_a(self, a):
        self.param_a = a

    def catenary(self, x):
        # if self.param_a == 0:
        #     self.find_a()
        if x == 0:
            return 0
        return self.param_a * cosh(x / self.param_a)

    def __get_param_eq(self):
        return sqrt(self.length**2 - self.param_h**2) / self.param_l

    def __catenary_b(self, b):
        param_eq = self.__get_param_eq()
        return 2 * b * sinh(1 / (2 * b)) - param_eq

    def catenary_a(self, b):
        return b * self.param_l

    def find_a(self, debug: bool = 0) -> float:
        res = sp.root_scalar(self.__catenary_b, bracket=self.B_BRACKET, method="brentq")
        
        self.param_a = self.catenary_a(res.root)

        if debug:
            print(f"a = {self.catenary_a(res.root)}")
            print(f"iterations: {res.iterations}")

            b_x = np.linspace(self.B_BRACKET[0], self.B_BRACKET[1], 1000)
            b_y = np.array([self.__catenary_b(b) + self.__get_param_eq() for b in b_x])
            param_const = np.array([self.__get_param_eq() for b in b_x])

            plt.figure("a_param")
            plt.plot(b_x, b_y)
            plt.plot(b_x, param_const)
            plt.ylim([0, 10])
            plt.show()
        return self.param_a
