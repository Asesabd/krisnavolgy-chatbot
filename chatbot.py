def valaszolo_bot(uzenet):
    u = uzenet.lower().strip()

    # 👋 Üdvözlés
    if any(k in u for k in ["szia", "hello", "csá", "üdv", "jó napot", "jó reggelt", "jó estét"]):
        return (
            "🙏 Hare Krisna! Itt a Krisna-völgy csetbot. Szolgálatodra – miben segíthetek?\n\n"
            "📋 Írd be a számod, ami érdekel:\n"
            "1️⃣ Búcsú jegyek\n"
            "2️⃣ Program lehetőségek\n"
            "3️⃣ Megközelítés\n"
            "4️⃣ Étkezés és vásár\n"
            "5️⃣ Családi tudnivalók\n"
            "6️⃣ Időjárás / eső esetén\n"
            "7️⃣ Egyéb"
        )

    # 🔢 Számozott menüpontok és kulcsszavak
    elif u in ["1", "1.", "jegy", "jegyek", "belépő", "belépőjegy"]:
        return (
            "🎟️ Van, természetesen. Itt tudsz online venni, vagy a helyszínen a Búcsú alatt:\n"
            "👉 https://krisnavolgy.hu/bucsujegy"
        )

    elif u in ["2", "2.", "program", "programok"]:
        return (
            "🎡 Várnak rád színpadi műsorok, vezetett túrák, kézműves vásár, gyermekprogramok,\n"
            "védikus esküvő, Holi Fesztivál és sok más élmény!"
        )

    elif u in ["3", "3.", "megközelítés", "utazás", "hogy jutok el"]:
        return (
            "🚗 Somogyvámos, Krisna-völgy – autóval, utazási irodával vagy kerékpárral is megközelíthető. "
            "A részletekért látogass el a weboldalra."
        )

    elif u in ["4", "4.", "étel", "vásár"]:
        return (
            "🍲 Ízletes húsmentes, vegán és ahimsza ételek!\n"
            "🛍 A vásárban kézműves portékák, édességek, ajándéktárgyak is kaphatók."
        )

    elif u in ["5", "5.", "család", "gyerek", "gyermek"]:
        return (
            "👨‍👩‍👧‍👦 Családbarát rendezvény: pelenkázó, árnyas pihenő, szári próba, arcfestés "
            "és szeretetteljes gyerekfoglalkozások."
        )

    elif u in ["6", "6.", "eső", "időjárás"]:
        return (
            "🌧 A Búcsú eső esetén sem marad el – sok program fedett helyszínen is megtartható. Hozz esernyőt!"
        )

    elif u in ["7", "7.", "egyéb"]:
        return (
            "ℹ️ Kérdezz bátran más témában is, vagy böngészd a részleteket itt:\n"
            "👉 https://krisnavolgy.hu/bucsu"
        )

    # 🙏 Pozitív visszajelzés
    elif any(k in u for k in ["köszi", "köszönöm", "szuper", "ez az", "de jó", "király", "zseniális"]):
        return (
            "😊 Örülök, ha segíthettem!\n"
            "🎉 Várunk szeretettel a Krisna-völgyi Búcsúban!\n"
            "👉 Elővételes jegyek: https://krisnavolgy.hu/bucsujegy"
        )

    # 🚪 Kilépés
    elif "kilépés" in u or u in ["exit", "quit"]:
        return "exit"

    # 🤷‍♂️ Nem értette
    else:
        return (
            "❓ Ezt most nem értettem teljesen.\n"
            "📋 Próbáld meg egy szám beírásával:\n"
            "1 – Jegyek, 2 – Programok, 3 – Megközelítés, 4 – Étkezés, stb."
        )
