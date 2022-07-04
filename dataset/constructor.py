import yfinance as yf
from talib import abstract
import numpy as np
import talib
yf.pdr_override()


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

    dataset = np.array(dataset_li)

    return dataset

