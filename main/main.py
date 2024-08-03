# Basic learning of Python
from modules import machine_learning
from modules import basic_module
from modules.MathLib import GridGenerator

dataDir = "data/"

from modules import MathLib

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
def main():
    # Example usage
    # Creating instance using the first constructor
    grid1 = GridGenerator(0, 10, 5)
    grid1.generate_grid()
    grid1.display_grid()
    grid1.save_grid_to_file("grid1.txt")

    # Creating instance using the second constructor
    grid2 = GridGenerator.from_length(10, 5)
    grid2.generate_grid()
    grid2.display_grid()
    grid2.save_grid_to_file("grid2.txt")


    read_file = dataDir + "Data.csv"
    machine_learning.basic_machine_learn(read_file)
    basic_module.print_hi('The code has executed')
    basic_module.tip_calculation()

main()
