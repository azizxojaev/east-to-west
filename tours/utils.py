import requests
from environs import Env


env = Env()
env.read_env()


def send_message(text):
    api_token = env.str('API_TOKEN')
    chat_id = env.str('CHAT_ID')
    api_url = f'https://api.telegram.org/bot{api_token}/sendMessage'

    try:
        response = requests.post(api_url, json={'chat_id': chat_id, 'text': text})
        response.raise_for_status()
    except Exception as e:
        print(f'Произошла ошибка: {e}')
