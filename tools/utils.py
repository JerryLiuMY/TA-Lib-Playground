import pandas_datareader as pdr
from pandas_datareader import data as pdr
import yfinance as yf
from time import sleep
yf.pdr_override()


def get_sp500(ticker, start_date, end_date):
    """Gets sp500 price dataS"""
    i = 1
    try:
        sp500_all_data = pdr.get_data_yahoo(ticker, start_date, end_date)
    except ValueError:
        print("ValueError, trying again")
        i += 1
        if i < 5:
            sleep(10)
            sp500_all_data = pdr.get_data_yahoo(ticker, start_date, end_date)
        else:
            print("Tried 5 times, Yahoo error. Trying after 2 minutes")
            sleep(120)
            sp500_all_data = pdr.get_data_yahoo(ticker, start_date, end_date)
    sp500_data = sp500_all_data["Adj Close"]

