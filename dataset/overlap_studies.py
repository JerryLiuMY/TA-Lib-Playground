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


class OverlapStudies:
    def __init__(self, close: np.array, low: np.array, high: np.array):
        """
        :param close: close time series
        """
        self.close = close
        self.low = low
        self.high = high

    # Moving average #
    def sma(self, timeperiod: int):
        """Simple Moving Average
        :param timeperiod: moving average window
        :return: moving average output
        """
        sma_output = talib.SMA(self.close, timeperiod)

        return sma_output

    def wma(self, timeperiod: int):
        """Weighted Moving Average
        :param timeperiod: moving average window
        :return: moving average output
        """
        wma_output = talib.WMA(self.close, timeperiod)

        return wma_output

    def ema(self, timeperiod: int):
        """Exponential Moving Average
        :param timeperiod: moving average window
        :return: moving average output
        """
        ema_output = talib.EMA(self.close, timeperiod)

        return ema_output

    def dema(self, timeperiod: int):
        """Double Exponential Moving Average
        :param timeperiod: moving average window
        :return: moving average output
        """
        dema_output = talib.DEMA(self.close, timeperiod)

        return dema_output

    def tema(self, timeperiod):
        """Triple Exponential Moving Average
        :param timeperiod: moving average window
        :return: moving average output
        """
        dema_output = talib.TEMA(self.close, timeperiod)

        return dema_output

    def trima(self, timeperiod):
        """Triangular Moving Average
        :param timeperiod: moving average window
        :return: moving average output
        """
        trima_output = talib.TRIMA(self.close, timeperiod)

        return trima_output

    def kama(self, timeperiod):
        """Kaufman Adaptive Moving Average
        :param timeperiod: moving average window
        :return: moving average output
        """
        kama_output = talib.KAMA(self.close, timeperiod)

        return kama_output

    def mama(self, timeperiod):
        """MESA Adaptive Moving Average
        :param timeperiod: moving average window
        :return: moving average output
        """
        mama_output = talib.KAMA(self.close, timeperiod)

        return mama_output

    def t3(self, timeperiod):
        """Triple Exponential Moving Average (T3)
        :param timeperiod: moving average window
        :return: moving average output
        """
        t3_output = talib.KAMA(self.close, timeperiod)

        return t3_output

    def ma(self, timeperiod: int, matype: int):
        """Moving average
        :param timeperiod: moving average window
        :param matype: moving average type
        :return: moving average output
        """
        ma_output = talib.MA(self.close, timeperiod, matype)

        return ma_output

    def mavp(self, minperiod, maxperiod, matype):
        """Moving average with variable period
        :param minperiod: moving average min period
        :param maxperiod: moving average max period
        :param matype: moving average type
        :return: moving average output
        """
        mavp_output = talib.MAVP(self.close, minperiod, maxperiod, matype)

        return mavp_output

    # indicator lines #
    def bbands(self, timeperiod: int, nbdevup: float, nbdevdn: float, matype: int):
        """Bollinger Bands
        :param timeperiod: moving average window
        :param nbdevup: number of non-biased standard deviations above the mean
        :param nbdevdn: number of non-biased standard deviations below the mean
        :param matype: moving average type
        :return: upperband, middleband, lowerband
        """
        upperband, middleband, lowerband = talib.BBANDS(self.close, timeperiod, nbdevup, nbdevdn, matype)

        return upperband, middleband, lowerband

    def ht_trendline(self):
        """Hilbert Transform - Instantaneous Trendline
        :return: trendline
        """
        trendline = talib.HT_TRENDLINE(self.close)

        return trendline

    def sar(self, acceleration: float, maximum: float):
        """Parabolic SAR
        :param acceleration: acceleration factor
        :param maximum: sensitivity
        :return: Parabolic SAR line
        """
        sar = talib.SAR(self.low, self.high, acceleration, maximum)

        return sar

    def sarext(self, **kwargs):
        """Parabolic SAR - Extended
        :return: Parabolic SAR line
        """
        key_list = [
            "startvalue",
            "offsetonreverse",
            "accelerationinitlong",
            "accelerationlong",
            "accelerationmaxlong",
            "accelerationinitshort",
            "accelerationshort",
            "accelerationmaxshort"
        ]

        for key, value in kwargs.items():
            if key not in key_list:
                raise ValueError(f"Invalid argument: {key}")

        sarext = talib.SAREXT(self.low, self.high, **kwargs)

        return sarext

    # midpoint & midprice #
    def midpoint(self, timeperiod: int):
        """MidPoint over period
        :param timeperiod: moving average window
        """
        midpoint = talib.MIDPOINT(self.close, timeperiod)

        return midpoint

    def midprice(self, timeperiod: int):
        """Midpoint Price over period
        :param timeperiod: moving average window
        """
        midprice = talib.MIDPRICE(self.high, self.low, timeperiod)

        return midprice


if __name__ == "__main__":
    pass

