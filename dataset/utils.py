from time import sleep
from pandas_datareader import data as pdr


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