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
    upperband, middleband, lowerband = talib.BBANDS(aapl["Close"].values, 100, 1, 1)
    fig, axes = plt.subplots(1, 2)
    axes[0].plot(sma200, label="SMA200")
    axes[0].plot(aapl["Close"].values, label="Price")
    axes[0].legend(loc="best")

    axes[1].plot(sma200, label="SMA200")
    axes[1].plot(upperband, label="Upper Band")
    axes[1].plot(middleband, label="Middle Band")
    axes[1].plot(lowerband, label="Lower Band")
    axes[1].legend(loc="best")

    return fig

