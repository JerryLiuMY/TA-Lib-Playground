import talib
import numpy as np

# SMA = 0
# EMA = 1
# WMA = 2
# DEMA = 3
# TEMA = 4
# TRIMA = 5
# KAMA = 6
# MAMA = 7
# T3 = 8


class MomentumIndicators:
    def __init__(self, high: np.array, low: np.array, close: np.array):
        """
        :param high: high time series
        :param low: low time series
        :param close: close time series
        """
        self.high = high
        self.low = low
        self.close = close

    def adx(self, timeperiod: int = 14):
        """Average Directional Movement Index
        :param timeperiod: moving average window
        """
        adx = talib.ADX(self.high, self.low, self.close, timeperiod)

        return adx

    def adxr(self, timeperiod: int = 14):
        """Average Directional Movement Index Rating
        :param timeperiod: moving average window
        """
        adxr = talib.ADXR(self.high, self.low, self.close, timeperiod)

        return adxr

    def apo(self, fastperiod: int = 12, slowperiod: int = 26, matype: int = 0):
        """Absolute Price Oscillator
        :param fastperiod:
        :param slowperiod:
        :param matype: moving average type
        """
        adxr = talib.ADXR(self.close, fastperiod, slowperiod, matype)

        return adxr
