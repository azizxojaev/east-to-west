import requests
from environs import Env


env = Env()
env.read_env()


def send_message(text):
    apiToken = env.str('API_TOKEN')
    chatID = env.str('CHAT_ID')
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': text})
    except Exception as e:
        print(e)