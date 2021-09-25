import talib
import numpy as np


class CycleIndicators:
    def __init__(self, close: np.array):
        """
        :param close: time series
        """
        self.close = close

    def ht_dcperiod(self):
        """Hilbert Transform - Dominant Cycle Period
        :return: Hilbert transform line
        """
        ht_dcperiod = talib.HT_DCPERIOD(self.close)

        return ht_dcperiod

    def ht_dephase(self):
        """Hilbert Transform - Dominant Cycle Phase
        :return:
        """
        ht_dephase = talib.HT_DCPHASE(self.close)

        return ht_dephase
