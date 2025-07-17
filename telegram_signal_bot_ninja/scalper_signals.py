import pandas as pd
import ta
from config import TAKE_PROFIT, STOP_LOSS

def analyze_candles(klines):
    if klines is None:
        return None

    # داده‌ها را به DataFrame تبدیل می‌کنیم
    df = pd.DataFrame(klines, columns=[
        "open_time", "open", "high", "low", "close", "volume",
        "close_time", "quote_asset_volume", "number_of_trades",
        "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume", "ignore"
    ])

    # ستون‌ها را به عدد تبدیل کنیم (float)
    for col in ["open", "high", "low", "close", "volume"]:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # اندیکاتور EMA 9 و EMA 21
    df["ema9"] = df["close"].ewm(span=9, adjust=False).mean()
    df["ema21"] = df["close"].ewm(span=21, adjust=False).mean()

    # RSI با دوره 14
    df["rsi"] = ta.momentum.RSIIndicator(df["close"], window=14).rsi()

    # MACD
    macd = ta.trend.MACD(df["close"])
    df["macd"] = macd.macd()
    df["macd_signal"] = macd.macd_signal()

    # آخرین کندل برای تصمیم
    last = df.iloc[-1]

    # سیگنال خرید: EMA9 بالای EMA21 و RSI زیر 70 و MACD بالاتر از سیگنال MACD
    if last["ema9"] > last["ema21"] and last["rsi"] < 70 and last["macd"] > last["macd_signal"]:
        return f"🟢 سیگنال خرید: {last['close']:.4f}"

    # سیگنال فروش: EMA9 زیر EMA21 و RSI بالای 30 و MACD پایین‌تر از سیگنال MACD
    elif last["ema9"] < last["ema21"] and last["rsi"] > 30 and last["macd"] < last["macd_signal"]:
        return f"🔴 سیگنال فروش: {last['close']:.4f}"

    return None
