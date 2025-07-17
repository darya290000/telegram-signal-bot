
import requests
import pandas as pd
from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator
from ta.trend import IchimokuIndicator

# تنظیمات
symbol = "AAVEUSDT"
interval = "5m"
limit = 200  # برای تحلیل، حداقل 100 کندل لازمه

# دریافت داده‌ها از API صرافی MEXC (یا مشابه Binance)
def fetch_ohlcv(symbol, interval, limit):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data, columns=[
        "timestamp", "open", "high", "low", "close", "volume",
        "_", "_", "_", "_", "_", "_"
    ])
    df["close"] = pd.to_numeric(df["close"])
    df["high"] = pd.to_numeric(df["high"])
    df["low"] = pd.to_numeric(df["low"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    return df

# تحلیل و بررسی شرایط ورود
def analyze(df):
    df["ema50"] = EMAIndicator(df["close"], window=50).ema_indicator()
    df["ema200"] = EMAIndicator(df["close"], window=200).ema_indicator()

    ichi = IchimokuIndicator(high=df["high"], low=df["low"], window1=9, window2=26, window3=52)
    df["tenkan"] = ichi.ichimoku_conversion_line()
    df["kijun"] = ichi.ichimoku_base_line()
    df["senkou_a"] = ichi.ichimoku_a()
    df["senkou_b"] = ichi.ichimoku_b()

    latest = df.iloc[-1]

    print("📊 آخرین وضعیت بازار AAVEUSDT (تایم‌فریم ۵ دقیقه):")
    print(f"قیمت: {latest['close']:.2f}")
    print(f"EMA50: {latest['ema50']:.2f} | EMA200: {latest['ema200']:.2f}")
    print(f"Tenkan: {latest['tenkan']:.2f} | Kijun: {latest['kijun']:.2f}")
    print(f"Senkou A: {latest['senkou_a']:.2f} | Senkou B: {latest['senkou_b']:.2f}")

    conditions = [
        latest["close"] > latest["ema50"],
        latest["close"] > latest["ema200"],
        latest["tenkan"] > latest["kijun"],
        latest["close"] > latest["senkou_a"],
        latest["close"] > latest["senkou_b"]
    ]

    if all(conditions):
        print("✅ سیگنال ورود به پوزیشن LONG صادر شد (تمام شرایط برقرار است)")
    else:
        print("❌ هنوز شرایط کامل برای ورود به پوزیشن LONG برقرار نیست")

if __name__ == "__main__":
    df = fetch_ohlcv(symbol, interval, limit)
    analyze(df)
