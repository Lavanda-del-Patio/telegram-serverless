import json
import os
from urllib.parse import urljoin
import requests

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_API_URL = "https://api.telegram.org/bot{}/".format(TELEGRAM_BOT_TOKEN)
TELEGRAM_BOT_CHAT = os.getenv('TELEGRAM_CHAT')
def lambda_handler(event, context):
    print(event)

    telegram_token = os.getenv('TELEGRAM_TOKEN')
    # Check Environment variables on next version
    if telegram_token is not None:
        print(event['Records'])
        for record in event['Records']:
           send_message(record['Sns']['Message'], TELEGRAM_BOT_CHAT)
        #print(eventJson)
        return {
            'statusCode': 200
        }
    else:
        raise EnvironmentError("Missing TELEGRAM_TOKEN env variable!")
        
def send_message(text, chat_id):
    url = TELEGRAM_API_URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(text, chat_id)
    requests.get(url)        