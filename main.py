from demo.demo_1 import get_data_df, get_holdings_df, visualize

if __name__ == "__main__":
    start, end = "2015-04-22", "2021-04-22"
    ticker, max_holding = "AAPL", 100
    data_df = get_data_df(ticker, start, end)
    holdings_df = get_holdings_df(data_df, max_holding)
    fig = visualize(data_df, holdings_df)
    fig.savefig("demo_1.pdf")
