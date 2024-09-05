# modules/basic_module.py
import numpy as np
from modules.MathLib import GridGenerator as Grid

class Function:
    def __init__(self, cen, sigma):
        self.cen = cen
        self.sigma = sigma

    def gaussian_function(self, v0, xgrid):
        return v0 * np.exp(-(xgrid - self.cen)**2/(2 * (self.sigma**2)))

    def softcore_poten(self, za, xgrid):
        return - za/np.sqrt((xgrid-self.cen)**2 + self.sigma**2)

class Potential(Grid, Function):
    def __init__(self, grid_min, grid_max, ngrid, cen, sigma):
        Grid.__init__(self, grid_min, grid_max, ngrid)
        Function.__init__(self, cen, sigma)

    @classmethod
    def poten_from_length(cls, length, ngrid, cen, sigma):
        grid_res = Grid.from_length(length, ngrid)
        return cls(grid_res.grd_min, grid_res.grd_max, ngrid, cen, sigma)
