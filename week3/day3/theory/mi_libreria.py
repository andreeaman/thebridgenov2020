import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

def grafica_verde(lista, ylabel):
    plt.plot(lista, linewidth=2, 
             marker='o', color="purple", linestyle='dashed', markersize=6)
    plt.ylabel(ylabel)
    plt.show()