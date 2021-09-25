import talib
import numpy as np


def add(series1: np.array, series2: np.array):
    """Vector Arithmetic Add
    :param series1:
    :param series2:
    :return:
    """

    return talib.ADD(series1, series2)


def sub(series1: np.array, series2: np.array):
    """Vector Arithmetic Substraction
    :param series1:
    :param series2:
    :return:
    """

    return talib.SUB(series1, series2)


def mult(series1: np.array, series2: np.array):
    """Vector Arithmetic Mult
    :param series1:
    :param series2:
    :return:
    """

    return talib.MULT(series1, series2)


def div(series1: np.array, series2: np.array):
    """Vector Arithmetic Div
    :param series1:
    :param series2:
    :return:
    """

    return talib.DIV(series1, series2)


def max(series: np.array, timeperiod: int = 30):
    """Highest value over a specified period
    :param series:
    :param timeperiod:
    :return:
    """

    return talib.MAX(series, timeperiod)


def maxindex(series: np.array, timeperiod: int = 30):
    """Index of highest value over a specified period
    :param series:
    :param timeperiod:
    :return:
    """

    return talib.MAXINDEX(series, timeperiod)


def min(series: np.array, timeperiod: int = 30):
    """Lowest value over a specified period
    :param series:
    :param timeperiod:
    :return:
    """

    return talib.MIN(series, timeperiod)


def minindex(series: np.array, timeperiod: int = 30):
    """Index of lowest value over a specified period
    :param series:
    :param timeperiod:
    :return:
    """

    return talib.MININDEX(series, timeperiod)


def minmax(series: np.array, timeperiod: int = 30):
    """Lowest and highest values over a specified period
    :param series:
    :param timeperiod:
    :return:
    """

    return talib.MINMAX(series, timeperiod)


def minmaxindex(series: np.array, timeperiod: int = 30):
    """Indexes of lowest and highest values over a specified period
    :param series:
    :param timeperiod:
    :return:
    """

    return talib.MINMAXINDEX(series, timeperiod)


def sum(series: np.array, timeperiod: int = 30):
    """Summation
    :param series:
    :param timeperiod:
    :return:
    """

    return talib.SUM(series, timeperiod)
