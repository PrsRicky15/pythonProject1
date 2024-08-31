# Basic learning of Python
from Mod_tddft import tddftProperties
from modules import machine_learning

dataDir = "data/"
def Machine_Learning():
    read_file = dataDir + "Data.csv"
    machine_learning.basic_machine_learn(read_file)


def TD_properties_Result():
    efield_params = tddftProperties.GaussianPulse(0.0005, 8, 0.05)
    tddft_res = tddftProperties.TddftProperties(efield_params)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #    Machine_Learning()
    TD_properties_Result()
