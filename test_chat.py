from chatbot import valaszolo_bot

print("Szia! Miben segíthetek Krisna-völggyel kapcsolatban? (Kilépés: kilépés)")

while True:
    uzenet = input("Te: ")
    if uzenet.lower() in ["kilépés", "exit", "quit"]:
        print("Bot: Viszlát!")
        break
    valasz = valaszolo_bot(uzenet)
    print("Bot:", valasz)