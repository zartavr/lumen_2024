from filament import *
from motor import *
import scipy.optimize as sp
from numpy import sinh, sqrt, cosh
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("TkAgg")
from drawnow import *


param_l = 1
param_h = 0
length = param_l
param_eq = sqrt(length**2 - param_h**2) / param_l

B_BRACKET = [1e-3, 2]


def catenary(x, a):
    if x == 0:
        return 0
    return a * cosh(x / a)


def catenary_b(b):
    return 2 * b * sinh(1 / (2 * b)) - param_eq


def catenary_a(b):
    return b * param_l


def find_a(debug: bool = 0) -> float:
    res = sp.root_scalar(catenary_b, bracket=B_BRACKET, method="brentq")

    if debug:
        print(f"a = {catenary_a(res.root)}")
        print(f"iterations: {res.iterations}")

        b_x = np.linspace(B_BRACKET[0], B_BRACKET[1], 1000)
        b_y = np.array([catenary_b(b) + param_eq for b in b_x])
        param_const = np.array([param_eq for b in b_x])

        plt.figure("a_param")
        plt.plot(b_x, b_y)
        plt.plot(b_x, param_const)
        plt.ylim([0, 10])
        plt.show()
    return res.root


catenary_x = []
catenary_y = []


def makeFig():  # Create a function that makes our desired plot
    plt.title("catenary")  # Plot the title
    plt.grid(True)  # Turn the grid on
    plt.xlabel("x")  # Set ylabels
    plt.ylabel("y")  # Set ylabels
    plt.ylim([-10, 1])
    plt.plot(catenary_x, catenary_y, label='length = {0:.2f}'.format(length))


if __name__ == "__main__":
    time_tick = 0

    filament = Filament(2)
    extruder = Motor(0, 0.1)
    winder = Motor(0, 0.1)
    
    extruder.set_velocity(0.5)

    while True:
        time_tick += 1
        if length >= 18:
            winder.set_velocity(1)
        if length <= 2:
            winder.set_velocity(0.1)
        delta_velocity = extruder.get_velocity() - winder.get_velocity()

        filament.set_velocity(delta_velocity, 1)
        length = filament.get_length()
        print(f"len: {length:.2f}", end="\t")
        param_eq = sqrt(length**2 - param_h**2) / param_l
        param_a = find_a()
        print(f"param a: {param_a:.2f}", end="\t")
        print()

        catenary_x = np.linspace(-param_l/2, param_l/2, 100)
        catenary_y = np.array(
            [catenary(x, param_a) - catenary(catenary_x[0], param_a) for x in catenary_x]
        )

        drawnow(makeFig)
        plt.pause(0.01)
