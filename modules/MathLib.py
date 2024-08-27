import math
import numpy as np

class Point:
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
        return Point(self.x * a, self.y * a, self.z * a)

    def new_point(self, other, scale):
        dist = self.distance(other)
        val = scale/dist
        return Point(self.x + val * (other.x - self.x),
                     self.y + val * (other.y - self.y),
                     self.z + val * (other.z - self.z))

class GridGenerator:
    def __init__(self, grd_min, grd_max, ngrid):
        self.grd_min = grd_min
        self.grd_max = grd_max
        self.ngrid = ngrid
        self.delta_grid = (grd_max - grd_min) / ngrid
        self.grid = None

    @classmethod
    def from_length(cls, length, ngrid):
        grd_min = -length/2
        grd_max = length/2
        return cls(grd_min, grd_max, ngrid)

    def generate_grid(self):
        self.grid = np.linspace(self.grd_min, self.grd_max, self.ngrid)

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