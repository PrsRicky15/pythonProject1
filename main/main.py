# Basic learning of Python
from modules import machine_learning
from modules.MathLib import GridGenerator, Point


def grid_fun():
    p2 = Point(0.89605, 0.57104, 0.54298)
    p1 = Point(0.60394, 0.42899, 0.54698)
    print(p1.new_point(p2,3.09073))
    print(p1.distance(p2))

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
    grid_fun()
    #    Machine_Learning()
    var = 0
