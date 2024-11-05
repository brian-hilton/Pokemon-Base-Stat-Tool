import numpy as np
import matplotlib
import matplotlib.pyplot
import pandas as pd
import sys

df = pd.read_csv('data/pokedex.csv')

# Obtain column from dataframe, convert to list
names = df['Pokemon'].to_list()

# Use .iloc function [row, column] to obtain all rows excluding first. Take sum of values and convert to list
stat_totals = df.iloc[:, 1:].sum(axis=1).to_list()

bstat_totals = pd.DataFrame({'Pokemon': names,
                           'Base Stat Total': stat_totals})
print(bstat_totals)



