import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import sys

# Goal: Produce graph of base stats given a pokemon name in the command line
df = pd.read_csv('data/pokedex.csv')

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python3 bstat_graph2.py 'Pokemon Name'")
    sys.exit(1)

# Get pokemon name
pokemon = sys.argv[1].capitalize()

def get_pokemon(pokemon):
    row = df[df['Pokemon'] == pokemon]
    if not row.empty:
        row_vals = row.iloc[0, 1:].tolist()
        print(row_vals)
        return row_vals
    else:
        print("Pokemon not found. Check spelling and try again")
        sys.exit(1)      
    

def plot_pokemon(pokemon):
    stat_vals = get_pokemon(pokemon)
    stat_colors = ['green', 'yellow', 'orange', 'cyan', 'blue', 'magenta']
    stat_names = df.columns[1:].tolist()
    _ = plt.figure(figsize=(8, 6))
    _ = plt.bar(stat_names, stat_vals, color=stat_colors)

    for bar in _:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, int(yval), ha='center', va='bottom')

    plt.title(pokemon + " Base Stats")
    plt.ylabel('Stat Points')

    plt.show()


plot_pokemon(pokemon)


