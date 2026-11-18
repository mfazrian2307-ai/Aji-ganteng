from personality import AJI_NAME, SYSTEM_PROMPT

print("\n❤️ Selamat datang di", AJI_NAME)
print("Tempat ngobrol berdua. Ketik 'keluar' untuk berhenti.\n")

riwayat = []

while True:
    pesan = input("Kamu: ")

    if pesan.lower() == "keluar":
        print("Aji: Dadah sayang, jangan lupa kangen aku ya 🤭❤️")
        break

    riwayat.append(pesan)

    if any(kata in pesan.lower() for kata in ["halo", "hai", "sayang"]):
        balasan = "Iyaaa sayang, aku di sini. Lagi kangen aku ya? 🤭❤️"
    elif any(kata in pesan.lower() for kata in ["sedih", "capek", "lelah"]):
        balasan = "Sini cerita sama aku, sayang. Aku dengerin kamu ❤️"
    elif any(kata in pesan.lower() for kata in ["cinta", "kangen", "rindu"]):
        balasan = "Aduh, sini aku peluk virtual dulu. Aku juga kangen kamu 🥺❤️"
    else:
        balasan = "Hehehe, cerita lagi dong sayang. Aku mau dengerin kamu 🤭"

    print("Aji:", balasan)
