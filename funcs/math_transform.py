import talib


def sin(series):
    """Vector Trigonometric Sin
    :param series:
    :return:
    """

    return talib.SIN(series)


def cos(series):
    """Vector Trigonometric Cos
    :param series:
    :return:
    """

    return talib.COS(series)


def tan(series):
    """Vector Trigonometric Tan
    :param series:
    :return:
    """

    return talib.TAN(series)


def asin(series):
    """Vector Trigonometric ASin
    :param series:
    :return:
    """

    return talib.ASIN(series)


def acos(series):
    """Vector Trigonometric ACos
    :param series:
    :return:
    """

    return talib.ACOS(series)


def atan(series):
    """Vector Trigonometric ATan
    :param series:
    :return:
    """

    return talib.ATAN(series)


def sinh(series):
    """Vector Trigonometric Sinh
    :param series:
    :return:
    """

    return talib.SINH(series)


def cosh(series):
    """Vector Trigonometric Cosh
    :param series:
    :return:
    """

    return talib.COSH(series)


def tanh(series):
    """Vector Trigonometric Tanh
    :param series:
    :return:
    """

    return talib.TANH(series)


def exp(series):
    """Vector Arithmetic Exp
    :param series:
    :return:
    """

    return talib.EXP(series)


def ln(series):
    """Vector Log Natural
    :param series:
    :return:
    """

    return talib.LN(series)


def log10(series):
    """Vector Log10
    :param series:
    :return:
    """

    return talib.LOG10(series)


def sqrt(series):
    """Vector Square Root
    :param series:
    :return:
    """

    return talib.SQRT(series)


def ceil(series):
    """Vector Ceil
    :param series:
    :return:
    """

    return talib.CEIL(series)


def floor(series):
    """Vector Floor
    :param series:
    :return:
    """

    return talib.FLOOR(series)
