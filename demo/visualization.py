import pandas_datareader.data as web
import pandas as pd
import numpy as np
from talib import RSI, BBANDS, SMA, MOM
import matplotlib.pyplot as plt
from global_settings import API_KEY


def get_data_df(ticker, start, end):
    data_df = web.DataReader(tickers=ticker, data_source="quandl", start=start, end=end, api_key=API_KEY).iloc[::-1]
    data_df.dropna(inplace=True)
    close = data_df["Adj Close"].values
    data_df["BB_up"], data_df["BB_mid"], data_df["BB_low"] = BBANDS(close, timeperiod=20, nbdevup=2, nbdevdn=2)
    data_df["BBP"] = _get_bbp(data_df)
    data_df["SMA_10"], data_df["SMA_50"] = SMA(close, 10), SMA(close, 50)
    data_df["RSI"], data_df["MOM"] = RSI(close, timeperiod=14), MOM(close, timeperiod=14)

    return data_df


def get_holdings_df(data_df, max_holding):
    index = data_df.index
    holdings_df = pd.DataFrame(index=index, data={"Holdings": np.array([np.nan] * index.shape[0])})
    holdings_df.loc[((data_df["RSI"] < 30) & (data_df["BBP"] < 0)), "Holdings"] = max_holding
    holdings_df.loc[((data_df["RSI"] > 70) & (data_df["BBP"] > 1)), "Holdings"] = 0
    holdings_df.ffill(inplace=True)
    holdings_df.fillna(0, inplace=True)
    holdings_df["Order"] = holdings_df.diff()
    holdings_df.dropna(inplace=True)

    return holdings_df


def visualize(data_df, holdings_df):
    index = data_df.index
    fig, axes = plt.subplots(3, 1, figsize=(12, 8))

    # Price
    axes[0].plot(index, data_df["Adj Close"], label="Adj_Close")
    axes[0].plot(index, data_df["SMA_10"], label="MA_10")
    axes[0].plot(index, data_df["SMA_50"], label="MA_50")
    axes[0].legend(loc="upper left")
    axes[0].set_xlabel("Date")
    axes[0].set_ylabel("Adj Close")
    axes[0].grid()
    for day, holding in holdings_df.iterrows():
        order = holding["Order"]
        if order > 0:
            axes[0].scatter(x=day, y=data_df.loc[day, "Adj Close"], color="green")
        elif order < 0:
            axes[0].scatter(x=day, y=data_df.loc[day, "Adj Close"], color="red")

    # RSI & MOM
    axes[1].plot(index, data_df["RSI"], label="RSI")
    axes[1].fill_between(index, y1=30, y2=70, color="#adccff", alpha=0.3)
    axes[1].legend(loc="upper left")
    axes[1].set_xlabel("Date")
    axes[1].set_ylabel("RSI")
    axes[1].grid()

    ax_ = axes[1].twinx()
    ax_.plot(index, data_df["MOM"], label="MOM", color="r", alpha=0.75)
    ax_.legend(loc="upper right")
    ax_.set_ylabel("MOM")

    # BBANDS
    axes[2].plot(index, data_df["Adj Close"], label="Adj_Close")
    axes[2].plot(index, data_df["BB_up"], label="BB_up")
    axes[2].plot(index, data_df["BB_low"], label="BB_low")
    axes[2].plot(index, data_df["BB_mid"], label="BB_mid")
    axes[2].fill_between(index, y1=data_df["BB_low"], y2=data_df["BB_up"], color="#adccff", alpha=0.3)
    axes[2].set_xlabel("Date")
    axes[2].set_ylabel("Bollinger Bands")
    axes[2].legend(loc="upper left")
    axes[2].grid()
    fig.tight_layout()

    return fig


def _get_bbp(data_df):
    close = data_df["Adj Close"].values
    up, mid, low = BBANDS(close, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    bbp = (close - low) / (up - low)

    return bbp
