import numpy as np
import pandas as pd


def basic_machine_learn(file):
    dataset = pd.read_csv(file)
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
    from sklearn.impute import SimpleImputer
    imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
    imputer.fit(x[:, 1:3])
    x[:, 1:3] = imputer.transform(x[:, 1:3])
    print("---------------------\n new X-Values :")
    print("--------------------")
    print(x)
