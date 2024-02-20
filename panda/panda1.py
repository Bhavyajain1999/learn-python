import numpy as np
import pandas as pd

ipl = pd.read_csv("D:\Coding journey 2024\datascience\panda\ipl-matches.csv")
ipl[~ipl['MatchNumber'].str.isdigit()]['Player_of_Match'].value_counts()