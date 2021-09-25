import talib
import numpy as np


class MomentumIndicators:
    def __init__(self, open: np.array, high: np.array, low: np.array, close: np.array, volume: np.array):
        """
        :param high: high time series
        :param low: low time series
        :param close: close time series
        """
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def mom(self, timeperiod: int = 10):
        """
        Momentum
        :param timeperiod:
        """
        mom = talib.MINUS_DM(self.close, timeperiod)

        return mom

    def adx(self, timeperiod: int = 14):
        """Average Directional Movement Index
        :param timeperiod: moving average window
        """
        adx = talib.ADX(self.high, self.low, self.close, timeperiod)

        return adx

    def adxr(self, timeperiod: int = 14):
        """Average Directional Movement Index Rating
        :param timeperiod: window size
        """
        adxr = talib.ADXR(self.high, self.low, self.close, timeperiod)

        return adxr

    def apo(self, fastperiod: int = 12, slowperiod: int = 26, matype: int = 0):
        """Absolute Price Oscillator
        :param fastperiod:
        :param slowperiod:
        :param matype: moving average type
        """
        apo = talib.APO(self.close, fastperiod, slowperiod, matype)

        return apo

    def aroon(self, timeperiod: int = 14):
        """Aroon
        :param timeperiod: window size
        """
        aroondown, aroonup = talib.AROON(self.high, self.low, timeperiod)

        return aroondown, aroonup

    def aroonosc(self, timeperiod: int = 14):
        """Aroon Oscillator
        :param timeperiod: window size
        """
        aroondown, aroonup = talib.AROONOSC(self.high, self.low, timeperiod)

        return aroondown, aroonup

    def bop(self):
        """Balance Of Power"""
        bop = talib.BOP(self.open, self.high, self.low, self.close)

        return bop

    def cci(self, timeperiod: int = 14):
        """Commodity Channel Index
        :param timeperiod: window size
        """
        cci = talib.CCI(self.high, self.low, self.close, timeperiod)

        return cci

    def cmo(self, timeperiod: int = 14):
        """Chande Momentum Oscillator
        :param timeperiod: window size
        """
        cmo = talib.CMO(self.close, timeperiod)

        return cmo

    def dx(self, timeperiod: int = 14):
        """Directional Movement Index
        :param timeperiod: window size
        """
        dx = talib.DX(self.high, self.low, self.close, timeperiod)

        return dx

    def macd(self, fastperiod: int = 12, slowperiod: int = 26, signalperiod: int = 9):
        """Moving Average Convergence/Divergence
        :param fastperiod:
        :param slowperiod:
        :param signalperiod:
        """
        macd = talib.MACD(self, fastperiod, slowperiod, signalperiod)

        return macd

    def macdext(self, fastperiod: int = 12, slowperiod: int = 26, signalperiod: int = 9, **kwargs):
        """MACD with controllable MA type
        :param fastperiod:
        :param slowperiod:
        :param signalperiod:
        """
        key_list = [
            "fastmatype",
            "slowmatype",
            "signalmatype",
        ]

        for key, value in kwargs.items():
            if key not in key_list:
                raise ValueError(f"Invalid argument: {key}")

        try:
            fastmatype = kwargs["fastmatype"]
        except KeyError:
            fastmatype = 0

        try:
            slowmatype = kwargs["slowmatype"]
        except KeyError:
            slowmatype = 0

        try:
            signalmatype = kwargs["signalmatype"]
        except KeyError:
            signalmatype = 0

        macd, macdsignal, macdhist = talib.MACDEXT(
            self.close,
            fastperiod, fastmatype,
            slowperiod, slowmatype,
            signalperiod, signalmatype
        )

        return macd, macdsignal, macdhist

    def macdfix(self, signalperiod: int = 9):
        """
        Moving Average Convergence/Divergence Fix 12/26
        :param signalperiod:
        """
        macd, macdsignal, macdhist = talib.MACDEXT(self.close, signalperiod)

        return macd, macdsignal, macdhist

    def mfi(self, timeperiod: int = 14):
        """
        Moving Average Convergence/Divergence Fix 12/26
        :param timeperiod:
        """
        macd, macdsignal, macdhist = talib.MFI(self.high, self.low, self.close, self.volume, timeperiod)

        return macd, macdsignal, macdhist

    def minus_di(self, timeperiod: int = 14):
        """
        Minus Directional Indicator
        :param timeperiod:
        """
        minus_di = talib.MINUS_DI(self.high, self.low, self.close, timeperiod)

        return minus_di

    def minus_dm(self, timeperiod: int = 14):
        """
        Minus Directional Indicator
        :param timeperiod:
        """
        minus_dm = talib.MINUS_DM(self.high, self.low, timeperiod)

        return minus_dm

    def plus_di(self, timeperiod: int = 14):
        """
        Plus Directional Indicator
        :param timeperiod:
        """
        mom = talib.MINUS_DI(self.high, self.low, self.close, timeperiod)

        return mom

    def plus_dm(self, timeperiod: int = 14):
        """
        Plus Directional Movement
        :param timeperiod:
        """
        mom = talib.MINUS_DM(self.high, self.low, timeperiod)

        return mom

    def plus_dm(self, timeperiod: int = 14):
        """
        Plus Directional Movement
        :param timeperiod:
        """
        mom = talib.MINUS_DM(self.high, self.low, timeperiod)

        return mom

