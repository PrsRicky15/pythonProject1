# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def tip_calculation():
    print("Welcome to the tip calculator!")
    val = float(input("Enter the total bill :-"))
    percent = float(input("How much you want to pay ( 10%, 15%, or 20%)"))
    result = (val * percent) / 100
    print("The tip is :", result)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    tip_calculation()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
