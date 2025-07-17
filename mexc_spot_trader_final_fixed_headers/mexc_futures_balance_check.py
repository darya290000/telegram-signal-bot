
import time
import hmac
import hashlib
import requests
from urllib.parse import urlencode

# ---------- اطلاعات API خودت رو اینجا وارد کن ----------
API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"
# ---------------------------------------------------------

base_url = "https://contract.mexc.com"

def get_futures_balance():
    path = "/api/v1/private/account/assets"
    url = base_url + path
    req_time = int(time.time() * 1000)

    params = {
        "api_key": API_KEY,
        "req_time": req_time
    }

    sign_string = urlencode(sorted(params.items()))
    signature = hmac.new(API_SECRET.encode(), sign_string.encode(), hashlib.sha256).hexdigest()
    params["sign"] = signature

    response = requests.get(url, params=params)
    data = response.json()

    if "data" in data:
        print("📊 موجودی حساب Futures (USDT-M):")
        for item in data["data"]:
            if float(item["available"]) > 0:
                print(f"→ {item['currency']}: موجودی = {item['available']}, در حال استفاده = {item['frozen']}")
    else:
        print("❌ خطا در دریافت اطلاعات:", data)

if __name__ == "__main__":
    get_futures_balance()
