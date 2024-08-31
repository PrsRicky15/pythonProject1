import matplotlib.pyplot as plot
import numpy as np
import math as mth
import pandas as pd

class GaussianPulse:
    def __init__(self, efield0, t0, sigma):
        self.efield0 = efield0
        self.t0 = t0
        self.sigma = sigma
        self.sigma_sq = sigma ** 2  # Precompute sigma squared

    def pulse_time(self, time):
        exponent = -(time - self.t0)**2 / (2 * self.sigma_sq)
        return self.efield0 * np.exp(exponent)

    def pulse_frequency(self, omega):
        exp_factor = np.exp(-1j * omega * self.t0)
        gauss_factor = np.exp(-0.5 * (self.sigma * omega)**2)
        return np.sqrt(2 * np.pi) * self.sigma * self.efield0 * exp_factor * gauss_factor

    def vector_potential(self, time):
        arg = (time - self.t0) / (np.sqrt(2) * self.sigma)
        return -np.sqrt(np.pi / 2) * self.efield0 * self.sigma * (1 + mth.erf(arg))


class TddftProperties:
    def __init__(self, pulse_parameter):
        self.dataset = None
        self.efield0 = pulse_parameter.efield0
        self.t0 = pulse_parameter.t0
        self.sigma = pulse_parameter.sigma

    def read_file(self, file):
        self.dataset = pd.read_csv(file,delim_whitespace=True,header=None)

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
