from filament import *
from motor import *
import scipy.optimize as sp
from numpy import sinh, sqrt


param_l = 5
param_h = 0.04
length = 21
const_c = sqrt(length**2 - param_h**2) / param_l


def catenary_b(b):
    return 2 * b * sinh(1 / (2 * b)) - const_c


def catenary_a(b):
    return b * param_l


if __name__ == "__main__":
    filament = Filament(1)

    extruder = Motor(0.1, 0.1)

    winder = Motor(0.1, 0.1)

    res = sp.root_scalar(catenary_b, bracket=[1e-3, 2], method="brentq")

    print(f"a = {catenary_a(res.root)}")
    print(f"iterations: {res.iterations}")
