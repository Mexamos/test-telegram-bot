import os

from dotenv import load_dotenv
import requests
from bottle import (
    run, post, request as bottle_request
)

load_dotenv()

TOKEN = os.getenv('TOKEN')
BOT_URL = f'https://api.telegram.org/bot{TOKEN}/'


def get_chat_id(data):
    return data['message']['chat']['id']


def send_message(request_data, message):
    url = BOT_URL + 'sendMessage'

    json_data = {
        "chat_id": get_chat_id(request_data),
        "text": message,
    }

    requests.post(url, json=json_data)


@post('/')
def main():
    request_data = bottle_request.json
    send_message(request_data, 'Hello!')


if __name__ == '__main__':
    if TOKEN is not None:
        run(host='localhost', port=8080, debug=True)
    else:
        print('TOKEN env variable not found!')