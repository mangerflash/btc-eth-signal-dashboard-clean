import yfinance as yf
import pandas_ta as ta

def generate_signals(symbol):
    df = yf.download(symbol, period="30d", interval="1h")
    df["EMA20"] = ta.ema(df["Close"], length=20)
    return df