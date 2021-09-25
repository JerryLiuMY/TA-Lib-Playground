import talib


def beta(series0, series1, timeperiod: int = 5):
    """Beta
    :param series0:
    :param series1:
    :param timeperiod:
    :return:
    """

    return talib.BETA(series0, series1, timeperiod)


def correl(series0, series1, timeperiod: int = 30):
    """Beta
    :param series0:
    :param series1:
    :param timeperiod:
    :return:
    """

    return talib.CORREL(series0, series1, timeperiod)


def linearreg(series, timeperiod: int = 14):
    """Linear Regression
    :param series:
    :param timeperiod:
    :return:
    """

    return talib.LINEARREG(series, timeperiod)


def linearreg_angle(series, timeperiod: int = 14):
    """Linear Regression Angle
    :param series:
    :param timeperiod:
    :return:
    """

    return talib.LINEARREG_ANGLE(series, timeperiod)


def linearreg_intercept(series, timeperiod: int = 14):
    """Linear Regression Intercept
    :param series:
    :param timeperiod:
    :return:
    """

    return talib.LINEARREG_INTERCEPT(series, timeperiod)


def linearreg_slope(series, timeperiod: int = 14):
    """Linear Regression Slope
    :param series:
    :param timeperiod:
    :return:
    """

    return talib.LINEARREG_SLOPE(series, timeperiod)


def stddev(series, timeperiod: int = 5, nbdev: float = 1):
    """Standard Deviation
    :param series:
    :param timeperiod:
    :param nbdev:
    :return:
    """

    return talib.STDDEV(series, timeperiod, nbdev)


def tsf(series, timeperiod: int = 14):
    """Time Series Forecast
    :param series:
    :param timeperiod:
    :return:
    """

    return talib.TSF(series, timeperiod)


def var(series, timeperiod: int = 5, nbdev: float = 1):
    """Variance
    :param series:
    :param timeperiod:
    :param nbdev:
    :return:
    """

    return talib.VAR(series, timeperiod, nbdev)
