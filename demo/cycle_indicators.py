import talib
import numpy as np


class CycleIndicators:
    def __init__(self, close: np.array):
        """
        :param close: close time series
        """
        self.close = close

    def ht_dcperiod(self):
        """Hilbert Transform - Dominant Cycle Period
        """
        ht_dcperiod = talib.HT_DCPERIOD(self.close)

        return ht_dcperiod

    def ht_dephase(self):
        """Hilbert Transform - Dominant Cycle Phase
        """
        ht_dephase = talib.HT_DCPHASE(self.close)

        return ht_dephase

    def ht_phasor(self):
        """Hilbert Transform - Phasor Components
        """
        inphase, quadrature = talib.HT_PHASOR(self.close)

        return inphase, quadrature

    def ht_sine(self):
        """Hilbert Transform - SineWave
        """
        sine, leadsine = talib.HT_PHASOR(self.close)

        return sine, leadsine

    def ht_trendmode(self):
        """Hilbert Transform - Trend vs Cycle Mode
        """
        ht_trendmode = talib.HT_PHASOR(self.close)

        return ht_trendmode
