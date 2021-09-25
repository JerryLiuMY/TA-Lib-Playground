import pandas_datareader.data as web
from talib import RSI, BBANDS
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

start = "2015-04-22"
end = "2017-04-22"

# RSI -- a momentum indicator
# High RSI (usually above 70) may indicate a stock is overbought, therefore it is a sell signal.
# Low RSI (usually below 30) indicates stock is oversold, which means a buy signal.

# Bollinger Bands -- a volatility indicator
# Bollinger Bands tell us most of price action between the two bands.
# Therefore, if %b is above 1, price will likely go down back within the bands. Hence, it is a sell signal.
# While if it is lower than 0, it is considered a buy signal.

# The strategy is a simple voting mechanism.
# When two indicators think it is time to buy, then it issues buy order to enter.
# When both indicators think it is time to sell, then it issues sell order to exit.


def loss():
    symbol = 'MCD'
    max_holding = 100
    price = web.DataReader(name=symbol, data_source='quandl', start=start, end=end)
    price = price.iloc[::-1]
    price = price.dropna()
    close = price['AdjClose'].values
    up, mid, low = BBANDS(close, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    rsi = RSI(close, timeperiod=14)
    print("RSI (first 10 elements)\n", rsi[14:24])
