import talib
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as pdr

# get head of the dataframe
aapl = pdr.get_data_yahoo("AAPL")
aapl.head()
aapl["Close"].plot()


def plot_aapl():
    sma200 = talib.SMA(aapl["Close"].values, 200)
    plt.plot(sma200, label="SMA200")
    plt.plot(aapl["Close"].values, label="Price")
    plt.legend(loc="best")

