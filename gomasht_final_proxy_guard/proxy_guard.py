
import time
import winreg

def disable_proxy():
    try:
        registry_path = r"Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, registry_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, 0)
        winreg.SetValueEx(key, "ProxyServer", 0, winreg.REG_SZ, "")
        winreg.CloseKey(key)
        print("✅ پراکسی غیرفعال شد.")
    except Exception as e:
        print(f"❌ خطا در غیرفعال‌سازی پراکسی: {e}")

def lock_proxy_settings():
    print("🔒 قفل‌گذاری روی تنظیمات پراکسی شروع شد...")
    while True:
        disable_proxy()
        time.sleep(5)
