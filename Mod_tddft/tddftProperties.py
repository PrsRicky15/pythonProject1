import pandas as pd
import matplotlib.pyplot as plot

class ExternalField:
    def __init__(self, efield0, t0, sigma):
        self.efield0 = efield0
        self.t0 = t0
        self.sigma = sigma

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
