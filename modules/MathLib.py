import math

import numpy as np

class point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.z})"

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)

    def same(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def scale(self, a):
        return point(self.x * a, self.y * a, self.z * a)

class GridGenerator:
    def __init__(self, xmin, xmax, ngrid):
        self.xmin = xmin
        self.xmax = xmax
        self.ngrid = ngrid
        self.dgrid = (xmax-xmin)/ngrid
        self.grid = None

    @classmethod
    def from_length(cls, length, ngrid):
        xmin = -length/2
        xmax = length/2
        return cls(xmin, xmax, ngrid)

    def generate_grid(self):
        self.grid = np.linspace(self.xmin, self.xmax, self.ngrid)

    def display_grid(self):
        if self.grid is None:
            print("Grid not generated yet.")
        else:
            print("Generated Grid:")
            print(self.grid)

    def save_grid_to_file(self, filename):
        if self.grid is None:
            print("Grid not generated yet.")
        else:
            np.savetxt(filename, self.grid)
            print(f"Grid saved to {filename}")