import numpy as np
import pandas as pd

ipl = pd.read_csv("D:\Coding journey 2024\datascience\panda\ipl-matches.csv")

print(ipl[['City','Season']])