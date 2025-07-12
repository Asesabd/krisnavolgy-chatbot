import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# 🔐 JSON fájl alapú hitelesítés
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
client = gspread.authorize(creds)

# 📄 A te Sheet ID-d alapján nyitjuk meg
sheet_id = "1t5QqHhRQFsC9GWUyfrzr8gc9RhrKohT7MX7YncND87M"
sheet = client.open_by_key(sheet_id).sheet1

# 🧠 Logoló függvény, hibakezeléssel
def sheet_logol(sender_id, uzenet):
    print("[LOGOL] Naplózás indul...")
    if not sheet:
        print("❌ Sheet nincs betöltve!")
        return
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sor = [timestamp, sender_id, uzenet]
        print(f"📦 Felküldés előtt: {sor}")
        sheet.append_row(sor)
        print(f"✅ Logolva: {sor}")
    except Exception as e:
        print(f"❌ HIBA a sheet_logol()-ban: {e}")

