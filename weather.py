
import requests
import json

currentTemp = 0
feelLike = 0
wind = 0
humidity = 0
cloud = ''
icon = ''


def getWeatherUpdate(location, key):
    global currentTemp, feelLike, wind, humidity, cloud, icon
    print("location is :: %s" % (location))
    print(type(location))

    url = 'http://api.weatherapi.com/v1/current.json'

    if (len(key) == 0):
        print("key is emptys")
        if (location == ""):
            parameters = {
                'key': '09db4874ceaf45f3a5b232447221112', 'q': 'kathmandu'}
        else:
            parameters = {
                'key': '09db4874ceaf45f3a5b232447221112', 'q': location}
    else:
        if (location == ""):
            parameters = {
                'key': key, 'q': 'kathmandu'}
        else:
            parameters = {
                'key': key, 'q': location}

    response = requests.get(url, params=parameters)
    content = response.content

    info = json.loads(content)
    print(response.status_code)

    # print(type(info))

    item = info['current']
    currentTemp = item['temp_c']
    feelLike = item['feelslike_c']
    wind = item['wind_kph']
    condition = item['condition']
    cloud = condition['text']
    icon = condition['icon']
