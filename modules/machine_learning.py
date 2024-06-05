import numpy as np
import matplotlib as plt
import pandas as pd


def basic_machine_learn():
    dataset = pd.read_csv("data/Data.csv")
    x = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values
    print("--------------------\n Data-set")
    print("--------------------")
    print(dataset)
    print("---------------------\n X-Values :")
    print("--------------------")
    print(x)
    print("---------------------\n Y-Values :")
    print("--------------------")
    print(y)
