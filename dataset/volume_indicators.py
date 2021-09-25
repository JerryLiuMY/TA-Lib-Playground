import talib
import numpy as np


class VolumeIndicators:
    def __init__(self, close: np.array, low: np.array, high: np.array, volume: np.array):
        """
        :param close: time series
        """
        self.close = close
        self.low = low
        self.high = high
        self.volume = volume

    def ad(self):
        """Chaikin A/D Line
        :return: Chaikin A/D Line
        """
        ad = talib.AD(self.high, self.low, self.close, self.volume)

        return ad

    def adosc(self, fastperiod: int = 3, slowperiod: int = 10):
        """Chaikin A/D Oscillator
        :param: fastperiod:
        :param: slowperiod:
        :return: Chaikin A/D Oscillator
        """
        adosc = talib.ADOSC(self.high, self.low, self.close, self.volume, fastperiod, slowperiod)

        return adosc

    def obv(self):
        """On Balance Volume
        :return: On Balance Volume
        """
        obv = talib.OBV(self.close, self.volume)

        return obv
