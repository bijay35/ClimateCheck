
import requests
import json

currentTemp = 0
feelLike = 0


def getWeatherUpdate(location):
    global currentTemp, feelLike
    # placeName = input("Enter the place name :: ")
    # print("the location -> %s"% (location))
    print("location is :: %s" % (location))
    print(type(location))

    url = 'http://api.weatherapi.com/v1/current.json'
    if (location is ""):
        parameters = {'key': '09db4874ceaf45f3a5b232447221112', 'q': 'kathmandu'}
    else:
        parameters = {'key': '09db4874ceaf45f3a5b232447221112', 'q': location}

    response = requests.get(url, params=parameters)
    content = response.content

    info = json.loads(content)
    print(response.status_code)

    # print(type(info))

    item = info['current']
    currentTemp = item['temp_c']
    feelLike = item['feelslike_c']

    # print("The current temp in %s is %sC" % (location,currentTemp))
    # print("It feels like %sC" % (feelLike))

    if currentTemp <= 0:
        print("Be warm while outside")
    elif currentTemp > 0 and currentTemp < 10:
        print("The temperature is okay okay")
    else:
        print("Its little cool")




