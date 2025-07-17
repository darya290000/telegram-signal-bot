
import time
import hmac
import hashlib
import requests
from config import API_KEY, API_SECRET

BASE_URL = "https://api.mexc.com"

def sign_request(params):
    query_string = '&'.join([f"{key}={params[key]}" for key in sorted(params)])
    signature = hmac.new(API_SECRET.encode(), query_string.encode(), hashlib.sha256).hexdigest()
    return signature

def get_spot_balance():
    url = BASE_URL + "/api/v3/account"
    timestamp = int(time.time() * 1000)

    params = {
        "timestamp": timestamp
    }
    params["signature"] = sign_request(params)

    headers = {
        "X-MEXC-APIKEY": API_KEY
    }

    response = requests.get(url, headers=headers, params=params)
    return response.json()

if __name__ == "__main__":
    print("💰 در حال بررسی موجودی حساب اسپات...")
    result = get_spot_balance()
    if "balances" in result:
        for asset in result["balances"]:
            free = float(asset.get("free", 0))
            locked = float(asset.get("locked", 0))
            if free > 0 or locked > 0:
                print(f"🪙 {asset['asset']}: آزاد = {free}, قفل‌شده = {locked}")
    else:
        print("❌ خطا:", result)
