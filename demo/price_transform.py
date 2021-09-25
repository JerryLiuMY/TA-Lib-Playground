import talib
import numpy as np


class PriceTransform:
    def __init__(self, open: np.array, high: np.array, low: np.array, close: np.array):
        """
        :param open: open time series
        :param high: high time series
        :param low: low time series
        :param close: close time series
        """
        self.open = open
        self.high = high
        self.low = low
        self.close = close

    def avgprice(self):
        """Average Price"""
        avgprice = talib.AVGPRICE(self.open, self.high, self.low, self.close)

        return avgprice

    def medprice(self):
        """Median Price"""
        medprice = talib.MEDPRICE(self.high, self.low)

        return medprice

    def typprice(self):
        """Typical Price"""
        typprice = talib.TYPPRICE(self.high, self.low, self.close)

        return typprice

    def wclprice(self):
        """Weighted Close Price"""
        wclprice = talib.WCLPRICE(self.high, self.low, self.close)

        return wclprice
