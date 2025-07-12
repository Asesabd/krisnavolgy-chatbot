
from flask import Flask, request
import requests
import os
from chatbot import valaszolo_bot
from log import logol  # ← EZT IDE

app = Flask(__name__)

VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN", "lokalis_token")
PAGE_ACCESS_TOKEN = os.environ.get("PAGE_ACCESS_TOKEN", "lokalis_page_token")

def send_message(recipient_id, message_text):
    url = "https://graph.facebook.com/v17.0/me/messages"
    params = {
        "access_token": PAGE_ACCESS_TOKEN
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "recipient": {"id": recipient_id},
        "message": {"text": message_text}
    }
    response = requests.post(url, params=params, headers=headers, json=data)
    print("Válasz elküldve:", response.status_code, response.text)

@app.route("/webhook", methods=["GET"])
def webhook_verification():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Invalid verification token", 403


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print("Üzenet jött:", data)

    response_text = "ok"

    try:
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
                if messaging_event.get('message'):
                    sender_id = messaging_event['sender'].get('id', '')
                    message_text = messaging_event['message'].get('text')

                    print("Sender ID:", sender_id)

                    if message_text:
                        logol(sender_id, message_text)  # <<< EZT IDE TEDD
                        valasz = valaszolo_bot(message_text)
                        print("Bot válasz:", valasz)

                        if not sender_id.isdigit():
                            print("Lokális teszt. Nem küldünk Messengerre.")
                            response_text = valasz
                        else:
                            send_message(sender_id, valasz)


    except Exception as e:
        print("Hiba:", e)

    return response_text, 200

@app.route("/privacy", methods=["GET"])
def privacy_policy():
    return """
    <html><body>
    <h2>Data Deletion Instructions</h2>
    <p>This chatbot does not store user data permanently.</p>
    <p>Adataid törlésével kapcsoaltban, kérlek írj erre az emailre: <strong>turizmus@krisnavolgy.hu</strong> with your Facebook username.</p>
    </body></html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)