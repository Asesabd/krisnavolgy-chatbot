# log.py
from datetime import datetime

def logol(sender_id, uzenet):
    try:
        with open("bot_log.csv", "a", encoding="utf-8") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sor = f"{timestamp},{sender_id},{uzenet.strip()}\n"
            f.write(sor)
    except Exception as e:
        print(f"[LOG HIBA] Nem sikerült naplózni: {e}")
