from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def check_prices():
    # Dati simulati (da sostituire con scraping Playwright)
    prices = {
        "BTC": 108950.00,
        "ETH": 2630.00,
        "MKR": 1918.00,
        "HZD": 727.30,
        "BCH": 508.00,
        "ISG": 17.12
    }

    # Invia i dati simulati al webhook di Replit (da personalizzare)
    webhook_url = "https://eo0bso7t3q5h2f.m.pipedream.net"
    requests.post(webhook_url, json=prices)

    return jsonify({"status": "ok", "data": prices})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
