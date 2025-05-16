def valaszolo_bot(uzenet):
    if "nyitvatartás" in uzenet.lower():
        return "Krisna-völgy minden nap 10 és 18 óra között látogatható!"
    elif "jegy" in uzenet.lower():
        return "A belépőjegy ára felnőtteknek 2500 Ft, diákoknak 1800 Ft."
    else:
        return "Kérlek, írj pontosabban, miben segíthetek Krisna-völggyel kapcsolatban."


if __name__ == "__main__":
    print("Szia! Miben segíthetek Krisna-völggyel kapcsolatban? (Kilépés: kilépés)")

    while True:
        uzenet = input("Te: ")
        if uzenet.lower() in ["kilépés", "exit", "quit"]:
            print("Bot: Viszlát!")
            break
        valasz = valaszolo_bot(uzenet)
        print("Bot:", valasz)