import talib
import numpy as np


class VolatilityIndicators:
    def __init__(self, high: np.array, low: np.array, close: np.array):
        """
        :param high: high time series
        :param low: low time series
        :param close: close time series
        """
        self.high = high
        self.low = low
        self.close = close

    def atr(self, timeperiod: int = 14):
        """Average True Range
        :param timeperiod: moving average window
        :return: moving average output
        """
        atr = talib.ATR(self.high, self.low, self.close, timeperiod)

        return atr

    def natr(self, timeperiod: int = 14):
        """Normalized Average True Range
        :param timeperiod: moving average window
        :return: moving average output
        """
        natr = talib.NATR(self.high, self.low, self.close, timeperiod)

        return natr

    def trange(self):
        """True Range
        :return: moving average output
        """
        sma_output = talib.NATR(self.high, self.low, self.close)

        return sma_output
