# modules/basic_module.py
import numpy as np
from modules.MathLib import GridGenerator as Grid

class Function:
    def __init__(self, sigma=1, center=0):
        self.cen = center
        self.sigma = sigma

    def gaussian_function(self, v0, xgrid):
        return v0 * np.exp(-(xgrid - self.cen)**2 / (2 * (self.sigma ** 2)))

    def softcore_poten(self, za, xgrid):
        return - za/np.sqrt((xgrid-self.cen) ** 2 + self.sigma ** 2)

    def harmonic_osc(self, xgrid):
        return self.sigma * (xgrid - self.cen)**2

    @staticmethod
    def polynomial(xgrid, coef_vec):
        res = 0
        for aval in coef_vec:
            res = res * xgrid + aval
        return res


class Potential(Grid, Function):
    def __init__(self, grid_min, grid_max, ngrid, sigma=1, center=0):
        Grid.__init__(self, grid_min, grid_max, ngrid)
        Function.__init__(self, sigma, center)

    @classmethod
    def poten_from_length(cls, length, ngrid, sigma, center):
        grid_res = Grid.from_length(length, ngrid)
        return cls(grid_res.grd_min, grid_res.grd_max, ngrid, sigma, center)

    def display_grid(self):
        pass