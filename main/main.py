# Basic learning of Python
from Mod_tddft import tddftProperties as TdProp
from modules.machine_learning import basic_machine_learn as machlearn
from modules.basic_module import Potential as Poten

dataDir = "data/"
def Machine_Learning():
    read_file = dataDir + "Data.csv"
    machlearn(read_file)

def potential_check():
    potenital = Poten(-5.,5.,20)
    potenital.generate_grid()

def TD_properties_Result():
    efield_params = TdProp.GaussianPulse(0.0005, 8, 0.05)
    grid = efield_params.field_frequency_Grid(-3,3,30)
    efield_params.plot_td_efield_pulse()
    print(grid)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    TD_properties_Result()
