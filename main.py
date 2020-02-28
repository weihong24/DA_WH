# External Lib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class DA:
     def read_data(self):
        file = 'Worksheet in D  Lesson 2019 Applied Sriptong Using Python Python Elective (IT49450) - Project_14Mar19.csv'
        df = pd.read_csv(file)
        print(df)



regeion = DA()
regeion.read_data()

import matplotlib.pyplot as plt

year = [2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
regeion = []