# External Lib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class DA:
     def read_data(self):
        file = 'data.csv'
        df = pd.read_csv(file)
        print(df)



regeion = DA()
regeion.read_data()
