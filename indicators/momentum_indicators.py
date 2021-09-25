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
        :param timeperiod: time window size
        """
        mom = talib.MINUS_DM(self.close, timeperiod)

        return mom

    def adx(self, timeperiod: int = 14):
        """Average Directional Movement Index
        :param timeperiod: window size
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

    def ppo(self, fastperiod: int = 12, slowperiod: int = 26, matype: int = 0):
        """
        Plus Directional Movement
        :param fastperiod:
        :param slowperiod:
        :param matype:
        """
        ppo = talib.PPO(self.close, fastperiod, slowperiod, matype)

        return ppo

    def roc(self, timeperiod: int = 10):
        """Rate of change : ((real/prevPrice)-1)*100
        :param timeperiod:
        :return:
        """
        roc = talib.ROC(self.close, timeperiod)

        return roc

    def rocp(self, timeperiod: int = 10):
        """Rate of change Percentage: (real-prevPrice)/prevPrice
        :param timeperiod:
        :return:
        """
        rocp = talib.ROCP(self.close, timeperiod)

        return rocp

    def rocr(self, timeperiod: int = 10):
        """Rate of change ratio: (real/prevPrice)
        :param timeperiod:
        :return:
        """
        rocr = talib.ROCR(self.close, timeperiod)

        return rocr

    def rocr100(self, timeperiod: int = 10):
        """Rate of change ratio 100 scale: (real/prevPrice)*100
        :param timeperiod:
        :return:
        """
        rocr100 = talib.ROCR100(self.close, timeperiod)

        return rocr100

    def rsi(self, timeperiod: int = 14):
        """Relative Strength Index
        :param timeperiod:
        :return:
        """
        rsi = talib.RSI(self.close, timeperiod)

        return rsi

    def stoch(
            self, fastk_period: int = 5, slowk_period: int = 3, slowk_matype: int = 0,
            slowd_period: int = 3, slowd_matype: int = 0
    ):
        """Stochastic
        :param fastk_period:
        :param slowk_period:
        :param slowk_matype:
        :param slowd_period:
        :param slowd_matype:
        :return:
        """
        slowk, slowd = talib.STOCH(
            self.high, self.low, self.close, fastk_period, slowk_period,
            slowk_matype, slowd_period, slowd_matype
        )

        return slowk, slowd

    def stochf(self, fastk_period: int = 5, fastd_period: int = 3, fastd_matype: int = 0):
        """Stochastic Fast
        :param fastk_period:
        :param fastd_period:
        :param fastd_matype:
        :return:
        """
        fastk, fastd = talib.STOCHF(
            self.high, self.low, self.close, fastk_period, fastd_period, fastd_matype
        )

        return fastk, fastd

    def stochrsi(self, timeperiod: int = 14, fastk_period: int = 5, fastd_period: int = 3, fastd_matype: int = 0):
        """Stochastic Relative Strength Index
        :param timeperiod:
        :param fastk_period:
        :param fastd_period:
        :param fastd_matype:
        :return:
        """
        fastk, fastd = talib.STOCHRSI(
            self.high, self.low, self.close, timeperiod, fastk_period, fastd_period, fastd_matype
        )

        return fastk, fastd

    def trix(self, timeperiod: int = 30):
        """1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
        :param timeperiod:
        :return:
        """
        fastk, fastd = talib.TRIX(self.close, timeperiod)

        return fastk, fastd

    def ultosc(self, timeperiod1: int = 7, timeperiod2: int = 14, timeperiod3: int = 28):
        """Ultimate Oscillator
        :param timeperiod1:
        :param timeperiod2:
        :param timeperiod3:
        :return:
        """
        ultosc = talib.ULTOSC(self.high, self.low, self.close, timeperiod1, timeperiod2, timeperiod3)

        return ultosc

    def willr(self, timeperiod: int = 14):
        """Williams' %R
        :param timeperiod:
        :return:
        """
        willr = talib.WILLR(self.high, self.low, self.close, timeperiod)

        return willr
