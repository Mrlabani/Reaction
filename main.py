import os
import random
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set your Telegram bot token
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')  # or replace with your token as a string
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/"

# Define the array of emojis
EMOJIS = ["🖤", "🌚", "🌸", "🫶", "⚡", "😉", "🩷", "🥹", "😻", "👍", "😂", "🌛", "😜", "🤎", "🩶", "💙", "💗", "🫂",
          "💕", "❤", "🔥", "🥰", "👏", "😁", "😢", "🎉", "🤩", "🙏", "👌", "🕊", "😍", "❤‍🔥", "🤣", "🌷", "💔", "🍓", 
          "🍾", "😊", "😍", "🥳", "😎", "🌈", "🌞", "🌟", "🎊", "🎈", "💖", "♥", "🍂", "🩵", "💚"]

def send_reaction(chat_id, message_id, emoji):
    url = TELEGRAM_API_URL + 'sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': emoji,
        'reply_to_message_id': message_id
    }
    response = requests.post(url, json=payload)
    return response.json()

@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.json
    if 'message' in update:
        message = update['message']
        chat_id = message['chat']['id']
        message_id = message['message_id']

        # Select a random emoji from the array
        random_emoji = random.choice(EMOJIS)

        # Send the reaction
        send_reaction(chat_id, message_id, random_emoji)
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
