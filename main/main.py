# Basic learning of Python
from modules import machine_learning
from modules.MathLib import GridGenerator


def grid_fun():
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


dataDir = "data/"


def Machine_Learning():
    read_file = dataDir + "Data.csv"
    machine_learning.basic_machine_learn(read_file)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #    grid_fun()
    #    Machine_Learning()
    var = 0
