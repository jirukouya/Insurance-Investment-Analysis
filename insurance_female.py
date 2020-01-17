# utf - 8


import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import math
import pandas as pd
import os

def extract_data():
    
    data = pd.read_csv('female.csv')
    df = pd.DataFrame(data)
    
    return ploting_graph(df)

def currency(x, pos):
    'The two args are the value and tick position'
    if x >= 1000000:
        return 'RM{:1.1f}M'.format(x*1e-6)
    return 'RM{:1.0f}K'.format(x*1e-3)

def ploting_graph(df):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    df.plot(kind='line',x='Age',y='Total Premium Paid', color='g', label='Total Premium Paid (Years)', marker='.',ax=ax)
    df.plot(kind='line',x='Age',y='Death Benefits', color='orange', label='Total Claim (Years)', marker='.',ax=ax)
    df.plot(kind='line',x='Age',y='Earnings', color='red', label='Total Earnings (Years)', marker='.',ax=ax)

    # format the currency
    formatter = FuncFormatter(currency)
    ax.yaxis.set_major_formatter(formatter)

    # Average for Total Earnings

    average_total_earnings = df.loc[:,'Earnings'].mean()
    print(average_total_earnings)
    ax.axhline(y=average_total_earnings, color='b', label='Average in Total Earnings', linestyle='--', linewidth=1)

    # limits and labels
    plt.xlabel('Age')
    plt.ylabel('Ringgits in RM')
    plt.title('Great Love4u Female - Yield Curve Index Analysis')
    plt.legend()
    plt.show()
    ax.figure.savefig('Great Love4u Female - Yield Curve Index Analysis.png', transparent=False, dpi=200, bbox_inches="tight")

def ploting_graph_ROI(df):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    df.plot(kind='line',x='Age',y='ROI', color='blue', label='ROI % (Years)', marker='.',ax=ax)

    # ROI mean
    ROI_mean = df.loc[:,'ROI'].mean()

    ax.axhline(y=ROI_mean, color='red', label='Average in ROI %', linestyle='--', linewidth=1)

    # limits and labels
    plt.xlabel('Age')
    plt.ylabel('ROI %')
    plt.title('Great Love4u Female - Return On Investment Analysis')
    plt.legend()
    plt.show()
    ax.figure.savefig('Great Love4u Female - Return On Investment Analysis.png', transparent=False, dpi=200, bbox_inches="tight")
    
extract_data()