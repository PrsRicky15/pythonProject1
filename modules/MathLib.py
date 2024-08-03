import numpy as np

class GridGenerator:
    def __init__(self, xmin, xmax, ngrid):
        self.xmin = xmin
        self.xmax = xmax
        self.ngrid = ngrid
        self.grid = None

    @classmethod
    def from_length(cls, length, ngrid):
        xmin = 0
        xmax = length
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
