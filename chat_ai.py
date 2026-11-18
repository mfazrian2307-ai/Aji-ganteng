import os
import json
import urllib.request
import urllib.error
from personality import SYSTEM_PROMPT

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = "gemini-3.8-flash"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

if not API_KEY:
    print("API Key belum terpasang. Buka ulang Termux dan pasang API Key.")
    raise SystemExit

history = []

print("\n❤️ AJI GANTENG AI")
print("Sekarang aku bisa ngobrol sama kamu, sayang!")
print("Ketik keluar untuk berhenti.\n")

while True:
    message = input("Kamu: ").strip()

    if message.lower() == "keluar":
        print("Aji: Dadah sayang, jangan lupa aku ya 🤭❤️")
        break

    if not message:
        continue

    history.append({
        "role": "user",
        "parts": [{"text": message}]
    })

    data = {
        "systemInstruction": {
            "parts": [{"text": SYSTEM_PROMPT}]
        },
        "contents": history[-12:],
        "generationConfig": {
            "temperature": 0.9,
            "maxOutputTokens": 500
        }
    }

    request = urllib.request.Request(
        URL,
        data=json.dumps(data).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "x-goog-api-key": API_KEY
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            result = json.loads(response.read().decode("utf-8"))

        reply = result["candidates"][0]["content"]["parts"][0]["text"]
        print("\nAji:", reply, "\n")

        history.append({
            "role": "model",
            "parts": [{"text": reply}]
        })

    except urllib.error.HTTPError as error:
        print("\nGagal menghubungi Gemini. Kode:", error.code)
        print("Periksa API Key, akses model, dan kuota akun.\n")
        history.pop()

    except Exception as error:
        print("\nKoneksi bermasalah:", str(error), "\n")
        history.pop()
