from pandas_datareader import data as pdr
import yfinance as yf
from talib import abstract
from time import sleep
import numpy as np
import talib
yf.pdr_override()


def get_yahoo(ticker, start, end):
    """Gets sp500 price dataS"""
    i = 1
    try:
        yahoo_df = pdr.get_data_yahoo(ticker, start, end)
    except ValueError:
        print("ValueError, trying again")
        i += 1
        if i < 5:
            sleep(10)
            yahoo_df = pdr.get_data_yahoo(ticker, start, end)
        else:
            print("Tried 5 times, Yahoo error. Trying after 2 minutes")
            sleep(120)
            yahoo_df = pdr.get_data_yahoo(ticker, start, end)

    return yahoo_df


def build_dataset(yahoo_df):
    inputs = {
        "open": yahoo_df["Open"],
        "high": yahoo_df["High"],
        "low": yahoo_df["Low"],
        "close": yahoo_df["Adj Close"],
        "volume": yahoo_df["Volume"]
    }

    dataset_li = []
    for func_name in talib.get_functions():
        func = abstract.Function(func_name)
        try:
            outputs = func(inputs)
        except Exception: # MAMA
            continue
        
        if type(outputs) is list:
            for output in outputs:
                dataset_li.append(output)
        else:
            output = outputs
            dataset_li.append(output)

    dataset_arr = np.array(dataset_li)

    return dataset_arr

