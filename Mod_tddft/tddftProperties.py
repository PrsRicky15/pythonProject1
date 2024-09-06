import matplotlib.pyplot as plot
import numpy as np
import pandas as pd
from scipy.special import erf

class Plot2d:
    @staticmethod
    def plot_with_line(data):
        plot.figure(figsize=(8, 6))
        plot.plot(data[:,0], data[:,1], label="val")
        plot.grid(True)
        plot.legend()
        plot.xlabel('Time in a.u.')
        plot.ylabel('<o>(t)')
        plot.title('Expectation value o(t)')
        plot.show()

    @staticmethod
    def plot_with_point(data):
        plot.figure(figsize=(8, 6))
        plot.scatter(data[:,0], data[:,1], c='green', marker='x')
        plot.grid(True)
        plot.xlabel('Time in a.u.')
        plot.ylabel('<o>(t)')
        plot.title('Expectation value o(t)')
        plot.show()

    @staticmethod
    def plot_with_linepoint(data):
        plot.figure(figsize=(8, 6))
        plot.plot(data[:,0], data[:,1], label="val", linestyle='-', color='blue')
        plot.scatter(data[:,0], data[:,1], c='green', marker='x')
        plot.grid(True)
        plot.xlabel('Time in a.u.')
        plot.ylabel('<o>(t)')
        plot.title('Expectation value o(t)')
        plot.legend()
        plot.show()


class GaussianPulse(Plot2d):
    def __init__(self, efield0, t0, sigma):
        self.efield0 = efield0
        self.t0 = t0
        self.sigma = sigma
        self.__sigma_sq = sigma ** 2
        self.__sigma_sqrt2 = sigma * np.sqrt(2)
        self.__prefactor = np.sqrt(2 * np.pi) * sigma * efield0
        self.__erf_prefactor = -np.sqrt(np.pi / 2) * efield0 * sigma

    def pulse_time(self, time):
        return self.efield0 * np.exp(-(time - self.t0) ** 2 / (2 * self.__sigma_sq))

    def pulse_frequency(self, omega):
        return self.__prefactor * np.exp(-1j * omega * self.t0 - 0.5 * (self.sigma * omega) ** 2)

    def vector_potential(self, time):
        return self.__erf_prefactor * (1 + erf((time - self.t0) / self.__sigma_sqrt2))

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
        tgrid, efield = self.field_time_Grid(16,1000)
        data = np.column_stack((tgrid, efield))
        Plot2d.plot_with_line(data)



class TddftProperties(GaussianPulse):
    def __init__(self, efield0, t0, sigma):
        super().__init__(efield0, t0, sigma)
        self.__dataset = None

    def _decaying_function(self):
        pass

    def read_file(self, file):
        self.__dataset = pd.read_csv(file, delim_whitespace=True, header=None)

    def plot_td_expectation_value(self, data=None):
        if self.__dataset is None:
            raise ValueError("Dataset is not loaded. Please call read_file() before plotting.")

        # Use the dataset directly if no data is provided
        if data is None:
            data = self.__dataset.to_numpy()

        Plot2d.plot_with_line(data)
