def valaszolo_bot(uzenet):
    u = uzenet.lower().strip()

    # 🔢 Kulcsszavak témák szerint (moduláris szótár)
    temak = {
        "udvozles": ["szia", "hello", "csá", "üdv", "jó napot", "jó reggelt", "jó estét"],
        "jegy": ["1", "1.", "jegy", "jegyek", "belépő", "belépőjegy", "ár", "mennyibe"],
        "program": ["2", "2.", "program", "programok", "műsor"],
        "megkozelites": ["3", "3.", "megközelítés", "utazás", "hogy jutok el", "cím", "helyszín"],
        "etkezes": ["4", "4.", "étel", "vásár", "kaják", "kaja", "evés"],
        "csalad": ["5", "5.", "gyerek", "gyermek", "család", "pelenkázó"],
        "eso": ["6", "6.", "eső", "időjárás", "zivatar", "esik"],
        "egyeb": ["7", "7.", "egyéb", "más", "infó", "információ"],
        "bucsuapp": ["8", "8.", "app", "térkép", "búcsú app", "interaktív"],
        "koszonet": ["köszi", "köszönöm", "szuper", "ez az", "de jó", "király", "zseniális"],
        "kilepes": ["kilépés", "exit", "quit"],
    }

    # 🤖 Válaszok
    valaszok = {
        "udvozles": (
            "🙏 Hare Krisna! Itt a Krisna-völgy csetbot. Szolgálatodra – miben segíthetek?\n\n"
            "📅 A Krisna-völgyi 3 napos Búcsú július 25–27. között kerül megrendezésre!\n\n"
            "📋 Írd be a számod, ami érdekel:\n"
            "1️⃣ Búcsú jegyek\n"
            "2️⃣ Program lehetőségek\n"
            "3️⃣ Megközelítés\n"
            "4️⃣ Étkezés és vásár\n"
            "5️⃣ Családi tudnivalók\n"
            "6️⃣ Időjárás / eső esetén\n"
            "7️⃣ Egyéb\n"
            "8️⃣ Búcsú App - interaktív térkép"
        ),
        "jegy": (
            "🎟️ Van, természetesen. Itt tudsz online venni, vagy a helyszínen a Búcsú alatt:\n"
            "👉 https://krisnavolgy.hu/bucsujegy\n\n"
            "🎉 Idén vagy éppen 30 éves? Vendégünk vagy! Ünnepeljük együtt, hiszen mi is 30 évesek vagyunk!\n"
            "📄 Látogatásod érvényes személyi okmánnyal ingyenes."
        ),
        "program": (
            "🎡 Várnak rád színpadi műsorok, vezetett túrák, kézműves vásár, gyermekprogramok,\n"
            "védikus esküvő, Holi Fesztivál és sok más élmény!"
        ),
        "megkozelites": (
            "🚗 Somogyvámos, Krisna-völgy – autóval, utazási irodával vagy kerékpárral is megközelíthető. "
            "A részletekért látogass el a weboldalra."
        ),
        "etkezes": (
            "🍲 Ízletes húsmentes, vegán és ahimsza ételek!\n"
            "🛍 A vásárban kézműves portékák, édességek, ajándéktárgyak is kaphatók."
        ),
        "csalad": (
            "👨‍👩‍👧‍👦 Családbarát rendezvény: pelenkázó, árnyas pihenő, szári próba, arcfestés "
            "és szeretetteljes gyerekfoglalkozások."
        ),
        "eso": (
            "🌧 A Búcsú eső esetén sem marad el – sok program fedett helyszínen is megtartható. Hozz esernyőt!"
        ),
        "egyeb": (
            "ℹ️ Kérdezz bátran más témában is, vagy böngészd a részleteket itt:\n"
            "👉 https://krisnavolgy.hu/bucsu"
        ),
        "bucsuapp": (
            "🗺️ A Búcsú App egy interaktív térkép, ahol megnézheted a programokat, helyszíneket, és segít eligazodni a rendezvényen.\n"
            "👉 https://bucsuapp.krisnavolgy.hu"
        ),
        "koszonet": (
            "😊 Örülök, ha segíthettem!\n"
            "🎉 Várunk szeretettel a Krisna-völgyi Búcsúban!\n"
            "👉 Elővételes jegyek: https://krisnavolgy.hu/bucsujegy"
        ),
        "kilepes": "exit"
    }

    # 🔍 Ellenőrzés témák szerint
    for tema, kulcsok in temak.items():
        if any(k in u for k in kulcsok):
            return valaszok.get(tema, "Hmm, erre még nincs válaszom.")

    # ❓ Alapértelmezett válasz
    return (
        "❓ Ezt most nem értettem teljesen.\n"
        "📋 Próbáld meg egy szám beírásával:\n"
        "1 – Jegyek, 2 – Programok, 3 – Megközelítés, 4 – Étkezés, stb."
    )
