from chatbot import valaszolo_bot
from log import logol
from datetime import datetime

print("🧘‍♂️ Krisna-völgy teszt chatbot (Kilépés: kilépés)")

while True:
    uzenet = input("Te: ").strip()
    if uzenet.lower() in ["kilépés", "exit", "quit"]:
        print("Bot: Viszlát!")
        break

    sender_id = "lokalteszt"
    logol(sender_id, uzenet)
    valasz = valaszolo_bot(uzenet)
    print("Bot:", valasz)
