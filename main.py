from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def check_prices():
    # Prezzi simulati (verranno in futuro estratti con Playwright)
    prices = {
        "BTC": 108950.0,
        "ETH": 2630.0,
        "MKR": 1918.0,
        "HZD": 727.3,
        "BCH": 508.0,
        "ISG": 17.12
    }

    # Webhook del Replit
    webhook_url = "https://b212283c-8104-4ac6-b436-5ca4a5e43d4d-00-3exekcncgaduf.riker.replit.dev/"

    try:
        response = requests.post(webhook_url, json=prices, timeout=5)
        print("✅ Dati inviati con successo a Replit.")
        print("📦 Payload:", prices)
        print("🔁 Risposta Replit:", response.status_code)
    except Exception as e:
        print("❌ Errore nell'invio dati a Replit:", e)

    return jsonify({"status": "ok", "data": prices})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
