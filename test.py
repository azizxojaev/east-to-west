import requests

# URL для получения списка стран и их столиц
url = "http://api.geonames.org/countryInfoJSON"

# Параметры запроса
params = {
    'username': 'azizxojaev',  # Замените на ваше имя пользователя GeoNames
    'lang': 'en'  # Язык ответа (русский)
}

# Отправляем запрос к API GeoNames
response = requests.get(url, params=params)

data = response.json()
countries = data['geonames']
print(countries)