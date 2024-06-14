# Basic learning of Python
from modules import machine_learning
from modules import basic_module

dataDir = "data/"


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
def main():
    read_file = dataDir + "Data.csv"
    machine_learning.basic_machine_learn(read_file)
    basic_module.print_hi('The code has executed')
#    basic_module.tip_calculation()


main()
