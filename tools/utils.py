import pandas_datareader as pdr
from pandas_datareader import data as pdr
import yfinance as yf
from time import sleep
yf.pdr_override()


def get_price(ticker, start_date, end_date):
    """Gets sp500 price dataS"""
    i = 1
    try:
        data_df = pdr.get_data_yahoo(ticker, start_date, end_date)
    except ValueError:
        print("ValueError, trying again")
        i += 1
        if i < 5:
            sleep(10)
            data_df = pdr.get_data_yahoo(ticker, start_date, end_date)
        else:
            print("Tried 5 times, Yahoo error. Trying after 2 minutes")
            sleep(120)
            data_df = pdr.get_data_yahoo(ticker, start_date, end_date)
    close_price = data_df["Adj Close"]

    return close_price
