import matplotlib.pyplot as plot
import numpy as np
import pandas as pd
from scipy.special import erf


class GaussianPulse:
    def __init__(self, efield0, t0, sigma):
        self.efield0 = efield0
        self.t0 = t0
        self.sigma = sigma
        self.sigma_sq = sigma ** 2
        self.sigma_sqrt2 = sigma * np.sqrt(2)
        self.prefactor = np.sqrt(2 * np.pi) * sigma * efield0
        self.erf_prefactor = -np.sqrt(np.pi / 2) * efield0 * sigma

    def pulse_time(self, time):
        return self.efield0 * np.exp(-(time - self.t0) ** 2 / (2 * self.sigma_sq))

    def pulse_frequency(self, omega):
        return self.prefactor * np.exp(-1j * omega * self.t0 - 0.5 * (self.sigma * omega) ** 2)

    def vector_potential(self, time):
        return self.erf_prefactor * (1 + erf((time - self.t0) / self.sigma_sqrt2))

    def vecpoten_Grid(self, total_time, nt_grid):
        t_grid = np.linspace(0., total_time, nt_grid)
        return self.vector_potential(t_grid)

    def field_time_Grid(self, total_time, nt_grid):
        t_grid = np.linspace(0, total_time, nt_grid)
        return t_grid, self.pulse_time(t_grid)

    def field_frequency_Grid(self, omega_min, omega_max, n_points):
        omega_grid = np.linspace(omega_min, omega_max, n_points)
        return self.pulse_frequency(omega_grid)

    def plot_td_efield_pulse(self):
        [x,y] = self.field_time_Grid(20,100)
        #Plot the data on a grid
        plot.figure(figsize=(8, 6))
        plot.plot(x,y)
        plot.grid(True)
        plot.xlabel('Time in a.u.')
        plot.ylabel('<o>(t)')
        plot.title('Expectation value o(t)')
        plot.show()


class TddftProperties(GaussianPulse):
    def __init__(self, efield0, t0, sigma):
        super().__init__(efield0, t0, sigma)
        self.dataset = None

    def decaying_function(self):
        pass

    def read_file(self, file):
        self.dataset = pd.read_csv(file, delim_whitespace=True, header=None)

    def plot_td_expectation_value(self):
        x = self.dataset.iloc[:, 1]  # Second column
        y = self.dataset.iloc[:, 2]  # Third column
        #Plot the data on a grid
        plot.figure(figsize=(8, 6))
        plot.scatter(x, y, c='green', marker='x')
        # Adding grid, labels, and title
        plot.grid(True)
        plot.xlabel('Time in a.u.')
        plot.ylabel('<o>(t)')
        plot.title('Expectation value o(t)')
        # Show the plot
        plot.show()
