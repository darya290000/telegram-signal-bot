
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

def safe_import(module_name, default_func):
    try:
        module = __import__(module_name)
        return getattr(module, module_name)
    except Exception:
        def fallback():
            print(f"⚠️ ماژول {module_name} یافت نشد. تابع پیش‌فرض اجرا شد.")
        return fallback

monitor_critical_process = safe_import("core_monitor", None)
dns_check_loop = safe_import("dns_guard", None)
monitor_network_and_block = safe_import("internet_kill_switch", None)
start_file_watchdog = safe_import("file_watchdog", None)
scheduled_backup = safe_import("backup_manager", None)
log_secure = safe_import("log_encryptor", None)
lock_proxy_settings = safe_import("proxy_guard", None)

def main():
    print("\U0001F441 گماشته پیشرفته فعال شد. در حال بارگذاری ماژول‌ها...")
    print("⏱️ شروع در:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    tasks = [monitor_critical_process, dns_check_loop, monitor_network_and_block,
             start_file_watchdog, scheduled_backup, log_secure, lock_proxy_settings]
    tasks = [t for t in tasks if callable(t)]
    with ThreadPoolExecutor(max_workers=min(len(tasks), 4)) as executor:
        for task in tasks:
            executor.submit(task)
        while True:
            time.sleep(60)

if __name__ == "__main__":
    main()
