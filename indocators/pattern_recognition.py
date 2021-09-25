import talib
import numpy as np


class PatternRecognition:
    def __init__(self, open: np.array, high: np.array, low: np.array, close: np.array):
        """
        :param close: time series
        """
        self.open = open
        self.high = high
        self.low = low
        self.close = close

    def candlestick(self):
        """Candlestick patterns
        :return: [int] values are -100, 0 or 100
        """
        candlestick_arr = np.array([
            talib.CDL2CROWS(self.open, self.high, self.low, self.close),  # Two Crows
            talib.CDL3BLACKCROWS(self.open, self.high, self.low, self.close),  # Three Black Crows
            talib.CDL3INSIDE(self.open, self.high, self.low, self.close),  # Three Inside Up/Down
            talib.CDL3LINESTRIKE(self.open, self.high, self.low, self.close),  # Three-Line Strike
            talib.CDL3OUTSIDE(self.open, self.high, self.low, self.close),  # Three Outside Up/Down
            talib.CDL3STARSINSOUTH(self.open, self.high, self.low, self.close),  # Three Stars In The South
            talib.CDL3WHITESOLDIERS(self.open, self.high, self.low, self.close),  # Three Advancing White Soldiers
            talib.CDLABANDONEDBABY(self.open, self.high, self.low, self.close, penetration=0.3),  # Abandoned Baby
            talib.CDLADVANCEBLOCK(self.open, self.high, self.low, self.close),  # Three Advancing White Soldiers
            talib.CDLBELTHOLD(self.open, self.high, self.low, self.close),  # Belt-hold
            talib.CDLBREAKAWAY(self.open, self.high, self.low, self.close),  # Breakaway
            talib.CDLCLOSINGMARUBOZU(self.open, self.high, self.low, self.close),  # Closing Marubozu
            talib.CDLCONCEALBABYSWALL(self.open, self.high, self.low, self.close),  # Concealing Baby Swallow
            talib.CDLCOUNTERATTACK(self.open, self.high, self.low, self.close),  # Counterattack
            talib.CDLDARKCLOUDCOVER(self.open, self.high, self.low, self.close, penetration=0.5),  # Dark Cloud Cover
            talib.CDLDOJI(self.open, self.high, self.low, self.close),  # Doji
            talib.CDLDOJISTAR(self.open, self.high, self.low, self.close),  # Doji Star
            talib.CDLDRAGONFLYDOJI(self.open, self.high, self.low, self.close),  # Dragonfly Doji
            talib.CDLENGULFING(self.open, self.high, self.low, self.close),  # Engulfing Pattern
            talib.CDLEVENINGDOJISTAR(self.open, self.high, self.low, self.close, penetration=0.5),  # Evening Doji Star
            talib.CDLEVENINGSTAR(self.open, self.high, self.low, self.close, penetration=0.5),  # Evening Star
            talib.CDLGAPSIDESIDEWHITE(self.open, self.high, self.low, self.close),  # Up/Down-gap side-by-side white lines
            talib.CDLGRAVESTONEDOJI(self.open, self.high, self.low, self.close),  # Gravestone Doji
            talib.CDLHAMMER(self.open, self.high, self.low, self.close),  # Hammer
            talib.CDLHANGINGMAN(self.open, self.high, self.low, self.close),  # Hanging Man
            talib.CDLHARAMI(self.open, self.high, self.low, self.close),  # Harami Pattern
            talib.CDLHARAMICROSS(self.open, self.high, self.low, self.close),  # Harami Cross Pattern
            talib.CDLHIGHWAVE(self.open, self.high, self.low, self.close),  # High-Wave Candle
            talib.CDLHIKKAKE(self.open, self.high, self.low, self.close),  # Hikkake Pattern
            talib.CDLHIKKAKEMOD(self.open, self.high, self.low, self.close),  # Modified Hikkake Pattern
            talib.CDLHOMINGPIGEON(self.open, self.high, self.low, self.close),  # Homing Pigeon
            talib.CDLIDENTICAL3CROWS(self.open, self.high, self.low, self.close),  # Identical Three Crows
            talib.CDLINNECK(self.open, self.high, self.low, self.close),  # In-Neck Pattern
            talib.CDLINVERTEDHAMMER(self.open, self.high, self.low, self.close),  # Inverted Hammer
            talib.CDLKICKING(self.open, self.high, self.low, self.close),  # CDLKICKING
            talib.CDLKICKINGBYLENGTH(self.open, self.high, self.low, self.close),  # Kicking - bull/bear determined by the longer marubozu
            talib.CDLLADDERBOTTOM(self.open, self.high, self.low, self.close),  # Ladder Bottom
            talib.CDLLONGLEGGEDDOJI(self.open, self.high, self.low, self.close),  # Long Legged Doji
            talib.CDLLONGLINE(self.open, self.high, self.low, self.close),  # Long Line Candle
            talib.CDLMARUBOZU(self.open, self.high, self.low, self.close),  # Marubozu
            talib.CDLMATCHINGLOW(self.open, self.high, self.low, self.close),  # Matching Low
            talib.CDLMATHOLD(self.open, self.high, self.low, self.close, penetration=0.5),  # Mat Hold
            talib.CDLMORNINGDOJISTAR(self.open, self.high, self.low, self.close, penetration=0.3),  # Morning Doji Star
            talib.CDLMORNINGSTAR(self.open, self.high, self.low, self.close, penetration=0.3),  # Morning Star
            talib.CDLONNECK(self.open, self.high, self.low, self.close),  # On-Neck Pattern
            talib.CDLPIERCING(self.open, self.high, self.low, self.close),  # Piercing Pattern
            talib.CDLRICKSHAWMAN(self.open, self.high, self.low, self.close),  # Rickshaw Man
            talib.CDLRISEFALL3METHODS(self.open, self.high, self.low, self.close),  # Rising/Falling Three Methods
            talib.CDLSEPARATINGLINES(self.open, self.high, self.low, self.close),  # Separating Lines
            talib.CDLSHOOTINGSTAR(self.open, self.high, self.low, self.close),  # Shooting Star
            talib.CDLSHORTLINE(self.open, self.high, self.low, self.close),  # Short Line Candle
            talib.CDLSPINNINGTOP(self.open, self.high, self.low, self.close),  # Spinning Top
            talib.CDLSTALLEDPATTERN(self.open, self.high, self.low, self.close),  # Stalled Pattern
            talib.CDLSTICKSANDWICH(self.open, self.high, self.low, self.close),  # Stick Sandwich
            talib.CDLTAKURI(self.open, self.high, self.low, self.close),  # Takuri (Dragonfly Doji with very long lower shadow)
            talib.CDLTASUKIGAP(self.open, self.high, self.low, self.close),  # Tasuki Gap
            talib.CDLTHRUSTING(self.open, self.high, self.low, self.close),  # Thrusting Pattern
            talib.CDLTRISTAR(self.open, self.high, self.low, self.close),  # Tristar Pattern
            talib.CDLUNIQUE3RIVER(self.open, self.high, self.low, self.close),  # Unique 3 River
            talib.CDLUPSIDEGAP2CROWS(self.open, self.high, self.low, self.close),  # Upside Gap Two Crows
            talib.CDLXSIDEGAP3METHODS(self.open, self.high, self.low, self.close),  # Upside/Downside Gap Three Methods
        ])

        return candlestick_arr

