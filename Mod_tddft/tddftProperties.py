import pandas as pd

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

