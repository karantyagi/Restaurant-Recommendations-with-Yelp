# libraries and data
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
import pprint
from tabulate import tabulate

def plot_line(df,header):
    # style
    plt.style.use('seaborn-darkgrid')

    # line plot
    # first is x axis, 2nd is y axis

    plt.plot(df[str(header[0])], df[str(header[1])], marker='', color='red', linewidth=1, alpha=1)

    # Add legend

    red_line = mlines.Line2D([], [], color='red', alpha=1, linewidth=2, label=str(header[1]))
    plt.legend(loc=1, ncol=2, handles=[red_line])
    #red_patch = mpatches.Patch(color='red', label=header[1])
    #plt.legend(loc=1, ncol=2, handles=[red_patch])


    # Add titles
    plt.title("hbsjfhdsgjbgksjbdkjzgnskdn", loc='left', fontsize=14, fontweight=0, color='orange')
    plt.xlabel(str(header[0]))
    plt.ylabel(str(header[1]))

    #plt.xticks(df[str(header[0])] , rotation=45 )
    plt.show(block=True)
