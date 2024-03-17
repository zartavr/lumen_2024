from filament import Filament
from motor import Motor
from catenary import Catenary

import scipy.optimize as sp
from numpy import sinh, sqrt, cosh
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("TkAgg")
from drawnow import *

catenary_x = []
catenary_y = []


def makeFig():  # Create a function that makes our desired plot
    plt.title("catenary")  # Plot the title
    plt.grid(True)  # Turn the grid on
    plt.xlabel("x")  # Set ylabels
    plt.ylabel("y")  # Set ylabels
    plt.ylim([-10, 1])
    plt.plot(catenary_x, catenary_y, label="length = {0:.2f}".format(length))


if __name__ == "__main__":
    time_tick = 0

    filament = Filament(2)
    extruder = Motor(0, 0.1)
    winder = Motor(0, 0.1)
    catenary = Catenary(1, 0, 1.5)

    extruder.set_velocity(0.5)

    while True:
        time_tick += 1
        if catenary.length >= 18:
            winder.set_velocity(1)
        if catenary.length <= 2:
            winder.set_velocity(0.1)
        delta_velocity = extruder.get_velocity() - winder.get_velocity()

        filament.set_velocity(delta_velocity, 1)
        length = filament.get_length()
        print(f"len: {length:.2f}", end="\t")
        catenary.set_catenary_length(length)
        catenary.find_a()
        print(f"param a: {catenary.param_a}", end="\t")
        print()

        catenary_x = np.linspace(-catenary.param_l / 2, catenary.param_l / 2, 100)
        catenary_y = np.array(
            [
                catenary.catenary(x) - catenary.catenary(catenary_x[0])
                for x in catenary_x
            ]
        )

        drawnow(makeFig)
        plt.pause(0.01)
