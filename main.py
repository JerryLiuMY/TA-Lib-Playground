from demo.visualization import get_data_df, get_holdings_df, visualize
from dataset.constructor import build_dataset
from global_settings import WORK_DIR, DATA_DIR
from dataset.utils import get_yahoo
import numpy as np
import os

ticker, start, end = "AAPL", "2018-01-01", "2020-12-31"


if __name__ == "__main__":
    max_holding =  100
    data_df = get_data_df(ticker, start, end)
    holdings_df = get_holdings_df(data_df, max_holding)
    fig = visualize(data_df, holdings_df)
    fig.savefig(os.path.join(WORK_DIR, "demo/fig", "demo.png"), dpi=300)


# if __name__ == "__main__":
#     yahoo_df = get_yahoo(ticker, start, end)
#     dataset = build_dataset(yahoo_df)
#     with open(os.path.join(DATA_DIR, f"{ticker}.npy"), "wb") as handle:
#         np.save(handle, dataset)
#     with open(os.path.join(DATA_DIR, f"{ticker}.npy"), "rb") as handle:
#         dataset = np.load(handle)


