# External Lib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import unittest



class DA:
     def read_data(self):
        file = 'Worksheet in D  Lesson 2019 Applied Sriptong Using Python Python Elective (IT49450) - Project_14Mar19.csv'
        df = pd.read_csv(file)
        print(df)
        #filter table
        print(df.iloc[360:480,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]])







regeion = DA()
regeion.read_data()



