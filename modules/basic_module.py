# modules/basic_module.py
def print_hi(name):
    print(f'Hi, {name}')


def tip_calculation():
    print("Welcome to the tip calculator!")
    val = float(input("Enter the total bill: "))
    percent = float(input("How much you want to pay (10%, 15%, or 20%): "))
    result = (val * percent) / 100
    print("The tip is:", result)
